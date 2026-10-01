# Rev-F procurement delta and fit-build list

Use the **live Rev-F Fusion assembly** with this document. The existing BOM.xlsx/BOM.csv and all 3D archives describe the earlier four-probe baseline; they are retained as historical purchasing references, not current quantity or print-release lists. No purchase was made.

## Quantity changes against the 79-line baseline

| Baseline IDs | Rev-F quantity | Change |
|---|---:|---|
| 014 | 2 | HS-65HB probe servos; steering SG90 remains one additional servo |
| 016–024 | 2 each | Seals, lower bushings, POM cartridges, cartridge gaskets, output shafts, arm pins, tip screws/nuts/terminals; retain only E2/E4 versions |
| 025 | 4 | Two timing pulleys per retained probe |
| 026–029 | 2 each | Belts, upper bushes, upper shafts, stock-horn adapters |
| 030 | 1 consumable lot | Two roof entries and two tip encapsulations; qualify actual dispensed quantity and wet bond |
| 031 | 2 runs | Cut electrode-lead lengths on the assembled prototype |
| 032 | 1 revised set | Two probe-servo disconnects, not four; retain fusing and strain relief |
| 033 | 1 revised set | Longer serviceable rear-controller interconnect; two active electrode inputs |
| 039 | 8 | M3×10 internal-cover screws, four per retained cover |
| 040 | 8 | M3×8 cartridge screws, four per retained cartridge |
| 041 | 4 | M2×6 probe-servo screws, two per retained servo |
| 044 | 4 | M3×8 cassette screws, revised pattern and blind-depth check |
| 045 | 4 | **Replace M3×8 with M3×30** for the shared rear shelf/frame stack |
| 046 | 6 | Two screws for each of the front-end, ESC and logic-regulator bridges; ESP32 frame uses ID045 |
| 076 | 2 | Print only covers **23 and 25** |
| 077 | 2 | Print only arms **27 and 29** |
| 079 | 1 | New PRINT_31 rear starboard shelf |
| Added | 1 fitted set | Electrically insulating compliant controller-retention pads; determine thickness/contact points with the real board |

All other baseline quantities remain one set/as listed, subject to the existing unresolved supplier and interface holds. The two retained nominal output shafts are the rear versions, approximately 35 mm long; do not buy the removed forward variants. No new price or availability claim is made.

## Nineteen printed pieces

| IDs | Pieces | Source |
|---|---:|---|
| 01 | 1 | Rev-F narrowed hull with two wet channels and new supports |
| 02 | 1 | Existing hatch; retain gasket outline and screw pattern |
| 03 | 1 | Rev-F shorter cassette, shifted aft |
| 04 | 1 | Retained Rev-E2 raised battery cradle |
| 09, 11, 14, 16, 17 | 5 | Rudder bracket, motor mounts, blade and tiller |
| 18 | 1 | Rev-F controller retention frame |
| 19–21 | 3 | Retained electronics capture bridges |
| 23, 25 | 2 | Retained E2/E4 internal covers |
| 27, 29 | 2 | Retained E2/E4 insulating probe arms |
| 30 | 1 | Steering saddle with Rev-F lower-foot chine fit |
| 31 | 1 | Rev-F rear controller shelf |

Prepare prints from the saved live Fusion model. Do not use the repository STL ZIP for these revisions. No new mesh, STEP, STL or F3D is supplied. Fit trials require a slicer review for support access, layer bonding, screw coupons, dimensional compensation and watertight skin. The hull's 320 mm length requires a printer/build orientation that accommodates it; no split-hull joining detail is released.

## Purchase in stages

1. Bench-fit the actual ESP32, ADC, regulators, ESC, battery and steering components against their nominal envelopes. Check header/connector heights, board clamp contacts, insulation and battery lead/strap space.
2. Obtain and fit **one** E2/E4 actuator set before duplicating it: actual HS-65HB horn, matched pulleys/belt, upper journal, retained output shaft, POM cartridge, seal and bushing. The smooth pulley/belt envelopes do not define manufacturable teeth, exact horn adaptation, tensioning or axial retention. Obtain the supplier parts/dimensions and release these interfaces first.
3. Qualify seal water duty and shaft finish, cartridge and hatch gaskets, wire potting, steering boot, and both the stern-tube outer bond and its internal rotating-shaft leakage path.
4. After fit, sealing and actuator tests, duplicate the validated actuator and print/assemble the full hull. Verify actual loaded mass, trim and freeboard in unenergized water before propulsion trials.

The reduced system is ready for targeted mechanical fit work only when the selected print process and hardware are checked. It is not a complete water-ready procurement release; unresolved items above must not be represented as certified or supplier-confirmed parts.
