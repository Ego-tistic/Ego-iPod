# Pro-Pods 3.0.0

Version 3 keeps the guarded BTStack allocation behavior from beta4 and removes
the ten-minute cutoff. The 96 MiB process RSS safeguard, manual disable,
device/OS restrictions and exact daemon/library checks remain. There is no
time expiration. This is not a guarantee of permanent connectivity.

The user reported successful playback, several songs, repeated reconnections
and restarts with beta4. Version 3 is newly compiled from that source with the
time check and associated clock bookkeeping removed, updated version/status
text, and a WorkaroundActive status key alongside the legacy TrialActive key.
No allocation sizes, hook targets, device IDs, or feature mappings changed.
Version 3 has passed build/package checks but has not yet been tested on an iPod.

## Install

Refresh Ego-iPod in Zebra and upgrade Pro-Pods to 3.0.0. When ready to interrupt
playback, restart Bluetooth's daemon or reboot and re-jailbreak to load the new
binary. A respring alone may leave the previous Bluetooth process loaded.
Installation itself does not restart Bluetooth or clear existing disable markers.
Use `pro-podsctl status` to check Version=3.0.0 and WorkaroundActive=true.
If previously disabled, `pro-podsctl enable` takes effect on a fresh daemon start.

Requires rootful iPod touch 6 (iPod7,1), iOS 12.5.8, mobilesubstrate
(>=0.9.5000) and preferenceloader. Conflicts with PodsGrant (com.lns.pogr).
The daemon/library image checks may reject another system image with the same
displayed iOS version; check runtime status rather than assuming compatibility.

If RSS exceeds 96 MiB, promotion stops until a fresh daemon start. Disabling
does not unload hooks or change flags on the existing guarded zone. For recovery,
use `pro-podsctl disable`, then restart bluetoothd. Beta4 and beta2 remain
indexed for rollback; earlier withdrawn builds remain unindexed.

## Downloads and provenance

[3.0.0 package](debs/com.propods.tweak_3.0.0_iphoneos-arm.deb)

[3.0.0 source](sources/Pro-Pods-3.0.0-source.zip)

SHA256: cbb5906c6b20d747db326b16e61cba6d42ced958b54f936aed61ff15a22387b1

Build succeeded for rootful arm64 using the iOS 12.4 SDK, minimum iOS 12.0.
Verification passed for package/dependency constraints, rootful ownership and
paths, plist files, bluetoothd-only injection and all three binaries' ad-hoc
code signatures. Public package and index hashes are checked during publication.
No live iPod installation or restart was performed for this release.

Adapted from [PodsGrant](https://github.com/LNSSPsd/PodsGrant) by Ruphane / LNSSPsd.
The [MIT license](LICENSE) retains upstream copyright and contributor attribution.
