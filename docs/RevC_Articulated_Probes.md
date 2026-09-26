# Rev-C.1 — independently articulated four-electrode array

27 September 2026. First mechanical concept iteration, based on repository `cb94758` and the live 1,250-item Rev-B.4 Fusion model. The user's present request and subsequent choice of **compact dry servos with serviceable seals** govern this work. Older briefs and the supplied Fusion-settings screenshot are context, not additional instructions.

## Stage and scope

The project has a detailed mechanical prototype, named electronics and drive components, revisioned Fusion/STEP exports and geometric checks. It does **not** yet have a validated protected front end, working instrument firmware, calibrated angle feedback, qualified seals, or a demonstrated electric-field reconstruction. Rev-C.1 changes the sensing architecture while preserving the 320 × 170 mm hull, battery, propulsion and steering layout.

Four separate electrode channels remain. Four independent servo-driven hinges replace the flush electrode screws. The MMC5983MA, pod, lid, rail, optional mast/boom and mounting pad are removed from the current assembly and procurement list. Old files remain historical records. No heading sensor is substituted: results are boat-frame measurements until a separately validated attitude/heading source is supplied.

This iteration supplies CAD packaging, serviceable cartridge geometry, printable fit prototypes, an updated BOM, a mathematical observability test and an assembly/test plan. **It is not a build-and-operate release.** The stock servo horn adapter, final seal specification and dynamic cable loop remain explicit engineering holds. An absent collision is not evidence that these interfaces work.

## Geometry and angle convention

Coordinates follow existing CAD: +X aft, +Y to the side formerly carrying E4, +Z up; Z=0 is the flat hull bottom. The hinges have transverse axes parallel to Y. Each arm moves in an XZ plane, with its projection parallel to the hull's long axis. At equal angles the arms are parallel; different angles intentionally destroy their 3D parallelism to create depth information.

| Channel | Hinge X,Y,Z (mm) | Exposed head center Y (mm) | Measurement angle |
|---|---|---:|---:|
| E1 / A0 | -75, -77, -18 | -82.3 | 90° |
| E2 / A1 | 90, -77, -18 | -82.3 | 30° |
| E3 / A2 | -75, 77, -18 | 82.3 | 30° |
| E4 / A3 | 90, 77, -18 | 82.3 | 90° |

`probe_E1_angle` through `probe_E4_angle` are editable Fusion angle parameters. 0° points aft, parallel to the bottom; 90° points vertically down. Use `scripts/revc_set_pose.py` for range-checked presets or a four-value list. Fusion itself does not enforce user-parameter limits; do not enter values outside 0–90°. The CAD rotation is not a physical servo calibration.

Hinge-to-electrode-center radius is **132 mm**. Hinge drop is 18 mm, giving **150 mm below the hull bottom at 90°**. This interprets the requested approximately 15 cm as deployed reach from the bottom, rather than adding a 150 mm arm below the hinge offset. At 0° the probes remain 18 mm below the bottom: they fold, but do not retract flush into the hull. Aft tip center reaches X=222 mm, 22 mm aft of the transom; the rudder already extends farther. Pods extend to approximately Z=-36 mm. These appendages change drag, handling and minimum water depth.

For hinge `(xh,yh,-18)` and angle θ:

```
x = xh + 132 cos θ
y = sign(yh) * 82.3
z = -18 - 132 sin θ
```

Lengths other than the four angles are reference parameters/fixed-coordinate geometry in this migration. Editing a displayed radius parameter alone does not rebuild the pods and arms. A geometry revision and audit are required.

## Mechanical and waterproofing architecture

Each printed dry pod bolts upward to a flat land under the hull. A small dry wiring aperture connects the pod interior to the main hull. This deliberately avoids running the servo's unsealed lead through a wet gland. **The pod is an extension of the hull's dry volume, not an independently sealed flood compartment.** A pod leak can flood the main hull.

Water boundaries are:

1. Continuous 1 mm silicone sheet face gasket, modeled at 0.75 mm compressed thickness, between pod and hull land. Four external compression stops set the nominal gap; bolt holes lie outside the continuous seal. This 25% compression is a prototype target requiring coupon validation, not a supplier-certified gasket design.
2. Removable machined POM-C cartridge with a separate sheet face gasket. Four outward-accessible M3 screws retain it; the shaft and seal are serviceable after the arm is detached.
3. Nominal SKF **6 × 16 × 7 HMSA10 RG** radial lip seal running on a smooth Ø6 shaft; igus **GFM-0608-06** flange bushing supports the shaft inboard. Neither the seal nor the servo spline is treated as a structural bearing by itself. Orient the primary lip toward water; keep it lubricated with a supplier-approved compatible lubricant.
4. A separate potted electrode-wire entry in the pod, and encapsulated tip terminal. The metal electrode is electrically isolated from shaft, drive pin, servo and hull fasteners. Only its outer head is intended to contact water electrically.

