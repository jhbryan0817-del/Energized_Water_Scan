# Current revision tools

Fusion scripts expose `run(context)` and operate on the active `Energized_Water_Scanner` design. Run with the Fusion Python API/MCP bridge; they are not ordinary standalone Python programs. Keep other documents inactive during execution.

1. `audit_interfaces.py`: measure propulsion alignment, battery clearance and boundary allocations.
2. `audit_service.py`: selected rigid tool corridors and sampled removal paths.
3. `audit_native_poses.py`: verify native electrode positions; restore stowed pose.
4. `audit_assembly.py`: all physical-solid static pairs and 2° sampled probe motion; records intentional overlaps separately.
5. `capture_previews.py`, then `export_current.py`: current views, millimetre STL files, ZIP, physical STEP and native F3D.
6. `verify_native_archive.py`: reopen archive, compare audited geometry and native controls, then save original Fusion cloud document.
7. Run `python check_exports.py` outside Fusion for mesh, file and audit consistency. It requires NumPy through `check_mesh.py`. Run `python gradient.py` for the synthetic measurement geometry checks.

`set_pose.py` sets the four native angle parameters; edit its POSE setting deliberately. It does not drive real servos. Revision change reports in verification record alignment, reinforcement and battery changes. Fixed mechanical dimensions are modeled features, not a fully generative master-parameter rebuild.

Do not interpret a geometric PASS as successful waterproofness, electrical safety, torque, structural life, continuous flexible motion or flotation testing.

For the 28–29 September audit, 3D export and upload are deliberately deferred. Run inspection/audit scripts independently; do not run `export_current.py` or `verify_native_archive.py` as part of this deferred-export policy. Historical RevE export reports describe the checked-in files, not proof that later live edits are included. See [build qualification](../docs/Build_Qualification.md) for physical test gates.


Rev-E1 post-repair validation is recorded in `verification/RevE1_Assembly_Audit.json` and `verification/RevE1_Repair_Record.json`. The read-only `audit_reve1.py` repeats the assembly/motion check without exporting geometry. Historical reports retain their original revision scope.
