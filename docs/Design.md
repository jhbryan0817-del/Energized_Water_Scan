# Mechanical design — Rev-E1 internal actuators and recessed folding probes

**Live Fusion is Rev-E1 (29 September 2026).** It closes an obsolete port-wall opening, removes an obsolete projecting foot, and adds blind end caps to 16 cartridge and four rudder mounting bores. See [changes and validation](RevE1_Changes.md). Existing Rev-E 3D exports are stale for the hull; regeneration and mesh checks are deferred.

Revision E restores the hull to the assembly datum, grounds it against accidental dragging, reinforces printed structures, and adds explicit bonded wet-wire entry allocations. The footprint is **320 × 176 mm**. This document describes the current design; Git history retains earlier revisions.

## Audit disposition of exterior features

The attachment supplied for the 28 September review shows Fusion MCP preferences, not the model. It cannot identify the user's specific protrusion or hole. The following are functional features identified in the design, rather than a confirmed match to that attachment:

- The small bored boss/sleeve at the lower stern is part of the inclined stern-tube penetration and its bonded support. Its circular bore is intentional; the installed tube-to-hull joint must be bonded and leak-tested.
- The retained rear bracket and current steering mounting land support the rudder/steering installation and provide structure around the steering interface. They must not be trimmed from the printed hull.
- The ledges visible above the cyan probe mechanism are the continuous hatch flange and the roofs of the intentionally wet probe channels. The channels flood from outside, but their roofs separate them from the dry electronics volume.
- Openings in the cyan internal covers are dry-side wire/service passages. They are not the wet-to-dry boundary and must not be treated as waterproof glands.

The stern-tube support, rudder bracket, hatch flange and channel roofs have functional roles. Their presence alone is not evidence of stray geometry. See the current audit for any specifically measured and revised stock; do not trim these interfaces arbitrarily.

## Alignment and reinforcement

The hull alone had acquired a translation of +2.040163 mm X, -4.854283 mm Y and +1.330194 mm Z. Restoring its identity transform realigns the cartridge openings, servo wells, covers, motor supports and surrounding structure. The motor, coupling and stern tube share the intended 15° downward axis; this inclination is deliberate.

Outer channel walls gain 3 mm outward material per side (approximately 8.4 mm wall locally); all channel roofs increase nominally from 3 to 5 mm. Probe beams increase from 8 × 8 to 8 × 10 mm while retaining wire grooves, end interfaces and electrode positions. Four covers increase from 3 to 5 mm. Motor supports receive thicker side cheeks; the battery cradle gains thicker rails and floor, preserving straps, flush mounting and tube clearance. Local relief maintains clearance around neighboring parts.

The battery moves 1.5 mm aft. Minimum nominal battery-to-coupling clearance is 2.081 mm, to stern tube 1.661 mm, and to motor can 29.58 mm. Its aft end is X=192 mm versus the hatch aperture at X=193 mm. These are nominal CAD values, with no allowance established for actual pack swelling, fabrication variation or vibration. Verify the purchased pack and restraints before assembly.

Rev-E reinforcement increased hull solid volume from 591.10 to 708.92 cm³. Rev-E1 hull repairs bring it to 711.69 cm³. Added material requires a fresh measured displacement, freeboard and trim check with the actual assembled mass. No structural or flotation certification follows from thicker CAD walls.

## Wet-to-dry boundary

See [Build qualification](Build_Qualification.md) for the complete leakage-path register and physical acceptance gates. The shaft-to-stern-tube internal path is a separate unresolved interface from the tube-to-hull adhesive joint.

Each shaft passes through a machined POM cartridge, a nominal 6 × 16 × 7 mm radial seal, and a separate lower bushing. A face gasket seals cartridge to hull. The wet electrode wire has a distinct stepped potted feedthrough in the channel roof: nominal 3.3 mm throat and 5.5 mm potting pocket around a 1.12 mm insulated lead. Four explicit cured-potting and lead envelopes are now present in CAD and the BOM.

The mechanism separates wet probes from dry servo space only when the shaft seal, cartridge gasket and bonded wire entry are successfully manufactured and tested. DP270 is a candidate potting material, not an immersion-qualified selection for this printed hull. Shaft finish, seal water duty, gasket compression, adhesion, flex relief and ingress must be qualified on hardware. The removable servo covers are service covers, not independent waterproof bulkheads: a failed boundary can flood the shared hull.


