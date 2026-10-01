# Rev-E2 print and procurement schedule

**Current live Fusion: Rev-E2, 1 October 2026.** Physical corrections to the controller shelf, battery cradle/mounts and wire restraints are saved in Fusion. See [Rev-E2 physical changes](RevE2_Changes.md) and the [component audit](Mechanical_Audit_2026-10-01.md). The BOM and all repository 3D files are unchanged; existing exports are stale.

**Rev-E1 baseline repairs (29 September 2026), retained in Rev-E2:** It closes an obsolete port-wall opening, removes an obsolete projecting foot, and adds blind end caps to 16 cartridge and four rudder mounting bores. See [changes and validation](RevE1_Changes.md). Existing Rev-E 3D exports are stale for the hull; regeneration and mesh checks are deferred.

See the [Rev-E design and holds](Design.md), [waterproofing audit](Waterproofing_and_Design_Audit.md), and [build qualification gates](Build_Qualification.md). This remains a fit prototype, not a released mechanism or water-ready assembly.

## Current 23-piece print package

| IDs | Parts |
|---|---|
| 01,02 | Hull with four integral wells/channels; extended service hatch |
| 03,04 | Main analog/power cassette; longitudinal battery cradle |
| 09,11,14,16,17 | Retained rudder bracket, motor mounts, rudder blade and tiller |
| 18–21 | Retained electronics capture bridges, relocated |
| 22–25 | Four internal servo covers, replacing external pods |
| 26–29 | Four 166 mm insulating probe arms |
| 30,31 | Steering saddle and forward removable controller shelf |

Use the current live Fusion bodies for slicer preparation. Existing repository STLs/STEP/F3D are historical and do not contain Rev-E1/E2 changes. No new 3D export is provided in this iteration. Reorient for slicing without scaling. The hull remains within 320 × 176 mm. Check support removal from the wet channels and hollow internal wells in the slicer before printing. PETG remains a fit-prototype candidate; porosity, wall strength, sealing flatness and sustained screw preload are unqualified.

## Revised bodies to print from live Fusion

Rev-E2 changes PRINT_01 hull (two dry blind battery bosses), PRINT_03 cassette (forward controller supports and ties), PRINT_04 raised cradle/strap passages and vertical-extraction relief, PRINT_25 E4 cover (ties), and PRINT_31 forward shelf. PRINT_18 is relocated but its print shape is unchanged. The package remains 23 pieces and the complete BOM is unchanged. Inspect the five revised single-solid bodies and support access in the slicer; check screw/strap coupons first. See [dimensions, fasteners and validation](RevE2_Changes.md).

## BOM changes from Rev-C

- Retain four Hitec HS-65HB probe servos, the SKF seal/igus lower-bushing candidates and machined POM cartridges. Relocate them inside the hull; the original seal-duty and horn-survey holds remain.
- Add eight 20T/2 mm pitch pulley allocations, four nominal 96 mm pitch-length × 6 mm belt allocations, and four upper journal/bushing allocations. Exact matched supplier parts, tooth geometry, bore/retention, tension adjustment, torque and life remain HOLD. Smooth CAD envelopes are not functional pulley or belt STLs.
- Replace the four output shafts with the longer nominal shafts shown in CAD. Release shaft surface, pin and axial retention only after the actual transmission is chosen.
- Replace four external pod gaskets and mounting sets with four internal covers and sixteen M3 cover screws. M3×10 is a starting length only; verify blind engagement and tool access.
- Retain the four cartridge face gaskets and sixteen cartridge screws; verify the new installed stack.
- Replace the main hatch gasket with the new shaped continuous sheet gasket. Do not reuse the old rectangular outline. Verify compression and screw lengths at the new opening and shortened rear-center boss.
- Retain the battery cradle with four flush M2 countersunk screws at (88,±13) and (185,±13) mm. Nominal Ø4.6 top countersinks and Ø1.7 blind pilots are fit-prototype starting geometry; verify head seating and screw length before loading the pack.
- Add the separate steering saddle and forward controller shelf with four M3 fasteners each; the main cassette also has four M3 fasteners. Verify engagement and printed-pilot strength.
- Replace the straight steering pushrod with the provisional M2 dogleg envelope. Bend geometry, stiffness, retention and full steering travel require a new validation.
- Four roof-entry potting cups, wet hinge loops and insulated tip terminals require the actual wire/encapsulant and flex/immersion tests.

All other named electronics, battery, motor, shaft/tube, propeller and rudder parts remain. Retain the separate D24V50F5 probe supply. Existing electrical protection and connector omissions remain open. No purchase has been made. Fit one complete actuator/transmission/cartridge before buying four sets or printing the complete hull.

The propulsion shaft/tube requires a supplier-confirmed internal sealing and lubrication arrangement in addition to its outer hull bond. That arrangement has no released additional part number or quantity yet; do not treat the existing BOM as a complete waterproof procurement package. Likewise confirm water duty and corrosion resistance for the exact probe seal, rather than buying by 6 × 16 × 7 mm envelope alone. The current BOM quantities remain unchanged by these qualification holds.

Do not trim the bored stern-tube boss, rudder/transom bracket, steering support land, hatch flange, or probe-channel roofs from the hull. They are functional model geometry, even where an isolated view makes them resemble stray overhangs. Remove only slicer-generated supports and inspect the underlying sealing surfaces afterward.


The authoritative current item list is [BOM.xlsx](../BOM.xlsx), with a [CSV mirror](../BOM.csv). Green rows detect electricity, red rows support the RC boat, and yellow rows serve both. Blank prices are unresolved procurement estimates; the total is partial. Native Google Sheets retains its live currency formulas; the XLSX uses a dated exchange-rate snapshot.

The Google Sheet is now an **11-line major-electronics procurement summary** (1 October 2026): controller, ADC, protected front end, probe servos, two regulators, ESC, motor, steering servo, battery and external charger. All seven columns remain; purpose highlights were removed and links contain concise Taobao keywords. Mechanical parts and minor supplies remain in the unchanged complete **79-line repository BOM**, including 23 printed pieces. Existing quantities, prices and live currency formulas were preserved; unpriced items still make the total partial.
