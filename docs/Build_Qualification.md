# Build qualification — 29 September 2026 audit

**Current live Fusion: Rev-E2, 1 October 2026.** Physical corrections to the controller shelf, battery cradle/mounts and wire restraints are saved in Fusion. See [Rev-E2 physical changes](RevE2_Changes.md) and the [component audit](Mechanical_Audit_2026-10-01.md). The BOM and all repository 3D files are unchanged; existing exports are stale.

**Rev-E1 baseline repairs (29 September 2026), retained in Rev-E2:** It closes an obsolete port-wall opening, removes an obsolete projecting foot, and adds blind end caps to 16 cartridge and four rudder mounting bores. See [changes and validation](RevE1_Changes.md). Existing Rev-E 3D exports are stale for the hull; regeneration and mesh checks are deferred.

The assembly remains a fit prototype. A connected CAD solid and an interference-free pose do not establish a watertight printed assembly. Complete these gates before committing to a full four-actuator build.

## Leakage paths to close

| Path | Required disposition before water operation |
|---|---|
| Printed hull and channel roofs | Establish print orientation, support removal, wall integrity and any coating process on coupons; leak-test the finished hull. Do not drill drains from a wet channel into the hull. |
| Main hatch | Select the actual gasket material and compression range; check the continuous contact band, lid flatness and compression between fasteners. The modeled 2 mm gasket thickness does not establish a compressed installation or a torque specification. |
| Four rotating probe shafts | Confirm the exact seal, water compatibility, corrosion-resistant spring/materials, lubrication, shaft finish and tolerance, lip orientation, seat fit, and axial retention. A nominal annular seal envelope is not a detailed lip model. |
| Four cartridge-to-hull joints | Validate face-gasket compression and screw engagement. Check for bypass paths around the seal outside diameter and cartridge perimeter. |
| Four electrode wire entries | Qualify potting against both the actual wire jacket and printed/coated hull. Inspect voids, wet-side strain relief, dry-side restraint and the full moving lead loop. |
| Stern tube outside diameter | Bond and seal the tube-to-hull joint; inspect alignment and bond continuity. |
| **Inside the stern tube, along the propeller shaft** | **Separate open hold:** specify the actual shaft/tube bearing, lubrication and inboard sealing arrangement. A bonded outer tube does not seal this internal path. Check static and running ingress, wear, axial shaft movement, and maintenance access. |
| Steering pushrod boot | Select and retain the real boot at both ends; check the relocated dogleg through the complete steering travel, including bending loads and fatigue. |
| Fasteners and later-added connectors | Rev-E1 caps the 16 cartridge and four rudder bores with 3 mm nominal material. Verify actual lengths against blind material depth and wall thickness; do not drill through the caps. Every new through-hole needs its own seal; no external connector gland is implied by a dry cover slot. |

The four probe servos share the main dry hull. Their service covers provide no independent flood containment. Do not purchase ordinary servos on the assumption that those covers make them waterproof.

SKF lists the 6 × 16 × 7 size within its HMS5/HMSA10 family, but size availability does not qualify a water-facing oscillating seal. Its handbook also distinguishes standard steel springs from corrosion-resistant executions. Obtain application confirmation for the chosen part and operating water, rather than treating the nominal CAD label as approval. Sources: [SKF size table](https://www.skf.com/mm/09433a92e9164581), [SKF seal materials and springs](https://cdn.skfmediahub.skf.com/api/public/0901d196807662c1/pdf_preview_medium/810-701_CRSeals_Handbook_Nov_2024_pdf_preview_medium.pdf).

The [Krick 65220 listing](https://www.krickshop.de/Schiffswelle-Stevenrohr-M2-x-153mm-Eco.htm?a=article&ProdNr=65220) identifies the shaft/tube product; the current CAD and audit do not demonstrate a qualified dynamic inboard seal. Do not infer that the propulsion assembly is watertight from the outer bonded boss alone.

## Procurement and assembly gates

1. Obtain one actual probe servo, stock horn, matched belt/pulley set, cartridge, seal, bushing, output shaft and electrode lead. Confirm the 96 mm belt allocation can be realized with a supplier-matched system. Survey fasteners, retention, bearing supports and tension adjustment.
2. Build one complete actuator coupon with the same print process, sealing interfaces and lead route as the hull. Demonstrate insertion/removal, tool access, tensioning, current under load and full travel without binding or wire rubbing. Record tolerances before ordering four sets.
3. Confirm the battery's actual envelope including leads, connector, straps and protective padding. Rev-E2 increases nominal tube/coupling gaps to 9.661/2.904 mm; the coupling remains an unverified allocation and actual leads, padding and pack variation still require checks. Keep the pack restrained away from rotating parts.
4. Verify connector mating and removal with the cassette installed. Label four analog leads; separate them from motor and servo power; provide strain relief and service slack without crossing moving belts, shafts or the hatch gasket.
5. Establish the maximum immersion head, water type, operating duration, temperature and motion-cycle requirement. These are test inputs still to be specified, not ratings provided by this model.
6. Test each wet/dry interface, then the empty assembled hull using dry internal witness material. Test both static and actuated conditions; inspect after repeated hatch openings. Record conditions, duration, cycles and any ingress. Any observed ingress fails the test; absence of visible ingress only supports the conditions actually tested.
7. After sealing passes, verify loaded freeboard, trim, stability, propulsion/steering operation, actuator current limits, jam response and retrieval in controlled unenergized water. Validate the sensing system separately.

## Print release

Inspect support accessibility under the hatch flange, wet-channel roofs and stern-tube support. Retain structural roofs and functional mounts; remove only generated supports or explicitly revised CAD stock. Check slicer layer paths and trial coupons before a long hull print. No slicer, physical leak, torque, fatigue or flotation test was performed by this digital audit.

Do not use stale STL/STEP/F3D exports to manufacture later live-Fusion geometry. Export and mesh validation are intentionally deferred at the user's request.

## Rev-E2 mass and service update — 1 October

The 23 print bodies total 1,106.542 cm³. A fully dense 1.27 g/cm³ PETG estimate is 1.405 kg of plastic; documented battery, motor, five servos and ESC add about 0.283 kg before other hardware. Actual infill, coatings and hardware mass must be measured. The relocated battery/controller changes trim. The 28 mm waterline remains an unqualified reference; establish loaded flotation and freeboard.

Verify the new straight battery lift with controller installed, the forward 40 mm USB service allocation, accessible X185 aft cradle screws, strap passages, tie saddles and E4 cover's inward-slide/lift path on actual hardware. Preserve sealed stern caps. Check battery leads, restraints, padding, antenna clearance, header/connector height and harness bends against the current live assembly. See [physical revision](RevE2_Changes.md).
