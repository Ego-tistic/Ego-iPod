#!/usr/bin/env python3
"""Check published indexes against actual .deb controls and source metadata."""
import bz2
import gzip
import hashlib
from pathlib import Path
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def fields(text):
    result = {}
    key = None
    for line in text.splitlines():
        if line.startswith((' ', '\t')):
            require(key is not None, 'Invalid continuation')
            result[key] += '\n' + line
        elif line:
            key, value = line.split(':', 1)
            require(key not in result, f'Duplicate field: {key}')
            result[key] = value.strip()
    return result


def main():
    raw = (ROOT / 'Packages').read_bytes()
    require(gzip.decompress((ROOT / 'Packages.gz').read_bytes()) == raw,
            'Packages.gz differs from Packages')
    require(bz2.decompress((ROOT / 'Packages.bz2').read_bytes()) == raw,
            'Packages.bz2 differs from Packages')
    packages = [fields(s) for s in re.split(r'\n\s*\n', raw.decode().strip())]
    seen = set()
    for pkg in packages:
        identity = tuple(pkg[k] for k in ('Package', 'Version', 'Architecture'))
        require(identity not in seen, f'Duplicate package: {identity}')
        seen.add(identity)
        name = pkg['Filename']
        require(name.startswith('./debs/') and '..' not in Path(name).parts,
                f'Unsafe package path: {name}')
        path = (ROOT / name).resolve()
        require(path.is_relative_to(ROOT.resolve()), 'Package escapes repository')
        data = path.read_bytes()
        require(len(data) == int(pkg['Size']), f'Wrong size: {name}')
        for field, algorithm in [('MD5sum', 'md5'), ('SHA256', 'sha256'), ('SHA512', 'sha512')]:
            require(hashlib.new(algorithm, data).hexdigest() == pkg[field],
                    f'Wrong {field}: {name}')
        control = fields(subprocess.check_output(['dpkg-deb', '-f', str(path)], text=True))
        for key, value in control.items():
            require(pkg.get(key) == value, f'Index/control mismatch: {name}: {key}')
        if pkg['Package'] == 'io.github.orbitlauncher':
            # Require a mandatory dependency, not an alternative or Recommends.
            require('libactivator' in [s.strip() for s in pkg['Depends'].split(',')],
                    'Mac-Launcher must depend directly on libactivator')
            archive = ROOT / 'sources' / f"Mac-Launcher-{pkg['Version']}-source.zip"
            with zipfile.ZipFile(archive) as source:
                src = fields(source.read('Mac-Launcher/control').decode())
            for key in ('Package', 'Version', 'Architecture', 'Depends'):
                require(src[key] == control[key], f'Source/control mismatch: {key}')
    require(any(p['Package'] == 'io.github.orbitlauncher' for p in packages),
            'Mac-Launcher missing from index')
    release = fields((ROOT / 'Release').read_text())
    for section, algorithm in [('MD5Sum', 'md5'), ('SHA256', 'sha256'), ('SHA512', 'sha512')]:
        entries = [line.split() for line in release[section].splitlines() if line.strip()]
        require(sorted(e[2] for e in entries) == ['Packages', 'Packages.bz2', 'Packages.gz'],
                f'Unexpected Release entries: {section}')
        for digest, size, filename in entries:
            data = (ROOT / filename).read_bytes()
            require(int(size) == len(data) and hashlib.new(algorithm, data).hexdigest() == digest,
                    f'Release mismatch: {section}: {filename}')
    print(f'PASS: {len(packages)} indexed packages, binary/source controls, compressed indexes and Release checksums')


if __name__ == '__main__':
    main()
