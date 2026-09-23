# Energized Water Scan — Rev-A Hardware & Mechanical-CAD Baseline

**Repository target:** `jhbryan0817-del/Energized_Water_Scan`  
**Revision:** Rev-A CAD-ready BOM  
**Mechanical-reference audit:** 2026-09-23  
**Primary design priority:** Every enclosure-driving purchased component must have a public mechanical reference sufficient to reproduce or import its geometry.

---

# 1. Project scope

This document defines the first hardware revision of a small remotely controlled surface craft intended to survey flooded water for possible electrical hazards using:

- two orthogonal submerged electrode pairs to sense local electric-potential gradients;
- one 3-axis magnetometer;
- one ESP32-based controller;
- one brushed propulsion motor;
- conventional rudder steering.

This revision intentionally focuses on:

- essential electronics;
- specific purchasable components;
- mechanical-reference availability;
- power architecture;
- component geometry;
- CAD-development direction;
- enclosure/hull serviceability.

The following remain outside Rev A:

- detection/classification algorithms;
- machine learning;
- calibrated hazard thresholds;
- field reliability;
- certification;
- production PCB design.

> **Safety note:** This prototype is an experimental detector, not protective equipment. A negative measurement must never be treated as proof that flooded water is safe to enter. Early testing should use isolated, low-voltage laboratory sources.

---

# 2. CAD-first selection rule

The original BOM contained several mechanically vague entries such as:

- "370/380 motor";
- "SG90-class servo";
- "2S 2200 mAh LiPo";
- generic shaft/coupler/propeller kit.

Those are no longer acceptable for the mechanical baseline.

For Rev A, every purchased component that drives the enclosure geometry is now assigned one of three reference classes:

## Class A — direct CAD reference

The manufacturer provides one or more of:

- STEP;
- DXF;
- official 3D model;
- detailed manufacturing/fabrication drawing.

These parts can be imported directly or reconstructed with high confidence.

## Class B — official dimension-controlled envelope

No trustworthy STEP file is available, but the manufacturer provides enough dimensions to build an accurate simplified solid.

These components should be represented in the boat assembly as clearance envelopes rather than photorealistic models.

## Class C — standardized/non-enclosure-driving hardware

Examples:

- M4 fasteners;
- resistors;
- capacitors;
- flexible wire;
- heat-shrink.

These do not justify individual high-detail boat-assembly models. Standard CAD-library geometry or a bounding volume is sufficient.

---

# 3. Revised CAD-ready BOM

## Budget position

The revised component-only planning total is approximately:

**US$149**

This deliberately excludes:

- international shipping;
- taxes/import charges;
- LiPo charger;
- hull fabrication;
- sealant;
- general workshop fasteners;
- replacement consumables.

Because exact branded parts must be sourced rather than substituted with anonymous equivalents, a **US$200 procurement allowance is recommended** even though the target component subtotal remains near $150.

Prices are planning values, not quotations.

