# Activator installation prerequisite

Mac-Launcher already requires Activator (`libactivator`) automatically. First add
**https://rpetri.ch/repo/** in Cydia or Zebra and refresh sources; then installing
Mac-Launcher will also install Activator and its available dependencies.
See [Activator setup, upstream source and redistribution assessment](ACTIVATOR.md).

# Mac-Launcher 1.1.2 update


Refresh https://ego-tistic.github.io/Ego-iPod/ in Cydia or Zebra, then upgrade
Mac-Launcher to **1.1.2**. The package manager offers a respring after dpkg completes. CLI installation prints a manual respring reminder. Close and reopen
Settings afterward so it loads the updated preference bundle.

- Installer repair: maintainer scripts no longer respring during dpkg configuration; they request the GUI respring button.
- Settings → Mac-Launcher → Theme: **Dark**, **Light**, or **Custom Color**.
- Custom Color Wheel: choose a hue/saturation on the wheel, then adjust
  brightness. Hue/Saturation/Brightness sliders also support accessibility.
  Choosing a color selects the Custom Color theme.
- Surface Opacity: **0–100% in 5% steps**. Each changed step saves during
  dragging, including interrupted drags. Close/reopen the launcher to apply.
- Reduce Transparency disables blur but no longer overrides the opacity value.
  Blur Behind Dock stays separately controlled. App icons/text remain opaque.
- Remaining user-facing Orbit wording is now Mac-Launcher. Existing app choices,
  recents and Activator assignments are preserved by retaining compatibility IDs.

This update changes the slider save path, consistent preference synchronization,
glass/shadow opacity and blur rendering. It uses iOS 12-compatible APIs rather
than the iOS 14 system color picker or iOS 26 Liquid Glass framework.

Compile, native opacity tests, repo tests, package architecture/deployment,
ad-hoc signatures and rootful metadata checks passed. **Physical iPod touch,
Amethyst injection, Preferences touch handling and visual behavior are untested
here.** Please check 0%, 35%, and 100% after installation, in both drawer and dock.

[Download .deb](debs/io.github.orbitlauncher_1.1.2_iphoneos-arm.deb) ·
[MIT source](sources/Mac-Launcher-1.1.2-source.zip)

## Earlier repository notes

# Mac-Launcher 1.1.1 update


Refresh https://ego-tistic.github.io/Ego-iPod/ in Cydia or Zebra, then upgrade
Mac-Launcher to **1.1.1**. The package manager offers a respring after dpkg completes. CLI installation prints a manual respring reminder. Close and reopen
Settings afterward so it loads the updated preference bundle.

- Installer repair: maintainer scripts no longer respring during dpkg configuration; they request the GUI respring button.
- Settings → Mac-Launcher → Theme: **Dark**, **Light**, or **Custom Color**.
- Custom Color Wheel: choose a hue/saturation on the wheel, then adjust
  brightness. Hue/Saturation/Brightness sliders also support accessibility.
  Choosing a color selects the Custom Color theme.
- Surface Opacity: **0–100% in 5% steps**. Each changed step saves during
  dragging, including interrupted drags. Close/reopen the launcher to apply.
- Reduce Transparency disables blur but no longer overrides the opacity value.
  Blur Behind Dock stays separately controlled. App icons/text remain opaque.
- Remaining user-facing Orbit wording is now Mac-Launcher. Existing app choices,
  recents and Activator assignments are preserved by retaining compatibility IDs.

This update changes the slider save path, consistent preference synchronization,
glass/shadow opacity and blur rendering. It uses iOS 12-compatible APIs rather
than the iOS 14 system color picker or iOS 26 Liquid Glass framework.

Compile, native opacity tests, repo tests, package architecture/deployment,
ad-hoc signatures and rootful metadata checks passed. **Physical iPod touch,
Amethyst injection, Preferences touch handling and visual behavior are untested
here.** Please check 0%, 35%, and 100% after installation, in both drawer and dock.

[Download .deb](debs/io.github.orbitlauncher_1.1.1_iphoneos-arm.deb) ·
[MIT source](sources/Mac-Launcher-1.1.1-source.zip)

## Earlier repository notes

Repository icon: an original silver iPod Classic illustration, served at `CydiaIcon.png` for Zebra/Cydia, with @2x/@3x variants and editable `repo-icon.svg`. Refresh sources after publication; cached icons may require restarting Zebra.

# Mac-Launcher 1.1.0 update


Refresh https://ego-tistic.github.io/Ego-iPod/ in Cydia or Zebra, then upgrade
Mac-Launcher to **1.1.0**. Installation resprings SpringBoard. Close and reopen
Settings afterward so it loads the updated preference bundle.

