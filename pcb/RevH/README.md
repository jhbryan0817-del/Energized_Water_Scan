# Energized Water Scanner — PCB Rev H

**Engineering prototype, 3 October 2026.** Native KiCad 10 sources for the two-electrode flood-hazard research USV. Open `EWS_RevH.kicad_pro`. This revision changes electronics only. A subsequent 4 October live Fusion Rev I iteration updates the mechanical fit representation; see [CAD audit](../../docs/CAD_Audit_2026-10-04.md). No new STEP, F3D or STL was generated.

## What changed

- U4 at I2C address **0x48** acquires the high range. New U7 at **0x49** acquires the sensitive range. Both use AIN0–AIN1; each can run continuously at 860 samples/s nominal without alternating ranges. Their clocks are independent, so this is concurrent acquisition, not phase-synchronous sampling.
- Amplifier diagnostics and conversion-ready signals are routed to ESP32 inputs. No diagnostic fly-wires are needed. The existing expansion header still exposes these nets, but they are now reserved.
- J11 feeds F1, then a P-channel reverse-polarity MOSFET Q1. D5 suppresses positive transients on protected VBAT; D6 limits gate-source voltage. Added local rail capacitors supplement the regulator modules.
- A filtered 200 kΩ/33 kΩ battery divider, with 10 kΩ series and 100 nF at GPIO32, feeds ADC1 GPIO32. Its nominal ratio is 7.0606:1 (1.190 V at an 8.4 V battery), with an approximately 41.5 Hz pole. Select and calibrate the ESP32 ADC attenuation accordingly. J14 supports a dry-compartment, 3.3 V, open-drain ingress sensor on GPIO23. This is a powered sensor interface, not a pair of bare-water electrodes.
- Existing high-voltage divider networks, isolation packages, antenna restriction, U-shaped perimeter, motor opening and mounting holes are retained. The schematic, BOM and connector map describe the same board.

## Measurement capability and limits

E2 and E4 measure **signed differential voltage** along one probe separation. The DC-coupled analog circuit also permits AC measurements; initial AC qualification is for 50/60 Hz. These electrodes do not measure total current in floodwater. Under a validated locally uniform field model, the projected field is approximately `E_parallel = V / separation`. Estimating current density further requires conductivity, `J = conductivity × E`; total current also requires a defined area and field distribution. No conductivity sensor is included in this board. Use an independently isolated conductivity instrument if that quantity is needed; the ordinary I2C header is not an isolation barrier.

Two probes can miss a field perpendicular to their separation. A scan must include validated changes in orientation, accurate pose/time/location, immersion verification and invalid-data handling. Position/heading sensors can use the available 3.3 V I2C/UART interfaces; they are not fitted by this revision. DC electrode polarization, electrode material, fouling, contact impedance and motion-generated signals must be characterized separately from electronic DC response.

| Property | High range | Sensitive range |
|---|---:|---:|
| Series resistance per electrode leg | 4 × 249 kΩ | 4 × 249 kΩ |
| Sense resistance per leg | 1 kΩ | 100 kΩ |
| Ideal attenuation before isolation | 997:1 | 10.96:1 |
| Isolation-amplifier differential gain | 2 | 2 |
| Initial measurement target | 600 V RMS, 50/60 Hz; ±850 V DC engineering ceiling | ±2 V instantaneous |
| Initial ADS1115 PGA | ±2.048 V | ±0.512 V |
| Ideal electrode-referred code step | 31.16 mV | 85.63 µV |

These are design calculations, **not demonstrated accuracy, detection thresholds or exposure ratings**. The DC ceiling gives approximately the same divider stress as the crest of the AC target; continuous DC and wet electrochemistry still require separate validation. The low range intentionally clamps during a large fault. Do not use it until recovery has been characterized. PGA changes cannot recover a clipped amplifier signal or improve the amplifier's input offset.

Each differential ADC filter is 1 kΩ + 1 kΩ with 330 nF across the inputs: ideal pole 241 Hz. The ideal analog amplitude factors are approximately 0.979 at 50 Hz and 0.970 at 60 Hz. Include ADC digital-filter response, source loading, capacitor tolerance and temperature in calibration. Neither this pole nor the converter establishes broadband anti-alias performance. Fast impulses, arbitrary inverter spectra and high-frequency hazard characterization are not released capabilities.

