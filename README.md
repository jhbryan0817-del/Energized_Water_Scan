# Energized Water Scanner USV

Energized Water Scanner is a small unmanned surface vessel (USV) research platform for measuring spatial voltage differences in water. Four independently actuated electrode probes fold into recessed channels for transport and deploy below the hull for measurement. The vessel combines the sensing mechanism with an electric propulsion shaft, rudder steering, onboard power conversion, protected analog acquisition, and an ESP32-class controller.

The project is intended to explore repeatable electric-potential-gradient measurements and their mapping from a mobile platform. It is **not** a certified electrical-safety instrument: a low or absent reading cannot establish that water is safe.

![Current live Fusion assembly with service hatch open](previews/RevE2_2026-10-01_open.png)

## System overview

- **Hull:** 320 × 176 mm printed enclosure with a continuous removable hatch and gasket.
- **Sensing array:** four 166 mm insulated probe arms with stainless tip electrodes and independent 0–90° deployment.
- **Actuation:** four dry HS-65HB servos driving sealed output shafts through proposed 1:1 timing transmissions.
- **Propulsion and steering:** RS-380-class motor, inclined shaft/stern tube, 30 mm propeller, rudder stock, and a separate steering servo.
- **Electronics:** protected electrode front end, ADS1115 conversion, ESP32-class controller, ESC, logic regulator, and a dedicated 5 V probe-servo supply.
- **Service architecture:** removable electronics cassette, longitudinal battery cradle, forward controller shelf, individually disconnectable probe actuators, and separated analog/power cable routes.

## Design package

- [Rev-E2 physical controller, battery and wiring corrections](docs/RevE2_Changes.md)
- [1 October live mechanical/component audit and service corrections](docs/Mechanical_Audit_2026-10-01.md)

- [Rev-E1 hull repairs, before/after and validation](docs/RevE1_Changes.md)
- [Mechanical design, interfaces, and measurement geometry](docs/Design.md)
- [Waterproofing and assembly audit](docs/Waterproofing_and_Design_Audit.md)
- [Leakage paths and build qualification gates](docs/Build_Qualification.md)
- [Wiring and assembly guide](docs/Wiring_and_Assembly.md)
- [Print and procurement plan](docs/Print_and_Procurement.md)
- [Complete BOM workbook](BOM.xlsx) and [CSV mirror](BOM.csv)
- [Fusion archive](cad/Energized_Water_Scanner_RevE.f3d) and [STEP reference](cad/Energized_Water_Scanner_RevE.step)
- [Verification reports](verification) and [Fusion audit scripts](scripts/README.md)

The live Fusion document is now **Rev-E2 (1 October 2026)**. It moves the controller onto a forward removable shelf, raises/repositions the battery for a straight lift, relocates two cradle mounts for driver access and adds wire-tie saddles. Five printed geometries change: 01/03/04/25/31; the print count and complete BOM remain unchanged. The earlier Rev-E1 wall repair and 20 sealed mounting-bore caps are retained. Repository STL/STEP/F3D files are historical and do not include these changes. Use the saved live Fusion assembly; no new 3D exports are included in this iteration.

## Build status

Rev-E2 is a **mechanical fit prototype**, not a water-ready release. The current audit finds nominal manufacturer agreement for most major envelopes, but exact servo horns/transmission, coupling assembly, propeller SKU, steering interfaces, sealing and loaded flotation remain open. Static solid checks found no unintended rigid-body intersections, and sampled probe motion found no modeled collisions. The propulsion train is coaxial at its intended 15° inclination. These are CAD results, not substitutes for hardware validation.

Before water operation, the team must qualify the shaft seals, cartridge gaskets, potted wire feedthroughs, stern-tube bond **and internal shaft-to-tube leakage path**, steering boot, hatch compression, flexible probe wiring, transmission retention, loaded flotation, and fail-safe actuator behavior. Fit and cycle one complete probe actuator before purchasing or printing four sets. The four servo service covers do not provide independent waterproof compartments.

## Measurement concept

The four deployed electrodes provide three coherent signed voltage differences relative to a reference electrode. Their known positions and vessel attitude can support a local field-gradient estimate when the geometry is sufficiently well conditioned. The current nominal measurement pose is E1/E2/E3/E4 = **60°/20°/20°/45°**; calibration must still account for arm-angle error, electrode offsets, phase, conductivity, and boat attitude.

## Electronics procurement summary

The [Energized Water Scanner sheet](https://docs.google.com/spreadsheets/d/129cdgjaWSUko2g8DQrpoiBbZISE-RidNFI1MubGNuU8/edit?gid=372890739#gid=372890739) is an 11-line major-electronics summary with the existing seven columns, concise search keywords and neutral table banding. The complete 79-line repository BOM, its quantities and estimates are unchanged. This audit publishes written guides and native viewport PNGs only; the current model is saved in Fusion without new CAD exports.