- Settings → Mac-Launcher → Theme: **Dark**, **Light**, or **Custom Color**.
- Custom Color Wheel: choose a hue/saturation on the wheel, then adjust
  brightness. Hue/Saturation/Brightness sliders also support accessibility.
  Choosing a color selects the Custom Color theme.
- Surface Opacity: **0–100% in 5% steps**. Each changed step saves during
  dragging, including interrupted drags. Close/reopen the launcher to apply.
- Reduce Transparency disables blur but no longer overrides the opacity value.
  Blur Behind Dock stays separately controlled. App icons/text remain opaque.
- Remaining user-facing Orbit wording is now Mac-Launcher. Existing app choices,
  recents and Activator assignments are preserved by retaining compatibility IDs.

This update changes the slider save path, consistent preference synchronization,
glass/shadow opacity and blur rendering. It uses iOS 12-compatible APIs rather
than the iOS 14 system color picker or iOS 26 Liquid Glass framework.

Compile, native opacity tests, repo tests, package architecture/deployment,
ad-hoc signatures and rootful metadata checks passed. **Physical iPod touch,
Amethyst injection, Preferences touch handling and visual behavior are untested
here.** Please check 0%, 35%, and 100% after installation, in both drawer and dock.

[Download .deb](debs/io.github.orbitlauncher_1.1.0_iphoneos-arm.deb) ·
[MIT source](sources/Mac-Launcher-1.1.0-source.zip)

## Earlier repository notes

# Pro-Pods recovery notice


The reported beta1 session shows repeated bluetoothd restarts, often approximately ten seconds apart, with no successful product mappings. Older logs contain implausible output values. The getter ABI/output interpretation requires validation; function hashes alone do not establish its correctness.

**Beta2 removes all Bluetooth mapping hooks. It is not a disconnect fix.** Its binary has no hook-installer references. It keeps only bounded logging and fresh-response status. No Settings switch can re-enable interception in this build.

Upgrade to 2.0.0~beta2 OR uninstall Pro-Pods, then **restart and re-jailbreak**. Old hooks remain loaded until that process is restarted. Turning Enabled off in beta1 alone does not uninstall hooks. Native iOS 12 headphone compatibility is not guaranteed after recovery.

Beta1 and earlier Pro-Pods builds are withdrawn from the package index. Their archived files remain only for existing cached URLs; do not reinstall them. Mac-Launcher is unchanged. The next compatibility patch requires the matching system bluetoothd binary and a fresh crash report. Repeated restarts do not establish whether the cause is this tweak, a native daemon bug, another tweak, or an external event.

## Earlier repository notes (superseded for Pro-Pods)

# Ego-iPod package repository

Add `https://ego-tistic.github.io/Ego-iPod/` to Cydia or Zebra. This replaces the old Pro-Pods repository address after the GitHub repository is renamed and Pages deploys.

## Mac-Launcher 1.0.0

Rootful arm64 iOS 12 launcher. Activator, PreferenceLoader and compatible MobileSubstrate injection are required. Opacity snaps to 5% steps (0–100%); a dark/light theme switch, magnifying dock, searchable drawer and five-item recent section are included. Build/package/signature checks passed; final-device interaction and runtime tests remain pending. See the [source archive](sources/Mac-Launcher-1.0.0-source.zip), its README/VALIDATION documents and [MIT license](Mac-Launcher-LICENSE). Internal package ID remains `io.github.orbitlauncher` to preserve upgrades/settings.

## Pro-Pods 2.0.0~beta1

New experimental Legacy Audio identity mapping for AirPods Pro 3 / Lightning and USB-C Max. Live Settings switches, fresh-response daemon status, bounded scalar diagnostics and root recovery helper. Max 2 remains opt-in. Host build/mapping/signature checks passed; a fix for connection drops has not been confirmed on hardware. Firmware is restricted to 12.5.8, with runtime iPod7,1 / exact daemon UUID/function-hash checks.

**Restart and re-jailbreak after upgrading; respring is insufficient.** Reopen Settings → Pro-Pods. See [installation/recovery instructions](Pro-Pods-2.0-INSTRUCTIONS.md). The Pro-Pods source remains private; no private source archive is published as part of this package update.

## Previous Pro-Pods 1.0.2~diagnostic2

The existing Pro-Pods package and original LICENSE are preserved. Targets iPod7,1/iOS 12.5.8 rootful; pairing compatibility remains unverified. Do not install alongside PodsGrant; the package declares that conflict. The Pro-Pods source repository is separate and private.

Adapted from [PodsGrant](https://github.com/LNSSPsd/PodsGrant) by Ruphane, upstream commit d727bf4f26474b6504be82fdbe0f391ff746db6d. See LICENSE.

## Indexes

This is a flat APT repo. Packages, Packages.gz, Packages.bz2 and Release are generated from all packaged debs, with package and index checksums. Origin/Label are Ego-iPod. No signing key was introduced or replaced; the existing repository was unsigned.
