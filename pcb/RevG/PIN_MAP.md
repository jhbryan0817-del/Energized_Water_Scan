# Rev G connector pin map

View the board from the component side. Square pad = pin 1. The reverse silkscreen is mirrored for reading from the back. All GPIO are 3.3 V only.

| Connector | Pin | Signal | Restriction |
|---|---:|---|---|
| J1 | 1 | 3V3 |  |
| J1 | 2 | EN |  |
| J1 | 3 | GPIO36 | Input only; no internal pull resistors |
| J1 | 4 | GPIO39 | Input only; no internal pull resistors |
| J1 | 5 | GPIO34 | Input only; no internal pull resistors |
| J1 | 6 | GPIO35 | Input only; no internal pull resistors |
| J1 | 7 | GPIO32 |  |
| J1 | 8 | GPIO33 |  |
| J1 | 9 | GPIO25 |  |
| J1 | 10 | GPIO26 |  |
| J1 | 11 | GPIO27 |  |
| J1 | 12 | GPIO14 |  |
| J1 | 13 | GPIO12 | Boot strap: attached circuitry must preserve boot levels |
| J1 | 14 | GND |  |
| J1 | 15 | GPIO13 |  |
| J1 | 16 | GPIO23 |  |
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
| J4 | 3 | HI_DIAG |  |
| J4 | 4 | LO_DIAG |  |
| J4 | 5 | ADC_READY |  |
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
| J8 | 2 | ESC_BEC_NC | Leave BEC disconnected and insulated |
| J8 | 3 | GPIO14 |  |
| J9 | 1 | REG_SHDN | VIN referenced; not a direct 3.3 V GPIO interface |
| J9 | 2 | REG_PG | VIN referenced; not a direct 3.3 V GPIO interface |
| J9 | 3 | SERVO_EN | VIN referenced; not a direct 3.3 V GPIO interface |
| J9 | 4 | GND |  |
| J10 | 1 | GND |  |
| J10 | 2 | 3V3 |  |
| J10 | 3 | LOGIC_5V |  |
| J10 | 4 | GND |  |
| J11 | 1 | VBAT |  |
| J11 | 2 | GND |  |
| J12 | 1 | E2 | Floating hazardous-voltage input; insulate and strain-relieve |
| J13 | 1 | E4 | Floating hazardous-voltage input; insulate and strain-relieve |