| # | Function | Exact component | Qty | Planning cost | Mechanical reference | CAD class |
|---|---|---|---:|---:|---|---|
| 1 | Main controller / wireless link | **Espressif ESP32-DevKitC V4** | 1 | ~$10 | Official dimensions PDF + **DXF source** + PCB layout | **A** |
| 2 | Magnetometer | **SparkFun SEN-19921 Qwiic Micro MMC5983MA** | 1 | $18.50 | Official board dimensions + Eagle files + hardware repository | **A/B** |
| 3 | Electrode ADC | **Adafruit ADS1115 PID 1085, STEMMA QT/Qwiic** | 1 | $14.95 | Official fab drawing + **3D model** + EagleCAD files | **A** |
| 4 | Logic regulator | **Pololu D24V10F5, item 2831** | 1 | $12.95 | Official dimension drawing + **STEP + DXF drill guide** | **A** |
| 5 | Brushed ESC | **Hobbywing QuicRun WP-1625, product 30120000** | 1 | ~$20 | Manufacturer envelope 34 × 24 × 14 mm + wire specifications | **B** |
| 6 | Propulsion motor | **Mabuchi RS-380PH-4045** | 1 | ~$10 | Detailed Mabuchi mechanical drawing: body, shaft, mounting holes, terminals | **A/B** |
| 7 | Prop shaft / stern tube | **Krick 65220 Eco M2 shaft assembly** | 1 | ~$6.50 | Published shaft/tube diameters and lengths | **B** |
| 8 | Coupling center | **Krick 63800 bridge coupling connector** | 1 | ~$5.50 | Published complete-coupling OD/length when assembled | **B** |
| 9 | Motor-side coupling insert | **Krick 63823, 2.3 mm** | 1 | ~$3.75 | Published bore, hex size, width and setscrew size | **B** |
| 10 | Shaft-side coupling insert | **Krick 63820, 2.0 mm** | 1 | ~$3.75 | Published coupling geometry; 2.0 mm bore | **B** |
| 11 | Propeller | **Krick/Graupner 2307.30, 3-blade, right-hand, M2** | 1 | ~$5 | Published 30 mm diameter, M2 connection, 16 mm pitch | **B** |
| 12 | Rudder servo | **Genuine TowerPro SG90 Digital** | 1 | ~$5 | Manufacturer body and mounting dimensions; third-party STEP models also exist | **A/B** |
| 13 | Battery | **Gens Ace G-Tech Soaring 2200 mAh 2S 30C, SKU GEA222S30X6GT** | 1 | ~$16 | Manufacturer envelope 104 × 34.5 × 14.5 mm and mass | **B** |
| 14 | Wet electrodes | **A4/316 stainless M4 machine bolts, standard geometry** | 4 | ~$4 | ISO-standard fastener geometry / standard CAD libraries | **C** |
| 15 | Electrode input network | 499 kΩ resistors, 100 kΩ resistors, BAT54S clamps, capacitors, bias-divider parts | set | ~$5 | Standard packages; mounted on one defined prototype-board envelope | **C** |
| 16 | Wiring / fuse / internal integration | Silicone wire, XT60 mating lead, Qwiic leads, heat-shrink, inline fuse, perfboard | set | ~$8 | Non-enclosure-driving; model only routing/clearance envelopes | **C** |

**Planning subtotal: approximately US$149**

A delivered build can exceed $150 because several exact parts may come from different suppliers. Therefore the **recommended purchasing ceiling is $200**.

---

# 4. Mechanical-reference audit

## 4.1 ESP32-DevKitC V4

**Status: keep**

Espressif provides:

- ESP32-DevKitC V4 dimensions PDF;
- dimensions source **DXF**;
- PCB layout;
- schematic.

Mechanical reference:

https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html

### CAD implementation

Import the DXF or reconstruct the board outline.

The assembly model should include clearance for:

- USB connector;
- pin headers;
- ESP32 module/shield;
- USB-cable insertion;
- wiring bend radius.

Do not create a tight snap-fit around the PCB itself.

---

## 4.2 SparkFun SEN-19921 MMC5983MA

**Status: keep**

SparkFun provides:

- board dimensions;
- Eagle files;
- schematic;
- open hardware repository.

Nominal board size:

**19.05 × 7.62 mm**

Reference:

https://www.sparkfun.com/sparkfun-micro-magnetometer-mmc5983ma-qwiic.html

### CAD implementation

No detailed manufacturer STEP is required.

Create a simplified sensor-board model from:

- PCB outline;
- PCB thickness;
- Qwiic connector volume;
- component-height clearance.

The magnetometer pod should have much more clearance than the PCB requires because the primary requirement is magnetic separation, not packing density.

---

## 4.3 Adafruit ADS1115 PID 1085

**Status: keep**

Adafruit publishes:

- official **ADS1115 3D models**;
- STEMMA QT fab print;
- EagleCAD files.

Official downloads:

https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/downloads

Nominal product envelope:

**25.4 × 17.8 × 4.6 mm**

Product reference:

https://www.adafruit.com/product/1085

### CAD implementation

Import the official model.

Add additional clearance around:

- STEMMA QT connectors;
- screw-terminal/header area if populated;
- electrode-front-end wiring.

---

## 4.4 Pololu D24V10F5

**Status: keep**

The original 1 A regulator is retained.

It only needs to power:

- ESP32;
- ADS1115;
- magnetometer;
- low-current front-end electronics.

The steering servo remains powered from the ESC BEC.

Pololu provides:

- official STEP;
- official drill-guide DXF;
- detailed dimensions.

Reference:

https://www.pololu.com/product/2831/resources

Nominal board size:

**0.5 × 0.7 × 0.14 in**

### Why not change to the larger 3 A regulator?

Pololu's S13V30F5 would be a mechanically excellent alternative because it also has official STEP/DXF files, but it costs more and is unnecessary if the SG90 is powered through the ESC BEC.

