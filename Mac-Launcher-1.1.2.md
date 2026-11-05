# Mac-Launcher 1.1.2

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
