# Rev G PCB and mechanical integration

2 October 2026. Source geometry was the live Fusion document; obsolete repository CAD was not used to derive the board.

## Delivered

The PCB replaces PRINT_03 with a 2 mm, four-layer carrier. Its exact U-shaped outline and hole centres are documented in [the PCB guide](../pcb/RevG/README.md). ESP32 DevKitC V4 WROOM sockets, 29-pin expansion, I2C/UART/power access, servo/ESC connectors and regulator control access are included. E2/E4 each have labelled solder pads. The ADS1115 is now a bare IC on the board; retain the former breakout as a spare.

Dual AMC3330 channels provide sensitive and high-voltage paths. The floating input circuitry is separated from logic by an explicit 8 mm copper rule; voltage-graded input rules also run in KiCad. These are engineering layout constraints, not a certified insulation design. Read the circuit limits and qualification requirements before purchasing or testing.

Removed: PRINT_03, PRINT_18/19/20/21 capture bridges, PRINT_31 rear controller shelf, former controller/front-end/ADC/regulator/ESC placeholders and ESC foam. The rear shelf's four posts and interior ribs were removed from the hull. Lower chine roots were retained; the remaining small supports belong to motor, battery, steering, probe or sealing functions. Hull volume changed from 556.919 to 543.531 cm³ and remains a solid body.

ESP32 and regulator models now show recognizable components and header geometry. Standard SMDs use KiCad models; the ESC has a detailed envelope and removable 22 × 29 mm adhesive fastener. It occupies X3…27, Y31.5…65.5 mm. Physical adhesive retention, heat and cable bends still require testing.

## Verification

- KiCad 10.0.6: zero DRC violations, zero unrouted connections, zero schematic parity issues; zero ERC violations in the saved reports.
- Fusion interference checks: carrier clears hull and motor/supports. Final ESC placement clears carrier and hull. Intentional contacts within component models are excluded from those assembly-pair checks.
- Current STL export: 13 solid print bodies; see the manifest. Native F3D and assembly STEP were saved from the edited live document.
- Native top/open Fusion images and populated/bottom-label KiCad renders are supplied. These are CAD images, not photographs of fabricated hardware.

No physical electrical, thermal, waterproofing or load tests were performed. The PCB remains an unqualified prototype for the requested 600 V environment. Generic passive/header procurement selections, load-derived fuse/wire ratings and the laboratory qualification plan remain release gates. There is no validated new firmware in this package.

## Assembly and service changes

Use the [Rev G pin map](../pcb/RevG/PIN_MAP.md). Historical E2=A1/E4=A3 wiring is superseded: ADS1115 A0−A1 is high range and A2−A3 is sensitive. J4 exposes diagnostics; wire them to spare inputs and implement invalid-state handling before measurement use. Remove JP1 before USB. Never connect HV_REF to logic ground. Never parallel the ESC BEC and the board's regulated outputs.

Use four 1 mm nylon spacers to preserve the original top plane at Z35; PCB occupies Z33…35. Check actual solder tails and nylon screw engagement before assembly. The ESP32 can be lifted from sockets for USB service. Board expansion header pins stay accessible without the former clamp.

Rev F descriptions are historical where they mention the tray or rear ESP32 shelf. The mechanical waterproofing qualification items remain open.
