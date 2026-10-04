# Assembly and procurement

Use the [Rev H PCB BOM](../pcb/RevH/BOM.csv) for the carrier and the [system BOM](../BOM.csv) for remaining hardware. Do not buy a separate ADS1115 breakout or obsolete front-end module: the two converters and isolated front ends are on the PCB. The component BOM lists 95 populated references including the modules. Add the sockets, shunt and module standoffs listed in the PCB assembly BOM; its harness/PCB-fastener rows cross-reference the system BOM and must not be counted twice. Blank manufacturer selections are procurement holds, not approved substitutions.

The system BOM preserves unresolved supplier/interface warnings. It uses two probe mechanisms, three servos total, the retained battery/drivetrain, the Rev G 13-body print set, and revised PCB/ESC mounting hardware. Obtain and qualify one probe actuator before ordering its duplicate. Smooth timing-pulley envelopes do not define actual teeth, horn adaptation, tensioning or shaft retention. Verify the exact SG90 horn/lugs, motor mounting depth, coupling dimensions and propeller/shaft interfaces on supplier hardware.

1. Inspect the current hull, wet roofs, blind pilots and sealing lands. Qualify printing/coating on coupons. Do not deepen a blind pilot into a wet channel.
2. Resolve one E2/E4 actuator with matched pulleys/belt, actual servo horn, upper journal, shaft retention, cartridge, seal and bushing. Test travel, jam response, current and temperature before duplication.
3. Route E2/E4 leads with insulated hinge loops, strain relief and qualified potted entries. Keep them separated from motor/servo wiring. External wet conductors terminate only at the designated isolated electrode inputs.
4. Fit the propulsion and steering hardware. Qualify both the stern-tube outer bond and the internal rotating-shaft leakage path; one does not seal the other.
5. Install the Rev H carrier using the retained mounting pattern, 1 mm nylon spacers and verified screw engagement. Check trimmed solder tails. Fit the regulator modules with measured ≥2 mm underside clearance, including the added capacitors beneath them. Consult the Rev I CAD audit and verify the selected hardware and mating connectors physically.
6. Fit the external fused harness and the independently fused motor branch. Observe J11 polarity, fit F1/Q1 correctly, leave the ESC BEC lead insulated, and never parallel regulator outputs. Use a current-limited supply for initial power-up.
7. Fit two battery straps and qualified ESC retention. Retain the existing SJ3550 attachment concept pending bond/thermal tests. Keep wiring away from the hatch gasket and provide service slack.
8. If fitted, connect a compatible 3.3 V open-drain dry-compartment ingress sensor to J14 and test it before each run. J14 is not a wet-electrode or conductivity connector.

The [PCB pin map](../pcb/RevH/PIN_MAP.md) is authoritative. GPIO34/35/36/39, GPIO32 and GPIO23 now have onboard functions. Remove boat power and JP1 before USB service; lift the ESP32 from its sockets if necessary. Disconnect leads and ties before lifting the carrier or probe covers. The E4 cover's documented service path is 3 mm inward then upward, subject to confirmation on hardware.

The current mechanical reference is the live Fusion Rev I assembly; the named Rev G exports are historical. No new STL/STEP/F3D was produced. Use the active PRINT components in Fusion, excluding ARCHIVE and LIBRARY components; all printed parts remain subject to the [qualification plan](Build_Qualification.md).
