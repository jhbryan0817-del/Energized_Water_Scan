> **Historical revision.** Current geometry, BOM and sensing architecture are [Rev-C.1](RevC_Articulated_Probes.md). Fixed-electrode and magnetometer instructions below are superseded.

# Rev-A.1 light design audit â€” 24 September 2026

## Scope and baseline

Reviewed all repository documentation, CAD/print inventories, previews and prior verification reports at commit `a364aa5ba2249f480e7dcc9e9159f0153d982758`. Inspected the open editable Fusion document `Energized_Water_Scanner` through its local MCP server. The live model had the same 950 timeline items, 39 user parameters and corresponding geometry as the published baseline. Its unsaved state was backed up before edits.

This is a mechanical packaging and serviceability revision. The repository still has no validated sensing firmware, production PCB, calibrated hazard thresholds, flotation qualification or field-test evidence. The original hardware document records design intent; its instructions are not an independent authorization to purchase hardware or redesign the project.

## Findings and corrections

| Finding | Evidence before change | Rev-A.1 correction |
|---|---|---|
| Electrode heads cannot clamp the exterior seal | Each head ended at Z=-10 mm; the sealing washer started at Z=-1 mm: a 9 mm air gap | Move the four heads to Z=-4â€¦-1 mm and shorten shank envelopes to 18 mm from Z=-1â€¦17 mm. Preserve internal nut/washer positions and electrode XY spacing. Exposed electrode depth changes from 13 to 4 mm below the hull datum. |
| Battery occupies motor-terminal space | Battery intersects the existing `Motor_rear_terminals` service envelope by 408.198 mmÂ³ | Add `battery_audit_forward_shift=6 mm`; move battery and its removal envelope forward. Extend the tray base and side rails 3 mm toward the bow. Battery is now X=-101â€¦3 mm; tray X=-104â€¦15 mm. |
| Reserved power-wire route is obstructed | Route overlaps the battery tray by 120 mmÂ³ and motor mount by 24.847 mmÂ³ | Move the 6 mm wide reserved route from Y=-26â€¦-20 to Y=-31â€¦-25 mm. It remains a routing envelope, not a printed duct or cable restraint. |
| Tiller has no positive torque/axial connection | A 3 mm shaft sits in a 3.2 mm cylindrical tiller socket; no cross-pin or clamp | Add matching 1.3 mm transverse holes in tiller and stock at X=278, Y=0, Z=67 mm, along X. Include a purchased 1.2 Ã— 8 mm retained-pin envelope. |
| Rudder can lift through its bearing | No lower axial stop | Add a purchased collar allocation: maximum Ã˜8 Ã— 5 mm, Z=34.5â€¦39.5 mm, 0.5 mm below the bearing. Select a real 3 mm-bore locking collar; the modeled 3.2 mm bore is a clearance envelope. |
| Steering rod clips hull near full travel | First sampled sweep found rod/hull intersections at +33Â°, +34Â° and +35Â° (up to 1.502 mmÂ³) | Enlarge hull steering seat from Ã˜6 to Ã˜7 mm; update boot neck allocation to Ã˜7 and outer flange/bellows allocation to Ã˜10 mm. Real boot remains to be selected and tested. |
| Regulator model provenance was overstated | Child model source is named D24V10F3 (3.3 V), while BOM specifies D24V10F5 (5 V) | Relabel the actual body-owning component `D24V10F5_PACKAGE_PROXY_from_D24V10F3_STEP_VERIFY`. Electrical procurement remains the F5; geometry is a packaging proxy pending exact-part verification. |

The tiller pin must be retained against walking out. Match-drill/ream the actual shaft and tiller in a jig; the printable 1.3 mm hole is a pilot/clearance intention, not a qualified FDM fit. Verify shaft strength and steering torque. The blade retains the existing bonded stock socket. The lower collar's locking screw and the pin retainers are not detailed in CAD.

The revised electrode envelope corresponds to an 18 mm under-head length. Select or trim actual hardware to the measured seal/lug/nut stack, deburr it and verify thread engagement. The CAD includes no terminal lug thickness and models the seal uncompressed; this correction establishes contact, not a proven watertight joint.

## Verification method

