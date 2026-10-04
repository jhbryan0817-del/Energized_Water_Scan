# Remaining qualification work

Current status: Rev H electronics design, live Fusion Rev I mechanical assembly. See the [CAD audit](CAD_Audit_2026-10-04.md). No physical tests or certifications are implied by the CAD or automated electrical reports.

## Electronics and sensing

1. Independent schematic/pinout/protection review; verify supplier package drawings, BOM selections, six-layer stack and effective capacitor values. Establish applicable installation category, pollution degree, CTI, creepage, clearance and exposure envelope with a qualified laboratory.
2. Current-limited dry power-up: polarity protection, fuse coordination, regulated rails, USB isolation procedure, startup/brownout, servo stall and motor-noise coupling. Measure peak currents and trace/via/component temperatures.
3. Isolated low-energy calibration: DC polarity/offset, 50/60 Hz amplitude and phase response, range overlap, noise versus temperature, ADC rate variation, data-ready/DIAG faults, clipping and overload recovery. Test electrode lead open/short and dry/fouled probes; they must not produce a false safe indication.
4. Laboratory insulation, common-mode/differential exposure, transient, dielectric, leakage and single-fault tests. Include clamp/resistor faults, contamination/condensation, enclosure and lead insulation. A clean ERC/DRC or an amplifier isolation certificate does not rate the whole instrument.
5. Validate immersed-electrode polarization/loading, motion and conductivity effects separately. Set a measured sensitivity/bandwidth/uncertainty specification before implementing hazard thresholds. A single pair has directional blind spots.
6. Validate location/heading/pose and acquisition timestamps, stale-data rejection and fail-safe behavior. No operational acquisition or mapping firmware has been released for Rev H.

## Mechanical and water boundary

| Interface | Required work |
|---|---|
| Hull, chines and wet roofs | Verify print porosity/coating, support removal, material continuity and leak performance. |
| Hatch/gasket | Actual material, compression, flatness, fastener lengths and repeated-opening tests. |
| Two probe shafts/cartridges | Water-rated seals, shaft finish/tolerance, lubrication, axial retention and face-gasket compression. |
| Two electrode lead entries | Actual jacket/potting adhesion, void control, insulation, strain relief and full-motion flex life. |
| Propulsion tube/shaft | Outer bonded seal plus separate internal dynamic seal, lubrication, alignment and wear tests. |
| Steering boot and blind fasteners | Retention, travel/fatigue, real screw engagement and no breakthrough into wet spaces. |
| PCB and modules | Validate the Rev H populated Fusion fit on real hardware, 2 mm module standoffs, underside tails, nylon hardware, ESC retention, wiring and hatch clearance. |

Specify immersion head, duration, water type, temperature and actuation cycles. Test coupons/interfaces, then the empty assembled hull using dry witness material. Repeat after service cycles. Any ingress fails the tested condition. Internal probe covers are service covers, not independent watertight compartments.

Weigh the actual completed vessel. Measure displacement, freeboard, trim, stability and retrieval capability with the real pack, hardware and coatings. Test steering, propulsion, probe stops and jam response in controlled **unenergized** water. Nominal CAD mass or earlier hull dimensions cannot substitute for flotation tests.

Hazardous-voltage tests require an appropriately equipped laboratory. Do not use people, animals or occupied floodwater as test loads. A low or invalid reading never grants access to potentially energized water.