At 600 V RMS, the ideal high-range AMC input is 0.851 V peak; its outputs remain approximately 0.589–2.291 V around the nominal 1.44 V common mode. Normal divider dissipation is about 22.5 mW per 249 kΩ resistor. Both channels together load the electrodes by about 1.044 MΩ before clamping and approximately 1 MΩ in a large fault. The source/electrode impedance can therefore produce substantial loading error. Per-resistor working voltage does not establish pulse withstand or a single-fault rating.

The AMC3330's specified input offset alone corresponds to about 0.299 V high-range or 3.29 mV sensitive-range electrode-referred error before calibration. Bias-current mismatch, clamp leakage, resistor matching, temperature and electrode effects add further error. A fine ADC code step is not proof of microvolt detection. Validate range overlap and retain separate calibration coefficients.

## Pin assignments

See [PIN_MAP.md](PIN_MAP.md) and `PIN_MAP.csv` for every connector pin.

| ESP32 GPIO | Rev H use |
|---|---|
| 36, input only | U4 high-range READY, active low; configure ADC conversion-ready mode |
| 35, input only | U7 sensitive-range READY, active low |
| 34, input only | U2 high-range DIAG, active low |
| 39, input only | U3 sensitive-range DIAG, active low |
| 32 / ADC1 | Battery health divider; calibrate ADC attenuation and gain |
| 23 | J14 ingress-sensor input; 10 kΩ pull-up, 1 kΩ series, 100 nF filter |
| 21 / 22 | SDA / SCL, 3.3 V I2C; addresses 0x48 and 0x49 reserved |
| 25 / 26 / 27 / 14 | E2 servo / E4 servo / steering / ESC control |

ADC AIN2 and AIN3 are grounded on each converter. They can support an occasional zero-input diagnostic during a deliberately invalidated acquisition interval. They are not available as general external analog inputs. J4 exposes both isolated-side analog pairs for service, and high READY/DIAG nets; low READY is also on J1 pin 6. Never connect anything on the floating electrode side to J4 or logic ground.

## Power and assembly

Use a **2S battery only**, 8.4 V maximum normal input. An external branch fuse near the battery remains necessary to protect its harness. F1 is a provisional 3 A fast fuse for the PCB branch; coordinate its interrupt rating and time-current curve with available fault current, inrush, connector ratings and measured loads. Motor/ESC propulsion current remains in its separate fused harness. F1 does not protect that harness.

Q1 is deliberately connected with **drain/tab to BAT_FUSED and source to protected VBAT**; reversing those connections defeats reverse-input blocking. At 2 A and the 10 mΩ room-temperature resistance limit quoted at −4.5 V gate drive, its calculated conduction loss is about 40 mW, before temperature increase. This is not a thermal qualification. It is not an ideal-diode controller and does not provide general backfeed isolation between powered sources.

D5 is a 12 V standoff SMBJ12A with a specified 19.9 V clamp at its rated test current. Actual overshoot, lead inductance, pulse energy and fuse coordination need testing. It is a battery-rail suppressor, not an electrode surge arrestor. Do not apply a sustained overvoltage or infer an automotive/load-dump rating. C40/C41/C42 are 25 V X5R parts; C41/C42 sit on 5 V outputs. Check effective capacitance under bias.

Keep combined servo load initially at or below the previous 2 A development limit, with a current-limited supply, and validate stall peaks and trace/via temperatures. Do not infer board current capacity from the D24V50F5 regulator name. New capacitors beneath U5/U6 require component height ≤1.35 mm and a measured ≥2 mm module standoff; check solder joints and module underside components too.

Disconnect the battery and remove JP1 before USB service. The ESP32 can be removed from its sockets. Battery monitoring is not an autonomous cell-balancing, undervoltage-cutoff or battery-management system. Do not leave the battery connected with the MCU supply deliberately removed: divider injection into an unpowered input has not been qualified. J14 is for short internal wiring to a compatible sensor; no exposed floodwater connection or external surge rating is provided. An absent sensor can resemble a dry condition and needs a pre-run functional check.

All GPIO are 3.3 V only. Retain a WROOM DevKitC V4. Flash pins remain unavailable; boot-strapping restrictions still apply to the remaining expansion pins. U5/U6 control pins at J9 are VIN-referenced, not direct GPIO interfaces. Leave the ESC BEC lead disconnected and insulated. Never parallel the regulator outputs.

## Mechanical interface

