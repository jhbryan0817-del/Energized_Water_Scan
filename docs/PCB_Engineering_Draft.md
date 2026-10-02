# IoT Beyond Lab — PCB engineering work in progress

**Not a completed PCB. Not for fabrication, assembly, or connection to energized water.**

The included KiCad project is a mechanical template only. It has the measured board perimeter, four non-plated mounting holes and branding. It has no electrical footprints, schematic, nets, routing or voltage rating. A clean mechanical DRC does not validate an electrical design.

## Confirmed requirements

- Replace the current PRINT_03 tray with a PCB; put the ESP32 and associated electronics on it.
- Provide clearly labeled accessible expansion connections and two electrode connections, E2/E4.
- Preserve separate logic and servo power rails and accommodate the existing motor/ESC, steering servo, two probe servos, ADC and controller.
- Branding: **IoT Beyond Lab**.
- The user selected a **600 V AC RMS, 50/60 Hz utility-mains fault envelope**, excluding higher-voltage distribution/transmission lines.
- The user selected **separate sensitive and high-voltage measurement ranges**.
- This is a design target, not a demonstrated or certified withstand rating. No measurement-category or impulse rating has been established.

## Verified mechanical interface

Source: live Fusion document `Energized_Water_Scanner`, inspected 2 October 2026. Repository CAD/STL files were not used as geometry sources.

- Base perimeter: 91 × 124 mm, from Fusion X −20…71 mm, Y −62…62 mm.
- Open motor cutout: X 13…71 mm, Y −24…24 mm (58 × 48 mm).
- Mounting axes: (−17, −58.5), (67, −58.5), (−17, 58.5), (67, 58.5) mm.
- Source holes: diameter 3.4 mm. Keep copper, components and high-voltage conductors away from fasteners.
- Existing tray base: Z 32…35 mm. The template's 1.6 mm board thickness is provisional; it does not preserve the previous screw stack or component elevations automatically. Spacers, screw engagement and underside clearance require resolution.
- The full tray bounding box also includes supports up to Z 67.5 and Y 65 mm. Those supports are not part of the flat base outline.
- Mapping: KiCad X = Fusion X + 50; KiCad Y = 100 − Fusion Y.

The electronics tray is U-shaped. Filling the motor opening with a rectangular PCB would interfere with the drivetrain. Mechanical fit of populated parts and wiring has not yet been checked.

## Electrical design findings

The repository contains no released electrode schematic or firmware implementation. Its `BOM-013` is explicitly a 40 × 30 × 12 mm allocation with resistor/clamp/filter quantities awaiting validation. The old 499 kΩ/100 kΩ/BAT54S description cannot be used as a validated 600 V protection circuit.

The ESP32 is an Espressif DevKitC V4. Its unused GPIOs need labeled headers, but flash pins D0/D1/D2/D3/CMD/CLK are not general-purpose expansion pins. GPIO34–39 are input-only; boot-strapping pins need explicit markings; GPIO16/17 availability depends on the fitted module. USB and external 5 V supplies must not be paralleled unintentionally. [Espressif reference](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html)

The ADS1115's programmable gain does not make its input pins tolerant of high voltage. It belongs downstream of a protected isolated interface. A1/A3 is an available differential MUX selection; the existing historical electrode names are not enough to establish the new signal-chain wiring. The two ranges require an intentional acquisition schedule, settling/filter calculations, saturation detection and calibration. [TI ADS1115 data sheet](https://www.ti.com/lit/ds/symlink/ads1115.pdf)

The Pololu D24V10F5 logic and D24V50F5 servo regulators must retain separate outputs. Their SHDN/ENABLE pins are pulled toward VIN on the modules; do not wire these directly as ordinary 3.3 V GPIO expansion signals. Provide suitable control interfacing or explicitly mark them as VIN-referenced. The ESC motor-current path should remain in a rated external harness unless PCB current capacity, connectors, fusing and thermal rise are designed and verified. [D24V10F5](https://www.pololu.com/product/2831), [D24V50F5](https://www.pololu.com/product/2851)

## Sensing architecture to develop

Two electrode terminals → high-voltage input/protection region → protected sensitive and wide measurement paths → isolation barrier → ADC/controller region.

Both paths must tolerate the full fault; a sensitive path must not bypass protection. An isolated amplifier such as TI's AMC3330 is a candidate building block for the wide path, with integrated isolated power. It is not a complete 600 V instrument. Its package isolation rating does not rate the surrounding resistor network, PCB, terminals, wiring or wet assembly. [TI AMC3330 data sheet](https://www.ti.com/lit/ds/symlink/amc3330.pdf), [TI split-tap reference circuit](https://www.ti.com/lit/an/sbaa553/sbaa553.pdf)

For an illustrative 1000:1 input divider and gain-2 isolation amplifier, an ADS1115 at ±4.096 V has 0.0625 V input-referred quantization. An isolation-amplifier input offset of ±0.3 mV becomes ±0.3 V at the electrodes before calibration. Increasing gain only on the isolated amplifier's output cannot recover information already lost to input offset/noise. These calculations are architecture checks, not a selected circuit or promised sensitivity.

Sensitive-path signal floor, bandwidth, allowable electrode loading and calibration stability remain to be specified or demonstrated. Protection design also needs surge/impulse conditions, common-mode exposure to the low-voltage system, condensation/pollution assumptions and fault behavior. Continuous 600 V RMS alone does not resolve those requirements. Select component voltage/pulse ratings and PCB creepage/clearance from the resulting insulation design, rather than treating a generic spacing rule as certification.

No minimum detected field, alarm threshold, detection probability or water-safety decision is claimed. Two electrodes measure a projection of the field; low/zero differential readings can occur with unfavorable orientation or failed leads.

## Mechanical changes after the populated PCB is ready

Candidates verified by live occurrence name:

- `PRINT_03_Removable_electronics_tray (1):1` — replace with the populated PCB/support stack.
- `PRINT_18_ESP32_capture_bridge:1`, `PRINT_19_Front_end_capture_bridge:1`, `PRINT_20_Regulator_capture_bridge:1`, `PRINT_21_ESC_capture_bridge:1` — obsolete only after replacement retention is supplied.
- `PRINT_31_Rear_starboard_controller_shelf:1` — remove after ESP32 relocation.
- Rear controller supports integrated into the hull — identify exact features and remove without damaging the hull shell, battery cradle, wet roofs or unrelated supports.

Keep the motor supports/liner, steering saddle, probe mechanisms, seals and battery retention. The ESC is a wired packaged module, not a through-hole daughterboard; it still needs mechanical retention and strain relief even when its electrical connections terminate on a PCB.

## Completion status

Completed: repository electronics/document review; live Fusion inventory and tray geometry extraction; KiCad mechanical source and constraints; this requirements/engineering record.

Not completed: released schematic, dual-range protection design, detailed component layout, routing, electrical ERC/DRC, populated 3D model, support removal, Fusion design update/save, new STL/assembly exports, fabrication outputs, bench tests or high-voltage qualification.

The current Fusion assembly was inspected but not altered. This follows the request to replace the tray **once the PCB is complete**. Old geometry has not been removed in advance of a functioning replacement.
