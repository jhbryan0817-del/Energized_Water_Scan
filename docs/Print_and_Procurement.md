# Rev-A audited CAD — print and procurement

Updated 23 September 2026. This set supersedes the earlier Rev-A exports. Native Fusion file preserves 39 parameters and the editable timeline. STEP contains the physical assembly; STL files contain only the 12 default printed parts, in millimeters.

## Audit and corrections

- Integrated the overlapping stern-tube sleeve into the hull, retaining the tube bonding bore.
- Moved ADS1115 12 mm aft and 4 mm inward, away from electrode E3; added four matching mounting bosses and through-holes.
- Relieved the motor cradle and motor-foot/electrode-boss clash; cleared the rudder-stock passage and adjusted the steering-boot flange.
- Integrated hull pillars/electrode bosses and tray supports into their parent prints; consolidated pod and bracket solids.
- Added pod-to-rail fastening clearance. Separated the printed rudder blade/tiller from the purchased metal stock.
- Physical assembly check: 87 solids, zero detected cross-component volume overlaps. Recomputed timeline: zero feature warnings/errors. Every default print is one solid.

This is a light CAD packaging audit, not a production release: real-part fits, full steering travel, wiring, fastening/retention, flotation and leak testing still require physical verification. The servo horn and flexible boot remain purchase/fit envelopes. Motor mounts, rail and rudder bracket require assembly attachment; bonding and hardware selection must be checked during the prototype build.

## Print — one of each (12 pieces)

| STL prefix | Part |
|---|---|
| PRINT_01 | Hull, including stern sleeve, electrode bosses and tray pillars |
| PRINT_02 | Main hatch cover |
| PRINT_03 | Electronics tray, including PCB and servo supports |
| PRINT_04 | Battery slide tray |
| PRINT_06 | Magnetometer adjustment rail |
| PRINT_07 | Magnetometer service pod with mounting shoe |
| PRINT_08 | Pod lid |
| PRINT_09 | Rudder transom bracket |
| PRINT_11 | Motor face mount |
| PRINT_14 | Motor lower cradle |
| PRINT_16 | Rudder blade |
| PRINT_17 | Rudder tiller |

The hull is 400 mm long; check printer capacity. Files retain assembly coordinates: place on the bed and choose orientation/supports in the slicer. Print interface trials before the complete hull. Seal the hull deliberately; FDM alone is not assumed watertight. No material, orientation or process has been qualified for production. Optional mast/boom configurations are excluded from this default print set.

Do not print the PCB, motor, battery, shaft, propeller, servo, gasket or other purchased/reference envelopes. The stern sleeve and internal supports no longer need separate prints.

## Procure — electronics and drive (one each unless noted)

| Item | Exact baseline |
|---|---|
| Controller | Espressif ESP32-DevKitC V4 |
| Magnetometer | SparkFun SEN-19921 MMC5983MA |
| ADC | Adafruit ADS1115 PID 1085 STEMMA QT/Qwiic |
| Regulator | Pololu D24V10F5, item 2831 |
| ESC | Hobbywing QuicRun WP-1625, 30120000 |
| Motor | Mabuchi RS-380PH-4045 |
| Shaft/stern tube | Krick 65220 |
| Coupling | Krick 63800 + 63823 (2.3 mm) + 63820 (2.0 mm), one of each |
| Propeller | Krick/Graupner 2307.30, 30 mm, RH, M2 |
| Servo | Genuine TowerPro SG90 Digital, with matching horn and mounting hardware |
| Battery | Gens Ace GEA222S30X6GT, 2200 mAh 2S 30C XT60 |
| Electrodes | Four A4/316 M4 bolts, nuts, washers, terminal lugs and sealing washers/O-rings; length to actual stack |
| Rudder/linkage | 3 mm metal stock, 86 mm modeled length; M2 pushrod, clevises/rod ends and compatible horn; nominal linkage span 131 mm |

## Procure — assembly supplies

- Hatch: eight M3 screws and eight matching brass inserts; nominal M3 x 12 starting length, verify actual insert/gasket stack. Continuous 2 mm gasket.
- Tray: four M3 screws, nominal 8 mm starting length; verify pilot-hole engagement. Battery straps and PCB restraints.
- ADS1115: four M2 x 12 screws with nuts/washers; verify board clearance and stack.
- Motor face: two M2.6 screws; nominal 6 mm starting length with 3 mm plate, verify actual motor engagement limit before installation.
- Pod lid: four M2 fasteners. Rail/pod: two nonmagnetic M2.5 bolts/nuts/washers, approximately 18 mm starting length. Install captive heads before attaching the rail.
- Flexible sealed M2 steering pushrod boot; stern-tube bonding epoxy/sealant; hull coating/sealant; pod sealing material. Confirm rudder axial retention and attachment methods during dry assembly.
- 1 mm nonmagnetic sensor mounting pad and 3 mm ESC mounting foam; cable ties/retainers.
- XT60 mating lead, inline fuse holder and correctly selected fuse, silicone wire, Qwiic leads, heat-shrink, approximately 40 x 30 mm front-end perfboard.
- Front-end parts from the brief: 499 kΩ and 100 kΩ resistors, BAT54S clamps, filter capacitors and bias-divider components; final values/quantities depend on the validated circuit.
- Compatible 2S LiPo balance charger if not already owned.

Part numbers come from the supplied baseline; availability/prices were not rechecked. Fastener lengths above are starting selections, not released manufacturing dimensions.
