# Rev-E print and procurement schedule

See [Rev-E design and holds](Design.md). The [historical reference](../HISTORY.md) is historical. This remains a fit prototype, not a released mechanism or water-ready assembly.

## Current 23-piece print package

| IDs | Parts |
|---|---|
| 01,02 | Hull with four integral wells/channels; extended service hatch |
| 03,04 | Main analog/power cassette; longitudinal battery cradle |
| 09,11,14,16,17 | Retained rudder bracket, motor mounts, rudder blade and tiller |
| 18–21 | Retained electronics capture bridges, relocated |
| 22–25 | Four internal servo covers, replacing external pods |
| 26–29 | Four 166 mm insulating probe arms |
| 30,31 | Steering saddle and removable overhead controller bridge |

STLs are millimetres and arms are exported stowed. Reorient for slicing without scaling. The hull remains within 320 × 176 mm. Check support removal from the wet channels and hollow internal wells in the slicer before printing. PETG remains a fit-prototype candidate; porosity, wall strength, sealing flatness and sustained screw preload are unqualified.

## BOM changes from Rev-C

- Retain four Hitec HS-65HB probe servos, the SKF seal/igus lower-bushing candidates and machined POM cartridges. Relocate them inside the hull; the original seal-duty and horn-survey holds remain.
- Add eight 20T/2 mm pitch pulley allocations, four nominal 96 mm pitch-length × 6 mm belt allocations, and four upper journal/bushing allocations. Exact matched supplier parts, tooth geometry, bore/retention, tension adjustment, torque and life remain HOLD. Smooth CAD envelopes are not functional pulley or belt STLs.
- Replace the four output shafts with the longer nominal shafts shown in CAD. Release shaft surface, pin and axial retention only after the actual transmission is chosen.
- Replace four external pod gaskets and mounting sets with four internal covers and sixteen M3 cover screws. M3×10 is a starting length only; verify blind engagement and tool access.
- Retain the four cartridge face gaskets and sixteen cartridge screws; verify the new installed stack.
- Replace the main hatch gasket with the new shaped continuous sheet gasket. Do not reuse the old rectangular outline. Verify compression and screw lengths at the new opening and shortened rear-center boss.
- Retain the battery cradle with four flush M2 countersunk screws at (88,±13) and (189,±13) mm. Nominal Ø4.6 top countersinks and Ø1.7 blind pilots are fit-prototype starting geometry; verify head seating and screw length before loading the pack.
- Add the separate steering saddle and upper controller bridge with four M3 fasteners each; the main cassette also has four M3 fasteners. Verify engagement and printed-pilot strength.
- Replace the straight steering pushrod with the provisional M2 dogleg envelope. Bend geometry, stiffness, retention and full steering travel require a new validation.
- Four roof-entry potting cups, wet hinge loops and insulated tip terminals require the actual wire/encapsulant and flex/immersion tests.

All other named electronics, battery, motor, shaft/tube, propeller and rudder parts remain. Retain the separate D24V50F5 probe supply. Existing electrical protection and connector omissions remain open. No purchase has been made. Fit one complete actuator/transmission/cartridge before buying four sets or printing the complete hull.


The authoritative current item list is [BOM.xlsx](../BOM.xlsx), with a [CSV mirror](../BOM.csv). Green rows detect electricity, red rows support the RC boat, and yellow rows serve both. Blank prices are unresolved procurement estimates; the total is partial. Native Google Sheets retains its live currency formulas; the XLSX uses a dated exchange-rate snapshot.

The Google Sheet is a prioritized **28-line procurement list**, with major electronics first. It excludes owned screws and minor supplies and combines selected mechanical kits. The repository BOM remains the complete **79-line assembly inventory**, including 23 printed pieces. These are different views of the same Rev-E design, not alternate revisions.
