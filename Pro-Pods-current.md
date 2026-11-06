# Pro-Pods: current version for now

The selected build remains **2.0.0~beta4**, package `com.propods.tweak`.
On November 6, 2026, the user confirmed working playback on the second iPod
touch 6 running iOS 12.5.8. They requested that this exact build be kept as
the final version for now. No executable was rebuilt, renamed, or modified.

An earlier connection attempt on this same device disconnected without a
bluetoothd crash. During the subsequent captured attempt, A2DP logs reported
connected audio streaming and a 62-second stream before suspension. The user
then reported that it was working. The daemon retained PID 294; no new
bluetoothd crash report appeared. This confirms the observed playback session,
not indefinite reliability or a proven cause of the improvement.

The fresh status response reported beta4, GuardZoneCreated=true and
TrialActive=true, approximately 11 MB resident memory. No preference file or
disable marker was present during inspection, so default-enabled settings
applied. Only the logging utility was added for this test; the tweak and
Bluetooth configuration were not changed. Log capture was stopped afterward.
Private raw Bluetooth logs and device identifiers are not published.

## Download and installation

Refresh the Ego-iPod source in Zebra and select Pro-Pods 2.0.0~beta4:

https://ego-tistic.github.io/Ego-iPod/

[Exact package](debs/com.propods.tweak_2.0.0~beta4_iphoneos-arm.deb)

Package SHA256:
`635d4d60b60935b61750a53b8a53ef984858294fbc13c13a62fe54e7b8bcc983`

Installed main dylib SHA256:
`36f7a1a8e4cd535560360642b428277de1f934459559de0b978e26d86cc22f22`

Requires mobilesubstrate (>= 0.9.5000), preferenceloader, and firmware
>=12.5.8 and <12.5.9. Conflicts with PodsGrant (`com.lns.pogr`).

## Existing limits remain

The binary is still a guarded-heap diagnostic with a nominal ten-minute trial
and 96 MiB memory cutoff. The source limits were not removed to label this
release. Long playback, reboot behavior and repeated reconnections on this
second iPod have not been validated. Keep a currently working session intact;
there is no need to reinstall the identical package on the test device.

See [beta4 configuration and recovery](Pro-Pods-beta4.md) for enable/disable
markers, daemon restart requirements and the beta2 recovery option.

Adapted from [PodsGrant](https://github.com/LNSSPsd/PodsGrant) by Ruphane / LNSSPsd.
The retained [MIT license](LICENSE) credits upstream and adaptation contributors.
