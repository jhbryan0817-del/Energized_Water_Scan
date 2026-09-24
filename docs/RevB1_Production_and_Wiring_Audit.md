# Rev-B.1 production and wiring audit — 25 September 2026

## Decision

**Improved prototype; not released for production.** A light CAD audit cannot establish that procurement of the named components alone produces an assemblable, watertight craft. The named electronics and drive parts are retained, but the baseline omits several exact integration parts and physical validation steps. No PCB was designed.

Repository baseline: `c00e548020134553f6556fff40d97cb7c4fb33dc`. The existing Fusion document `Energized_Water_Scanner` (lineage `ybjJzCieRSuTtp7MFNwhCA`) matched Rev-B's 1009 timeline items and component bounds. The repository documentation, part inventory, verification methods and live assembly were reviewed. Historical documents are design evidence, not independent instructions to buy parts or expand the task.

## Changes made directly in Fusion

Added twelve through-slots to PRINT_03, using one fixed-coordinate sketch and one cut feature on a construction plane. The 3 mm tray plate remains one solid. Five stations accept narrow nonconductive cable ties; two additional slots provide an ESC restraint path. No purchased part was resized or substituted. No hull penetration or sealing surface was changed.

Coordinates below are assembly millimeters. Slots run through Z=16–19 mm; the cut starts at Z=15 and ends at Z=20. Paired harness slots leave a 5 mm bridge between them. Use ties no wider than 2.5 mm; verify actual tie thickness and printed passage with a coupon. Install ties from below on the removed tray, with locking heads above the tray and away from connectors. Deburr edges; do not cinch directly against bare conductors, PCB components or the battery.

| Station | Slot centers X,Y (mm) | Each opening X×Y | Purpose |
|---|---|---|---|
| Power aft | (76,44), (84,44) | 3×4 mm | Restrain low-voltage distribution branch near regulator/ESC |
| Logic front | (-4,25), (4,25) | 3×4 mm | Restrain controller branch before connector |
| Sensor front | (-16,-24), (-8,-24) | 3×4 mm | Front-end branch strain relief |
| Sensor middle | (74,-44), (82,-44) | 3×4 mm | ADC/sensor harness restraint |
| Sensor aft | (101,-44), (109,-44) | 3×4 mm | Servo/control branch restraint, separated from shaft |
| ESC retention | (110,27), (110,57) | 4×3 mm | Retention tie over insulated ESC housing, keeping vents/heat-dissipation area clear |

The cut removes 432 mm³. The tray remains 235×122×27 mm overall. At the narrowest relevant slot-to-edge locations there is 2.5 mm nominal material (ESC outer slot); harness stations next to the drive opening leave at least 3 mm nominal material. These are nominal CAD dimensions, not measured print strength. Only PRINT_03 needs reprinting relative to Rev-B. All twelve STLs are regenerated as a consistent package.

The completed design has 1012 timeline items and retains 40 user parameters.

## Whole-design audit

| Area | Finding / disposition |
|---|---|
| Hull/deck | Retained 320×170 mm hull and 245×130 mm hatch. One-piece hull requires a bed exceeding the actual oriented footprint plus brim/support margin. Overhanging deck lip and internal features need slicer review; mesh closure is not watertightness. |
| Hatch | 269×154×3 mm cover with eight screws. Flatness, stiffness, gasket compression and insert retention remain untested. Do not prescribe tightening torque without actual material/insert/gasket tests. |
| Electronics tray | New harness and ESC restraint slots improve assembly. Board support pads do not positively retain the ESP32, front-end or regulator. A board-specific removable clip/carrier and exact connector stack remain unresolved. ADS1115 retains its four mounting locations. |
| Battery | Existing transverse tray and straps remain. Allow main and balance leads to leave freely; fit a pull loop. Battery plus tray must be removed for USB access and main-tray service. No pack compression or lifting by leads. |
| Motor/shaft | Existing aligned face mount, cradle, coupling and bonded stern tube remain. Verify motor screw engagement and reach, solder-tab insulation, coupling screw access, alignment and bond strength using actual parts. |
| Steering | Ideal 17.9 mm horn radius and 131 mm linkage are provisional. The model explicitly labels horn spline fit TBD. A stock SG90 horn is not proven to reproduce that radius; real horn/clevis geometry must be settled before setting travel. Boot, collar and pin retainers lack exact manufacturer parts. |
| Electrodes | Existing heads, seal washers and terminal-access openings retained. Ring-lug thickness, barrel orientation and wiring are absent from CAD; verify under-tray clearance and compression stack before selecting bolt length. Wire these before installing tray. |
| Magnetometer | Pod has a cable exit, but the main-hull sealed cable-entry hardware/path is not released. Do not pinch a cable under the main hatch gasket. Select and measure a sealed bulkhead/potted feedthrough, then locate and model it away from rail and gasket. No arbitrary hole was added. |
| Bonded attachments | Rail, motor supports and rudder bracket need material-compatible surface preparation, bond-line control and load testing. Geometric contact does not specify an assembly process. |
| Fasteners/print fits | Several lengths and pilots remain starting values. Inserts, boot, collar, gasket, connectors, wire and fuse are not a complete exact-part BOM. Procurement of only the main component table is insufficient. |
| Sensing/control | No validated firmware, front-end circuit, thresholds or failsafe behavior. This remains experimental sensing equipment. |

## Wiring findings verified against primary sources