If later revisions place all 5 V loads on one rail, S13V30F5 is the preferred upgrade:

https://www.pololu.com/product/4082/resources

---

# 5. Propulsion system — now dimensionally frozen

The most important BOM tightening is the propulsion chain.

Rev A now uses:

```text
Mabuchi RS-380PH-4045
        |
      Ø2.3
        |
Krick 63823 coupling insert
        |
Krick 63800 bridge connector
        |
Krick 63820 coupling insert
        |
      Ø2.0
        |
Krick 65220 shaft assembly
        |
       M2
        |
Krick/Graupner 2307.30 propeller
```

This chain is now mechanically specified instead of being a generic RC-boat drivetrain.

---

# 6. Mabuchi RS-380PH-4045 motor

**Status: replaces generic "370/380 motor"**

Mabuchi provides a detailed mechanical drawing for the RS-380PH family.

Important geometry:

- body length: approximately **37.8 mm**;
- maximum can diameter: **Ø29.2 mm**;
- principal can diameter: **Ø27.7 mm**;
- output shaft: **Ø2.3 mm**;
- two front **M2.6 × 0.45** mounting holes;
- shaft/mounting-face geometry publicly documented;
- approximately **80 g**.

Electrical reference for RS-380PH-4045:

- operating range: approximately 3–12 V;
- nominal data published at 6 V;
- no-load speed around 12,500 rpm in the currently published catalog specification.

Manufacturer reference:

https://product.mabuchi-motor.com/detail.html?id=99

A detailed RS-380PH mechanical drawing is also widely mirrored from Mabuchi's published data.

### CAD implementation

Reconstruct the motor as a parametric component using the drawing.

Model:

- can;
- front boss;
- output shaft;
- M2.6 mounting holes;
- rear terminal clearance.

Do **not** mount by clamping tightly around the thin motor can alone.

Preferred mount:

- front-face screw location control;
- semi-cylindrical cradle for radial support;
- terminal ventilation/clearance.

---

# 7. Krick 65220 M2 shaft / stern-tube assembly

**Status: replaces generic shaft kit**

Exact part:

**Krick 65220 — Ship shaft + stern tube M2 × 153 mm Eco**

Published dimensions:

- stern-tube length: **153 mm**;
- shaft length: approximately **178 mm**;
- stern-tube outside diameter: **5.5 mm**;
- propeller thread: **M2**;
- propeller-thread length: **5 mm**.

Reference:

https://www.krickshop.de/Schiffswelle-Stevenrohr-M2-x-153mm-Eco.htm?ProdNr=65220&a=article

### CAD implementation

Create separate solids for:

- 5.5 mm OD stern tube;
- central 2 mm-class rotating shaft;
- exposed motor-side shaft;
- M2 propeller thread envelope.

The stern tube, not merely the shaft, should define the hull penetration.

---

# 8. Krick bridge coupling

## 8.1 Center connector — 63800

Exact component:

**Krick 63800 Stegkupplung connector**

Reference:

https://www.krickshop.de/Zubehoer-Ersatzteile/Zubehoer-fuer-Schiffsmodelle/Schiffswellen-Kupplungen/Stegkupplung-Verbinder-1-Stck-.htm?ProdNr=63800&a=article

## 8.2 Motor-side insert — 63823

Exact component:

**Krick 63823, 2.3 mm bore**

Published insert geometry includes:

- bore: **2.3 mm**;
- hex: **10 mm**;
- width: **5 mm**;
- setscrew thread: **M3**.

Reference:

https://www.krickshop.de/Zubehoer-Ersatzteile/Zubehoer-fuer-Schiffsmodelle/Schiffswellen-Kupplungen/Welleneinsatz-f-Stegkupplung-2-3mm.htm?ProdNr=63823&a=article&p=192

## 8.3 Shaft-side insert — 63820

Exact component:

**Krick 63820, 2.0 mm bore**

The assembled coupling family is documented at approximately:

- total length: **20 mm**;
- outside diameter: **15 mm**.

Reference:

https://www.krickshop.de/Zubehoer-Ersatzteile/Zubehoer-fuer-Schiffsmodelle/Schiffswellen-Kupplungen/Welleneinsatz-f-Stegkupplung-2mm.htm?ProdNr=63820&a=article&p=192

### CAD implementation

A high-detail coupling model is unnecessary.

Model the assembled coupling as:

- Ø15 mm maximum rotating envelope;
- 20 mm nominal length;
- Ø2.3 mm motor bore;
- Ø2.0 mm shaft bore.