The seal is an industrial oil/grease seal with a supported dimensional reference, **not a documented subsea assembly rating**. Water compatibility, corrosion of its spring, pressure direction, lubrication, breakaway friction and cycle life require confirmation. POM seat tolerances and a lead-free ground shaft surface are machining tasks; a nominal CAD hole is not an H8 inspection result. General SKF counterface guidance includes Ra 0.2–0.8 μm; obtain the final hardness, lead, chamfer and runout requirements for this exact application before machining. Bare 316 stock is not automatically a qualified long-life seal track. See [mechanical references](RevC_Mechanical_References.md).

The dry Hitec HS-65HB is IP4X and receives no underwater claim. Its manufacturer drawing—not its rounded headline size—governs the 26 mm base-to-horn datum, 28.6 mm middle-lug pitch and M25T Ø5 spline allocation. The adapter between the **supplied horn** and the separate Ø6 shaft is an `INTERFACE_HOLD` volume. Do not print a guessed spline or infer a finished coupling from that volume. Measure the real horn, add retained drive features and axial location, verify alignment, and test the complete torque path before powered assembly. This interface is intentionally excluded from the print package.

The arm uses an external Ø2 cross-pin beyond the shaft's seal track. Pin capture and shaft axial retention must be finalized with the horn adapter; the present pin is a nominal envelope, not a retained spring pin assembly. The printed arm carries a recessed conductor groove and a tip potting pocket. A flexible loop at the hinge must accommodate the full range without entering the shaft seal or dragging on adjacent parts. No loop is approved by the rigid-motion audit. The recessed groove connects to the terminal potting pocket. Radius and deburr its edges during lead fitting, then validate insulation and potting; the rigid model does not establish flex life.

## Sensing changes required by the new geometry

Equal-angle poses are coplanar, including all four at 90°. They cannot recover a full 3D gradient. Use a non-coplanar pose such as **[90,30,30,90]°**, which creates a 66 mm depth separation. The retained two-pair measurement scheme must change: two numbers cannot determine three gradient components.

With positions in metres, set each row of A to `ri-r4`, i=1,2,3. Measure three coherent differences `[V1-V4, V2-V4, V3-V4]` and solve `A g = ΔV`. Here `g=grad(V)` in V/m and electric field `E=-g`. The ADS1115 supports the required 0–3, 1–3 and 2–3 mux selections. Calibration must undo individual analog-path gains, offsets and phase responses before solving. The reference electrode is a mathematical reference, **not a connection to battery ground**.

The supplied NumPy demonstrator verifies rank, conditioning, signed DC and complex-phasor recovery, and invalid-angle rejection. Its default pose condition number is about **3.36**; equal-angle poses are rejected. The threshold of 10 is an engineering screening choice, not an experimentally established instrument limit. For an illustrative 1 mV independent error on each electrode, common-reference noise is correlated and the computed gradient standard deviations are approximately 0.0061, 0.0061, 0.0184 V/m. Actual noise is unknown.

The ADS1115 multiplexes conversions. Its three readings are not simultaneous. DC measurements require a field stable over the scan; AC reconstruction requires timestamped, phase-coherent waveform fitting at a common frequency and phase reference. Three unsigned RMS values lose sign and phase and must **not** be inserted into the vector solve. At 860 conversions/s, three channels share the converter; acquisition timing, conversion latency, external RC settling and 50/60 Hz performance need bench validation. No firmware implementing this acquisition is supplied.

Four electrodes yield an affine field estimate over a finite volume, not a volumetric map, a unique source location, or a complete nonlinear field solution. Hull insulation, conductive shafts/fasteners, local conductivity boundaries and the large probe sweep can distort the field. A map requires repeated spatially registered samples. No magnetometer means no magnetic heading; a vertical boat-axis measurement is also not gravity-vertical when the hull pitches or rolls. Record boat attitude or keep it fixed in the first tests.

## Motion, loading and power

Same-side hinge spacing is 165 mm; the nominal arm including tip envelope reaches 138 mm from its hinge. Its inboard hub reaches 12 mm in the opposite direction, leaving 15 mm nominal longitudinal separation in the worst stowed arrangement. Different sides occupy separate Y lanes. The BRep audit checks each arm against static geometry in 5° increments; flexible wires and real fasteners are additional checks.

