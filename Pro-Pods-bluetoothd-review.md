# Pro-Pods: uploaded Bluetooth daemon review

November 4, 2026. This review analyzes the supplied binary without executing,
modifying, or redistributing it. It does not establish the cause of a disconnect.

## Confirmed findings

- The uploaded arm64 daemon matches the previously required UUID and SHA-256.
  The old build was not simply targeting a different daemon image.
- The device-ID getter uses four 32-bit output pointers and a boolean success
  result. The previous argument-size suspicion is not supported by this binary.
- The second function previously described as a "HID product ID" getter is
  actually a supported-features-version getter. Its corresponding setter logs
  `supportedFeaturesVersion`, and its caller reads
  `APPLE_DEV_FEATURES_VERSION_KEY`. It stores a 16-bit value internally and
  writes a 32-bit output. Product-ID mapping must not be applied to it.
- The actual device-ID setter stores source, vendor, product and version before
  notifying another component. Altering a getter result later does not change
  that stored identity. This is a limitation of the old approach, not proof that
  hooking the setter would fix playback. No new setter hook is being shipped.

The user's beta1 report recorded 17 device-getter calls, zero mappings, and zero
calls to the second getter in that snapshot. The misclassified second function
is a code/design defect, but those counts do not show that it caused this
disconnect. The repeated startup records establish repeated daemon starts, not
their reason. Exhaustive product-mapping tests did not validate function
semantics, Bluetooth negotiation, or real playback.

## Current package

Pro-Pods **2.0.0~beta2 remains the recovery version** in the APT index. Its
binary contains neither of the old function hooks. There is no new compatibility
package or demonstrated disconnect fix from this review. Earlier builds remain
withdrawn. If beta1 is still installed, upgrade to beta2 or uninstall Pro-Pods,
then restart and re-jailbreak to unload the old hooks.

## Next evidence needed

A recent **bluetoothd crash report**, captured after a playback disconnect, can
identify the failing thread and exception. In a file manager, check
`/var/mobile/Library/Logs/CrashReporter/` and `/Library/Logs/CrashReporter/` for
the newest file whose name starts with `bluetoothd`. Share that file privately;
it can contain device identifiers. Do not upload the Apple daemon to the repo.
If no report exists, that does not rule out termination or a non-crash
disconnect; a device log from the same time is needed next.

No hardware pairing, playback, crash reproduction, or Amethyst injection test
was possible in this workspace. Device IDs, feature versions, and codec/audio
profile compatibility must not be treated as interchangeable.