Add axial service clearance for setscrew access.

---

# 9. Krick/Graupner 2307.30 propeller

**Status: replaces generic 30–35 mm propeller**

Exact part:

**2307.30**

Published data:

- 3 blades;
- **30 mm outer diameter**;
- **16 mm pitch**;
- right-hand rotation;
- **M2** threaded connection;
- impact-resistant plastic with brass threaded insert.

Reference:

https://www.krickshop.de/Accessories-Spare-Parts/Accessories-for-Ship-Models/Propellers-for-shipmodels/Schiffsschraube-3Bl-30mm-R-M2.htm?ProdNr=gr2307-30&a=article&p=186&shop=krick_e

### CAD implementation

Do not waste time recreating exact blade surfaces for hull packaging.

Use a propeller keep-out solid:

```text
Diameter: 30 mm
Radial safety envelope: 34–36 mm recommended
```

The hull and rudder must remain outside this swept volume.

---

# 10. Hobbywing QuicRun WP-1625 ESC

**Status: keep**

Exact part:

**Hobbywing QuicRun WP-1625 Brushed, product 30120000**

Manufacturer-published body envelope:

**34 × 24 × 14 mm**

Other mechanical information:

- approximately 23.5–24 g;
- input/output wire size and lengths are manufacturer documented;
- integrated waterproof/dustproof housing.

Reference:

https://www.hobbywing.com/en/products/quicrun-wp-1625-brushed53

North American product page:

https://www.hobbywingdirect.com/products/quicrun-16-esc-brushed

### Important BEC note

Different current Hobbywing regional pages/documentation report the BEC as nominally **5 V or 6 V / 1 A** depending on page/revision.

Both are within the genuine TowerPro SG90's stated practical voltage range, but Rev A should **verify actual BEC output with a multimeter before connecting the servo**.

Do not power the ESP32 from this BEC.

### CAD implementation

Use a conservative envelope rather than an ornamental ESC model:

```text
ESC body: 34 × 24 × 14 mm
CAD allocation: approximately 38 × 28 × 18 mm
```

Add separate wire-bend volumes.

---

# 11. Genuine TowerPro SG90 Digital

**Status: replaces generic "SG90-class servo"**

Exact component:

**TowerPro SG90 Digital**

Manufacturer data:

- body dimension approximately **23 × 12.2 × 29 mm**;
- mass: approximately 9 g;
- detailed dimension table available;
- nominal 4.8 V operation;
- TowerPro states 4.8–6 V is acceptable in its support information.

Reference:

https://towerpro.com.tw/product/sg90-7/

### CAD implementation

A public third-party SG90 STEP can be used for convenience, but it must be checked against the genuine TowerPro dimensions before the mount is frozen.

Do not design around an anonymous SG90 clone.

Recommended printed-clearance allowance:

- approximately 0.3–0.5 mm per constrained side;
- slotted mounting holes;
- servo horn/linkage service envelope above the servo.

---

# 12. Gens Ace G-Tech 2200 mAh 2S battery

**Status: replaces generic "2S 2200 mAh LiPo"**

Exact battery:

**Gens Ace G-Tech Soaring 2200 mAh 7.4 V 30C 2S1P with XT60**  
**SKU: GEA222S30X6GT**

Manufacturer-published data:

- capacity: 2200 mAh;
- nominal voltage: 7.4 V;
- discharge rating: 30C;
- mass: approximately **126 g**;
- dimensions: approximately **104 × 34.5 × 14.5 mm**.

Reference:

https://gensace.de/products/gens-ace-g-tech-soaring-2200mah-7-4v-30c-2s1p-lipo-battery-pack-with-xt60-plug

### CAD implementation

Do **not** make the battery cavity exactly 104 × 34.5 × 14.5 mm.

Use a removable strap tray approximately:

```text
minimum usable bay:
110 × 39 × 19 mm
```

plus:

- XT60 wire exit;
- balance-lead clearance;
- strap thickness;
- finger-removal clearance.

A soft LiPo must not be rigidly compressed by the enclosure.

---

# 13. M4 stainless electrodes

**Status: keep, now mechanically defined**

Use:

**A4 / 316 stainless M4 standard machine bolts**

Exact bolt length remains intentionally undefined until the hull-bottom thickness is fixed.

The required bolt length is approximately:

```text
bolt length =
hull thickness
+ sealing washer/O-ring stack
+ internal washer
+ terminal lug
+ nut thickness
+ desired exposed electrode length
```

M4 hardware is standardized and can be generated from:

- Fusion fastener library;
- SolidWorks Toolbox;
- FreeCAD Fasteners;
- McMaster/MISUMI/TraceParts equivalents.

### CAD implementation

Model electrode bosses parametrically.

Do not model these as fixed holes in an otherwise finished hull.

---

# 14. Electrode sensing arrangement

Use four electrodes arranged as two perpendicular differential axes.

Bottom view:

```text
               BOW

                E1
                |
                |
         E3 ----+---- E4
                |
                |
                E2

               STERN
```

Conceptual measurements:

```text
Vx = V(E1) - V(E2)
Vy = V(E3) - V(E4)
```

Suggested initial parametric ranges:

- E1–E2: **100–160 mm**
- E3–E4: **80–140 mm**

The ADS1115 can configure:

- A0–A1 as one differential pair;
- A2–A3 as the second differential pair.

The channels are multiplexed/sequential rather than truly simultaneous.

---

# 15. Electrode front-end

The electrodes must not connect directly to the ADS1115.

Prototype each electrode input with a high-impedance, current-limited network.

Conceptual direction:

```text
electrode
   |
 499k
   |
 499k
   |
   +------ ADC input
   |
 bias network / filtering / clamps
```

The final values must be validated against the intended experimental voltage range.

The front end should include:

- symmetric current-limiting resistance;
- low-leakage clamping;
- RC filtering;
- controlled bias/common-mode point;
- replaceable prototype board.

### Mechanical implementation

Do not model every resistor in the boat.

Define one front-end module envelope, initially:

```text
~40 × 30 × 12 mm
```

This envelope includes:

- perfboard or prototype PCB;
- passives;
- connectors;
- wiring bend radius.

A future custom PCB can replace this placeholder directly.

---

# 16. Revised power architecture

## Propulsion branch

```text
2S LiPo
   |
inline fuse / battery disconnect
   |
Hobbywing WP-1625
   |
Mabuchi RS-380PH-4045
```

## Steering branch

```text
Hobbywing ESC BEC
   |
verify actual output voltage
   |
TowerPro SG90
```

## Sensing/control branch

```text
2S LiPo
   |
Pololu D24V10F5
   |
5 V
   |
ESP32-DevKitC V4
   |
3.3 V sensor rail as appropriate
   |
ADS1115 + MMC5983MA + front-end
```

Keeping the control/sensing supply independent from the servo load reduces disturbance on the MCU/sensor rail.

---

# 17. Wireless control

Rev A does not require a separate RC transmitter/receiver.

The ESP32 can accept basic commands over:

- Wi-Fi;
- BLE.

This saves both cost and enclosure volume.

A conventional receiver can be added later.

Reserve approximately:

```text
35 × 25 × 15 mm
```

of optional tray space for a future receiver/telemetry module.

---

# 18. Overall mechanical architecture

Recommended starting hull:

**slow displacement monohull**

Suggested initial envelope:

- overall length: **350–450 mm**;
- beam: **160–220 mm**;
- shallow draft;
- substantial electronics freeboard.

The craft is a sensing platform, not a racing boat.

---

# 19. Three functional zones

## Zone A — bow sensing zone

Contains:

- MMC5983MA pod;
- electrode wiring;
- optional future second sensor;
- removable mast/boom.

The magnetometer should be separated from:

- motor;
- ESC;
- battery high-current wiring;
- coupling;
- steel shaft;
- servo;
- ferromagnetic hardware.

Start with an adjustable motor-to-magnetometer separation of approximately:

**150–250 mm**

This is an experimental starting range, not a proven interference threshold.

---

## Zone B — central dry compartment

Contains:

- battery;
- ESP32;
- ADS1115;
- front-end board;
- Pololu regulator;
- internal fuse;
- wiring distribution.

Use one removable electronics tray.

Battery should be low and near the longitudinal center of buoyancy.

---

## Zone C — aft propulsion zone

Contains:

- Mabuchi motor;
- Krick coupling;
- Krick stern tube;
- ESC;
- TowerPro servo;
- rudder linkage.

Keep high-current conductors short and local.

---

# 20. Magnetometer pod

The magnetometer should not be permanently embedded in the hull.

Design a removable pod supporting at least three configurations:

1. flush bow;
2. raised mast;
3. forward boom.

Mechanical requirements:

