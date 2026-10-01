# Waterproofing and assembly audit

**Current live Fusion: Rev-E2, 1 October 2026.** Physical corrections to the controller shelf, battery cradle/mounts and wire restraints are saved in Fusion. See [Rev-E2 physical changes](RevE2_Changes.md) and the [component audit](Mechanical_Audit_2026-10-01.md). The BOM and all repository 3D files are unchanged; existing exports are stale.

**Rev-E1 baseline repairs (29 September 2026), retained in Rev-E2:** It closes an obsolete port-wall opening, removes an obsolete projecting foot, and adds blind end caps to 16 cartridge and four rudder mounting bores. See [changes and validation](RevE1_Changes.md). Existing Rev-E 3D exports are stale for the hull; regeneration and mesh checks are deferred.

This audit reviews the Rev-E/Rev-E1 baseline and current Rev-E2 Fusion model from the perspective of printing, procuring, assembling, wiring, and operating a small USV. The baseline was rechecked on 28 September and repaired geometry on 29 September 2026 through the local Fusion MCP connection. It distinguishes geometric checks from tests that require physical hardware. See [build qualification](Build_Qualification.md) for the expanded leakage register and physical acceptance gates.

## Overall result

The [29 September post-repair assembly check](../verification/RevE1_Assembly_Audit.json) reports no unintended rigid-solid intersections, no sampled probe-motion collisions through 0–90° at 2° increments, no Boolean failures, and no unhealthy Fusion timeline features. Earlier interface measurements establish the propulsion motor, coupling, stern tube, and shaft alignment on the intended 15° axis. The design is suitable for a fit prototype, but **waterproof qualification and assembly release remain open**. The motion check uses nominal rigid solids; it does not test flexible wires, seal drag, belt teeth, fastener tolerances or continuous swept motion.

## Water-entry paths

| Interface | CAD provision | Required physical evidence |
|---|---|---|
| Main hatch | Continuous shaped sheet gasket and ten fasteners | Compression map, flatness, fastener preload, repeated-open leak test |
| Four probe shafts | Machined POM cartridge, 6 × 16 × 7 mm radial-seal candidate, lower bushing, cartridge face gasket | Shaft finish, water-duty compatibility, seal drag, axial retention, static and cycle ingress tests |
| Four electrode leads | Separate 3.3 mm throat and 5.5 mm potting pocket | Jacket-to-potting adhesion, PETG bond, flex relief, immersion and cycle tests |
| Stern tube | Bored hull boss/sleeve around the inclined tube | Bond-line preparation, adhesive selection, concentricity, static leak test |
| Propeller shaft inside stern tube | Nominal shaft/tube envelopes only; no qualified inboard dynamic sealing arrangement demonstrated | Specify bearing/lubrication/sealing stack; test static and running ingress separately from the outer hull bond |
| Steering linkage | Flexible pushrod boot envelope | Full-rudder travel, clamp/retention, fatigue, and leak test |
| Hatch and service fasteners | Blind printed pilots where modeled | Confirm no through-holes, correct screw length, pullout strength, and sealing under preload |

The four underside probe channels are intentionally wet. Their openings are not leaks into the electronics compartment if the continuous channel roofs, shaft cartridges, and separate potted lead entries are manufactured correctly. The cyan actuator covers are service/dust covers only; they do not create four independently waterproof servo chambers.

## Clearance and interference

- The static assembly report covers 145 physical solid envelopes and records no unintended intersections.
- Probe motion was sampled every 2° from stowed to deployed; separate transverse lanes prevent probe-to-probe contact in the modeled geometry.
- Rev-E2 battery clearance is 2.904 mm to the coupling and 9.661 mm to the stern tube. These margins are small and exclude pack swelling, straps, wiring, print tolerance, and vibration.
- The service audit reports clear modeled corridors for the main cassette, controller bridge, battery lift, selected cover screws, and separated dry analog/power routes. It does not prove hand access, connector mating, flexible harness motion, or cartridge extraction.
- Three overlaps are intentional envelope construction: servo case/lugs, propeller hub/shaft, and horn/link pin. They are not accidental component collisions.

## Highlighted “sticking-out” geometry

The supplied attachment shows Fusion MCP preferences, not a CAD view. It does not establish which feature the user means. The following explanations apply to identified model features and must not be read as a confirmed match to the attachment:

1. The square-looking boss with a circular bore supports and locates the stern-tube penetration. The bore must remain open for the tube; the tube-to-hull annulus is sealed during assembly.
2. The current rudder bracket and steering mount are functional. A separate obsolete foot at X174–182, Y−75.5 to −60, Z0–4 mm was trimmed in Rev-E1; the current steering boss at (178,−62) was preserved. An obsolete relief near (143,−72) had broken through the port wall and was filled.
3. The apparent interior overhang above a probe mechanism is a hatch/channel structural surface. It separates the wet exterior lane from the dry hull and provides a sealing or load path.

An isolated CAD view can make these joined hull features look like loose parts. The live hull is one connected BRep solid; earlier mesh checks apply to the existing exports only. Connectivity is not a waterproofness test. Preserve functional interfaces and remove only temporary print supports or specifically documented revised stock.

## Build gates

1. Print or machine one probe cartridge coupon and one complete actuator bay before committing to four sets.
2. Select a matched 2 mm-pitch pulley/belt set and prove horn adapter, tension adjustment, journal retention, shaft retention, torque margin, stall behavior, and cycle life.
3. Leak-test the cartridge, feedthrough, stern tube, and steering boot independently before a full empty-hull test.
   Test both the outside of the stern tube and the separate rotating-shaft path through its inside. Specify operating head, water type, duration and cycles before accepting a result.
4. Confirm the purchased battery, straps, wires, connectors, and bend radii against the revised 9.661 mm tube and 2.904 mm coupling clearances.
5. Perform dry motion tests one actuator at a time, then four-channel sequencing with jam detection and current limits.
6. Measure loaded displacement, freeboard, trim, stability, and recovery with the actual mass distribution before energized-water experiments.
7. Calibrate the complete analog chain and electrode geometry in a controlled field. Treat a missing reading as an instrument result, never as proof of safe water.

## Fusion disposition

The live document now contains Rev-E2 physical controller, battery and wire-restraint corrections, retaining all Rev-E1 sealing repairs. Two new battery bosses have blind pilots entirely inside the dry hull; no wet wall or sealed cap was drilled through. See [exact changes](RevE2_Changes.md) and the [current component audit](Mechanical_Audit_2026-10-01.md) for fresh rigid-body, service and probe checks. The saved model remains a fit prototype; sealing, flexible mechanisms and loaded flotation require hardware validation. No new 3D export was generated and the BOM is unchanged.
