# Pro-Pods crash review — November 4, 2026

This is a sanitized technical summary. The user's original crash report and
Apple executable are not published.

## What the supplied report establishes

- iPod7,1, iOS 12.5.8 (16H88): bluetoothd suffered EXC_BAD_ACCESS / SIGSEGV,
  with an invalid access at address 0x30, approximately ten seconds after launch.
- The triggered thread is RxLoop. Its top five frames are in
  libsystem_malloc.dylib. The first daemon frame is +0x1336ec.
- The loaded Pro-Pods UUID exactly matches our archived **2.0.0~beta1** binary.
  It differs from beta2's UUID. This report therefore documents a process that
  still had beta1 loaded; it does not establish whether beta2 is currently
  installed or whether Bluetooth crashes without the earlier hooks.

## Matching the stack to the uploaded daemon

The daemon UUID matches the uploaded executable. Subtracting its runtime image
base from the return addresses gives these leading daemon frame offsets:
0x1336ec, 0x54334, 0xf5718, 0x10a82c, 0x10a428, 0xd719c, 0xd7604,
0x3e790, and 0x3c390.

At +0x1336e8, the characteristic-read response handler calls an allocation
wrapper at +0x53190. The wrapper tail-calls malloc_zone_malloc. The following
instruction is the reported return address +0x1336ec. Nearby code appends read
data and handles continuation reads. Native logging identifies this as a
characteristic-read path, and the receiving parser contains ATT handling.

This is an allocator crash during Bluetooth receive processing. Earlier heap
corruption is a plausible explanation; a damaged allocation zone or another
memory defect cannot be distinguished from this report alone. The fault address
0x30 is not sufficient to identify the original bad write. Neither an audio
codec failure nor product-ID mapping is demonstrated by this stack. No Pro-Pods
frame appears on the crashed thread, which also does not exclude earlier damage
from an injected tweak. Other injection components are present in the report.

## Required comparison before another compatibility patch

1. Remove Pro-Pods through the package manager. If dpkg reports an interrupted
   operation, complete `dpkg --configure -a` as root, then remove Pro-Pods.
2. Restart the iPod, then re-jailbreak. This is needed to unload already-injected
   beta1 code. Merely turning off a preference or installing a replacement file
   cannot unload the old code from an existing daemon process.
3. Connect the headphones and play audio again.
4. If it disconnects, share the newest bluetoothd crash report from that test.
   Its image list should no longer contain Pro-Pods.dylib. If there is no new
   report, report that result; a disconnect can happen without a crash.

The APT index continues to offer beta2 as a recovery package, with no product-ID
or feature-version hooks. There is no new .deb or proven playback fix from this
report. No further hook is justified until the comparison identifies whether
this failure occurs without Pro-Pods. Hardware testing remains outstanding.