- repeatable sensor XYZ orientation;
- Qwiic-cable strain relief;
- plastic/non-magnetic fasteners near sensor;
- sensor-board replacement without opening main hull;
- multiple fore-aft mounting positions.

Avoid steel threaded inserts directly beside the magnetometer.

---

# 21. Hull penetration for the stern tube

The Krick 65220 stern tube gives a defined hull-interface diameter:

**5.5 mm OD**

Do not simply create a nominal 5.5 mm hole.

The hull should include:

- shaft-line reference bore;
- local reinforcement;
- bonding/sealant annulus;
- alignment feature;
- adequate stern-wall thickness.

A reasonable first printed/bonded interface can use a slightly oversized controlled bore and epoxy/sealant rather than relying on FDM dimensional sealing.

---

# 22. Motor mount

Build the motor mount from the Mabuchi drawing.

Suggested architecture:

- front mounting plate using M2.6 holes;
- semi-cylindrical lower cradle;
- removable upper retainer if needed;
- terminal clearance behind motor;
- access to mounting screws.

Do not trap the motor permanently between printed hull structures.

---

# 23. Coupling keep-out zone

Because the assembled Krick bridge coupling is approximately:

- **20 mm long**;
- **15 mm OD**,

model a larger rotating/service envelope:

```text
length allowance: 25–30 mm
diameter allowance: 18–20 mm
```

This gives room for:

- shaft alignment error;
- coupling flex;
- setscrew tools;
- installation/removal.

---

# 24. Propeller and rudder clearance

The selected propeller is:

**Ø30 mm**

Use a minimum propeller swept-volume model of:

```text
Ø30 mm actual
Ø34–36 mm preferred keep-out
```

Position the rudder behind the propeller while keeping:

- full prop rotation clear;
- rudder stock clear of blade tips;
- removable propeller access.

The rudder itself can be custom fabricated and therefore does not need a purchased-part CAD reference in Rev A.

---

# 25. Electronics tray

Create one removable tray with dedicated positions for:

- ESP32;
- ADS1115/front-end;
- Pololu regulator;
- ESC;
- battery;
- future receiver reserve.

Recommended features:

- M2/M2.5/M3 standoff grid;
- battery-strap slots;
- zip-tie channels;
- separate sensor and motor wire channels;
- connector access;
- inspection space below boards.

Do not glue PCBs directly to the hull.

---

# 26. Main service hatch

Use one large hatch.

Recommended features:

- continuous perimeter gasket;
- wide flange;
- 6–8 compression screws;
- splash lip;
- all regular-service fasteners above the design waterline where possible.

Avoid:

- snap-fit-only waterproofing;
- many small deck holes;
- separate hatches for every subsystem.

---

# 27. FDM construction direction

If the hull is FDM printed:

- do not assume layer lines are watertight;
- use adequate shell thickness;
- design sealant-compatible joints;
- minimize penetrations below waterline;
- provide flat gasket surfaces;
- use threaded inserts only where their material/location will not compromise the magnetometer;
- consider coating or sealing the lower hull after printing.

The printed hull should define geometry; waterproofing should come from deliberate sealing design.

---

# 28. CAD master parameters

At minimum expose:

```text
hull_length
hull_beam
hull_height
design_waterline
deck_height

hatch_length
hatch_width
hatch_flange_width

battery_length
battery_width
battery_height
battery_clearance

motor_can_diameter
motor_body_length
motor_shaft_diameter

stern_tube_OD
stern_tube_length
shaft_angle

coupling_length
coupling_OD

propeller_diameter
propeller_keepout_diameter

electrode_fore_aft_spacing
electrode_port_starboard_spacing

magnetometer_forward_offset
magnetometer_height

electronics_tray_height
tray_standoff_pitch
```

These parameters should control the design before cosmetic hull refinement.

---

# 29. Component modeling plan

## Import directly

Use supplied models/files where possible:

### ESP32
Official DXF:
https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html

### ADS1115
Official 3D model:
https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/downloads

### Pololu regulator
Official STEP:
https://www.pololu.com/product/2831/resources

---

## Reconstruct accurately from published mechanical drawings

### Mabuchi RS-380PH-4045
https://product.mabuchi-motor.com/detail.html?id=99

### SparkFun MMC5983MA
https://www.sparkfun.com/sparkfun-micro-magnetometer-mmc5983ma-qwiic.html

### Krick shaft
https://www.krickshop.de/Schiffswelle-Stevenrohr-M2-x-153mm-Eco.htm?ProdNr=65220&a=article

