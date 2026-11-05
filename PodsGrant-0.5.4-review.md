# Uploaded PodsGrant 0.5.4 comparison

The user reports that audio worked until they disconnected the headphones, then
reconnection failed. That observation is retained; its cause is not established.
This inspection does not reproduce the successful session.

## Exact package inspected

- Package: com.lns.pogr, version 0.5.4, iphoneos-arm.
- SHA-256: 8065a81495474c77074f6fc348145c68fa7e663758a3408a1ddd9b3bf4614685.
- Main arm64 dylib UUID: 684eae6b-f34c-3cee-9edb-54ead9605250.
- Package contents were read as data. Maintainer scripts were not executed.
  Neither the uploaded .deb nor Apple executable is redistributed by this review.

## Bluetooth-hook setup on the supplied iOS 12 daemon

The shipped PGS_findAddresses function scans /usr/sbin/bluetoothd. The exact
shipped first pattern (10 mask/value pairs) and second pattern (5 pairs) both
produce zero matches in the supplied daemon. The compiled scanner reads aligned
32-bit words. The constructor returns before its MSHookFunction calls if address
discovery fails. Under these inputs, it does not install its three main daemon
hooks. Its separately named recvLoggingHandler is not wired into this
constructor, so its presence alone does not establish logging suppression.

This conclusion is conditional on the inspected package and supplied daemon
being the files used during the successful session. It is not an on-device hook
trace and does not show that no other component affected that session.

## Other behavior that differs from Pro-Pods beta1

The package also injects outside bluetoothd and installs Objective-C pairing
payload hooks, conditional on its enabled setting and class availability. These
rewrite the product ID in a copied advertisement payload. This path is separate
from the failed daemon pattern discovery. Availability and execution of these
private methods on the iPod have not been verified.

The compiled preset table includes 8231 -> 8206 for OS versions 0 through 15.
It does not include 8232 or the Max product IDs 8202, 8223, and 8237. Custom
mapping entries loaded from the settings file can take precedence. Those settings
have not yet been supplied. The exact package therefore must not be assumed to
contain every mapping present in newer upstream source.

Its post-install script sends TERM to bluetoothd, sharingd, heard, and
SharingViewService. A transient improvement after installation could involve
that restart, a pairing payload change, persisted state, or another cause.
Current evidence cannot distinguish them. A successful first connection is not
evidence of a stable reconnect implementation.

## Next useful artifact

Preserve and privately share this installed settings file before uninstalling:

`/var/mobile/Library/Preferences/com.lns.pogr.bin`

The package's removal script deletes it. This is a read/copy request, not a
request to edit or delete pairing records. If absent, report its absence.
Settings can show which custom identities and enable state were in use; they
cannot prove which runtime hook executed. A fresh crash after the failed
reconnect can then be compared with the existing allocator failures.

No new Pro-Pods compatibility .deb is published from this observation. Beta2
remains a recovery build, without Bluetooth mapping hooks. Pro-Pods declares a
conflict with PodsGrant; installing them together is not a supported test.
