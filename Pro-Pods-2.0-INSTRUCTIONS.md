# Pro-Pods 2.0 beta — start here

This is the rebuilt test package for your Pro 3 / Max disconnects. **It is not yet a confirmed fix.**

1. Install Pro-Pods_2.0.0-beta1.deb over your existing Pro-Pods. PreferenceLoader and compatible MobileSubstrate injection are required. Do not run it alongside PodsGrant.
2. **Restart the iPod, then re-jailbreak.** A respring alone will not load the new Bluetooth component. Reopen Settings after upgrading.
3. Open **Settings → Pro-Pods → Show Runtime Status**. Leave Enabled, Pro 3, Max and Second ID Path on. Leave Old Pro Identity and Experimental Max 2 off. The default is Legacy Audio.
4. Pair and test **one headphone set at a time** with a downloaded song. The new default uses an older AirPods identity that iOS 12 supports; it does not add iOS 26 features or guarantee ANC menus. Use the headphones' physical noise-control buttons where supported.
5. If it still drops, **Copy Diagnostic Report** in Settings makes a report available for when you have time. No reply is needed now. A changing Bluetooth process ID means a daemon restart; the crash report is still needed to establish why.

Turn Enabled off to bypass mapping live after the new version is loaded. Root recovery command: `pro-podsctl disable`. If the daemon/device is stuck, use your jailbreak's documented no-tweak mode and remove Pro-Pods, then restart/re-jailbreak. No pairing databases or firmware are modified by this package.

Build, policy and package/signature checks passed on the computer. Headphone stability and the new Settings controls require the actual iPod. The public Ego-iPod repo's existing package has not been replaced with this untested beta.
