# Ego-iPod package repository

Add `https://ego-tistic.github.io/Ego-iPod/` to Cydia or Zebra. This replaces the old Pro-Pods repository address after the GitHub repository is renamed and Pages deploys.

## Mac-Launcher 1.0.0

Rootful arm64 iOS 12 launcher. Activator, PreferenceLoader and compatible MobileSubstrate injection are required. Opacity snaps to 5% steps (0–100%); a dark/light theme switch, magnifying dock, searchable drawer and five-item recent section are included. Build/package/signature checks passed; final-device interaction and runtime tests remain pending. See the [source archive](sources/Mac-Launcher-1.0.0-source.zip), its README/VALIDATION documents and [MIT license](Mac-Launcher-LICENSE). Internal package ID remains `io.github.orbitlauncher` to preserve upgrades/settings.

## Pro-Pods 1.0.2~diagnostic2

The existing Pro-Pods package and original LICENSE are preserved. Targets iPod7,1/iOS 12.5.8 rootful; pairing compatibility remains unverified. Do not install alongside PodsGrant; the package declares that conflict. The Pro-Pods source repository is separate and private.

Adapted from [PodsGrant](https://github.com/LNSSPsd/PodsGrant) by Ruphane, upstream commit d727bf4f26474b6504be82fdbe0f391ff746db6d. See LICENSE.

## Indexes

This is a flat APT repo. Packages, Packages.gz, Packages.bz2 and Release are generated from both real debs, with package and index checksums. Origin/Label are Ego-iPod. No signing key was introduced or replaced; the existing repository was unsigned.
