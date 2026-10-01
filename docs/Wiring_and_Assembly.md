# Rev-F wiring and assembly

Use the saved live **Energized_Water_Scanner** Fusion assembly and [Rev-F procurement delta](RevF_Procurement.md). The earlier four-probe BOM, CAD archives and gradient scripts are historical.

## Mechanical sequence

1. Inspect the current hull, both retained wet-channel roofs, cartridge lands, two potting cups and blind pilots. Trial the selected print process and screw fits on coupons before printing the complete 320 mm hull.
2. Fit one complete E2/E4 actuator with the actual horn, matched timing transmission, upper journal, output-shaft retention, cartridge, seal and lower bushing. Verify tool access, belt tension, shaft alignment and full motion before duplicating it.
3. Install both cartridges, arms and retained pins. Route each electrode lead in its arm groove with an insulated flexible hinge loop, clear of seals and rotating parts. Qualify the wire/potting bond before encapsulation.
4. Install the two probe servos and covers 23/25. Disconnect leads and release ties before cover service. With the hatch/gasket removed, slide E4's cover 3 mm inward before lifting. Confirm removal on real hardware.
5. Install the motor supports, shaft/tube and steering saddle/servo. Retain the stern-tube bond, blind rudder caps and steering boot. Check the actual coupling, shaft retention, internal tube sealing and full steering travel.
6. Fit the revised cassette using four M3×8 screws at (−17,±58.5) and (67,±58.5) mm. Nominal pilots are Ø2.5 × 5.5 mm; do not deepen them through the wet roofs.
7. Fit the rear controller shelf/frame with four M3×30 screws at (145,23), (145,59), (183,23), (183,59) mm. Verify the actual board, clamp-safe surfaces and insulating compliant pads. Nominal pilot engagement is 6.9 mm with 2.1 mm tip margin. Tighten only after confirming the real stack and printed-pilot fit.
8. Fit the retained raised cradle with four flush M2×6 screws at (88,±13) and (185,±13) mm. Thread both straps through their tunnels, pad/deburr battery contact surfaces, and avoid compressing the pack. The controller remains beside the pack for battery service.
9. Fit and qualify the continuous hatch gasket and cover. Keep all wires off the gasket land; confirm actual compression, screw lengths and leak performance.

## Wiring

Keep the retained probes labeled **E2 and E4**. Their historical ADC assignments are A1 and A3; verify the protected front-end schematic and firmware before selecting a differential acquisition mode. Remove E1/E3 leads and servo connections from the active harness. Do not connect unprotected wet electrodes directly to an ADC as a substitute for the protected front end.

Retain the separate logic and probe-servo regulators. Do not parallel regulator outputs. Keep analog electrode wiring away from motor and servo current paths, use keyed disconnects and strain relief, and allow both actuator covers and the rear shelf to be serviced. Actual connector ratings, wire gauge, fuse sizing and lead lengths require the validated circuit and load measurements.

Nominal dry routing allocations to check against real bundles:

- Analog spine: X−12…88, Y−26…−22, Z42…46 mm (4 × 4 mm).
- Power spine: X13…130, Y59…63, Z63…67 mm (4 × 4 mm).
- Rear-controller signal route: a 3 × 3 mm riser near X75…78, Y−44…−41, then across to Y24…27 at Z65…68, continuing aft toward X150. Keep connector bends and slack inside the hatch.

These are clearance allocations, not modeled flexible cables or confirmed bundle capacity. Use ties no wider than 2.5 mm in the retained saddle slots. Disconnect/release harnesses before lifting any tray or cover.

## Service and initial tests

Disconnect the battery, remove the hatch, release straps and lift the pack. For cradle removal, remove the pack and its four flush screws. Disconnect the rear-controller harness and remove its shared frame/shelf screws before lifting the controller shelf for USB access. USB faces the transom and is not accessible with an assumed straight plug while installed. Disconnect boat power before USB power.

Dry-cycle one actuator at a time, observing current, slack, shaft retention and interference. A jam must stop sustained drive. Qualify the two wet shaft seals, cartridge gaskets, potting entries, hatch, steering boot, stern-tube outer bond and internal rotating-shaft path before any water test with electronics installed. Use the [build qualification record](Build_Qualification.md).

The old four-angle measurement preset and three-dimensional gradient estimator do not apply to this two-electrode revision. Mechanical clearance does not validate sensing, protection, calibration or water safety.