### Krick coupling
https://www.krickshop.de/Zubehoer-Ersatzteile/Zubehoer-fuer-Schiffsmodelle/Schiffswellen-Kupplungen/Welleneinsatz-f-Stegkupplung-2mm.htm?ProdNr=63820&a=article&p=192

### TowerPro SG90
https://towerpro.com.tw/product/sg90-7/

---

## Use conservative envelopes

### Hobbywing ESC
34 × 24 × 14 mm actual; allow wire and installation clearance.

https://www.hobbywing.com/en/products/quicrun-wp-1625-brushed53

### Gens Ace battery
104 × 34.5 × 14.5 mm nominal; make the tray larger.

https://gensace.de/products/gens-ace-g-tech-soaring-2200mah-7-4v-30c-2s1p-lipo-battery-pack-with-xt60-plug

### Propeller
Use a swept cylinder rather than detailed blades.

https://www.krickshop.de/Accessories-Spare-Parts/Accessories-for-Ship-Models/Propellers-for-shipmodels/Schiffsschraube-3Bl-30mm-R-M2.htm?ProdNr=gr2307-30&a=article&p=186&shop=krick_e

---

# 30. Recommended CAD workflow

## Stage 1 — build the component library

Before drawing the boat, create/import:

- ESP32;
- ADS1115;
- regulator;
- magnetometer;
- ESC envelope;
- battery envelope;
- motor;
- coupling;
- shaft/tube;
- propeller keep-out;
- servo.

Verify all units and coordinate systems.

---

## Stage 2 — create a layout-only master assembly

Place every component in space.

Do **not** make the hull.

Establish:

- centerline;
- shaft line;
- intended waterline;
- battery location;
- sensor separation;
- electrode axes;
- hatch service envelope.

---

## Stage 3 — driveline first

Align:

```text
motor axis
    =
coupling axis
    =
prop shaft axis
```

Then choose the shaft angle based on:

- propeller immersion;
- hull bottom;
- motor height;
- coupling clearance.

Do not bend the CAD around an arbitrary stern shape.

---

## Stage 4 — mass layout

Major known masses include:

- battery ~126 g;
- motor ~80 g;
- ESC ~24 g;
- electronics;
- printed hull.

Place the battery so it can be moved fore-aft during initial flotation tests.

A slotted battery tray is preferable to a fixed pocket.

---

## Stage 5 — sensing geometry

Add:

- four electrode bosses;
- magnetometer pod;
- multiple pod mounting positions.

The sensing geometry must remain adjustable.

---

## Stage 6 — service envelopes

Confirm that the following can be removed without damaging the boat:

- battery;
- ESP32;
- ADC/front-end;
- regulator;
- ESC;
- motor;
- servo;
- magnetometer pod;
- propeller;
- shaft if possible.

---

## Stage 7 — hull shell

Only now create:

- lower hull;
- deck;
- internal ribs;
- hatch flange;
- motor supports;
- shaft penetration;
- electrode bosses.

---

## Stage 8 — print interface coupons first

Before printing an entire 350–450 mm hull, print representative sections for:

- hatch/gasket;
- M4 electrode seal;
- stern-tube bond;
- PCB standoffs;
- motor mounting face.

Correct these interfaces before committing to the full print.

---

# 31. What should NOT be modeled in detail

Do not waste CAD time on:

- resistor bodies;
- individual wires;
- heat-shrink;
- detailed propeller blade aerodynamics;
- ESC decorative features;
- battery label artwork;
- screw threads except where needed for fabrication drawings.

For enclosure development, use:

- interface geometry;
- mounting geometry;
- keep-out envelopes;
- connector clearance;
- service clearance.

That is mechanically more useful than a photorealistic assembly.

---

# 32. Procurement order

Purchase in this order:

1. **Mabuchi RS-380PH-4045**
2. **Krick 65220 shaft**
3. **Krick 63800 + 63820 + 63823 coupling components**
4. **Krick/Graupner 2307.30 propeller**
5. **Gens Ace GEA222S30X6GT battery**
6. **TowerPro SG90**
7. **Hobbywing WP-1625**
8. **ESP32-DevKitC V4**
9. **Adafruit ADS1115**
10. **SparkFun MMC5983MA**
11. **Pololu D24V10F5**
12. electrode/passive/integration hardware

The drivetrain and battery should be physically measured before the hull is frozen even though public references exist.

