# Pro-Pods beta2 recovery update

The reported beta1 session shows repeated bluetoothd restarts, often approximately ten seconds apart, with no successful product mappings. Older logs contain implausible output values. The getter ABI/output interpretation requires validation; function hashes alone do not establish its correctness.

**Beta2 removes all Bluetooth mapping hooks. It is not a disconnect fix.** Its binary has no hook-installer references. It keeps only bounded logging and fresh-response status. No Settings switch can re-enable interception in this build.

Upgrade to 2.0.0~beta2 OR uninstall Pro-Pods, then **restart and re-jailbreak**. Old hooks remain loaded until that process is restarted. Turning Enabled off in beta1 alone does not uninstall hooks. Native iOS 12 headphone compatibility is not guaranteed after recovery.

Beta1 and earlier Pro-Pods builds are withdrawn from the package index. Their archived files remain only for existing cached URLs; do not reinstall them. Mac-Launcher is unchanged. The next compatibility patch requires the matching system bluetoothd binary and a fresh crash report. Repeated restarts do not establish whether the cause is this tweak, a native daemon bug, another tweak, or an external event.
