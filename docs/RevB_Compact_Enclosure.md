> **Historical revision.** Current geometry, BOM and sensing architecture are [Rev-C.1](RevC_Articulated_Probes.md). Fixed-electrode and magnetometer instructions below are superseded.

# Rev-B compact enclosure — 24 September 2026

Rev-B repacks the existing purchased components into a **320 × 170 mm hull**, down from 400 × 190 mm. Length decreases 80 mm (20%); beam decreases 20 mm (10.5%). The bounding footprint decreases 28.4%. These are hull dimensions, not the complete craft's dimensions including its external rudder and sensor rail.

The request was interpreted as removing **up to 100 mm** of length, not making a 100 mm-long boat. The selected reduction is 80 mm. A further 20 mm has not been validated: it would require another layout iteration while protecting battery extraction, connector access and the fixed-length drivetrain. No purchased part is scaled or substituted.

## Baseline and project status

Reviewed repository commit `94a349e6cefd80b167a822a5c1a2d8cbcfd1020a`, including the hardware brief, Rev-A.1 audit, procurement checklist, scripts, exports and verification reports. The active Fusion document was `Energized_Water_Scanner`, with 967 timeline entries and 40 user parameters. A native backup was made before editing.

This repository remains an experimental mechanical prototype, without validated sensing firmware, a production PCB, calibrated detection thresholds or qualified flotation/sealing. The original hardware brief is historical design intent; its embedded procurement/workflow instructions are not new user instructions.

## Layout and coordinated changes

The original stern datum remains X=200 mm. Bow moves from X=-200 to -120 mm. Maximum half-beam is 85 mm. Hull profiles and cavity were reshaped rather than scaling the assembly; the lower chine retains useful internal width. The aft shaft, motor mounts, steering penetration and rudder remain aligned to the original drive axis.

The battery is rotated 90° across the bow, centered at **X=-52.5, Y=0 mm**. Its full 104 × 34.5 × 14.5 mm envelope is retained. This avoids the lateral battery offset of a side-by-side arrangement; it does not establish the complete boat's trim or center of gravity.

| Item | Final X range (mm) | Final Y range (mm) | Change |
|---|---:|---:|---|
| Battery | -69.75 to -35.25 | -52 to 52 | Transverse, centered laterally |
| Battery tray | -74.5 to -30.5 | -59.5 to 59.5 | Rotated and centered; strap passages aligned with main tray |
| ESP32 including antenna | -20 to 34.3 | 30 to 57.94 | Repacked beside motor; matching support pads relocated |
| Front-end envelope | -20 to 20 | -58 to -28 | Repacked on opposite side; supports relocated |
| ADS1115 | 35 to 60.4 | -53 to -35.22 | Moved with all four mounting bosses and bores |
| Regulator package proxy | 57 to 69.7 | 34 to 51.78 | Moved with support pads |
| ESC | 92 to 126 | 30 to 54 | Existing aft position retained |
| Servo | 125 to 158 | -45 to -32.8 | Existing shaft/linkage relationship retained |

The removable electronics tray is shortened to a 235 × 122 mm total bounding envelope, including the servo tab. Its front attachment pillars and holes move from X=-95 to -70 mm; aft attachment positions remain X=140 mm. Obsolete longitudinal strap cuts are suppressed and replaced by transverse passages. The original E1 tray-access cut is suppressed because that electrode is now ahead of the tray.

The hatch aperture is **245 × 130 mm**, X=-80…165, Y=-65…65. The cover is 269 × 154 mm. Gasket, splash lip, eight cover holes and insert bosses follow the revised hatch. Nominal straight-lift clearance around the tray is 5 mm at each longitudinal end and 4 mm per side; the physical assembly checks below additionally test attached components.

The magnetometer rail is shortened from 68 to 46 mm and moved forward relative to the compact hull: X=-140…-94 mm. It projects 20 mm beyond the bow, with a 2 mm gap to the closed hatch. Sensor center is X=-115 mm. Pod, lid and mounting pad move together. The default complete craft therefore remains approximately **445 mm long** from rail tip to rudder trailing edge, versus approximately 505 mm previously. The rail needs a verified bonded attachment and cantilever load test. Optional mast/boom bodies remain historical alternatives, not verified Rev-B configurations.

