# Mechanical design — Rev-F

The current source is the live **Energized_Water_Scanner** Fusion assembly, revised 2 October 2026. See [physical changes and validation](RevF_Changes.md). Repository 3D exports and older audit reports describe previous revisions.

## Hull and retained mechanisms

The hull is 320 mm long, with a 125.2 mm maximum bottom beam and retained 170 mm upper hatch flange. The new sloping lower sides replace the obsolete E1/E3 outer channels and projecting strips. The forward dry wells and unused mounts are removed. The two inner wet channels retain their continuous roofs, shaft cartridges, capped mounting pilots and bonded wire-entry interfaces. The continuous hatch gasket and cover remain separate parts.

| Probe | Hinge X,Y,Z (mm) | Fold direction | Nominal arm radius |
|---|---|---|---|
| E2 | 110, −52, 16 | Forward (−X) | 166 mm |
| E4 | 110, 52, 16 | Forward (−X) | 166 mm |

The retained probes stow at 0° and deploy to 90°. Their nominal exposed-head centers are Y−57.3 and Y57.3 mm. Position is `x = 110 − 166 cos(theta)`, `z = 16 − 166 sin(theta)`. The two separated lanes remain open to water and require rinsing after use. Their roofs form the wet/dry boundary; internal servo covers do not.

Two dry HS-65HB servos drive the retained shafts through nominal 1:1 timing transmissions. Each uses two smooth 20T/2 mm-pitch pulley allocations, a nominal 96 mm × 6 mm belt allocation, and an upper journal. These are packaging envelopes. Exact matched parts, teeth, stock-horn adapter, tension adjustment, shaft finish, bearing fits and axial retention must be resolved on one actual actuator before duplication.

## Electronics and service

The main cassette carries port-side analog acquisition and starboard power electronics. It is 8 mm aft of Rev-E2, with its front edge shortened to X−20 mm. Four mounting axes are (−17,±58.5) and (67,±58.5) mm. The motor corridor and drivetrain retain their installed positions.

The ESP32 is on a separately removable rear starboard shelf beside the battery, rotated 90°. PCB limits are X144.5…192.76, Y27…54.94, Z49…50.6 mm. Its antenna faces forward. Four shared M3×30 screws secure the retention frame and shelf at (145,23), (145,59), (183,23), (183,59) mm. Fit insulating compliant pads and confirm robust contact surfaces against the actual board; the conservative header/module envelope does not specify clamp-safe component locations.

USB faces the transom. Remove/lift the controller shelf for USB access and disconnect boat power before connecting USB. Provide keyed service connectors and adequate slack for shelf removal. Do not force a plug into the installed transom gap.

The battery remains X84…188, Y±17.25, Z33…47.5 mm in the Rev-E2 cradle, retained by two straps. The steering saddle, motor mounts, inclined shaft/tube, rudder bracket, boot and existing blind stern caps remain functional. They are not stray elements.

## Measurement change

Only E2/E4 are active. Their voltage difference measures one field projection over the electrode separation under the applicable field model and calibration. A single simultaneous pair cannot determine a three-dimensional gradient. Do not apply the historical four-electrode estimator or its four-angle default pose. Firmware channel selection, angle calibration, protected input circuitry, phase/offset behavior and any scanning method require a separate validated implementation.

## Manufacture

Use the [19-piece print list and procurement delta](RevF_Procurement.md), [assembly sequence](Wiring_and_Assembly.md) and [qualification gates](Build_Qualification.md). Current CAD checks are recorded in [Rev-F changes](RevF_Changes.md). A solid-body check is not a slicer/manifold-mesh test, physical tolerance validation, watertightness test or flotation result. No 3D export was created for this revision.
