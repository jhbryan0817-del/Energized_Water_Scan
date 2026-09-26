> **Historical revision.** Current geometry, BOM and sensing architecture are [Rev-C.1](RevC_Articulated_Probes.md). Fixed-electrode and magnetometer instructions below are superseded.

# Rev-B.3 wiring and assembly work instruction

> Current revision: [Rev-B.4 component audit](RevB4_Component_Compatibility.md). Use Rev-B.4 CAD/current print ZIP; only PRINT_20 changes from Rev-B.3. E1 access is now builder-accepted; historical results below are retained. Supplier fit and sealing gates remain open.

> **Current mechanical overrides:** see [Rev-B.3](RevB3_Assembly_Readiness.md). E1 is beneath the bow deck: straight vertical socket access fails, and the tested low-profile wrench allowance also clips the hull. Qualify actual tooling before the full hull print. Install the four electronics-tray screws before the battery tray; PRINT_04's new scallops clear their front heads. PRINT_18 now opens the ESP32 upper header area. Motor-support M3×8 starting screws have 2 mm nominal tip margin in revised blind pilots. All actual screw, connector and wire fits remain to be checked.

This is a prototype integration plan, not a released electrical schematic or pin-numbered production harness. Resolve the open selections in the [production audit](RevB1_Production_and_Wiring_Audit.md) before building for use. Keep the original named components; additional integration hardware is still required.

> See the [Rev-B.2 electrode route/stack and retention schedule](RevB2_Prototype_Readiness.md) first. E2 must be terminated before motor installation; a 6×8 mm tray riser carries conductors to above-tray service connectors. Capture bridges and screw pilots replace the earlier unsecured-board arrangement. Actual connector passage and wire bends remain dry-assembly checks.

## Connection schedule

| Harness | From → to | Assembly requirement |
|---|---|---|
| P1 | Battery XT60 → fused distribution → ESC small Tamiya input | Mating polarized connector pair and fuse close to battery. Select wire/fuse from measured motor starting/loaded current, connector limits and protection coordination; ESC's 25 A rating alone is not a fuse value. |
| P2 | Fused distribution → Pololu VIN/GND | Separate branch; strain-relieve soldered leads and insulate every joint. Keep return paired with supply. |
| P3 | Pololu VOUT 5 V/GND → ESP32 5 V/GND header | One power source only. Disconnect for USB programming; do not feed ESP32 3V3 with 5 V. |
| P4 | ESC BEC 6 V/GND → servo power/GND | Loaded current test required. BEC positive must remain isolated from Pololu/ESP32 5 V. Logic signals require common reference ground; motor/servo load current must not flow through sensor return wiring. |
| C1 | ESP32 PWM + reference ground → ESC signal + ground | Firmware pin allocation and ESC calibration/failsafe remain to be defined. Identify actual connector pins, not wire colors alone. |
| C2 | ESP32 PWM + reference ground → servo signal + ground | Confirm signal compatibility and travel on bench with linkage disconnected, then limit travel on real mechanism. |
| S1 | ESP32 3.3 V/GND/SDA/SCL → ADS1115 and remote MMC5983MA | Confirm pin order and 3.3 V pull-ups on actual boards. Qwiic/STEMMA connectors do not provide an ESP32 DevKitC socket by themselves: a terminated adapter lead is needed. |
| S2 | E1/E2/E3/E4 ring terminals → protected front end → ADS1115 A0/A1/A2/A3 | Label both ends E1–E4. Keep E1/E2 and E3/E4 as their respective pairs. Never bypass the unvalidated protection/bias network and connect electrodes directly. |
| M1 | ESC motor outputs → motor tabs | Matching 4 mm male bullets / suitably rated insulated terminations and motor-tab solder joints required. Restrain before tabs; keep clear of coupling and motor can. Verify direction with propeller removed. |

Do not publish guessed pin numbers as a released harness. Record actual connector manufacturer/part, mating part, cavity numbers, polarity, wire gauge, insulation, cut length, strip length and crimp tool after a dry harness build. Check continuity and shorts with all power disconnected; verify each supply separately before connecting electronics.

## Routing and assembly sequence

1. Print and finish interfaces. Install and seal electrodes, stern tube, steering boot and qualified attachments. Fit the four ring lugs in their specified orientations and route E2 through the cradle side exit. Tighten E2 before motor/cradle installation. Use the new blind M3 support fasteners and confirm tool access/alignment.
2. On the removed electronics tray, thread the five harness restraint ties and ESC restraint. Tie heads remain above the plate. Fit M2 ADC/servo screws into the new receiving pilots, the four M3 capture bridges and the ESC pad. Bridge feet seat on printed pedestals; verify real electronics cannot escape and no screw load presses on components.
3. Build the fused adapter/distribution harness outside the hull. Put bulky XT60/Tamiya junctions and fuse in a measured accessible free volume; the 6×8 mm side routing allocation is for conductors, not connector bodies or fuse holders. Exact junction placement is an open CAD gate.
4. Route propulsion supply and return together on the positive-Y side; keep motor leads local and paired. Branch to the logic-side restraint at (80,50), with slack to unplug the regulator. Keep antenna area free of bundled wire or metal.
5. Route electrode/ADC wiring on negative Y, using stations (-12,-24) and (78,-44) as appropriate. The front-end-to-ADC run should stay short. Use (105,-44) for the separate servo/control branch; do not bundle that branch with high-impedance electrode conductors. Cross power wiring approximately at right angles where unavoidable.
6. Route the magnetometer cable through a selected sealed bulkhead/potted feedthrough into the main hull. This interface is not yet designed. Provide strain relief on both sides, a drip loop where applicable and a service disconnect inside. Never run it across the hatch gasket. Do not assume an assembled Qwiic plug passes the existing pod's small wire exit; select a feedthrough assembly process compatible with the plug and seal.
7. Leave measured service loops between fixed hull and tray, then disconnect those interfaces before lifting the tray. Do not make a loop large enough to reach the motor shaft, coupling, linkage or gasket. Tie-downs are restraints, not certified clearance corridors; inspect with actual cables in place.
8. Lower and secure tray, reconnect labeled hull/sensor/motor interfaces, fit and adjust the real horn/clevis linkage, and test the mechanism unpowered through its intended travel.
9. Thread battery straps through matching tray passages; fit battery with pull loop and free balance lead. Keep fuse/disconnect accessible. Connect battery only after polarity/continuity inspection and electrical commissioning.
10. For USB, unplug battery and remove battery plus loose battery tray; isolate external 5 V before inserting USB. For tray removal, additionally unplug fixed harnesses, remove servo horn/linkage and release the four tray screws.
11. Inspect all seals and wiring before evenly closing hatch. Perform unpowered leak/float tests, loaded steering/BEC tests, motor thermal/noise tests and controlled sensing validation. No powered-water acceptance is inferred from CAD.

## Harness release record (not yet filled)

Required records: exact connector/fuse/lead BOM; wiring diagram with connector cavities; final GPIO allocation and firmware revision; actual cut lengths and bend radii; restraint and service-loop photographs; continuity/polarity results; motor and servo peak-current traces; BEC/logic rail minima; fuse coordination rationale; sealed-entry drawing and leak results. These are the remaining inputs for repeatable production assembly.
