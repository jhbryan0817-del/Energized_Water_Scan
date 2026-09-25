# Rev-B.3 — print, procurement and assembly

Updated 25 September 2026. Use **Rev-B.3** CAD, all sixteen current STLs and the matching ZIP. Reprint PRINT_01, PRINT_04 and PRINT_18 relative to Rev-B.2. See the [current audit and unresolved assembly blockers](RevB3_Assembly_Readiness.md) and [wiring/assembly schedule](Wiring_and_Assembly.md). This BOM is not a complete exact-part procurement/assembly BOM. The builder has screws, an ESP32 and basic components; nearly all named hardware still requires procurement and measurement.

**Printer plan:** H2D for hull and hatch; X1C for smaller parts. The 320 mm hull has only 5 mm total spare width in the H2D's published 325 mm single-nozzle direction before supports/brim. The hatch is 269 × 154 mm and is not an axis-aligned flat X1C print. Confirm Bambu Studio's actual usable area and adhesion plan; do not scale. Print material is unconfirmed. See the source-linked plan in the current audit.

**New interface overrides:** motor-support Ø2.5 pilots end at Z=2.0 rather than 3.8 mm, giving nominal 2 mm M3×8 tip margin. Battery-tray open corner reliefs clear typical front tray M3 heads. PRINT_18 now has an upper header access window. Exact fastener and owned ESP32 fit remain coupon gates. E1 tool access is unresolved and must be demonstrated before the full hull print.

## Print — one of each (16 pieces)

The hull is **320 × 170 mm**; the hatch opening is 245 × 130 mm. Rev-B.3 changes three parts relative to Rev-B.2. Use the complete current package. The hull-section coupon in `coupons/` is separate from the sixteen assembly parts and is not a watertight part.

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
| PRINT_18 | ESP32 capture bridge |
| PRINT_19 | Front-end capture bridge |
| PRINT_20 | Regulator capture bridge |
| PRINT_21 | ESC capture bridge |

STLs are in millimeters and retain assembly coordinates. Position/orient them in the slicer; check that the printer accommodates the 320 mm hull. Optional mast/boom layouts are excluded from this print package. Verify interface coupons, actual hardware fits, print tolerances and sealing before a complete build. FDM is not assumed watertight.

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
| Electrodes | Four A4/316 M4 bolts, nuts, terminal lugs and sealing washers/O-rings; length to actual stack. The modeled lug replaces the internal washer: do not add another internal washer without revising the stack. |
| Rudder/linkage | 3 mm metal stock, 86 mm modeled length; match-drilled 1.3 mm cross-hole at 82 mm from lower end. M2 pushrod, compatible horn/clevises; nominal span 131 mm |

## Procure — assembly supplies

See the [current fastening schedule](RevB2_Prototype_Readiness.md#retention-and-fastening-schedule) for all pilot/clearance sizes and provisional screw lengths. New items: four M3 motor-support screws, eight M3 capture-bridge screws, two flush nonmagnetic M3 rail screws, four M3 transom screws, two M2 servo screws and a nominal 0.4 mm nonconductive motor-cradle liner. Qualify actual liner material/thickness and motor temperature. Do not treat screw lengths as released until coupons and dry assembly pass.


- Hatch: eight M3 screws and eight matching brass inserts; nominal M3 x 12 starting length, verify actual insert/gasket stack. Continuous 2 mm gasket.
- Tray: four M3 screws, nominal 8 mm starting length; verify pilot-hole engagement. Battery straps and PCB restraints.
- ADS1115: four M2 x 6 starting screws into new Ø1.7 mm blind pilots; verify board/head clearance and actual engagement.
- Motor face: two M2.6 screws; nominal 6 mm starting length with 3 mm plate, verify actual motor engagement limit before installation.
- Pod lid: four M2 fasteners. Rail/pod: two nonmagnetic M2.5 bolts/nuts/washers, approximately 18 mm starting length. Install captive heads before attaching the rail.
- Steering retention: retained 1.2 × 8 mm transverse pin; locking collar for a 3 mm shaft, fitting within Ø8 × 5 mm. Position collar top 0.5 mm below the bearing; verify axial play and retain the pin.
- Flexible sealed M2 steering pushrod boot compatible with a 7 mm hull seat; CAD allocates a 7 mm neck and 10 mm outer flange/bellows envelope. Verify real boot fit, seal and travel; stern-tube bonding epoxy/sealant; hull coating/sealant; pod sealing material. Confirm rudder axial retention and attachment methods during dry assembly.
- 1 mm nonmagnetic sensor mounting pad and 3 mm ESC mounting foam; cable ties/retainers.
- XT60 mating lead, inline fuse holder and correctly selected fuse, silicone wire, Qwiic leads, heat-shrink, approximately 40 x 30 mm front-end perfboard.
- Front-end parts from the brief: 499 kΩ and 100 kΩ resistors, BAT54S clamps, filter capacitors and bias-divider components; final values/quantities depend on the validated circuit.
- Compatible 2S LiPo balance charger if not already owned.
- Correctly polarized XT60-to-small-Tamiya fused distribution harness for the stock ESC connector; matching 4 mm male motor bullet terminations. Exact manufacturer parts, current ratings, wire gauge and lengths remain to be selected and verified.
- Nonconductive ties up to 2.5 mm wide for new tray slots; four printed M3 capture bridges now provide restraint geometry; actual board fit and the sensor cable sealed bulkhead/potted feedthrough remain integration gates.

The WP-1625 BEC is specified as 6 V / 1 A. Test loaded servo current and supply transients before accepting this power arrangement; do not parallel it with the Pololu output. Disconnect external power before USB programming. See the source-backed current audit for details.

Part numbers come from the supplied baseline; availability/prices were not rechecked. Fastener lengths above are starting selections, not released manufacturing dimensions.

## Rev-B assembly and service checks

- Mount the battery transversely, centered at X=-52.5, Y=0 mm. Its tray occupies X=-74.5…-30.5, Y=-59.5…59.5 mm. Retain the pack with straps through the matching tray passages and provide a fabric pull loop. Do not lift by wires or compress the pack.
- Assemble and wire boards on the removed electronics tray. Verify actual hardware against the pads/bosses and PRINT_18–21 capture bridges. Fit the tray using the four M3 positions at X=-70/140 and Y=-55/55 mm.
- Remove both battery and battery tray for USB insertion. Remove them, disconnect wiring and remove the servo horn/linkage before lifting the electronics tray.
- Keep power wiring in the Y=59…65, Z=20…28 mm allocation; use the separate sensor-route allocation at Y=-30…-24, Z=40…47 mm. These are free-space reservations, not physical cable restraints or a complete harness.
- The shortened 46 mm sensor rail projects 20 mm beyond the bow. Use its two new flush M3 blind screw positions and verify cantilever strength, cable strain relief and magnetic performance. Keep its 2 mm gap to the closed hatch clear.
- Retain Rev-A.1 electrode head/seal contact, the retained tiller cross-pin, lower locking collar and 7 mm steering-boot seat. Match actual fastener stackups and seal compression.
- Dry-cycle the real horn, rod, clevises and boot before setting controller limits. The ideal CAD linkage uses a 17.9 mm horn radius, 21 mm tiller radius and 131 mm link span.
- The regulator remains a D24V10F5 procurement requirement with an F3-derived package proxy in CAD. Confirm actual output voltage and package dimensions.
- Repeat mass/trim, flotation/freeboard, leak and sensor-interference tests for the smaller hull. CAD checks do not establish these properties.

