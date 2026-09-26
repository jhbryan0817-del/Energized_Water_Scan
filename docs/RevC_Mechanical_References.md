# Rev-C.1 component and material reference register

Checked 27 September 2026. Links establish nominal dimensions/material properties, not proof that the assembled scanner is waterproof. No purchasing was performed. Part status below distinguishes a modeled candidate from a released interface.

| Item | Primary mechanical reference | CAD use and unresolved detail |
|---|---|---|
| Hitec HS-65HB, four additional units | [Manufacturer v2.2 dimension/specification sheet](https://www.hiteccs.com/public/uploads/data_sheet/HCS_HS-65HB_Specsheetv2.2_10-1729887930.pdf) | Drawing gives 23.6 ×11.6 case plan, 26 base-to-horn datum, 4.4 horn stack and 3.1 spline detail. Mounting positions 20.0 and 8.6 from output axis. General tolerance ±0.1. IP4X. Supplied horn geometry still requires measurement; no invented spline adapter. |
| SKF 6×16×7 HMSA10 RG, four | [SKF dimensional table](https://www.skf.com/mm/09433a92e9164581), [industrial seal engineering handbook](https://www.skf.com/binaries/pub12/Images/0901d196801073eb-Industrial-Shaft-Seals_tcm_12-115527.pdf) | Nominal ID6, OD16, width 7; elastomeric envelope modeled. Nitrile industrial seal, water/spring/lubricant qualification open. Supplier seat/counterface requirements govern final machining. |
| igus GFM-0608-06, four | [igus flange-bearing dimensional table](https://www.igus.com/ContentData/Products/Downloads/iglide_G300_FM_USen.pdf) | ID6, OD8, flange 12, length 6, flange 1. Nominal shaft 5.970–6.000 and housing 8.000–8.015 mm from table. CAD uses nominal seat; verify press-fit, installed clearance and moisture effects. Bearing remains in the dry side. |
| Pololu D24V50F5 /2851, one | [Dimension drawing](https://www.pololu.com/file/0J1436/d24v50f5-step-down-voltage-regulator-dimensions.pdf), [electrical/thermal limits](https://www.pololu.com/product/2851) | PCB17.8×20.3×1.57; upper components 6.1, lower 1.1. TwoØ2.18 holes separated 13.5×16.0. ±0.3 board edge and ±0.1 drill location. Model is a conservative envelope, not official STEP. Keep screw/lead/thermal space open. |
| M4×12 A4 DIN84 electrode screws, four | [TR Fastenings TR00007556](https://www.trfastenings.com/Products/Catalogue/Screws-and-Bolts/Machine-Screws/Cheese-Head/Slotted-Drive/TR00007556) | Replace old18 mm flush-hull screws with 12 mm arm-tip screws. Nominal headØ7×2.6. Confirm actual natural finish and dimensions; do not buy brass or a socket-cap substitution. |
| Printed pod and insulated arm material | [Prusament unfilled PETG technical datasheet](https://prusament.com/wp-content/uploads/2022/10/PETG_Prusament_TDS_2021_10_EN.pdf) | Prototype material choice with published mechanical data. Use unfilled material, not carbon/metal-filled conductive composites. Source print settings are starting points; orientation, water absorption, creep, porosity and sealing remain process tests. |
| Machined seal cartridge material | [Ensinger TECAFORM AH natural POM-C](https://www.ensingerplastics.com/en-us/shapes/acetal-tecaform-ah-natural) | Named machinable material with mechanical data; nominal shape supplied by CAD and interface table. Do not substitute a printed POM cartridge or assume adhesive bonds to it. |
| Pod and cartridge face gaskets | [Polymax 3043956:1 mm clear platinum-cured silicone sheet,60 ShA](https://www.polymax.co.uk/media/documents/Datasheet/platinum-cured-silicone-sheet-clear-1000-1-3043956.pdf) | Cut to CAD outlines, modeled compressed to 0.75 mm. Hard stops/compression and long-term seal performance need coupon tests. |
| Electrode terminal/entry potting | [3M DP270 technical datasheet](https://multimedia.3m.com/mws/media/1235390O/dp270-technical-data-sheets.pdf) | Low-shrinkage nonconductive potting candidate. No claim of certified PETG/wire-jacket immersion bond; qualify preparation, cure and adhesion, or replace before release. |
| Flexible electrode lead, candidate | [Alpha Wire 1854 manufacturer construction/bend data](https://www.alphawire.com/en/products/wire/hook-up-wire/premium/1854) | NominalØ1.12 mm fits 3 mm groove/Ø4 entry allocation. 10×OD minimum bend reference is not repeated underwater flex qualification. Final cable/termination selection remains HOLD; no immersion claim from this reference. |
| Custom shaft and pin | [Alleima Sanmac 316/316L bar mechanical data](https://www.alleima.com/en/technical-center/material-datasheets/bar-and-hollow-bar/bar/sanmac-316316l/), [SKF counterface requirements](https://www.skf.com/binaries/pub12/Images/0901d196801073eb-Industrial-Shaft-Seals_tcm_12-115527.pdf) | Custom 316 shaftØ6×30.5, pinØ2×22; cross-drill outside sealing track. Bar reference provides strength and hardness for a named 316/316L family; obtain a stock certificate and machine the custom diameters. It does not qualify the finished sealing track. Final shaft hardness/finish, pin retention and galvanic/field effects require validation. |

## Custom nominal interface drawing schedule

All values are millimetres. Mirrored module geometry uses transverse local coordinate u=abs(Y); longitudinal dimensions below are relative to its hinge X. Pivot Z=-18. Consult the editable STEP/F3D for the full solids. This table defines custom shapes; it is not a shop release or toleranced production drawing.

| Feature | Nominal geometry |
|---|---|
| Pod body | x=-28…14,u=17…64,Z=-36…-3.75; open-top cavityx=-25…11,u=20…60,Z=-33 upward |
| Mounting flange | x=-35…21,u=13…65,Z=-7.75…-3.75; fourØ3.4 clearances, centresx=-31/17,u=19/59 |
| Hull land | x=-35…21,u=13…65,Z=-3…3;20×20 dry wire aperturex=-16…4,u=25…45 |
| Hull attachment | Ø8 bosses;Ø2.5 blind M3 starting pilots endZ=5, boss topZ=8; M3×10 from flange gives nominal 5.25 mm engagement and 2.75 mm tip margin |
| Motor-foot clearance exception | E2/E4 inboard forward screws at global (59,±19): boss finishes Z=3, pilot ends Z=2; use M3×8, nominal 3.25 mm engagement and 1.75 mm tip margin. Coupon strength check mandatory. |
| Pod compression stop | FourØ6 annular stops around flange holes,0.75 high, outside gasket path |
| Cartridge barrel | Ø22,u=56…71.75; nominal Ø8 bushing seat,Ø12.1 flange reliefu=62.75…64.75;Ø16 seal seatu=64.75…71.75 |
| Cartridge flange |36×26 rectangle,x=±18,Z=-31…-5,u=64.75…67.75; fourØ3.4 holesx=±14,Z=-26/-10 |
| Cartridge gasket |36×26×1 sheet with Ø22.2 center opening and four screw holes; modeled0.75 compressed |
| Shaft |Ø6,u=51…81.5;Ø2 cross-hole throughX at u=77,Z=-18; no hole or flat on seal track |
| Arm |8×8 beam at u=73…81; tip radius132;Ø24 hinge hub;Ø6.2 shaft bore;Ø2.2 cross-hole; recessed3×2.5 wire groove |
| Electrode terminal |Ø4.5 clearance;Ø9 inner potting pocket; exposed headcenteru=82.3. Nut/lug/lead stack remains a measured assembly hold. |
| Potted pod entry | Final center localx=-23,Z=-28,Ø4 bore,Ø8 external boss extending to u=69; clears the cartridge flange. Qualify potting/strain relief and wire bends. |
| Servo mounting | MiddleØ2 lug holesx=-20/8.6,Z=-18; matchingØ1.7 pilots along u in support rails, nominal u=30…37 |
| Regulator tray mount | PCB corner79,-55; mounting centres81.2,-52.8 and94.7,-36.8 at Z=24 |

Fastener tolerances, lead-in chamfers, cartridge retention preload and seal/bushing coaxiality must be specified before manufacture. STEP solid dimensions alone do not convey these requirements. Supplier drawings should be rechecked against the exact purchased revision.
