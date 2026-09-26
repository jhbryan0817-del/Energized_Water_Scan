# Energized Water Scan

**Rev-B.4 — supplier mechanical audit, 26 September 2026.** Verified official ADC/regulator model dimensions, checked nominal BOM dimensions, opened the regulator connection row in PRINT_20, and corrected M4 nut corner envelopes.

**Not yet ready to print everything and assemble.** E1 access is builder-accepted. Servo/horn/boot interfaces, complete harness, sensor feedthroughs and physical fit/seal tests remain open. The new report distinguishes verified nominal geometry from unverified mating details and proposes specific alternatives.

## Start here

- [Component compatibility audit, sources, proposed alternatives and remaining gates](docs/RevB4_Component_Compatibility.md)
- [Current print and procurement checklist](docs/Print_and_Procurement.md)
- [Wiring and assembly schedule](docs/Wiring_and_Assembly.md)
- [Historical Rev-B.3 assembly access work and printer plan](docs/RevB3_Assembly_Readiness.md)
- [Retained fastening schedule](docs/RevB2_Prototype_Readiness.md#retention-and-fastening-schedule)
- [Editable Rev-B.4 Fusion design](cad/Energized_Water_Scanner_RevB4.f3d), [physical STEP assembly](cad/Energized_Water_Scanner_RevB4.step)
- [All 16 current print STLs](prints/Print_STLs.zip) — only PRINT_20 changes from Rev-B.3
- [Supplier-interface checks](verification/RevB4_Supplier_Interface_Audit.json), [source hashes and official model comparison](verification/RevB4_Reference_Check.json)
- [Assembly/steering](verification/RevB4_Assembly_Audit.json), [service](verification/RevB4_Service_Audit.json), [wiring](verification/RevB4_Wiring_Support_Audit.json), [fastener/access](verification/RevB4_Fastener_Access_Audit.json)
- [STL checks](verification/RevB4_STL_Check.json), [export and native-roundtrip checks](verification/RevB4_Export_Check.json)

![Regulator connection access](previews/RevB4_regulator_connection_access.png)

## Assembly intent

Install the electronics-tray screws before the battery tray; its new front scallops clear typical M3 heads. The revised ESP32 bridge leaves an upper header access window, but the real board, leads and retention still need a fit trial. E1 straight-down socket access is obstructed; the builder has accepted a manual access workaround. Seal/retention qualification remains open. Four motor-support pilots now provide 2 mm nominal M3×8 tip clearance.

E1–E4 connect by labeled ring lugs to the protected front end, then the ADC. E2 sits beneath the motor: wire and tighten it before installing the cradle/motor. Its new side exit leads toward the sensor side of the tray. The new tray riser is for conductors; install service connectors above the tray. The front-end circuit and connector pinout are still unvalidated.

PRINT_18–21 are four screw-secured capture bridges for the ESP32, front-end envelope, regulator family model and ESC. They seat on tray pedestals, leaving nominal package clearance rather than using screw torque to press on electronics. Verify the real boards, headers, connectors and thermal clearances before accepting the restraints.

Permanent printed attachments use M3 blind pilots where space allows. M2 remains at small board/servo interfaces, and the motor retains its factory M2.6 interface. The regularly removed main hatch retains M3 screws/inserts and its gasket. The [retention schedule](docs/RevB2_Prototype_Readiness.md#retention-and-fastening-schedule) records screw starting lengths and the deliberate bonded/strapped exceptions.

## CAD, printing and verification limits

Use Rev-B.4 exports together. STLs use millimeters and assembly coordinates; orient them in the slicer without scaling. Reprint only PRINT_20 relative to Rev-B.3. Plan both the 320 × 170 mm hull and 269 × 154 mm hatch on the H2D; smaller parts can use the X1C. The hull leaves only 5 mm total in the H2D's 325 mm single-nozzle width before print aids. See the current report for profile, brim and material qualification limits.

The 245 × 130 mm hatch and the transverse battery layout remain. Disconnect and remove the battery and its tray for USB access. Disconnect hull wiring and remove the servo horn/linkage before electronics-tray removal. Some legacy geometry uses fixed coordinates; changing master parameters requires a new audit.

The reports distinguish physical-solid collisions, sampled motion/service checks, route allocations and intentional bearing/fastener fits. They do not certify real connector fit, printed screw strength, water sealing, flotation, continuous motion or sensing performance. The experimental sensing system is not protective equipment; a negative measurement does not establish that water is safe. No production PCB, validated firmware or calibrated hazard threshold is supplied.

## Repository layout

| Folder | Contents |
|---|---|
| `cad/` | Current Rev-B.4 F3D/STEP and historical exports |
| `prints/` | Sixteen current STLs and matching ZIP |
| `docs/` | Current integration instructions/readiness gates and historical design evidence |
| `previews/` | Revision-specific assembly and interface images |
| `verification/` | Current `RevB4_*` reports; previous revisions retained as historical evidence |
| `coupons/` | Separate open-section interface sample; not a watertight assembly part |
| `scripts/` | Re-runnable Fusion audits, migration source and export checks |

Historical [Rev-B layout](docs/RevB_Compact_Enclosure.md), [Rev-A.1 audit](docs/RevA1_Design_Audit.md) and [original hardware brief](docs/Energized_Water_Scan_RevA_Hardware_and_CAD.md) explain prior design intent. Their coordinates and fabrication instructions do not supersede the current revision.

