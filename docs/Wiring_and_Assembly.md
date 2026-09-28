# Rev-E1 wiring and assembly

**Live Fusion is Rev-E1 (29 September 2026).** It closes an obsolete port-wall opening, removes an obsolete projecting foot, and adds blind end caps to 16 cartridge and four rudder mounting bores. See [changes and validation](RevE1_Changes.md). Existing Rev-E 3D exports are stale for the hull; regeneration and mesh checks are deferred.

Use the [Rev-E design](Design.md), [waterproofing audit](Waterproofing_and_Design_Audit.md), [build qualification gates](Build_Qualification.md), and [current BOM](Print_and_Procurement.md). The transmission, sealing, and flexible harness remain unreleased interfaces.

1. Use the updated Rev-E1 hull after its deferred export/mesh check. Inspect the hull channels, continuous roofs, cartridge lands, potting cups and blind pilots. Confirm support removal and sealing surfaces before assembly.
2. Bench-fit one HS-65HB, actual stock horn adapter, matched timing drive, upper journal, output shaft and cartridge/seal/bushing. Establish retention and tension adjustment before powering it.
3. Install cartridges from the wet channels, arms and retained pins. Route the tip conductor in its arm groove and form a controlled hinge loop clear of the shaft seal and full sweep. The loop returns through its potted groove-roof entry. Check insulation, restraint and flex before potting.
4. Install actuators and internal covers. The forward covers sit partly under the bow flange: use the angled screw approach, then slide/tilt the cover aft before lifting. Confirm this physically; a rigid tool allocation does not prove ergonomics.
5. Install motor supports and the relocated steering saddle/servo. Fit the dogleg pushrod through the existing boot and tiller line. Recheck full steering travel, end stops, retention, stiffness and boot motion; old steering-travel evidence no longer validates this arrangement.
6. Fit the main cassette: protected analog front end and ADS1115 on port; ESC and logic regulator on starboard; separate D24V50F5 probe supply on the forward crosspiece.
7. Secure the longitudinal battery cradle with four flush M2 screws, check that no head protrudes into the pack, and install the two straps, then the upper controller bridge. Remove and disconnect the bridge, undo both battery straps and lift the battery alone; the cradle stays installed. Disconnect power before any actuator service.
8. Route labeled E1/A0, E2/A1, E3/A2 and E4/A3 conductors along the port-side dry corridor. Route servo/motor power on starboard, with a keyed service disconnect and strain relief for each well. Keep electrode leads isolated from shafts and fasteners.
9. Fit the new continuous shaped hatch gasket and cover. Verify compression and fastener lengths rather than assuming nominal printed pilots have rated pullout strength.

10. Before installing electronics, perform a staged leak test: cartridges and feedthrough coupons first, then the empty closed hull with the stern tube and steering boot installed. Test the stern-tube outer bond and the internal rotating-shaft path separately; the bonded boss seals only the former. Specify and install the actual inboard sealing/lubrication arrangement before a running test. Use dry witness paper or an equivalent non-energized indicator inside; do not use production electronics as the leak detector. Record immersion head, duration and motion cycles under the qualification plan.

Exact connectors, cable bends, lead lengths, potting bonds, flex life and strap/connector hand access require physical checks. The internal cover exits are dry wiring passages; they do not seal the wet electrode entry. Do not parallel regulator outputs or run all probes from the ESC's 1 A BEC.

Test dry first, one actuator at a time through 0–90°, recording angle and current. A jam must inhibit measurement and sustained stall. Perform isolated cartridge ingress/cycle tests before complete-hull tests. The original protected-front-end, calibration, controlled-field and flotation gates remain.

The new geometry preset is **60°/20°/20°/45°** for E1/E2/E3/E4. Use the Rev-E pose and gradient scripts. Three coherent signed differences are required; these scripts do not control hardware or establish safe water.


The authoritative current item list is [BOM.xlsx](../BOM.xlsx), with a [CSV mirror](../BOM.csv). Green rows detect electricity, red rows support the RC boat, and yellow rows serve both. Blank prices are unresolved procurement estimates; the total is partial. Native Google Sheets retains its live currency formulas; the XLSX uses a dated exchange-rate snapshot.

The Google Sheet is a prioritized **28-line procurement list**, with major electronics first. It excludes owned screws and minor supplies and combines selected mechanical kits. The repository BOM remains the complete **79-line assembly inventory**, including 23 printed pieces. The repository BOM now records Rev-E1 repair and procurement holds. The separate Google Sheet was not updated in this pass; reconcile it before purchasing.


## Rev-E1 screw installation

The cartridge flanges are 3 mm, with 0.75 mm compressed face gaskets and 5 mm-deep Ø2.5 mm pilots. Nominal M3×8 screws engage 4.25 mm and leave 0.75 mm tip clearance. Verify the real gasket, head seating, screw length and printed thread strength before tightening. Do not deepen the pilots through their 3 mm caps.

Rudder pilots end at X193 mm and have 3 mm caps toward the interior. Measure each bracket seating face and select screw length so its tip stays at X≥193.75 mm while providing adequate engagement. Upper and lower seating geometry differs; do not assume one universal screw length. Test these joints for ingress after assembly.