1. **Battery-to-ESC connector mismatch:** the baseline battery specifies XT60, while Hobbywing specifies a small Tamiya battery connector on WP-1625 and 4 mm female motor bullets. Add a correctly polarized, current-rated fused adapter/distribution harness and matching motor terminations. Exact adapter/fuse selection remains open. Do not assume the factory leads reach the compact routed installation.
2. **Servo supply margin:** Hobbywing specifies a 6 V / 1 A linear BEC. TowerPro's SG90 Digital specification lists 4.8 V; its manufacturer response on the same page allows 4.8–6 V and cites approximately 0.5–2 A operation current. Voltage is not a demonstrated incompatibility, but 1 A BEC capacity is not established for the loaded servo. Test current/transients and BEC temperature at steering load; a separately rated servo supply may be necessary and would require another packaging check. Do not connect BEC output to the Pololu 5 V output.
3. **USB power:** Espressif specifies mutually exclusive USB, 5 V header and 3.3 V header powering. Disconnect battery/external 5 V before USB programming. Physical battery removal alone is not an electrical isolation procedure unless the lead is unplugged.
4. **Regulator:** D24V10F5 is a 5 V regulator, with achievable current dependent on dissipation. The CAD remains an explicitly labeled F3-derived package proxy. Verify the actual F5 board and insulated terminals; do not cover its hot components with a restraint.

Sources checked 25 September 2026: [Hobbywing WP-1625](https://www.hobbywing.com/en/products/quicrun-wp-1625-brushed53), [TowerPro SG90 Digital including manufacturer responses](https://towerpro.com.tw/product/sg90-7/), [Espressif DevKitC V4 power and pin headers](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html), [Pololu D24V10F5](https://www.pololu.com/product/2831), [Adafruit ADS1115](https://www.adafruit.com/product/1085). Stock and prices are not procurement guarantees.

## Print process and acceptance

Use the material qualified by the builder for water, sunlight, electronics temperature and the chosen adhesive/sealant. PETG is a reasonable prototype candidate, not a released material specification. Start tray trials with a 0.4 mm nozzle, approximately 0.2 mm layers and at least four perimeters; inspect the slicer's actual remaining walls around holes rather than assuming nominal wall count is achieved. Adjust after coupons.

| Printed part | Orientation / inspection focus |
|---|---|
| Hull | Opening upward is a starting orientation. Inspect support access beneath deck flange and stern sleeve; prevent trapped supports. Check bottom sealing and long-part warping. Do not scale to fit a smaller printer. |
| Hatch | Broad flat face on bed; inspect sealing-face flatness and hole fit. |
| Electronics tray | Base downward, supports upward. New slots are vertical through-cuts requiring no new bridge/support feature. Thread ties before installation. |
| Battery tray | Base downward. Check strap slots, edge finish and pack clearance with padding. |
| Rail | Broad face downward. Check slot strength, captive hardware access and bonded overlap. |
| Pod/lid | Pod cavity upward; lid flat. Inspect shoe support and seal lands. |
| Rudder bracket | Select orientation to strengthen cantilever layers; verify support removal and stock bearing alignment. |
| Motor face/cradle | Inspect screw bores and shaft alignment; orient cradle opening upward where practical. Finish bores without thinning mounting webs. |
| Rudder blade/tiller | Orient for stock socket and torque-path strength; ream/match-drill tiny pin holes, remove burrs and verify retention. |

Print interface coupons first for tie passages, fasteners/inserts, electrode seals, stern tube and gasket. Record printer/material/settings and measured deviation; fit compensation must be based on these measurements. Dry-assemble the whole harness on the tray, inspect underside protrusions, then repeat removal with actual connectors and service loops. Leak-test unpowered, then measure loaded freeboard/trim and test drivetrain/servo heat and electrical noise. These physical tests are outstanding.

## Custom PCB assessment

**Yes: a compact interconnect/carrier PCB would materially improve repeatable assembly.** It can provide keyed labeled connectors, positive board mounting, a controlled sensor-ground layout, service disconnects, test points and separation between servo power and logic power. It would reduce flying junctions and the chance of connecting the BEC to the logic supply.

Initially retain the exact purchased ESP32, ADS1115 and Pololu modules on a carrier or connected harness, keep the magnetometer remote, and keep propulsion current in a separately rated fused harness. Place the high-impedance electrode front end close to its input connectors and away from switching/current loops. Do not route motor current through an unqualified small PCB or run electrode leads alongside motor wiring.

Freeze neither the PCB outline nor pinout yet: resolve front-end protection/bias/filtering, servo current budget, actual connector mating/bend volumes, firmware pin assignments and mounting clearance first. A PCB reduces wiring complexity; it does not solve hull sealing, horn fit or sensing validation. No schematic, layout, Gerbers or PCB manufacture files were created.

## Evidence and scope limits

Final results: 89 physical solids; zero detected cross-component overlaps or Boolean failures; zero feature warnings/errors; zero tested steering collisions at 71 positions; zero tested service-access intersections. All twelve STLs pass topology checks. The native F3D reopens with 1012 timeline items, 40 parameters and the expected tray volume. The physical STEP has 89 solid records, and the print ZIP matches the individual STLs. Historical suppressed/rolled-back/unknown timeline states remain listed in the audit rather than being called healthy.

See `RevB1_Assembly_Audit.json`, `RevB1_Service_Audit.json`, `RevB1_STL_Check.json` and `RevB1_Export_Check.json` in `verification/`. The assembly audit uses temporary exact BRep intersections, skips same-occurrence purchased-part internals, and checks 71 ideal steering positions. Service lift is sampled every 5 mm to 100 mm after stated removals. Cables, ties, connector mating sweeps, hands, fastener engagement, flexible boot, print deformation, seal compression and real loads are not fully represented. Passing these checks supports this geometry revision; it is not a production certificate.