- Recompute the editable design and explicitly collect warning/error states. Unknown timeline-group states and a rolled-back legacy feature are reported separately, not misreported as errors or silently called healthy.
- Check physical solid pairs using exact temporary BRep intersections, including the normally hidden hatch. Exclude `DATUM`, `REFERENCE`, `OPTION` and `CLEARANCES` components; skip pairs within the same occurrence because purchased multi-body representations include intentional intersections.
- Check service volumes separately. Containment of the object being serviced is expected. Battery removal requires the hatch to be removed. The broad provisional linkage box is not a swept-motion proof.
- Solve the ideal 131 mm rigid steering linkage at 71 rudder positions, -35Â° to +35Â° in 1Â° increments. Test moving blade, tiller, pin, horn, link pins and rod against static obstacles. Flexible boot, stock contact and unmodeled clevises/fasteners are excluded. This is sampled geometry, not a continuous collision or load simulation.
- Regenerate all 12 STL files from Fusion and check binary integrity, welded edge incidence, winding, degeneracy, connectedness, dimensions and positive signed volume. These checks do not detect every possible self-intersection or establish watertight manufacture.

Machine-readable results: [assembly and steering](../verification/RevA1_Assembly_Audit.json), [STL checks](../verification/RevA1_STL_Check.json). Earlier JSON files retain the previous revision's evidence only.

## Final CAD results

- 89 physical solids; zero detected cross-component volume overlaps; zero Boolean-operation failures.
- 967 timeline items and 40 user parameters; zero feature warnings/errors. Existing Group2/Group3 report Unknown state (5); legacy Hollow_interior reports RolledBack state (4). They are preserved and explicitly recorded.
- No static obstacles intrude into the revised motor-terminal or power-wire service envelopes. Battery removal is clear with the hatch removed.
- No collisions with tested static obstacles at the 71 sampled steering positions after enlarging the port. Ideal servo rotation ranges from +41.183Â° at -35Â° rudder to -43.564Â° at +35Â° rudder, relative to the modeled neutral position. These are geometric predictions, not controller calibration values.
- All 12 binary STL exports passed: one connected component each, zero unmatched/nonmanifold edges, zero inconsistent winding edges, zero degenerate triangles and positive signed volume. STEP contains 89 solid records; native F3D reimport into Fusion passes; print ZIP matches all individual STLs. See [export checks and hashes](../verification/RevA1_Export_Check.json).

## Remaining limitations and build gates

1. **Purchased parts and hardware:** Confirm exact motor screw engagement, horn spline and arm length, shaft/coupling fits, collar locking, pin retention, electrode stack, board supports and connector bend radii. Bonded motor supports/rail/rudder bracket still need a qualified attachment process. Do not infer a fastening method from zero interference.
2. **Steering boot:** Confirm the real boot accommodates both rod stroke and lateral movement without leakage or binding; actual clevis geometry is absent. Set servo travel only after dry testing.
3. **Battery adjustment:** The new forward position clears the modeled motor terminal volume. Moving aft undoes this fix. Recheck terminal clearance and battery removal after any trim adjustment; restrain with straps without compressing the pack.
4. **Sealing:** Hatch gasket compression and cover stiffness are not validated. Pod lid/cable exit, four electrodes, stern tube and moving pushrod remain leak-test gates. The collar/pin changes do not seal a joint.
5. **Flotation and strength:** No mass-calibrated center of gravity, displacement/freeboard, stability or structural analysis. Print density and hardware masses are not validated. Conduct ballast/flotation and mechanical load checks before powered water testing.
6. **Manufacturability:** The 400 mm hull requires an appropriate build volume. No split hull joint is introduced in this light audit. Material, orientation, support removal and dimensional process capability remain unqualified.
7. **Parameter limits:** Forty user parameters are retained, but many legacy interfaces and placements use fixed dimensions. This is not a fully scalable boat generator. After changing master dimensions, rerun checks and inspect every dependent interface.
8. **Sensing:** Keep the existing experimental status: a negative reading does not show that water is safe. Mechanical fit does not validate the electrical front end or detection performance.

## API references used

Autodesk's [temporary BRep operations](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_TemporaryBRepManager_booleanOperation.htm) and [STL export API](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_ExportManager_createSTLExportOptions.htm), plus the installed Fusion server's API documentation, informed the scripts. Supplier prices and availability were not re-audited.
