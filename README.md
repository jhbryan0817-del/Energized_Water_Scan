# Energized Water Scanner USV

A small unmanned surface vessel for research into detecting and mapping electrical hazards in flooded areas. Two deployable electrodes, E2/E4, measure voltage difference; the vessel must combine that measurement with validated probe pose, orientation and location. A low reading cannot establish that water is safe.

## Current state — 3 October 2026

**Electronics: Rev H engineering prototype. Mechanical assembly: Rev G.** The PCB retains the 91 × 124 mm U-shaped perimeter, 58 × 48 mm motor opening, four mounting holes and 2 mm thickness. Six copper layers accommodate the revised electronics. Fusion integration of the new populated PCB is the next iteration; no 3D files changed here.

- [PCB design, operating limits and assembly](pcb/RevH/README.md)
- [Editable KiCad project](pcb/RevH/EWS_RevH.kicad_pro), [schematic PDF](pcb/RevH/EWS_RevH_schematic.pdf), [PCB BOM](pcb/RevH/BOM.csv), [connector pin map](pcb/RevH/PIN_MAP.md)
- [System design](docs/Design.md), [assembly and procurement](docs/Wiring_and_Assembly.md), [remaining qualification work](docs/Build_Qualification.md)
- [System BOM](BOM.csv): mechanical/harness items plus one assembled carrier. Components on that carrier are listed only in its PCB BOM.

Rev H adds a dedicated ADC per voltage range, hard-wired diagnostic/ready signals, reverse-input protection, a PCB-branch fuse and transient suppressor, battery monitoring and a dry-compartment ingress-sensor interface. The circuit targets sensitive measurements and a separate 600 V RMS, 50/60 Hz fault range. These are unqualified design targets. Bench calibration, insulation/protection review, physical fault testing and environmental qualification remain open. No validated acquisition firmware is supplied.

![Current Rev H PCB assembly drawing](previews/RevH_PCB.png)

![Retained Rev G mechanical assembly — electronics model pending Rev H update](previews/RevG_assembly_top.png)

Two electrodes provide one field projection, not a full 3D field map or a direct measurement of floodwater current. Current-density estimates require independently measured conductivity and a valid field/geometry model. Fast transient measurement and an electrical-safety clearance decision are not released capabilities.

## Next milestones

1. Review the new PCB and validate components, protection, calibration, acquisition timing and fault behavior on a controlled bench.
2. Model and fit the Rev H populated board in the live Fusion assembly; verify module standoffs, ESC attachment, solder tails, wiring and hatch clearance.
3. Resolve actuator hardware and sealing, then test the unpowered hull for leakage and loaded flotation.
4. Implement and validate acquisition, invalid-state handling, pose/location logging and mapping; obtain appropriate laboratory qualification before hazardous exposure.

Detailed revision narratives and superseded preview images have been removed from the current documentation; Git history preserves them. Existing named CAD releases are unchanged. The `pcb/RevG` files are retained as the electrical baseline corresponding to the current mechanical model; use Rev H for new electronics work. Historical scripts and verification records retain their original scope and must not be treated as current acceptance evidence.
