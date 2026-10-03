# Rev H connector pin map

Component-side view; square pad identifies pin 1. All GPIO are 3.3 V only. GPIO34/35/36/39 and GPIO32/23 have onboard functions; the expansion header does not make them free GPIO.

| Connector | Pin | Net | Restriction |
|---|---:|---|---|
| J1 | 1 | 3V3 |  |
| J1 | 2 | EN |  |
| J1 | 3 | ADC_READY | GPIO36: high ADC ready, reserved input |
| J1 | 4 | LO_DIAG | GPIO39: low amplifier diagnostic, reserved input |
| J1 | 5 | HI_DIAG | GPIO34: high amplifier diagnostic, reserved input |
| J1 | 6 | LO_READY | GPIO35: low ADC ready, reserved input |
| J1 | 7 | GPIO32 | Battery monitor ADC1 input; do not drive externally |
| J1 | 8 | GPIO33 |  |
| J1 | 9 | GPIO25 |  |
| J1 | 10 | GPIO26 |  |
| J1 | 11 | GPIO27 |  |
| J1 | 12 | GPIO14 |  |
| J1 | 13 | GPIO12 | Boot strap: attached circuitry must preserve boot levels |
| J1 | 14 | GND |  |
| J1 | 15 | GPIO13 |  |
| J1 | 16 | GPIO23 | Ingress sensor input; do not drive from expansion |
| J1 | 17 | GPIO22 |  |
| J1 | 18 | GPIO1 |  |
| J1 | 19 | GPIO3 |  |
| J1 | 20 | GPIO21 |  |
| J1 | 21 | GPIO19 |  |
| J1 | 22 | GPIO18 |  |
| J1 | 23 | GPIO5 | Boot strap: attached circuitry must preserve boot levels |
| J1 | 24 | GPIO17 |  |
| J1 | 25 | GPIO16 |  |
| J1 | 26 | GPIO4 |  |
| J1 | 27 | GPIO0 | Boot strap: attached circuitry must preserve boot levels |
| J1 | 28 | GPIO2 | Boot strap: attached circuitry must preserve boot levels |
| J1 | 29 | GPIO15 | Boot strap: attached circuitry must preserve boot levels |
| J2 | 1 | GND |  |
| J2 | 2 | 3V3 |  |
| J2 | 3 | GPIO21 |  |
| J2 | 4 | GPIO22 |  |
| J3 | 1 | GND |  |
| J3 | 2 | GPIO1 |  |
| J3 | 3 | GPIO3 |  |
| J3 | 4 | EN |  |
| JP1 | 1 | LOGIC_5V |  |
| JP1 | 2 | ESP_5V |  |
| J4 | 1 | GND |  |
| J4 | 2 | 3V3 |  |
| J4 | 3 | HI_DIAG | GPIO34: high amplifier diagnostic, reserved input |
| J4 | 4 | LO_DIAG | GPIO39: low amplifier diagnostic, reserved input |
| J4 | 5 | ADC_READY | GPIO36: high ADC ready, reserved input |
| J4 | 6 | HI_ADC_P |  |
| J4 | 7 | HI_ADC_N |  |
| J4 | 8 | LO_ADC_P |  |
| J4 | 9 | LO_ADC_N |  |
| J5 | 1 | GND |  |
| J5 | 2 | SERVO_5V |  |
| J5 | 3 | GPIO25 |  |
| J6 | 1 | GND |  |
| J6 | 2 | SERVO_5V |  |
| J6 | 3 | GPIO26 |  |
| J7 | 1 | GND |  |
| J7 | 2 | SERVO_5V |  |
| J7 | 3 | GPIO27 |  |
| J8 | 1 | GND |  |
| J8 | 2 | ESC_BEC_NC | Do not connect ESC BEC |
| J8 | 3 | GPIO14 |  |
| J9 | 1 | REG_SHDN | VIN referenced: no direct GPIO connection |
| J9 | 2 | REG_PG | VIN referenced: no direct GPIO connection |
| J9 | 3 | SERVO_EN | VIN referenced: no direct GPIO connection |
| J9 | 4 | GND |  |
| J10 | 1 | GND |  |
| J10 | 2 | 3V3 |  |
| J10 | 3 | LOGIC_5V |  |
| J10 | 4 | GND |  |
| J11 | 1 | BAT_RAW | 2S battery, externally fused; 8.4V normal maximum |
| J11 | 2 | GND |  |
| J12 | 1 | E2 | Floating electrode input; insulation and strain relief required |
| J13 | 1 | E4 | Floating electrode input; insulation and strain relief required |
| J14 | 1 | GND |  |
| J14 | 2 | 3V3 |  |
| J14 | 3 | LEAK_EXT | Internal 3.3V open-drain sensor only; never an external water electrode |