Supplier dimensions are design inputs; the purchased parts are the final acceptance geometry.

---

# 33. CAD freeze rule

Do not freeze the hull until the following actual parts are physically on hand:

- motor;
- shaft;
- coupling;
- propeller;
- battery;
- servo;
- ESC.

Electronics boards with official CAD can be modeled safely before purchase, but physically checking them is still preferable.

---

# 34. Rev-A success criteria

Rev A is successful if it provides:

- stable low-speed flotation;
- single-motor propulsion;
- rudder steering;
- removable battery;
- removable electronics tray;
- replaceable four-electrode array;
- adjustable magnetometer position;
- physically separated sensing and high-current zones;
- maintainable hatch;
- dimensionally controlled drivetrain;
- room for later radio/GPS/data-logging additions.

Hydrodynamic efficiency and visual polish are secondary.

---

# 35. Final design position

The BOM is now sufficiently specific to begin a real master CAD assembly.

The most important changes from the earlier version are:

1. **Generic 370/380 motor → Mabuchi RS-380PH-4045**
2. **Generic shaft kit → Krick 65220**
3. **Generic coupling → Krick 63800 + 63820 + 63823**
4. **Generic propeller → Krick/Graupner 2307.30**
5. **SG90-class servo → genuine TowerPro SG90 Digital**
6. **Generic 2S battery → Gens Ace GEA222S30X6GT**

The electronics were already comparatively well documented and remain:

- ESP32-DevKitC V4;
- SparkFun SEN-19921;
- Adafruit ADS1115 PID 1085;
- Pololu D24V10F5;
- Hobbywing WP-1625.

The resulting assembly can be built from a combination of:

- official STEP/DXF;
- manufacturer fabrication drawings;
- verified dimensional envelopes.

A detailed STEP file for every object is neither necessary nor desirable. The mechanical design requires trustworthy **interfaces and keep-out geometry**, not photorealistic component models.

---

# 36. Primary reference links

- Espressif ESP32-DevKitC V4  
  https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html

- SparkFun MMC5983MA SEN-19921  
  https://www.sparkfun.com/sparkfun-micro-magnetometer-mmc5983ma-qwiic.html

- Adafruit ADS1115 PID 1085  
  https://www.adafruit.com/product/1085

- Adafruit ADS1115 CAD/downloads  
  https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/downloads

- Pololu D24V10F5  
  https://www.pololu.com/product/2831/resources

- Hobbywing WP-1625  
  https://www.hobbywing.com/en/products/quicrun-wp-1625-brushed53

- Mabuchi RS-380PH-4045  
  https://product.mabuchi-motor.com/detail.html?id=99

- Krick 65220 M2 shaft  
  https://www.krickshop.de/Schiffswelle-Stevenrohr-M2-x-153mm-Eco.htm?ProdNr=65220&a=article

- Krick 63800 coupling connector  
  https://www.krickshop.de/Zubehoer-Ersatzteile/Zubehoer-fuer-Schiffsmodelle/Schiffswellen-Kupplungen/Stegkupplung-Verbinder-1-Stck-.htm?ProdNr=63800&a=article&p=192

- Krick 63820 2.0 mm coupling insert  
  https://www.krickshop.de/Zubehoer-Ersatzteile/Zubehoer-fuer-Schiffsmodelle/Schiffswellen-Kupplungen/Welleneinsatz-f-Stegkupplung-2mm.htm?ProdNr=63820&a=article&p=192

- Krick 63823 2.3 mm coupling insert  
  https://www.krickshop.de/Zubehoer-Ersatzteile/Zubehoer-fuer-Schiffsmodelle/Schiffswellen-Kupplungen/Welleneinsatz-f-Stegkupplung-2-3mm.htm?ProdNr=63823&a=article&p=192

- Krick/Graupner 2307.30 propeller  
  https://www.krickshop.de/Accessories-Spare-Parts/Accessories-for-Ship-Models/Propellers-for-shipmodels/Schiffsschraube-3Bl-30mm-R-M2.htm?ProdNr=gr2307-30&a=article&p=186&shop=krick_e

- TowerPro SG90 Digital  
  https://towerpro.com.tw/product/sg90-7/

- Gens Ace G-Tech 2200 mAh 2S, GEA222S30X6GT  
  https://gensace.de/products/gens-ace-g-tech-soaring-2200mah-7-4v-30c-2s1p-lipo-battery-pack-with-xt60-plug
