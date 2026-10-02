# IoT Beyond Lab — EWS Rev G

Rev G replaces the live Fusion PRINT_03 electronics tray with a four-layer, 2 mm carrier PCB. It brings the ESP32 forward onto sockets, exposes its usable pins, integrates a dual-range isolated analog front end and the ADS1115, and retains separate Pololu logic and servo supplies. This is an **engineering prototype, not a qualified 600 V instrument**. The manufacturing exports are review candidates; do not energize the electrodes at hazardous voltage on the strength of ERC/DRC results.

Open `EWS_RevG.kicad_pro` in KiCad 10. The native hierarchical schematic, routed board, project symbol/footprint libraries, component models, BOM, pin map and verification reports are included. `EWS_RevG_schematic.pdf` is the printable circuit reference. The companion mechanical directory (`mechanical/` in the download, `../../cad/RevG/` in the repository) contains the updated live Fusion exports; `manufacturing_review/` contains Gerber and drill files.

## Mechanical interface

- Exact measured tray base perimeter: X −20…71 mm, Y −62…62 mm; 91 × 124 mm overall. The motor opening is 58 × 48 mm, bounded by X 13…71 and Y −24…24.
- Four Ø3.4 mm mounting holes: (−17, −58.5), (67, −58.5), (−17, 58.5), (67, 58.5), in Fusion millimetres. KiCad X = Fusion X + 50; KiCad Y = 100 − Fusion Y.
- Initial stack: original supports at Z32, 1 mm nylon spacers, PCB Z33…35. Use nylon hardware. Trim solder tails and inspect underside clearance. Verify screw engagement in the actual printed pilots; do not deepen pilots into wet channels.
- U1 uses two 19-way, 2.54 mm sockets with 25.4 mm row spacing. WROOM DevKitC V4 is required. GPIO16/17 availability differs on WROVER variants.
- ESC retains its original 34 × 24 × 14 mm envelope, rotated into X3…27/Y31.5…65.5. A 22 × 29 mm pair of SJ3550 fastener pieces replaces the printed clamp, with nominal 5.8 mm engaged thickness. Bond, retention and thermal performance require physical tests. The motor power harness remains external to the PCB.
- USB service: remove boat power and JP1. The ESP32 can be lifted from its sockets for a straight USB cable; the installed connector neighbourhood does not guarantee room for every plug.

The ESP32 and large servo regulator models show PCB, headers, shield/inductor and recognizable package details. They are fit models, not manufacturing drawings. The smaller regulator uses the existing official Fusion model. ESC fin details are illustrative within its measured envelope. Standard SMD models come from KiCad.

## Circuit and operating assumptions

E2/E4 feed two continuously connected measurement paths. Each electrode leg contains four 249 kΩ resistors in series. The high path has 1 kΩ sense resistors to floating HV_REF (nominal differential attenuation 997:1); the sensitive path uses 100 kΩ (10.96:1). Each path has its own AMC3330 isolated amplifier/DC-DC converter. The floating high-side references are common; their isolated supply outputs are **not** paralleled. HV_REF must never be connected to logic ground, an expansion ground, USB ground or an earth-referenced oscilloscope ground.

BAV199 antiparallel clamps protect both input nodes of each path. The sensitive path intentionally overloads on high voltage. Its conservative initial working span is ±2 V differential; its true linearity and recovery must be measured. The high path targets 600 V AC RMS at 50/60 Hz, excluding distribution lines. This voltage target does not define an installation category, impulse withstand rating, common-mode immunity or wet-enclosure rating.

At 600 V RMS differential, the nominal high-channel input peak is 0.851 V. Each 249 kΩ resistor carries approximately 75 V RMS and dissipates about 22.5 mW in normal high-voltage division. Both parallel paths together load the electrodes by approximately 1 MΩ during a large fault. These calculations do not cover an open resistor, shorted component, arc, surge, contamination or failed clamp.

The two AMC outputs feed differential ADS1115 channels through 1 kΩ/330 nF filters. AIN0−AIN1 is high range; AIN2−AIN3 is sensitive range. These replace the historical E2=A1/E4=A3 assignments. The approximately 241 Hz analog pole attenuates 50/60 Hz and must be included in calibration. Suggested starting PGA settings: ±2.048 V for high and ±0.512 V for sensitive, at 860 samples/s. Alternate channels with explicit conversion-complete timing; account for settling and sampling phase when computing RMS. This package does not include validated acquisition firmware.

Nominal input-referred quantization is about 31 mV/count on high and 86 µV/count on sensitive. **Neither is an accuracy or detection-floor claim.** AMC offset alone can contribute about 3.3 mV input-referred on sensitive; input bias mismatch can contribute roughly 20 mV using conservative limits, before diode leakage, temperature, resistor error, noise and calibration. A low reading cannot establish that water is safe.

