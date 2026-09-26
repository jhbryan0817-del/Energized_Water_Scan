# Current verification scripts — Rev-C.1

Run Fusion scripts sequentially with the scanner active. Supply `__file__` when executing source text through MCP so outputs resolve inside this repository.

1. `revc_build.py`: one-time migration from exactly 1,250-item Rev-B.4. Backs up native design outside the repository; result has 1,439 items. Do not rerun on a migrated design.
2. `revc_interface_fixes.py`: one-time follow-up from 1,439 items, completing motor-foot and cartridge/entry clearance changes.
3. `revc_mesh_finish.py`: one-time finishing pass from 1,487 items, removing the tangent entry stub that failed mesh topology checks and trimming old rail-fill projections.
4. `revc_arm_finish.py`: one-time pass from 1,515 items, joining wire grooves to terminal pockets before the angle features. Final model has 1,523 items.
5. `revc_set_pose.py`: change POSE to `stowed`, `deployed`, `measurement`, or four angles in 0–90°. Four native user parameters drive root-level rotate features. Other dimensions are fixed migration geometry, not fully generative master parameters.
6. `revc_audit.py`: read-only BRep intersections, 5° probe-motion samples, feature health and exact electrode head positions. Writes `RevC_Assembly_Audit.json` without asserting a physical release.
7. `revc_gradient.py`: outside Fusion, Python 3 + NumPy. Tests rank/conditioning, signed DC/complex recovery, correlated reference noise and invalid angles. Writes `RevC_Observability.json`.
8. `revc_export.py`: export 21 stowed-pose STLs, ZIP, measurement-pose F3D/physical STEP and previews. Deletes only the three explicitly retired magnetometer STLs from the current print directory.
9. `revc_roundtrip.py`: reopen native export, compare body volumes, parameter expressions and timeline, then save the original cloud scanner design.
10. `revc_check_exports.py`: outside Fusion, check topology, winding, connectedness, BRep/mesh bounds and volume, ZIP contents, STEP count, native roundtrip and hashes. Imports the unchanged standard-library mesh checker from `revb4_check_stl.py`.

No script drives real servos or performs instrument acquisition. A geometric pass does not resolve the documented seal, horn, cable, strength, power or flotation gates. Older scripts below apply only to their original revisions.

# Verification scripts — Rev-B.4

Run `revb4_supplier_fixes.py` **once** on the unchanged 1,236-item Rev-B.3 design. It backs up the native model, changes PRINT_20 and four nut envelopes, and resolves regulator provenance. Final Rev-B.4 has 1,250 timeline items; never rerun this migration on it.

Run `revb4_supplier_audit.py`, `revb4_assembly_audit.py`, `revb4_service_audit.py`, `revb4_wiring_audit.py`, and `revb4_fastener_access_audit.py` through Fusion MCP on the active design. Run sequentially. The source comparison report records downloaded source hashes and translated nominal body bounds/volumes; it is not a manufacturing-tolerance certificate.

Then use `revb4_visuals.py`, `revb4_export.py`, `revb4_roundtrip.py`; the latter saves the authorized updated cloud design. Outside Fusion run `revb4_check_stl.py` then `revb4_check_exports.py`. Existing E2 coupon geometry is unchanged. All new reports use RevB4 filenames and preserve historical evidence. A regression pass never means full assembly release.

# Verification scripts - Rev-B.3

Current revision scripts:

1. `revb3_assembly_fixes.py` is a **one-time migration** from the untouched 1216-item Rev-B.2 model. Then run `revb3_relief_finish.py` to open the corner reliefs and remove thin edge lands. Do not rerun either migration on final Rev-B.3 (1236 items).
2. Run `revb3_assembly_audit.py`, `revb3_service_audit.py`, `revb3_wiring_audit.py` and `revb3_fastener_access_audit.py` inside Fusion with the scanner active. These use temporary BRep geometry and write `RevB3_*` evidence. The last script intentionally records blocked E1 tool volumes and `assembly_release_passed: false`; its regression assertion only requires no new unexpected intersections. It does not release assembly.
3. `revb3_coupon.py` exports the actual E2/motor-support hull subsection and checks the nominal 2 mm pilot floors. This temporary-document operation is not read-only. It does not change the scanner geometry.
4. `revb3_visuals.py` makes revision-specific previews; `revb3_export.py` exports all sixteen STLs/ZIP, native F3D and physical-only STEP. These use temporary documents or visibility changes.
5. `revb3_roundtrip.py` reopens the export, checks body volumes/feature health and saves the original cloud design. Run only as part of an authorized saved revision.
6. Outside Fusion, run `python scripts/revb3_check_stl.py` and then `python scripts/revb3_check_exports.py`. The latter also checks the coupon mesh and includes its hash.

Keep repository paths intact so `__file__` resolves the outputs. When using MCP with script text, set `__file__` to the actual script path or use a wrapper that loads that file. Never run multiple model operations concurrently. See [Rev-B.3 findings](../docs/RevB3_Assembly_Readiness.md).

## Historical Rev-B.2 scripts

The following scripts write Rev-B.2 filenames; do not run them against Rev-B.3 and overwrite historical evidence.

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