Six copper layers, 2 mm thickness, 91 × 124 mm overall. Fusion coordinates: X −20…71, Y −62…62 mm. Motor opening: X 13…71, Y −24…24 mm. Four Ø3.4 mm holes: (−17,−58.5), (67,−58.5), (−17,58.5), (67,58.5). KiCad X = Fusion X + 50; KiCad Y = 100 − Fusion Y.

Retain the Rev G 1 mm nylon spacer arrangement, subject to actual screw engagement and underside solder-tail clearance. The existing outline and hole geometry are checked against the previous board. Populated heights, leads, connectors, ESC attachment and hatch clearance must be checked in the next Fusion iteration and on real hardware. The populated fit representation is maintained only in the live Fusion document; it is not a supplier-certified assembly or a manufacturing export.

The nominal six-layer stack uses 70 µm outer and 35 µm inner copper, dielectric layers 0.20/0.30/0.70/0.30/0.20 mm, and 0.01 mm mask per side. It totals 2.00 mm. The fabricator must confirm materials, pressed thickness, tolerances and insulation requirements. No controlled impedance is claimed. The added layers provide space through the restricted neck without reducing the input-isolation rules.

## Verification and next work

**Final automated results: zero ERC violations, zero DRC violations, zero unrouted connections and zero schematic parity issues.** A separate schematic-netlist/board/manifest comparison matched 319 connected pins. Exact Edge.Cuts geometry and the four mounting holes match Rev G. `ERC.json`, `DRC.json`, `verification.json` and `calculations.json` record the checks actually performed. ERC/DRC cannot validate a circuit topology, component derating, electrode performance or electrical safety. Custom copper rules retain the prior 8 mm floating-input-to-logic target and graded internal divider spacing. They do not derive creepage, installation category, pollution degree, laminate CTI or wet-insulation compliance.

Before hazardous exposure, obtain a qualified insulation/protection review and laboratory verification of common-mode and differential exposure, surges, single faults, resistor failures, clamp leakage/recovery, humidity/contamination, dielectric withstand, lead/enclosure insulation and thermal limits. Establish actual sensitivity and calibrated bandwidth using isolated, current-limited laboratory sources. Do not test in occupied energized water. A low reading, broken lead, dry probe, stalled conversion or saturated channel must never be interpreted as safe water.

Firmware is deferred. Its contract is: configure both converters explicitly; timestamp each ready event; detect stale data, clipping, DIAG faults, startup and recovery; invalidate health failures; calculate DC and AC quantities separately; log pose/location and uncertainty. No minimum detectable field or alarm threshold is released.

## Primary references

- [TI AMC3330](https://www.ti.com/lit/ds/symlink/amc3330.pdf): isolated amplifier limits, input/output behavior and supply network.
- [TI ADS1115](https://www.ti.com/lit/ds/symlink/ads1115.pdf): PGA, MUX, I2C addressing and conversion-ready timing.
- [Diodes DMPH3010LK3](https://www.diodes.com/datasheet/download/DMPH3010LK3.pdf): MOSFET pinout and ratings.
- [Littelfuse SMBJ](https://m.littelfuse.com/~/media/electronics/datasheets/tvs_diodes/littelfuse_tvs_diode_smbj_datasheet.pdf.pdf) and [451/453 fuse series](https://www.littelfuse.com/~/media/electronics/datasheets/fuses/littelfuse_fuse_451_453_datasheet.pdf.pdf).
- [Espressif DevKitC V4](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html), [Pololu logic module](https://www.pololu.com/product/2831), [Pololu servo module](https://www.pololu.com/product/2851).

Native files were edited through KiCad's pcbnew API and checked with kicad-cli 10.0.6. The local IPC server answered the version query but returned no open-document handler. No claim of live IPC board editing or physical testing is made.

The native schematic uses project-local functional pin-map symbols with named global nets, continuing the previous project style. It is electrically editable and checked for board parity; it is not a substitute for an independent circuit review. No new fabrication order or manufacturing release is authorized by these reports.

Checks use the configured project rules. The reports list inherited ignored checks, including missing courtyards, track-to-via centering and footprint filters. No new violation was excluded to obtain the result. Mechanical fit of parts above sockets or module standoffs remains a separate check. The archive intentionally excludes 3D models; references inherited from Rev G are represented in the live Fusion fit assembly, with provisional envelopes identified in the CAD audit.
