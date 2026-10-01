# Rev-F build qualification

**2 October 2026.** Current geometry is the live **Energized_Water_Scanner** Fusion assembly. The [Rev-F change record](RevF_Changes.md) records CAD checks. The [procurement delta](RevF_Procurement.md) supersedes the four-probe quantities in historical BOM files.

A mechanical fit prototype is not a water-ready release. Removing two mechanisms reduces the number of wet interfaces, but every retained interface still needs qualification.

## Leakage paths

| Interface | Required verification |
|---|---|
| Printed hull, new chines and two retained channel roofs | Inspect layer paths, continuous material and support removal; qualify porosity/coating and leak-test the empty hull. No drain may connect a wet channel to the dry interior. |
| Main hatch | Confirm actual gasket material, compression, continuous contact band, lid flatness, screw lengths and repeatability after opening. |
| Two rotating probe shafts | Select exact water-compatible seals, corrosion-resistant materials, lubrication, shaft finish/tolerance, lip orientation and axial retention. Nominal seal envelopes are not proof of water duty. |
| Two cartridge face joints | Verify closed gasket perimeter, compression, fit and fastener engagement. Retain the eight blind mounting-pilot caps. |
| Two electrode wire entries | Qualify adhesion to actual wire jacket and printed/coated hull, potting void control, strain relief and full flex travel. |
| Stern tube outer joint | Verify bonded tube-to-hull seal and alignment. |
| Internal propeller-shaft/tube path | Specify the real bearing, lubrication and inboard dynamic sealing arrangement. Test this separately from the outer bond. |
| Steering boot | Fit the actual boot and retain both ends; verify full relocated linkage travel and fatigue. |
| Blind fasteners | Check real lengths and printed pilot strength. Preserve rudder caps and the wet roof below new cassette pilots. Do not drill through blind stops. |

The two internal probe covers are service covers, not independent watertight compartments.

## Staged build gates

1. Survey actual board/connectors, battery/padding/leads, motor, coupling, steering servo/horn and fasteners. Fit the rear controller's insulating retention pads to robust contact surfaces and verify shelf removal for USB service.
2. Fit one E2/E4 actuator. Resolve matched pulleys/belt, stock-horn adapter, journal support, tensioning, shaft and pin retention, precision cartridge tolerances and tool access. Cycle it under representative load and record current/temperature before duplicating it.
3. Establish the print process on coupons: hole compensation, screw insertion, sustained preload, layer strength, seal flatness, porosity and coating. Review support removal from channel roofs and under the hatch flange. Check the 320 mm hull against the available printer.
4. Fit the real harness, keyed disconnects, fuse/protection components, clamps and restraints. Check connector mating, wire capacity/bends and service slack with the hatch closed. CAD bundle corridors do not prove electrical ratings or flexible-wire behavior.
5. Specify the intended immersion head, duration, water type, temperature and motion-cycle requirement. Test coupons/interfaces, then the empty assembled hull with dry witness material under static and actuated conditions. Test after repeated hatch openings. Any visible ingress fails the tested condition.
6. Weigh the printed and fully assembled vessel. Measure displacement, freeboard, trim and stability with actual batteries, coatings and hardware. The narrower hull changes buoyancy and the rear controller changes trim; historical waterline references do not establish flotation.
7. In controlled unenergized water, verify propulsion, full steering travel, probe stops, jam response and retrieval. Validate the protected sensing chain and two-electrode measurement separately.

No slicer, physical leak, torque, fatigue, electrical-safety or flotation test was performed by this CAD revision. No 3D files were exported. The historical four-electrode gradient algorithm is not a validated two-electrode implementation.
