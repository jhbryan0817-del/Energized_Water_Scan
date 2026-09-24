# Rev-A.1 audited CAD — print and procurement

Updated 24 September 2026. Current files are **Rev-A.1**: 40 user parameters, an editable Fusion timeline, a physical-only STEP and 12 STL files in millimeters. See the [new design audit](RevA1_Design_Audit.md) for evidence and unresolved limitations.

## Audit and corrections

This revision closes electrode head/seal gaps, moves the battery clear of the motor-terminal envelope, extends its tray support, reroutes the reserved power-wire corridor, adds a tiller cross-pin interface and lower rudder collar envelope, and enlarges the steering penetration to clear sampled ±35° travel. It also labels the imported regulator as a package proxy.

**Reprint changed parts:** PRINT_01 hull (7 mm steering port), PRINT_04 battery tray (119 mm long), and PRINT_17 tiller (1.3 mm transverse pin hole). Other prints are regenerated from the same final assembly. The matching stock hole is a machining operation, not a printed part.

Earlier corrections remain: integrated stern sleeve/supports, relocated ADC and matching mounts, motor cradle relief, consolidated pod/bracket, and separate metal rudder stock.

This is still a prototype. Physical fits, sealing, retention, strength, trim/flotation and actual linkage travel require verification. The boot, horn, pin and collar are procurement envelopes.

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
| Rudder/linkage | 3 mm metal stock, 86 mm modeled length; match-drilled 1.3 mm cross-hole at 82 mm from lower end. M2 pushrod, compatible horn/clevises; nominal span 131 mm |

## Procure — assembly supplies

- Hatch: eight M3 screws and eight matching brass inserts; nominal M3 x 12 starting length, verify actual insert/gasket stack. Continuous 2 mm gasket.
- Tray: four M3 screws, nominal 8 mm starting length; verify pilot-hole engagement. Battery straps and PCB restraints.
- ADS1115: four M2 x 12 screws with nuts/washers; verify board clearance and stack.
- Motor face: two M2.6 screws; nominal 6 mm starting length with 3 mm plate, verify actual motor engagement limit before installation.
- Pod lid: four M2 fasteners. Rail/pod: two nonmagnetic M2.5 bolts/nuts/washers, approximately 18 mm starting length. Install captive heads before attaching the rail.
- Steering retention: retained 1.2 × 8 mm transverse pin; locking collar for a 3 mm shaft, fitting within Ø8 × 5 mm. Position collar top 0.5 mm below the bearing; verify axial play and retain the pin.
- Flexible sealed M2 steering pushrod boot compatible with a 7 mm hull seat; CAD allocates a 7 mm neck and 10 mm outer flange/bellows envelope. Verify real boot fit, seal and travel; stern-tube bonding epoxy/sealant; hull coating/sealant; pod sealing material. Confirm rudder axial retention and attachment methods during dry assembly.
- 1 mm nonmagnetic sensor mounting pad and 3 mm ESC mounting foam; cable ties/retainers.
- XT60 mating lead, inline fuse holder and correctly selected fuse, silicone wire, Qwiic leads, heat-shrink, approximately 40 x 30 mm front-end perfboard.
- Front-end parts from the brief: 499 kΩ and 100 kΩ resistors, BAT54S clamps, filter capacitors and bias-divider components; final values/quantities depend on the validated circuit.
- Compatible 2S LiPo balance charger if not already owned.

Part numbers come from the supplied baseline; availability/prices were not rechecked. Fastener lengths above are starting selections, not released manufacturing dimensions.

## Rev-A.1 assembly checks

- Four electrode heads now contact the exterior sealing washers. Modeled shank length is 18 mm under-head; select/trim/deburr actual bolts after measuring the complete seal, lug and nut stack. Do not reuse the former 9 mm head-to-washer gap. Head bottom is now Z=-4 mm.
- Set battery at X=-101…3 mm with straps; do not slide it aft without rechecking the motor terminal keep-out. The tray extends X=-104…15 mm. Preserve lead/finger clearance.
- Route power wiring in the revised Y=-31…-25 mm corridor and provide actual strain relief. The corridor is not a physical duct.
- Match-drill the tiller and shaft, retain the cross-pin, install the lower locking collar and verify the blade's bonded socket. The stock is not print material.
- Dry-cycle the actual horn, rod, clevises and flexible boot through the intended travel before setting controller limits. Sampled CAD motion assumes a 17.9 mm horn radius, 21 mm tiller radius and 131 mm link span.
- Measure the regulator output and confirm the purchased part is D24V10F5. The model uses shared-package geometry sourced from an F3 STEP and is not proof of electrical compatibility.
