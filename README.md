# Energized Water Scanner USV — Rev G

The live Fusion **Energized_Water_Scanner** now uses an **IoT Beyond Lab custom PCB** in place of the PRINT_03 tray. The ESP32 sits on the carrier with accessible GPIO expansion. Two isolated measurement ranges, an onboard ADS1115 and separate logic/servo supplies replace the prior loose electronics arrangement.

![Rev G live Fusion assembly](previews/RevG_assembly_top.png)

## Current files — 2 October 2026

- [KiCad 10 project and circuit/assembly guide](pcb/RevG/README.md)
- [Schematic PDF](pcb/RevG/EWS_RevG_schematic.pdf), [PCB](pcb/RevG/EWS_RevG.kicad_pcb), [BOM](pcb/RevG/BOM.csv), [connector pin map](pcb/RevG/PIN_MAP.md)
- [Fusion archive](cad/RevG/Energized_Water_Scanner_RevG.f3d), [STEP assembly](cad/RevG/Energized_Water_Scanner_RevG.step), [current STL set](cad/RevG/stl), [print manifest](cad/RevG/print_manifest.json)
- [Changes and verification](docs/RevG_Changes.md)
- [Manufacturing review files and release limits](pcb/RevG/manufacturing_review/READ_BEFORE_ORDERING.md)

The 91 × 124 mm PCB matches the measured U-shaped tray base and four mounting holes. The old tray, four electronics capture bridges and rear ESP32 shelf have been removed. The obsolete rear controller posts/ribs were cut from the hull; lower roots at the chine remain to preserve hull structure. Motor, battery, steering and probe supports retain their useful functions. The current print export has **13 bodies**, down from 19.

**Electrical status:** routed engineering prototype; automated ERC, DRC, connectivity and schematic parity checks pass. The design targets separate sensitive and 600 V AC RMS, 50/60 Hz ranges for low-voltage utility faults. It has **not** passed physical high-voltage, transient, single-fault, wet-insulation, sensitivity or calibration tests. It is not a certified electrical-safety instrument. A low reading does not mean water is safe. Fabrication files are supplied for engineering review and controlled prototype development.

The two E2/E4 probes provide one differential measurement along their separation. Historical four-probe firmware/presets and procurement files do not apply unchanged. The prior root-level BOM.xlsx/BOM.csv and CAD releases remain historical references; use the Rev G package for electronics and the current STL manifest for printing.

[Earlier mechanical qualification](docs/Build_Qualification.md) and [waterproofing audit](docs/Waterproofing_and_Design_Audit.md) remain relevant. Rev G does not claim those physical qualification gates are complete.
