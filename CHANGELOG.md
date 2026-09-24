# Changelog

## Rev-B.1 — 2026-09-25

- Add twelve through-slots to the existing Fusion electronics tray: five harness restraint stations and an ESC retention path; preserve the outer envelope and exact purchased-component sizes.
- Audit all mechanical subsystems for print and assembly risks, and document unresolved production gates.
- Add a wiring connection schedule, power-source isolation, connector mismatch correction, servo/BEC current-budget check and service sequence.
- Assess a compact interconnect PCB without creating a PCB design.
- Regenerate native CAD, physical STEP and twelve STLs; rerun collision, steering, service and mesh/export checks.

## Rev-B — 2026-09-24

- Reduce hull from 400 × 190 to 320 × 170 mm while retaining the stern/shaft datum.
- Rotate the battery across the bow and repack electronics with matching supports and ADC mounting holes.
- Shorten the electronics tray, relocate front pillars and strap passages, and resize hatch/gasket/fastener interfaces together.
- Shorten the magnetometer rail and relocate the sensor assembly; separate revised wiring allocations.
- Document battery/tray removal for USB access and the assembly/service sequence.
- Recheck solid overlaps, 71 steering positions, sampled tray removal, tool/grip access, twelve STL meshes and exported files.
- Save the existing Fusion design and provide Rev-B F3D, STEP, print package, previews and audit documentation.

## Rev-A.1 — 2026-09-24

- Restore clamping contact between all four electrode heads and exterior seal washers.
- Clear the motor rear-terminal service envelope by moving the battery forward 6 mm; extend tray support 3 mm toward the bow.
- Move the reserved power-wire corridor clear of the battery rail and motor mount.
- Add matching tiller/stock cross-pin holes, a purchased retained-pin envelope and a lower stop-collar allocation.
- Increase steering penetration to 7 mm and update the boot allocation after finding a collision at +33…+35 degrees.
- Correct regulator CAD provenance labeling.
- Re-export native CAD, physical-only STEP, all 12 STLs, print ZIP and previews; add reproducible validation and updated assembly documentation.

## Rev-A — 2026-09-23

Original published mechanical packaging audit. Historical reports remain in `verification/`; source commit: `a364aa5ba2249f480e7dcc9e9159f0153d982758`.
