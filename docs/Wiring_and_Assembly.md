# Rev-C.1 — wiring and assembly

Current design: [four articulated probes](RevC_Articulated_Probes.md). This is an integration plan; no validated schematic, firmware or completed harness is supplied. Older fixed-electrode and magnetometer wiring instructions are superseded.

## Connection changes

| Connection | Rev-C.1 arrangement |
|---|---|
|E1–E4|Four electrically independent exposed arm-tip heads → individually insulated leads → protected/bias/filter front end → ADS1115 A0/A1/A2/A3. No connection to hinge shaft, servo or hull hardware.|
|ADC|Retain 3.3 V I²C interface. For 3D solve use coherent 0–3,1–3,2–3 differential measurements, or four coherently calibrated single-ended channels followed by differencing. Two old perpendicular pairs are insufficient.|
|Magnetometer|Remove sensor, remote cable, firmware initialization/read/calibration requirements and heading dependency. This repository had no firmware implementation to delete.|
|Probe power|Fused 2S branch → added D24V50F5 → four HS-65HB servo supply/returns. Separate from logic supply and ESC BEC positive.|
|Probe controls|Four independent ESP32 PWM channels plus signal ground. Final GPIO/connector cavity map is unassigned; validate 3.3 V signal recognition before fixing hardware. Do not treat vendor wire colours as pinout verification.|
|Logic|Retain D24V10F5 → ESP32 5 V input; disconnect all external power before USB.|
|Steering|Existing ESC BEC → existing SG90 only. Its original loaded-current/boot/linkage gates remain open.|
|Returns|Common signal reference with star distribution. Servo/motor load return must not flow through the high-impedance front-end return. Do not parallel regulator outputs.|

The new regulator has 5 V±4% nominal accuracy; its lower bound is the servo's 4.8 V minimum before cable losses. Measure voltage at each moving servo under load, low battery and closed-hull temperature. Nominal 5 A rating alone does not establish margin. Measure loaded torque/current and handle jams quickly; avoid sustained hard-stop drive. A separately engineered power stage may be needed after tests.

## Build order and service access

1. Resolve the horn adapter, shaft axial/pin retention, electrode terminal stack and seal application first. Print one pod/arm; machine one cartridge. Check actual servo drawing revision and mounting screws. Do not power an incomplete coupling.
2. Measure cartridge bore, coaxiality and shaft finish; install bushing and lubricated seal without lip damage. The seal is not pressed over a cross-drilled edge. Use a protective installation sleeve. Confirm acceptable breakaway torque and smooth 0–90° travel.
3. Install the servo in its dry pod from the open top and wire the service connector. Fit the finished horn adapter, supported shaft, arm and retained cross-pin. Calibrate mechanical 0° and 90° with a physical jig; do not assume PWM endpoints equal these angles.
4. Fit an A4 electrode screw, nut and selected terminal in the tip pocket. Bed the lead in its groove, insulate/encapsulate all metal except the outer head, and verify that copper/terminal metal cannot contact water. Qualify the potting bond and cure before immersion.
5. Route a measured flexible service loop around the hinge into the separate potted pod entry. Protect it from shaft, lip, pin and stops. Dry-cycle the entire range and inspect tension/chafe at intermediate angles. The conductor is not a rotary seal. Keep sensor lead separate from the servo supply/return inside the pod and hull.
6. Finish pod/hull lands. Fit the continuous sheet gasket, pass dry leads through the 20×20 hull aperture, and bolt each pod from below. Nominal hard stops set 0.75 mm compression. Use a coupon-qualified tightening procedure. Inspect all four blind pilot floors and the smooth face-gasket path.
7. Mount the additional D24V50F5 on its two new tray standoffs, with two M2 screws and insulated soldered leads. Leave the connection row, both board sides and surrounding thermal space clear. Confirm screw heads miss components. Route its power branch away from ADC inputs.
8. Assemble the retained drivetrain and electronics tray. Terminate probe harnesses at labeled accessible dry connectors above the tray; provide enough slack to unplug, but not enough to reach the coupling or gasket. Final bundle diameters and connector bodies must be fitted physically.
9. Install tray screws before battery tray; retain the transverse battery and pull loop. For USB, disconnect and remove battery plus battery tray and isolate external 5 V. For tray removal, also unplug pod harnesses and remove the steering horn/linkage before releasing tray screws.
10. To service a pod: disconnect battery, remove battery/tray as needed to access its dry connectors, unplug them, then remove the four underside pod screws. Do not pull wires through the hull while connected. Lift out servo only after withdrawing its cartridge/shaft assembly as required. Replace and requalify disturbed gaskets/potting.
11. Verify polarity, continuity, insulation between all four electrodes and all hardware, and each isolated supply before energizing electronics. Test one motor-free pod on the bench. Then perform unpowered immersion/leak and representative-ballast flotation tests. Only proceed to controlled low-energy laboratory sensing after all earlier gates pass.

## Measurement sequence to implement

- Confirm valid calibrated angles, all four wetted tips, field/pose stability and sufficient clearance.
- Command one axis at a time to the chosen non-coplanar pose. Enforce 0–90° command limits, timeout/jam handling and physical end limits after calibration. The CAD limits are not firmware.
- Stop propulsion; settle until measured noise/repeatability criteria are met. Retain enough holding torque to prevent backdrive. Record servo status and motion state.
- Acquire timestamped coherent signed differences or common-frequency complex phasors. Reject saturated, unsettled or mismatched-phase data. Fit/calibrate electrode offsets and transfer functions in a known field.
- Calculate actual tip coordinates from calibrated angles, assess matrix rank/conditioning, then solve in boat coordinates. Log raw voltages, timestamps, angles, covariance/quality flags and the exact geometry/calibration revision.
- Report no 3D estimate for equal-angle/degenerate poses. Changes in voltage during movement combine spatial and temporal effects; do not label them vertical gradients without a stationary/coherent acquisition model.

Final GPIO assignments, exact keyed connectors, wire lengths, fuse coordination, angle feedback/repeatability, jam protection and firmware state machine remain open. No guessed pin-number harness or automatic powered-water operation is included.