A screening drag estimate at 0.2 m/s uses freshwater density 1000 kg/m³, Cd=1.2, an 8 mm wide ×132 mm long arm: `F=0.5*rho*Cd*A*v²≈0.025 N`, moment≈0.0017 N·m at midspan. This omits the tip, pod, acceleration, fouling, impact and seal friction. At 0.5 m/s the same estimate increases 6.25×. Use stopped or very slow sampling, not high-speed deployment. Measure actual breakaway/holding torque; the HS-65HB's stall torque is not its continuous operating torque. Its quoted peak-efficiency torque is only about 0.039 N·m.

Add a **separate Pololu D24V50F5 5 V supply** for the four probe servos. Four HS-65HBs can approach 3.84 A stall at 4.8 V and 4.8 A at 6 V; 5 V operation falls between those endpoints. The manufacturer's 5 A regulator rating depends on input voltage and heat removal. It has up to approximately 1.5 V dropout under load, so a sagging 2S pack can lose 5 V regulation. Commission at the lowest permitted loaded pack voltage in the closed hull. Set power margin, fuse protection, brownout and jam handling from measurements. Do not use the old 1 A ESC BEC for all four probes, and do not parallel any regulator outputs.

Move one probe at a time initially; hold pose and allow mechanical/electrical settling before acquisition. Disabling PWM or servo power may allow backdrive, so do not assume power-off noise reduction preserves angle. A command timeout should inhibit measurement and prevent sustained stall. Emergency retraction is conditional on a clear sweep and available power, not a guaranteed passive behavior.

## Verification completed for this iteration

The final Fusion design has **1,523 timeline items, 47 user parameters and 119 physical solids**. The [BRep audit](../verification/RevC_Assembly_Audit.json) reports no feature warnings/errors, cross-component interference or Boolean failures. Each probe was checked against static solids at 5° increments through 0–90°. This is sampled rigid geometry, not a continuous swept-volume or flexible-harness test. Analytical electrode positions match the CAD to numerical precision.

All **21 STLs** pass connectedness, manifold-edge, winding and degeneracy checks. Mesh bounds agree with the stowed BRep manifest within 0.05 mm and volumes within 0.1%. The ZIP equals the individual meshes byte-for-byte. STEP contains 119 solids. The exported F3D reopened with matching volumes, parameter expressions and timeline, and the original cloud design was saved. The 11 retained printable parts other than the revised hull and electronics tray retain their Rev-B.4 bounds and volumes. See [export checks and hashes](../verification/RevC_Export_Check.json) and [native roundtrip](../verification/RevC_Native_Roundtrip.json).

The [numerical demonstrator](../verification/RevC_Observability.json) passes signed DC and complex-phasor recovery for a synthetic affine field, rejects coplanar poses and invalid angles, and reports correlated reference-noise propagation. These checks establish geometry and numerical consistency only. No powered actuator, waterproofing, flotation or actual field-acquisition test has been performed; `assembly_release_passed` remains false.

## Assembly, printing and release gates

See [current BOM/print plan](Print_and_Procurement.md) and [assembly/wiring](Wiring_and_Assembly.md). Start with one complete pod/arm fit prototype and a machined seal cartridge; do not buy four complete sets before the coupling and seal tests close. PETG arms print flat with their long fibres in the bed plane. Print pods open side up and keep support scars off sealing lands; finish flatness after printing. All flange/pilot fits are coupon starting dimensions. Precision seal and bushing seats must be machined, not printed at nominal size and called finished.

| Gate | Evidence needed before release |
|---|---|
| Servo-to-shaft adapter and pin retention | Exact horn survey, completed coupling drawing, retained shaft/pin, full travel and torque test |
| Seal cartridge | Supplier application confirmation, machining tolerances/finish, measured seal drag, wet cycling and ingress test |
| Printed pod/hull interface | Flatness, gasket compression and bolt retention tests; no porosity or cracking under sustained compression |
| Electrode lead/tip | Actual wire and terminal selection, bond/immersion test, insulation test, repeated 0–90° flex cycling and retained slack |
| Complete assembly/service | Measured hardware, tool access, harness bends, underside pod removal and tray/battery removal |
| Buoyancy/trim | Measured assembly mass, displacement, static/dynamic freeboard and stability with all poses; no validated result yet |
| Electrical | Protected front end, return routing, low-battery supply/load traces, safe input range and motor/servo interference measurements |
| Reconstruction | Per-channel gain/phase/offset and angle calibration; controlled known-field tests including vertical and mixed directions |

The experimental scanner is not protective equipment. A low or absent reading cannot establish that water is safe. First sensing trials should use a controlled isolated laboratory field, with no people contacting the water.
