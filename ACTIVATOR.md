# Activator dependency and installation

Mac-Launcher 1.1.2 already requires `libactivator` in all three places: the
published Packages index, the .deb's DEBIAN/control, and the source archive's
control file. Its full dependency field is:

```text
Depends: mobilesubstrate, preferenceloader, libactivator, firmware (>= 12.0), firmware (<< 13.0)
```

## Install through Cydia or Zebra

1. Add Ryan Petrich's upstream source: **https://rpetri.ch/repo/**.
2. Keep your jailbreak's compatible injection and PreferenceLoader sources enabled.
3. Refresh sources, then install Mac-Launcher from Ego-iPod. The package manager
   will include Activator and its dependencies in the installation transaction
   unless already installed. Review any conflicts before proceeding.
4. Complete installation and respring, then choose a gesture in Settings →
   Activator and assign Mac-Launcher.

[Add upstream to Zebra](zbra://sources/add/https://rpetri.ch/repo/) ·
[Add upstream to Cydia](cydia://url/https://cydia.saurik.com/api/share#?source=https://rpetri.ch/repo/)

For manual APT source configuration the upstream line is:

```text
deb https://rpetri.ch/repo/ ./
```

Depends names a package, not a repository URL. Adding Ego-iPod alone cannot
automatically register another source; this repository does not modify device
source lists in maintainer scripts. Direct `dpkg -i` installation also does not
download missing dependencies. If resolution fails, refresh upstream and inspect
the missing package or conflict reported by your package manager.

## Upstream and redistribution assessment (2026-11-05)

The upstream Release and Packages.bz2 were reachable over HTTPS. The index offers
Activator `1.9.13~rc6`, architecture `iphoneos-arm`, depending on:

- `mobilesubstrate (>= 0.9.5101)`
- `preferenceloader (>= 2.2.2)`
- `com.a3tweaks.flipswitch (>= 1.0.16~rc3)`
- `com.rpetrich.rocketbootstrap (>= 1.0.9)`

The upstream binary was downloaded privately for inspection; its size and SHA256
matched the upstream index and its control metadata confirmed those dependencies.
It was not added here. This establishes package availability and rootful package
architecture, not runtime compatibility with every iOS 12 jailbreak. Installation
and gesture behavior still require a physical-device test.

[Ryan Petrich's Activator page](https://rpetri.ch/cydia/activator/) identifies the
author. The [public libactivator repository](https://github.com/rpetrich/libactivator)
contains API headers, not the complete implementation or a binary redistribution
license. No redistribution grant was identified in the inspected upstream pages,
header repository, package control archive, or package paths. Free download does
not establish redistribution permission, and Ego-iPod's MIT license does not
license Activator. Mirroring is therefore deferred unless the rights holder
provides permission or an applicable binary license is verified. This is a
permission assessment, not a conclusion that redistribution is forbidden.

## Build and publication

This repository publishes prebuilt packages and source ZIPs; it previously had
no checked-in GitHub Actions workflow. The source ZIP includes Theos build and
flat-repository generation helpers, but rebuilding every archived .deb into the
index would reintroduce withdrawn Pro-Pods versions. Preserve the currently
indexed package set.

Run `python3 tools/check_repo.py` on Linux/WSL with `dpkg-deb` before publication.
The CI workflow runs the same offline consistency check. It does not build,
deploy, sign, or test on a device. Package rebuilding requires the source ZIP's
Theos/iOS SDK setup. Existing package bytes and version 1.1.2 are preserved:
the dependency is already correct, so regenerating Packages, its compressed
variants, or Release is unnecessary for this documentation/validation change.
GitHub Pages deployment settings are managed outside this checkout.
