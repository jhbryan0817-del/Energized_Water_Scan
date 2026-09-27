# Rev-D — internal actuators and recessed folding probes

The user's current request governs this revision: retain the 320 × 170 mm hull footprint, put the four HS-65HB servos inside, expose only the probe arms below the sensing area, provide four stowage channels, repackage electronics for assembly and wiring, and use a robot-like visual palette. Earlier documents are historical engineering context, not new instructions.

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

Primary design references: [SDP/SI timing profiles](https://sdp-si.com/products/details/timing-belt-detail.php), [SDP/SI belt/pulley alignment and center-distance tools](https://www.sdp-si.com/tools/), and [Gates light-power and precision drive design manual](https://www.gates.com/content/dam/documents-library/catalogs/light-power-and-precision-manual.pdf). These support the drive architecture and sizing method, not the specific unreleased assembly. The original [Rev-C mechanical references](RevC_Mechanical_References.md) continue to govern the HS-65HB envelope, seal, bushing, electrode and materials.

The machined cartridge, radial seal and lower bushing are relocated within the recessed hinge region. The two rear cartridges have a 1.7 mm shorter inboard nose, ending at local absolute Y=32.7 mm, while the lower bushing begins at 32.75 mm; seal and bushing seats remain unchanged. The rear belt plane shifts 3 mm outboard and its servo shifts 5 mm outboard to preserve battery lift access. Their original water-duty and machining holds remain. Removing the external pod flange removes one wet gasket interface per channel. The 319 × 154 mm shaped hatch uses ten fasteners and a new continuous gasket; its aft aperture reaches X=193 mm for tray and battery lift-out. The removable internal covers are service/dust covers, not a second watertight compartment. A failed shaft seal can still flood the hull.

## Electronics and service

The main cassette has separate port analog and starboard power shelves with an open central motor corridor. The battery turns lengthwise into a lower aft cradle. A separately removable upper bridge carries the ESP32 over the battery. The steering servo uses a separate saddle at its original height, shifted 20 mm aft and 15 mm toward port, with a provisional dogleg pushrod returning to the original boot and tiller line.

Assembly order: install and inspect shaft cartridges and actuator mechanisms; fit and route their local harnesses; install the steering saddle and motor hardware; fit the main analog/power cassette; fit the battery cradle and straps; install the controller bridge; then connect the removable harnesses and hatch. Remove the upper bridge and release the two straps to lift the battery alone vertically; the cradle remains installed. The rear upper journals sit outside the battery lift lane. Disconnect the battery before servo service. Remove the main cassette where it obstructs an actuator cover screw. Full actuator replacement may require withdrawing the arm, cartridge and shaft before lifting the servo/belt assembly.

Keep the four electrode conductors individually identified and insulated from shafts and fasteners. Route their dry tails along the port side toward the analog front end. Route servo power and motor power on the starboard side, with a local disconnect at each well and strain relief before each connector. The small internal cover exits are dry passages; they do not replace the required potted wet-to-dry electrode entry and a qualified flexible hinge loop. Exact connector mating, cable bends, wire fatigue, potting and retention remain physical assembly checks.

The dedicated D24V50F5 probe rail is retained. Do not parallel regulator outputs or power all probe servos from the ESC's 1 A BEC. The [Rev-C acquisition and power limitations](RevC_Articulated_Probes.md) remain applicable.

## Measurement geometry

For channel i, `x = xh + direction × 166 cos(theta)`, `y = yh + sign(yh) × 5.3`, `z = 16 - 166 sin(theta)` in mm. The supplied geometry demonstrator uses three coherent signed differences against E4 and rejects rank-deficient/poorly conditioned poses. Its default pose is [60,20,20,45]°; synthetic conditioning is approximately 2.59. The old [90,30,30,90]° pose has condition number approximately 9.15 in the final geometry, so the new preset provides substantially better conditioning.

These mathematical checks do not validate sensing hardware or establish safe water. Equal-angle poses remain planar. Real calibration must include arm-angle error, offsets, phase, water conductivity and boat attitude.

## Appearance and manufacture

Graphite hull, light gray hatch/electronics carriers, cyan actuator covers/arms and restrained orange retained fittings distinguish enclosure, sensing and service parts. These are Fusion appearances, independent of filament selection.

This revision requires a new hull and changed trays/arms; it is not a bolt-on conversion of a printed Rev-C hull. The closed roofs above wet channels require a slicer/support-removal trial. Check access through each bottom groove and cartridge aperture before committing to a hull print. Printed walls, sealing lands, fasteners, sustained load and porosity remain unqualified. Do not machine precision seal seats from the STL or print a guessed servo spline.

## Evidence and release status

Use only the revision-matched RevD reports and exports. The migration preserves earlier timeline history; fixed lengths are reference values, not a fully generative master-parameter model. Angle parameters remain editable. Reports distinguish rigid-solid checks from unavailable flexible-harness, sealing, torque and flotation tests. `assembly_release_passed` remains false until the retained and new interface holds are closed.

The final rigid-body evidence covers 137 physical solids and 1,700 timeline items, with no feature errors, static intersections or sampled probe/static collisions. Each probe is sampled every 5° through 0–90°. A separate native-parameter audit verifies all four actual electrode positions at 0°, 30°, 90° and the measurement preset; this caught and corrected six superseded component-owned rotation drivers. Only one live angle driver remains per probe. Eight enclosed obsolete pod-pilot cavities were filled after STL inspection, with the added material checked against components and probe motion. The final package includes 23 connected manifold meshes, a matching ZIP, physical STEP and a reopened native archive; consult the linked JSON evidence for exact results and limits.

The rigid service audit covers selected driver corridors, the main cassette, controller bridge and battery lift, and two dry bundle corridors. It does not validate cartridge extraction, every cover removal trajectory, belt replacement, connector mating, or the relocated steering sweep; those remain physical-fit checks. The wet cartridge access pockets may require cartridge tilting with the arm removed. Verify the actual tool approach and extraction on one full actuator fit prototype.
