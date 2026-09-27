# Energized Water Scan

**Rev-D — internal servos, recessed arms and stacked electronics, 27 September 2026.** The hull retains its **320 × 170 mm** footprint. Four HS-65HB probe servos now sit in integral internal wells with top-access covers. Four long underside channels receive the folded arms; electrode reach remains 150 mm below the original bottom at 90°.

**Mechanical packaging / fit prototype.** The internal timing transmissions are nominal allocations, with supplier selection, horn adapters, tension adjustment and retention still unreleased. Existing shaft-seal, wet-wire, protected-front-end and flotation validation gates remain open. The relocated steering servo and dogleg pushrod require a new steering travel check.

## Start here

- [Design, dimensions, sensing geometry and limitations](docs/RevD_Internal_Servos.md)
- [Current 23-piece print and procurement schedule](docs/Print_and_Procurement.md)
- [Wiring and assembly sequence](docs/Wiring_and_Assembly.md)
- [Editable Fusion design](cad/Energized_Water_Scanner_RevD.f3d) and [physical STEP assembly](cad/Energized_Water_Scanner_RevD.step)
- [Revision-matched fit-prototype STLs](prints/Print_STLs.zip)
- [Rigid-body/motion audit](verification/RevD_Assembly_Audit.json), [native angle-control audit](verification/RevD_Native_Pose_Audit.json), [service audit](verification/RevD_Service_Audit.json), [numerical geometry checks](verification/RevD_Observability.json), [export verification](verification/RevD_Export_Check.json)

![Internal wells and repackaged electronics](previews/RevD_open.png)

![Four recessed arms, stowed](previews/RevD_stowed_bottom.png)

The front pair folds aft in outer channels; the rear pair folds forward in inner channels. All four use independent 0–90° user parameters. The battery is longitudinal beneath a removable controller bridge; analog and power electronics sit on separate sides of the main cassette. A shaped hatch opening improves access while preserving the original footprint. Graphite, light gray and cyan replace the previous appearance scheme.

“Nearly flat” describes the stowed sensing appendages. The propulsion shaft, propeller, rudder and existing stern sleeve remain below/behind the hull. The channels are wet, open recesses, not sealed exterior doors.

Use [Rev-D pose controls](scripts/revd_set_pose.py) and the [updated geometry demonstrator](scripts/revd_gradient.py). The measurement preset is [60,20,20,45]°; three coherent signed voltage differences are required. The scripts do not drive real actuators or implement instrument firmware. Equal-angle poses cannot recover a 3D gradient. No magnetometer is installed, so results are in the boat frame.

## Repository layout

| Folder | Contents |
|---|---|
| cad/ | Current Rev-D F3D/STEP and historical versions |
| prints/ | Current 23 fit-prototype parts and matching ZIP |
| docs/ | Current design/BOM/assembly, with prior revisions labeled historical |
| previews/ | Open, closed, underside, wells, deployed and measurement views |
| verification/ | RevD evidence; earlier reports retained as historical |
| scripts/ | Reproducible migration/refinement, poses, audits and exports |
| coupons/ | Historical motor-support coupon; not a Rev-D actuator qualification |

Earlier Rev-A/B/C documents do not supersede Rev-D. A CAD clearance pass does not establish water tightness, mechanical life or sensing performance. No production PCB, calibrated instrument firmware or measured flotation result is supplied. A low or absent reading cannot establish that water is safe.