J4 exposes active-low amplifier diagnostics and ADC READY, plus both differential analog outputs. Firmware must treat diagnostic failure, ADC clipping, stale data, startup and uncharacterized sensitive-range recovery as invalid measurements. Diagnostic pins are available at J4 for wiring to spare ESP32 inputs; they are not silently assigned to an existing actuator GPIO.

## Power and assembly

1. Assemble passives, ICs and headers from the BOM and top assembly drawing. MSOP-10 ADS1115 has 0.5 mm pitch: inspect every joint under magnification. Check pin-1 orientation and both AMC supply decoupling networks.
2. Fit regulators with at least 2 mm underside clearance. U5 pin order is PG, SHDN, VIN, GND, 5V; U6 is EN, VIN, GND, GND, 5V, as viewed in the project footprint. J9 control pins are VIN-referenced; do not connect them directly to an ESP32 GPIO.
3. Feed J11 from a separately fused 2S branch, observing polarity. The board has no reverse-battery protection. Use a current-limited bench supply for first power-up. The 1.2 mm power routes and 2 oz outer copper are a design starting point; initially limit combined servo load to 2 A and qualify peak/stall current, temperature and connector ratings. Do not infer 5 A board capability from the regulator's product name.
4. ESC motor/battery current uses an appropriately fused external harness. At J8, remove/insulate the ESC BEC lead: centre pad is deliberately NC. Never parallel the ESC BEC with either regulator.
5. JP1 feeds the ESP32's 5 V pin from U5. Remove it before USB. All expansion signals are 3.3 V only. Input-only and boot-strapping GPIO restrictions remain applicable.
6. Solder suitably insulated electrode leads to J12/E2 and J13/E4; provide strain relief and a qualified insulating enclosure over the entire input section. No raw electrode connection is exposed on the logic expansion headers. Lead insulation, wet penetrations and potting must be qualified for the intended exposure.

See `PIN_MAP.csv` and `PIN_MAP.md` for every pin, including unused GPIO. Square copper pads identify pin 1. Reference labels and connector legends are also printed on the reverse side; use the top assembly drawing when soldering SMDs.

## Checks and release limits

The saved `DRC.json` and `ERC.json` record automated checks, including schematic parity. Custom rules enforce an 8 mm copper separation between floating input and logic nets and voltage-graded functional spacing within the resistor networks. Solder mask is not credited as safety insulation. The rules are engineering targets, not a derivation of regulatory compliance. Four-layer dielectric construction and conductor overlaps also require an insulation review.

Before hazardous-voltage use, an appropriately equipped laboratory must establish the applicable measurement category/pollution degree and validate creepage, clearance, laminate CTI, dielectric withstand, transient withstand, leakage, single faults, humidity/contamination, enclosure/lead insulation, power-load faults, thermal rise, EMI, calibration, sensitivity and overload recovery. Use isolated, current-limited signal sources for initial development. Do not use a person, animal or energized body of water as a test load.

No physical test, calibration, environmental qualification or certification was performed in this design session. Manufacturing output exists to support review and controlled prototype development, not a safety release.

## Primary design references

- [TI AMC3330 datasheet](https://www.ti.com/lit/ds/symlink/amc3330.pdf): pinout, supply networks, input/output limits and isolation component ratings.
- [TI ADS1115 datasheet](https://www.ti.com/lit/ds/symlink/ads1115.pdf): differential multiplexer, PGA, timing and input limits.
- [Nexperia BAV199](https://assets.nexperia.com/documents/data-sheet/BAV199.pdf): pin 1 anode, pin 2 cathode, pin 3 shared midpoint; leakage and limits.
- [Vishay TNPW e3](https://www.vishay.com/docs/28758/tnpw_e3.pdf): 1206 resistance/tolerance, working voltage and dissipation.
- [Espressif DevKitC V4](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html): header and power constraints.
- [Pololu D24V10F5](https://www.pololu.com/product/2831), [D24V50F5](https://www.pololu.com/product/2851): module drawings and control pins.
- [3M SJ3550](https://www.3m.com/3M/en_US/p/d/b40072056/): nominal engaged thickness and removable fastening system.

## Tool provenance

Fusion was edited and saved through its local MCP script interface. KiCad native files were authored through KiCad 10’s pcbnew API and checked/exported by kicad-cli. The enabled IPC endpoint answered its version request but did not expose an open-document handler, so live IPC board-editing was unavailable. The saved project remains fully editable in KiCad 10.
