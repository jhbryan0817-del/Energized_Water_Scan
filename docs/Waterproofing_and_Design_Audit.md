# Waterproofing and assembly audit

This audit reviews the Rev-E Fusion model from the perspective of printing, procuring, assembling, wiring, and operating a small USV. It distinguishes geometric checks from tests that require physical hardware.

## Overall result

The CAD assembly has no reported unintended rigid-solid intersections, no sampled probe-motion collisions through 0–90°, and no unhealthy Fusion timeline features. The propulsion motor, coupling, stern tube, and shaft are coaxial on the intended 15° axis. The design is suitable for a fit prototype, but **waterproof qualification and assembly release remain open**.

## Water-entry paths

| Interface | CAD provision | Required physical evidence |
|---|---|---|
| Main hatch | Continuous shaped sheet gasket and ten fasteners | Compression map, flatness, fastener preload, repeated-open leak test |
| Four probe shafts | Machined POM cartridge, 6 × 16 × 7 mm radial-seal candidate, lower bushing, cartridge face gasket | Shaft finish, water-duty compatibility, seal drag, axial retention, static and cycle ingress tests |
| Four electrode leads | Separate 3.3 mm throat and 5.5 mm potting pocket | Jacket-to-potting adhesion, PETG bond, flex relief, immersion and cycle tests |
| Stern tube | Bored hull boss/sleeve around the inclined tube | Bond-line preparation, adhesive selection, concentricity, static leak test |
| Steering linkage | Flexible pushrod boot envelope | Full-rudder travel, clamp/retention, fatigue, and leak test |
| Hatch and service fasteners | Blind printed pilots where modeled | Confirm no through-holes, correct screw length, pullout strength, and sealing under preload |

The four underside probe channels are intentionally wet. Their openings are not leaks into the electronics compartment if the continuous channel roofs, shaft cartridges, and separate potted lead entries are manufactured correctly. The cyan actuator covers are service/dust covers only; they do not create four independently waterproof servo chambers.

## Clearance and interference

- The static assembly report covers 145 physical solid envelopes and records no unintended intersections.
- Probe motion was sampled every 2° from stowed to deployed; separate transverse lanes prevent probe-to-probe contact in the modeled geometry.
- The battery has 2.081 mm nominal clearance to the coupling and 1.661 mm to the stern tube. These margins are small and exclude pack swelling, straps, wiring, print tolerance, and vibration.
- The service audit reports clear modeled corridors for the main cassette, controller bridge, battery lift, selected cover screws, and separated dry analog/power routes. It does not prove hand access, connector mating, flexible harness motion, or cartridge extraction.
- Three overlaps are intentional envelope construction: servo case/lugs, propeller hub/shaft, and horn/link pin. They are not accidental component collisions.

## Highlighted “sticking-out” geometry

The questioned features are retained:

1. The square-looking boss with a circular bore supports and locates the stern-tube penetration. The bore must remain open for the tube; the tube-to-hull annulus is sealed during assembly.
2. The nearby rear projection/land supports the rudder and steering interface. Removing it would weaken or mislocate that hardware.
3. The apparent interior overhang above a probe mechanism is a hatch/channel structural surface. It separates the wet exterior lane from the dry hull and provides a sealing or load path.

An isolated CAD view can make these joined hull features look like loose parts. The hull export is nevertheless a single connected manifold solid. Only temporary print supports should be removed.

## Build gates

1. Print or machine one probe cartridge coupon and one complete actuator bay before committing to four sets.
2. Select a matched 2 mm-pitch pulley/belt set and prove horn adapter, tension adjustment, journal retention, shaft retention, torque margin, stall behavior, and cycle life.
3. Leak-test the cartridge, feedthrough, stern tube, and steering boot independently before a full empty-hull test.
4. Confirm the purchased battery, straps, wires, connectors, and bend radii in the 1.661–2.081 mm drivetrain clearance region.
5. Perform dry motion tests one actuator at a time, then four-channel sequencing with jam detection and current limits.
6. Measure loaded displacement, freeboard, trim, stability, and recovery with the actual mass distribution before energized-water experiments.
7. Calibrate the complete analog chain and electrode geometry in a controlled field. Treat a missing reading as an instrument result, never as proof of safe water.

## Fusion disposition

The live `Energized_Water_Scanner` document was saved after the audit. Model attributes now record the release status, wet/dry boundary, highlighted-feature disposition, and assembly hold points. No new STL, STEP, or F3D export was generated during this pass.
