# Verification scripts - Rev-B.2

Run `check_stl.py` with Python 3 from the repository root. It checks sixteen binary STLs for welded topology, winding, degeneracy, connectedness, dimensions and volume, and writes `verification/RevB2_STL_Check.json`.

Run the following inside Fusion with `Energized_Water_Scanner` active, retaining this repository directory structure so `__file__` resolves outputs:

- `fusion_audit.py`: physical-solid intersections, feature health, service allocations and 71 ideal steering positions; writes `RevB2_Assembly_Audit.json`.
- `fusion_service_audit.py`: screwdriver/grip allocations and tray lift sampled every 5 mm over 100 mm after the stated disassembly; writes `RevB2_Service_Audit.json`.
- `revb2_wiring_audit.py`: electrode-wire and tool corridors, printed-solid connectedness, E2 lug distances and support proximity; writes `RevB2_Wiring_Support_Audit.json`. Proximity alone is not proof of fastening.
- `revb2_visuals.py`: revision previews, restoring visibility afterward.
- `revb2_export.py`: sixteen STLs, matching print ZIP, native F3D and a physical-only STEP via a disposable design.
- `revb2_roundtrip.py`: reopen the exported F3D; compare all physical-body volumes, timeline, parameters and feature health; close its temporary document and save the original cloud design.

After exports and the native roundtrip, run `check_exports.py` with Python 3. It checks STEP solid count, native results, mesh-to-BRep dimensions/volumes, ZIP equality and SHA-256 hashes.

One-time migration order from the 1012-item Rev-B.1 baseline: `revb2_interfaces.py`, `revb2_finish.py`, `revb2_branding.py`, `revb2_mesh_corrections.py`, `revb2_exit_margin.py`, `revb2_transom_access.py`. Do not rerun migrations on the finished model. These fixed-coordinate scripts preserve the original timeline and add named features. They remove the tangent rail-boss junction, move the power tie slots clear of the ESC pedestal, finish the E2 exit at 12 x 7 mm, and open driver bores through the upper transom gussets.

See [current readiness gates](../docs/RevB2_Prototype_Readiness.md) and [assembly instructions](../docs/Wiring_and_Assembly.md). These scripts do not qualify printed screw strength, real hardware/connector fit, waterproofing, flotation or sensing performance. Historical `RevB1_*` reports describe older geometry.
