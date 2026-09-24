# Energized Water Scan

**Rev-B — compact mechanical layout, 24 September 2026.** The hull is now **320 × 170 mm**, reduced from 400 × 190 mm: **80 mm shorter and 20 mm narrower**. Existing purchased components retain their original sizes. This is an experimental surface-craft packaging design, not a qualified production release.

![Rev-B open assembly](previews/RevB_assembly.png)

## Start here

- [Compact layout, dimensions, assembly order and limits](docs/RevB_Compact_Enclosure.md)
- [Current print and procurement checklist](docs/Print_and_Procurement.md)
- [Editable Fusion design — Rev-B](cad/Energized_Water_Scanner_RevB.f3d)
- [Physical assembly STEP — Rev-B](cad/Energized_Water_Scanner_RevB.step)
- [All 12 current printable parts](prints/Print_STLs.zip), or [individual STLs](prints/)
- [Assembly and steering audit](verification/RevB_Assembly_Audit.json), [service audit](verification/RevB_Service_Audit.json), and [STL checks](verification/RevB_STL_Check.json)
- [Export verification](verification/RevB_Export_Check.json)

## What changed

The battery sits transversely across the bow, centered laterally. The controller, front-end board, ADC and regulator are repacked beside the drivetrain, with matching supports. The shorter electronics tray has relocated mounting pillars and transverse strap passages. Hatch, gasket, lip and fasteners follow the shorter opening. The magnetometer rail is shortened and moved with its pod; shaft and steering alignment remain intact.

The 245 × 130 mm hatch allows the electronics tray to lift out after removing the battery and its tray, disconnecting wiring, and removing the servo horn/linkage. **USB access also requires removal of the battery and battery tray.** Assemble and wire the boards outside the hull before installing the tray.

The chosen length reduction is 80 mm of the requested maximum 100 mm. A 300 mm hull has not been validated. The default craft including its forward sensor rail and external rudder is approximately **445 mm long**; 320 mm refers to the hull alone.

## CAD and printing

Use the Rev-B files together. Reprint the hull, hatch, electronics tray and magnetometer rail. Other parts retain their shapes; all STLs are regenerated in millimeters and retain assembly coordinates. Place and orient them in the slicer. The 320 mm hull still requires an appropriate printer build volume.

The native F3D retains 40 user parameters and an editable timeline. Some interfaces remain fixed dimensions; changing master parameters requires a new audit. STEP contains physical printed and purchased-part representations, including the hatch, with optional/reference/clearance geometry excluded.

## Verification and limits

CAD checks report **89 physical solids, zero detected cross-component volume overlaps and zero feature warnings/errors**. The 71 sampled steering positions (±35°), sampled tray lift, screwdriver corridors and battery pull-loop allocation have no detected tested-obstacle collisions. The reports document exclusions, expected service-volume intersections and required disassembly. All twelve STL meshes pass the topology checks.

These are geometric checks, not proof of real connector fit, hand assembly, print tolerances, continuous motion, strength, waterproofing, flotation or sensing performance. Dry-assemble actual hardware and repeat trim, leak and magnetic-interference tests for the smaller hull.

The sensing system is experimental and is not protective equipment. A negative measurement does not establish that water is safe. There is no validated detection firmware, production PCB or calibrated hazard threshold in this repository.

## Repository layout

| Folder | Contents |
|---|---|
| `cad/` | Rev-B F3D and physical STEP; previous Rev-A.1 exports retained for reference |
| `prints/` | Twelve current Rev-B STLs and matching ZIP |
| `docs/` | Current compact-layout report/checklist and historical baseline/audit |
| `previews/` | Current Rev-B and historical assembly views |
| `verification/` | Current `RevB_*` evidence; other reports are historical |
| `scripts/` | Re-runnable current Fusion, service-access and STL audits |

Historical [Rev-A.1 audit](docs/RevA1_Design_Audit.md) and [original hardware baseline](docs/Energized_Water_Scan_RevA_Hardware_and_CAD.md) explain prior design intent. Their coordinates and print instructions do not supersede Rev-B.
