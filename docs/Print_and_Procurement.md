# Rev-C.1 — print and procurement schedule

Updated 27 September 2026. **First-iteration fit prototype, not an unconditional procurement or water-test release.** Current design and holds: [articulated probes](RevC_Articulated_Probes.md); dimensions and material evidence: [reference register](RevC_Mechanical_References.md). Historical Rev-B.4 lists are preserved separately and must not be used as the current BOM.

## Removed from the current BOM

- SparkFun SEN-19921 / MMC5983MA magnetometer, its dedicated Qwiic lead and adhesive pad.
- PRINT_06 magnetometer rail, PRINT_07 service pod, PRINT_08 lid, optional mast/boom and their mounting hardware.
- Four original flush-hull M4×18 electrode screws, their wet sealing washers and old through-hull lug stack. The four electrical input channels remain, with electrodes at moving arm tips.

The old mounting bores are closed by solid CAD fill; do not simply leave open holes if converting an already printed hull. Reprint the revised hull. Legacy internal electrode bosses remain as harmless solid features rather than editing fragile historical dependencies.

## Added or changed BOM

Quantities are for one boat. Buy one actuator set first for fit/seal/coupling development; all four are required for the intended independent operation.

| Qty | Item | Selection / status |
|---:|---|---|
| 4 | Probe servos | Hitec HS-65HB, dry only; supplied Micro25T horn/hardware. New, additional to the steering servo. Body/lug drawing referenced; horn adapter HOLD. |
| 4 | Radial shaft seals | SKF 6×16×7 HMSA10 RG nominal candidate; water duty, spring, lubrication and drag qualification HOLD. |
| 4 | Shaft bushings | igus GFM-0608-06, nominal 6/8/12×6, flange 1 mm; installed fit check required. |
| 4 | Seal cartridges | Custom machined Ensinger TECAFORM AH natural POM-C; CAD + interface dimensions supplied. Precision drawing/tolerance release HOLD. Do not FDM-print functional seal seats. |
| 4 | Output shafts | Custom 316 Ø6×30.5 with Ø2 cross-hole beyond seal track. Final surface/hardness, coupling and axial retention HOLD. |
| 4 | Arm cross-pins | Custom 316 Ø2×22 nominal; retained-pin solution HOLD. |
| 4 | Tip electrode screws | A4 stainless DIN84 M4×12, TR00007556 dimensional reference; verify finish and head. |
| 4 each | Tip M4 nuts and electrical terminals | Retain natural A4 DIN934 nut family; choose a terminal that fits the Ø9 potting pocket and actual wire. Full terminal/crimp geometry HOLD. Do not reuse the large old under-hull lug blindly. |
| 4 | Horn-to-shaft adapters | Custom design pending actual supplied horn measurements; visible CAD allocation only, not an STL. |
| 1 | Probe-servo regulator | Pololu D24V50F5 /2851, 5 V; separate rail. Nominal modeled dimensions and two tray standoffs. Thermal/dropout/connector commissioning HOLD. |
| 2 | Regulator screws | M2×6 starting length; verify actual board/screw engagement and head clearance. |
| 14+2 | Pod-to-hull screws | Fourteen A4 M3×10 and two M3×8 starting lengths. The two M3×8 positions are E2/E4 inboard-forward at (59,±19), where the boss is flush to clear the motor foot. Actual printed thread life/preload qualification required; do not drill through pilot floors. |
| 16 | Cartridge retention screws | A4 M3×8 starting length; nominal 3 mm flange +0.75 mm gasket leaves 4.25 mm engagement. Verify strip margin and seal compression. |
| 8 | Probe-servo mounting screws | M2×6 starting length; supplied lug and receiving pilot fit to be verified. |
| 4+4 | Pod / cartridge sheet gaskets | Custom cut Polymax 3043956, 1 mm, 60 ShA platinum silicone; CAD outlines, nominal compressed thickness 0.75 mm. |
| As needed | Printed pod and arm stock | Unfilled Prusament PETG; [mechanical datasheet and qualification limits](RevC_Mechanical_References.md). |
| As needed | Tip/entry encapsulant | 3M DP270 candidate; PETG/metal/jacket adhesion and immersion qualification required. |
| 4 runs | Electrode leads | Alpha Wire 1854 Ø1.12 mm candidate for sizing; final repeated-flex/immersion choice HOLD. Lengths determined on one assembled moving prototype. |
| 1 branch | Servo harness/protection | Dedicated fused regulator branch, four keyed service connectors, common signal reference and servo power enable/jam handling. Exact connectors/fuse/current protection remain HOLD; not represented by released harness geometry. |

All newly selected material families have linked manufacturer mechanical data in the reference register. HOLD items are not released purchases or fabricated mechanisms. CAD geometry explicitly labels the incomplete adapter and nominal purchased envelopes.

## Retained electronics, propulsion and steering

One each: ESP32-DevKitC V4; Adafruit ADS1115 PID 1085 STEMMA QT revision; protected 40×30×12 mm front-end allowance; Pololu D24V10F5 logic regulator; Hobbywing WP-1625 ESC; Mabuchi RS-380PH-4045; Krick 65220 shaft/tube; Krick 63800 coupling with 63823/63820 inserts; Krick/Graupner 2307.30 propeller; Gens Ace GEA222S30X6GT battery; existing TowerPro SG90 steering servo and linkage. Rev-B.4's unresolved steering horn/boot/collar and drive-interface qualifications still apply. The new probe-servo selection does not silently replace the steering servo.

Retain hatch gasket/inserts/screws, tray and capture-bridge hardware, battery straps, motor screws/liner, rudder retention, ESC mounting pad and fused XT60-to-Tamiya drive wiring. See the [historical baseline inventory](RevB4_Print_and_Procurement_Historical.md) for unchanged items, excluding all magnetometer and fixed-electrode hardware. Existing exact connector/fuse omissions are not cured by this redesign.

## Current printed parts

Use the revision-matched package. It contains **21 pieces**: 13 retained part IDs and 8 new pieces. PRINT_01 hull and PRINT_03 electronics tray change; PRINT_06–08 are removed.

| Part IDs | Quantity / purpose |
|---|---|
|01,02,03,04|One each: hull, hatch, electronics tray, battery tray|
|09,11,14,16,17|One each: rudder bracket, motor face/cradle, rudder blade/tiller|
|18,19,20,21|One each: existing electronics capture bridges|
|22,23,24,25|One each: E1–E4 dry servo pods|
|26,27,28,29|One each: E1–E4 insulated probe arms|

STLs are millimetres. The export uses the **stowed pose** to keep each arm's local dimensions easy to inspect; reposition/orient in the slicer without scaling. The editable F3D and assembly STEP show the staggered measurement pose. The arm tip, groove, pin holes and pod interfaces are fit prototypes, not water-ready parts.

Use H2D for the 320×170 mm hull and 269×154 mm hatch; the hull leaves only 5 mm in the nominal 325 mm single-nozzle direction before aids. Other parts fit an X1C. Print arms flat, with the long direction in the layer plane; machine/ream cross holes after a coupon. Print pods cavity-up, support the cartridge opening as needed and finish sealing faces without thinning them. Source PETG settings are only a starting point. Inspect slicer walls, support removal and sustained screw/gasket load. FDM is not assumed watertight.

The old E2 motor-support coupon no longer verifies the moving probe system. Do not print it as the new probe coupon. First print one full pod and one arm, then check the actual servo/horn, cartridge, seal/bushing, shaft, wire and screw stack before printing the revised hull or all four sets.