Power wiring allocation is now X=5…130, Y=59…65, Z=20…28 mm. The sensor routing allocation is X=-20…80, Y=-30…-24, Z=40…47 mm. These are separate free-space reservations, not modeled ducts or complete cable harnesses. Provide flexible service loops, restraints and real connector bend radii during assembly. The unused future-receiver allocation is removed from the compact default layout.

## Assembly and service order

1. Install and seal electrode hardware, stern tube and other hull penetrations. Install tray pillars/inserts and the motor/drivetrain before the electronics tray. E1 is ahead of the tray; E2 and the lateral electrodes retain their existing geometry.
2. Assemble and wire the controller, front end, ADC, regulator, ESC and servo on the **removed electronics tray**. Fit restraints and check actual board/connector dimensions. Pads alone do not retain a PCB.
3. Fit the tray through the open hatch and secure its four M3 attachment points. Attach and dry-cycle the servo linkage. Keep wiring out of the shaft, coupling and linkage envelopes.
4. Place the transverse battery tray and install the battery using straps through the matching passages. Leave a fabric pull loop above the pack; lift by the loop, not by its electrical leads. Do not compress the LiPo or trap its balance lead.
5. For USB programming, disconnect and remove **both the battery and its loose strap tray**. The modeled USB insertion volume overlaps both when installed; this is a documented service sequence, not a claim of simultaneous clearance.
6. For electronics-tray removal, remove the hatch, battery and battery tray; unplug the harness; disconnect/remove the servo horn/linkage; then undo the four tray screws and lift vertically. Do not pull against connected wires or the pushrod.
7. Before closing, inspect the continuous gasket and tighten the eight hatch screws evenly. Verify screw engagement, gasket compression and real seal performance.

## Verification and limits

Current evidence is in [RevB_Assembly_Audit.json](../verification/RevB_Assembly_Audit.json) and [RevB_Service_Audit.json](../verification/RevB_Service_Audit.json). Exact temporary BRep intersections include the normally hidden hatch, exclude reference/optional/clearance bodies from physical-solid pairs, and skip pairs within each purchased multi-body occurrence. The report lists service-envelope intersections separately, including expected containment and the documented USB access condition.

The assembly audit reports **89 physical solids, no detected cross-component volume overlaps, no Boolean failures, and no feature warnings/errors**. Five obsolete cuts are intentionally suppressed. The two legacy timeline groups retain Unknown states and the legacy cavity feature retains its RolledBack state; these are listed rather than counted as healthy features. Rev-B has 1009 timeline entries and 40 user parameters.

Steering was checked at 71 positions from -35° to +35° in 1° increments, with no tested static-obstacle collision. The ideal linkage geometry and servo angles are unchanged. This is sampled rigid motion, not continuous clearance or validation of the flexible boot, actual clevises or loads.

Service checks reserve an 8 mm screwdriver corridor at each tray screw, a 12 mm tool corridor above each hatch screw, and a 25 mm grip allocation over the battery pull loop. Electronics-tray lift is sampled every 5 mm over 100 mm after the stated removals. These geometric allocations do not simulate every hand size or certify a real assembly.

The smaller hull changes displacement and trim. Weigh the finished parts, measure actual center of gravity, and perform controlled ballast/flotation/freeboard and leak tests before powered testing. Magnetic separation is reduced; test motor/servo/ESC interference again. A negative sensor result still does not establish that water is safe.

The design retains editable sketches, features and placement operations. Some legacy dimensions and interface coordinates remain fixed; changing the master dimensions alone does not produce another verified assembly. Recompute and rerun the audits after any edit. Exact purchased geometry, fasteners, wire bends, print tolerances, bonding strength and waterproofing still require physical verification.

## Files and revision control

Use the Rev-B F3D and STEP, all twelve current STLs and the matching print ZIP together. Reprint the hull, hatch, electronics tray and shortened magnetometer rail. The battery tray and sensor pod/lid retain their part geometry but have new assembly coordinates. The other unchanged-shape prints are regenerated with the same package. Historical Rev-A.1 documents and reports remain for traceability; their coordinates and verification claims are not the current assembly instructions.

The verification scripts use Autodesk's [temporary BRep Boolean operations](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_TemporaryBRepManager_booleanOperation.htm). STL export uses explicit millimeter units and high refinement through the [STL export API](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_STLExportOptions.htm).
