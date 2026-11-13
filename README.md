<div align="center">
  <img src="assets/flight-deck.svg" alt="Evans Kwashie — embedded systems, firmware, hardware and autonomous systems" width="100%">
</div>

<div align="center">
  <a href="https://github.com/Evans-Kwashie">GitHub</a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/evans-klenam-kwashie-seyram/">LinkedIn</a> &nbsp;·&nbsp;
  <a href="https://pcb-portfolio.vercel.app">Hardware Portfolio</a>
</div>

## `001 / MISSION BRIEF`

I build the electronics and firmware behind physical systems — from circuit design and PCB layout to peripheral bring-up, low-level drivers and system integration.

My focus is **embedded firmware, custom hardware, sensing, motion and UAV systems**.

**Embedded Firmware & Hardware · UAV & Autonomous Systems**  
B.Sc. Computer Science · University of Cape Coast, Ghana

```text
$ systemctl status evans

HARDWARE       ● active    KiCad / multilayer PCB / board bring-up
FIRMWARE       ● active    C / C++ / STM32 / ESP32
INTERFACES     ● active    UART / I²C / SPI / RS-485 / BLE
RTOS           ◉ learning  Zephyr RTOS
EMBEDDED LINUX ◉ learning  Linux internals / boot flow / low-level systems
```

## `002 / FLIGHT & CONTROL`

| PROJECT | BUILD NOTES |
|:--|:--|
| [**UAV-PHMC**](https://github.com/Evans-Kwashie/UAV-PHMC) | Custom four-layer STM32G071 UAV controller PCB with power monitoring, protected I/O and UART / I²C / RS-485 interfaces. Includes design files and generated manufacturing outputs. |
| **Search & Rescue UAV** | Team concept integrating flight-control electronics, mission computing, thermal imaging, GPS and telemetry. |

<div align="center">
  <img src="assets/signal-path.svg" alt="Sensor to MCU to control to actuator signal path" width="100%">
</div>

## `003 / HARDWARE BOARDS`

| PROJECT | ENGINEERING FOCUS |
|:--|:--|
| [**INA219 Voltage Sensing PCB**](https://github.com/Evans-Kwashie/INA219-Voltage_Sensing_PCB) | Four-layer current and power-monitoring board; Kelvin-sense shunt routing, analogue filtering and I²C. |
| [**UART-to-RS-485 PCB**](https://github.com/Evans-Kwashie/UART-2-RS-485-PCB) | Differential serial interface hardware with protection for field communication. |

## `004 / FIRMWARE`

| PROJECT | ENGINEERING FOCUS |
|:--|:--|
| [**Tiny-Tanks**](https://github.com/Evans-Kwashie/Tiny-Tanks) | Dual-board embedded control project paired with a 3D-printed chassis. |
| **STM32C071 Low-Level Firmware** | Register-level STM32C071 firmware project. Repository link will be added when the existing-history repository is published. |

## `005 / TEAM & COMMUNITY`

**UCC IoT / MicroPython** — ESP32-S3 Mini Pro board-support and bring-up work connected to the UCC IoT course ecosystem and its MicroPython demonstrations.

## `006 / ENGINEERING STACK`

| DOMAIN | TOOLS & TECHNOLOGIES |
|:--|:--|
| **Firmware** | C · C++ · Embedded C · MicroPython · STM32 HAL · CMSIS |
| **Platforms** | STM32 · ESP32 · RP2040 |
| **Embedded** | GPIO · interrupts · timers · PWM · DMA · UART · I²C · SPI |
| **Connectivity** | RS-485 · BLE · ESP-NOW · Wi-Fi · LoRa |
| **Hardware** | KiCad · schematic capture · multilayer PCB layout · DRC · board bring-up |
| **Tooling** | Git · Linux · VS Code · CMake · Ninja · GNU Arm GCC · GDB |

## `007 / CURRENT FLIGHT PLAN`

- **Zephyr RTOS** — learning threads, scheduling, message queues and driver/application structure.
- **Embedded Linux** — building foundations in Linux internals, boot flow and low-level systems.
- **STM32 bare-metal** — strengthening register-level peripheral control and understanding what happens beneath vendor HALs.
- **UAV electronics** — developing practical experience in power distribution, sensing, interfaces and hardware integration.

## `008 / BUILD PHILOSOPHY`

I value engineering that can be inspected, built, measured and debugged — not just code that compiles.

<div align="center">
  <sub>MAKE THE HARDWARE REAL. MAKE THE FIRMWARE RELIABLE.</sub>
</div>
