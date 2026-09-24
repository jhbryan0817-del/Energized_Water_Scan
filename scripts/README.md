# Verification scripts — Rev-B

`check_stl.py` uses Python 3's standard library. Run `python scripts/check_stl.py` from the repository root. It checks twelve binary STLs and writes `verification/RevB_STL_Check.json`.

`fusion_audit.py` runs inside Autodesk Fusion with `Energized_Water_Scanner` active. It reads the design and writes `verification/RevB_Assembly_Audit.json`, checking physical-solid intersections, feature health, service-volume intersections and 71 ideal steering positions.

`fusion_service_audit.py` runs in the same environment and writes `verification/RevB_Service_Audit.json`. It checks screwdriver/grip allocations and tray removal sampled every 5 mm over 100 mm. Its exclusions require the hatch, battery, battery tray and servo horn/linkage to be removed and wiring disconnected first.

Keep the scripts in this repository's `scripts` directory when running them so `__file__` resolves the output directory. Recompute the model first. These checks are specific to the current component names and coordinates; update them after layout changes. They can take several minutes.

Read [the compact-layout report](../docs/RevB_Compact_Enclosure.md) for exclusions and assembly order. Passing geometry and mesh checks does not qualify manufacturing, sealing, structural loads, flotation or sensing performance.
