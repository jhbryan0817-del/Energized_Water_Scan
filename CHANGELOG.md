# Changelog

## Rev-C.1 — 27 September 2026

- Replace four flush electrodes with independently parameterized 0–90° fore–aft arms, 150 mm deployment below the hull bottom and a non-coplanar measurement pose.
- Remove magnetometer hardware and current procurement/print/wiring requirements.
- Add four removable dry HS-65HB pod concepts, replaceable nominal machined seal/bushing cartridges, insulated arms and a separate probe-servo regulator mount.
- Close old wet electrode holes and rail pilots; correct pod/cartridge and motor-foot interference.
- Update BOM, supplier/material references, assembly, waterproofing boundaries, sensing plan and explicit interface holds.
- Add synthetic 3D observability tests, Fusion angle presets, rigid motion/clearance checks and revision-matched exports. No claim of completed horn coupling, qualified waterproofing or validated field measurements.


## Rev-B.4 — 26 September 2026

- Audit all named purchased components against manufacturer/supplier references; record nominal-versus-tolerance limitations and source hashes.
- Compare downloaded official ADC and regulator STEP body bounds/volumes with the live Fusion assembly; verify ADC drill coordinates and regulator edge tolerance.
- Revise PRINT_20 with a connected bypass around the five-pin connection row, preserving its screw centres.
- Enlarge four M4 nut envelopes from Ø7 to Ø8.1 to include hex corners; resolve official D24V10Fx family model provenance.
- Propose Hitec HS-65HB, TE 34145, Ruland MCL-3-A and Scanstrut DS6-P with explicit integration gaps; specify DIN 84 M4×18 A4 electrode screws.
- Record E1 access as builder-accepted without claiming physical seal qualification. Assembly release remains false.
- Export revision-matched editable F3D/STEP, print package and regression evidence; PRINT_20 is the only changed printable geometry.

## Rev-B.3 — 25 September 2026

- Clear battery-tray overlap with front M3 tray screw heads using two open corner reliefs.
- Open the ESP32 capture bridge above the upper header row and reinforce its remaining crossbar.
- Increase four motor-support M3×8 blind-hole tip margins from 0.2 to 2 mm while retaining nominal 2 mm bottom skin.
- Add fastener-head/header-access checks and explicitly failed E1 tool-access evidence; assembly release remains false.
- Document the H2D hull/hatch and X1C small-part plan, staged procurement, missing sealed sensor entry, exact harness/steering interfaces and physical qualification gates.
- Regenerate Rev-B.3 CAD, all sixteen prints, a separate fit coupon and verification evidence. Electronics architecture remains unchanged.

## Rev-B.2 — 25 September 2026

- Added electrode ring-lug/crimp envelopes, an E2 cradle side exit, a tray conductor riser and checked routing allocations.
- Added blind M3 screw interfaces for motor supports, sensor rail and rudder bracket; converted ADC/servo support bores to M2 pilots. Main hatch inserts remain.
- Added four screw-secured electronics capture bridges, locating stops and a motor-cradle liner envelope.
- Joined raised “IoT Beyond Lab” branding into the hull side.
- Regenerated CAD/print exports and documented the remaining hardware, screw coupon, harness, sealing and prototype-test gates.


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