## Packaging

The hull floor incorporates four raised actuator wells with removable top covers. The forward wells drive the outer channels; the rear wells drive the inner channels. Front arms fold aft, rear arms fold forward. Opposing fold directions and separate transverse lanes permit long arms without lengthening the hull. The existing propulsion shaft, propeller and rudder remain; “nearly flat” refers to the stowed electrode system, not to removing the propulsion hardware.

The shaft center is 16 mm above the original Z=0 bottom. A 166 mm hinge-to-electrode radius retains the 150 mm fully deployed electrode-center depth. The hub is recessed at least 4 mm above the bottom, and the arm beam is recessed 12 mm. These are open wet channels with a continuous raised roof, not dry slots open to the main electronics compartment. They can collect silt; rinse and inspect before retraction. A flat exterior skin across an open recess is not claimed.

| Channel | Hinge X,Y,Z, mm | Stowed direction | Exposed-head center Y, mm |
|---|---|---|---|
| E1 | -81,-72,16 | aft (+X) | -77.3 |
| E2 | 110,-52,16 | forward (-X) | -57.3 |
| E3 | -81,72,16 | aft (+X) | 77.3 |
| E4 | 110,52,16 | forward (-X) | 57.3 |

Four existing user angle parameters retain the operational convention 0°=stowed and 90°=down. Native rotations reverse sign for the rear pair. The measurement geometry must use the new positions and fold directions; the old Rev-C geometry must not be loaded into an estimator.

## Internal transmission

The retained dry HS-65HB servos sit above the hinge shafts. A nominal 1:1 synchronous belt drive makes this possible without raising the electrode hinge or placing a motor under the hull. The package allocates two 20-tooth, 2 mm pitch pulleys, 6 mm belt width and 28 mm shaft centers per channel. The equal-pulley pitch-length relation is `L = 2C + Np = 96 mm`.

**This is a packaging prototype, not a released transmission.** Pulley solids and belts are smooth clearance envelopes. They are not accurate tooth profiles or STL parts. No supplier stock number, load rating or belt tension is asserted for a 96 mm belt. A supplier-approved matched belt/pulley pair, exact horn survey, journal bearing retention, shaft axial retention, tension adjustment and a torque/cycle test remain required. The upper shaft journal allocation supports belt radial load separately from the servo spline. It does not establish a qualified bearing fit or structural capacity.

