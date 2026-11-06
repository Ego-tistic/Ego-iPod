# Pro-Pods 2.0.0~beta4: recovered successful trial build

Published unchanged from the local artifact installed in the earlier device trial.
Package: com.propods.tweak; architecture: iphoneos-arm (rootful arm64 binaries).
Size: 15984 bytes.
SHA256: 635d4d60b60935b61750a53b8a53ef984858294fbc13c13a62fe54e7b8bcc983

## What actually worked

The November 5 conversation records the user confirming audio stayed connected,
then confirming playback after disconnecting and reconnecting on the identified
iPod touch 6. Earlier negative attempts involved confusion between two iPods.
The agent reported beta4 installed and the guard active; native Pro 3 identity
was retained. The later control test disabled the guard and restarted Bluetooth;
the user subsequently reported failure. That control test was not completed with
enough evidence to isolate causation. This publication does not claim a permanent
fix, long-duration stability, or success after reboot.

## Configuration and limits

This is the guarded BTStack heap diagnostic, not a device-ID mapping build.
The successful session had the guard enabled. Source reads boolean `enabled`
from /var/mobile/Library/Preferences/com.propods.tweak.plist (default true).
Either /var/lib/pro-pods/disabled or
/var/mobile/Library/Preferences/com.propods.disabled disables startup hooks.
The complete live preference file from the successful session was not preserved
here, so other settings cannot be certified byte-for-byte. Identity switches do
not enable identity mapping in this build.

Runtime requires iPod7,1, iOS 12.5.8, matching daemon/library UUIDs and function
hashes. Allocation promotion stops after ten minutes or above 96 MiB RSS;
hooks remain loaded until bluetoothd restarts. This package contains no
post-install restart script. Installation alone does not restore an already
disabled guard or restart the daemon. Re-enable through its controls and restart
the process/device deliberately; a reboot requires re-jailbreaking. Check fresh
/var/tmp/pro-pods-status.plist and /var/tmp/pro-pods-status.log for actual status.
No device configuration was changed during this publication.

Depends: mobilesubstrate (>= 0.9.5000), preferenceloader,
firmware (>= 12.5.8), firmware (<< 12.5.9).
Conflicts: com.lns.pogr (PodsGrant); do not install both together.
Beta2 remains available as a recovery build. Beta1 and diagnostic1/2 remain
withdrawn from the index. Beta3 failed startup and is not published.

## Provenance and verification

Pro-Pods is an adaptation of PodsGrant by Ruphane / LNSSPsd, not wholly original
work. See https://github.com/LNSSPsd/PodsGrant and LICENSE for the retained MIT
copyright and permission notice. The accompanying source snapshot is the local
beta4 source recovered during publication; it is not a reproducible-build proof.

The older upstream PodsGrant 0.5.4 observation was initial audio success followed
by reconnect failure, with default-enabled settings bytes 01 00 00. It is not the
later successful Pro-Pods beta4 trial and has not been relabeled or republished.

Publication checks passed for package identity, dependency/firmware constraints,
rootful paths, ownership/modes, XML, bluetoothd-only injection, and arm64 ad-hoc
signature integrity. The initial publication performed no fresh hardware playback test. On November 6, the user confirmed playback on the second iPod; see [current release evidence](Pro-Pods-current.md).