Primary design references: [SDP/SI timing profiles](https://sdp-si.com/products/details/timing-belt-detail.php), [SDP/SI belt/pulley alignment and center-distance tools](https://www.sdp-si.com/tools/), and [Gates light-power and precision drive design manual](https://www.gates.com/content/dam/documents-library/catalogs/light-power-and-precision-manual.pdf). These support the drive architecture and sizing method, not the specific unreleased assembly. Verify exact purchased parts against the current CAD and BOM.

The machined cartridge, radial seal and lower bushing are relocated within the recessed hinge region. The two rear cartridges have a 1.7 mm shorter inboard nose, ending at local absolute Y=32.7 mm, while the lower bushing begins at 32.75 mm; seal and bushing seats remain unchanged. The rear belt plane shifts 3 mm outboard and its servo shifts 5 mm outboard to preserve battery lift access. Their original water-duty and machining holds remain. Removing the external pod flange removes one wet gasket interface per channel. The 319 × 154 mm shaped hatch uses ten fasteners and a new continuous gasket; its aft aperture reaches X=193 mm for tray and battery lift-out. The removable internal covers are service/dust covers, not a second watertight compartment. A failed shaft seal can still flood the hull.

## Electronics and service

The main cassette has separate port analog and starboard power shelves with an open central motor corridor. The battery turns lengthwise into a lower aft cradle. A separately removable upper bridge carries the ESP32 over the battery. The steering servo uses a separate saddle at its original height, shifted 20 mm aft and 15 mm toward port, with a provisional dogleg pushrod returning to the original boot and tiller line.

Assembly order: install and inspect shaft cartridges and actuator mechanisms; fit and route their local harnesses; install the steering saddle and motor hardware; fit the main analog/power cassette; fit the battery cradle and straps; install the controller bridge; then connect the removable harnesses and hatch. Remove the upper bridge and release the two straps to lift the battery alone vertically; the cradle remains installed. The rear upper journals sit outside the battery lift lane. Disconnect the battery before servo service. Remove the main cassette where it obstructs an actuator cover screw. Full actuator replacement may require withdrawing the arm, cartridge and shaft before lifting the servo/belt assembly.

Keep the four electrode conductors individually identified and insulated from shafts and fasteners. Route their dry tails along the port side toward the analog front end. Route servo power and motor power on the starboard side, with a local disconnect at each well and strain relief before each connector. The small internal cover exits are dry passages; they do not replace the required potted wet-to-dry electrode entry and a qualified flexible hinge loop. Exact connector mating, cable bends, wire fatigue, potting and retention remain physical assembly checks.

The dedicated D24V50F5 probe rail is retained. Do not parallel regulator outputs or power all probe servos from the ESC's 1 A BEC. The protected front end, acquisition chain, and calibration are not validated by this mechanical revision.

## Measurement geometry

For channel i, `x = xh + direction × 166 cos(theta)`, `y = yh + sign(yh) × 5.3`, `z = 16 - 166 sin(theta)` in mm. The supplied geometry demonstrator uses three coherent signed differences against E4 and rejects rank-deficient/poorly conditioned poses. Its default pose is [60,20,20,45]°; synthetic conditioning is approximately 2.59. The old [90,30,30,90]° pose has condition number approximately 9.15 in the final geometry, so the new preset provides substantially better conditioning.

These mathematical checks do not validate sensing hardware or establish safe water. Equal-angle poses remain planar. Real calibration must include arm-angle error, offsets, phase, water conductivity and boat attitude.

## Appearance and manufacture

Graphite hull, light gray hatch/electronics carriers, cyan actuator covers/arms and restrained orange retained fittings distinguish enclosure, sensing and service parts. These are Fusion appearances, independent of filament selection.

This revision requires a new hull and changed trays/arms; it is not a bolt-on conversion of a printed Rev-C hull. The closed roofs above wet channels require a slicer/support-removal trial. Check access through each bottom groove and cartridge aperture before committing to a hull print. Printed walls, sealing lands, fasteners, sustained load and porosity remain unqualified. Do not machine precision seal seats from the STL or print a guessed servo spline.

## Evidence and release status

Use the RevE1 reports for the live repairs; RevE reports and exports describe the historical baseline. The migration preserves earlier timeline history; fixed lengths are reference values, not a fully generative master-parameter model. Angle parameters remain editable. Reports distinguish rigid-solid checks from unavailable flexible-harness, sealing, torque and flotation tests. `assembly_release_passed` remains false until the retained and new interface holds are closed.

The Rev-E1 assembly report covers 145 physical solid envelopes and 1,768 timeline items. Static checks include bodies within the same component. Three named intersections are explicitly classified as intentional envelope construction (SG90 case/lug overlap, propeller hub/shaft overlap, and steering horn/pin attachment). They are not hidden as collision-free geometry. Probe motion is sampled every 2° through 0–90° against static geometry; separate transverse lanes prevent probe-to-probe collisions. Historical native parameter checks verified all four electrode positions at stowed, 30°, 90° and the measurement pose; Rev-E1 changes only the hull. These are sampled checks, not a continuous-motion proof for wires, belts or steering.

The next export pass must check 23 single-connected manifold meshes, exact ZIP identity, 145 STEP solid envelopes, and a reopened native F3D matching solid volumes, occurrence transforms, parameters and timeline. These checks have not been run for Rev-E1 because 3D export is deferred. Existing export verification JSON applies only to Rev-E.

The rigid service audit covers selected driver corridors, the main cassette, controller bridge and battery lift, and two dry bundle corridors. It does not validate cartridge extraction, every cover removal trajectory, belt replacement, connector mating, or the relocated steering sweep; those remain physical-fit checks. The wet cartridge access pockets may require cartridge tilting with the arm removed. Verify the actual tool approach and extraction on one full actuator fit prototype.

The stern-tube sleeve, rudder bracket and current steering-saddle support land remain functional hull interfaces. The separate obsolete port foot was removed. Historical Rev-E exports passed the 23-body mesh check; the repaired Rev-E1 hull still requires a fresh export and mesh check.
