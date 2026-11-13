<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0b132b,60:1c2541,100:00e5a0&height=210&section=header&text=Evans&fontSize=64&fontColor=ffffff&fontAlignY=38&animation=fadeIn&desc=Embedded%20Systems%20%C2%B7%20Firmware%20%C2%B7%20Hardware%20%C2%B7%20UAV&descSize=18&descAlignY=60" alt="Evans banner" />

<a href="https://github.com/Evans-Kwashie">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=20&pause=1200&color=00E5A0&center=true&vCenter=true&width=700&lines=Schematic+%E2%86%92+layout+%E2%86%92+bring-up+%E2%86%92+firmware;STM32+%C2%B7+ESP32+%C2%B7+RP2040;Flight+controllers+and+drone+payload+electronics;Making+hardware+and+firmware+talk+to+each+other" alt="Typing SVG" />
</a>

</div>

---

### `$ ./boot --profile evans`

```text
[  OK  ] Hardware    schematic capture, 4-layer PCB layout, differential pairs, sensing front-ends
[  OK  ] Firmware    C, C++, MicroPython on STM32, ESP32 and RP2040
[  OK  ] Wireless    ESP-NOW, BLE HID, LoRa telemetry
[  OK  ] UAV         flight controllers, payload electronics, ROS 2 digital twins
[ RUN  ] Mission     low-cost modular search-and-rescue drone (team capstone)
```

I design the board, write the firmware that runs on it, and debug the two together. My work sits where electronics meets flight: custom PCBs, sensor pipelines, and the embedded software that keeps a vehicle in the air.

---

### 🛰️ Flight and UAV

| Project | What it is |
|---|---|
| [**UAV-PHMC**](https://github.com/Evans-Kwashie/UAV-PHMC) | Modular 4-layer payload management and health controller for a lightweight drone, built on an STM32G071 with a ROS 2 digital twin |
| **SAR Drone** (in progress) | Team capstone: F450 quadcopter, STM32F405 flight controller, ESP32 mission computer, thermal camera, GPS and LoRa telemetry feeding a live rescue dashboard |

### 🔌 Custom boards

| Board | What it does |
|---|---|
| [**INA219 Voltage Sensing PCB**](https://github.com/Evans-Kwashie/INA219-Voltage_Sensing_PCB) | 4-layer current and power monitor with Kelvin-sense shunt routing |
| [**UART to RS-485**](https://github.com/Evans-Kwashie/UART-2-RS-485-PCB) | Differential-pair RS-485 converter with TVS protection |
| [**CH340C USB to UART**](https://github.com/Evans-Kwashie/CH340c-usb-uart-board) | First fully self-designed board, USB data lines to UART |

### 🤖 Firmware and motion control

| Project | What it does |
|---|---|
| [**Gyroscope-Controlled Car**](https://github.com/Evans-Kwashie/Gyroscope-Controlled-Car) | MPU6050 hand-orientation sensing drives an RC car over ESP-NOW with low latency |
| [**ESP32 Air Mouse**](https://github.com/Evans-Kwashie/Esp32-Air-Mouse) | Wearable air mouse: Kalman-filtered IMU data sent as a BLE HID device |
| [**Tiny Tanks**](https://github.com/Evans-Kwashie/Tiny-Tanks) | Dual-board real-time firmware project with a 3D-printed snap-fit chassis |

---

### 🧰 Toolbox

<div align="center">

![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MicroPython](https://img.shields.io/badge/MicroPython-2B2728?style=for-the-badge&logo=micropython&logoColor=white)

![STM32](https://img.shields.io/badge/STM32-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white)
![ESP32](https://img.shields.io/badge/ESP32-E7352C?style=for-the-badge&logo=espressif&logoColor=white)
![Raspberry Pi Pico](https://img.shields.io/badge/RP2040-A22846?style=for-the-badge&logo=raspberrypi&logoColor=white)
![PlatformIO](https://img.shields.io/badge/PlatformIO-F5822A?style=for-the-badge&logo=platformio&logoColor=white)

![ROS 2](https://img.shields.io/badge/ROS_2-22314E?style=for-the-badge&logo=ros&logoColor=white)
![Betaflight](https://img.shields.io/badge/Betaflight-FFBB00?style=for-the-badge&logoColor=black)
![Fusion 360](https://img.shields.io/badge/Fusion_360-0696D7?style=for-the-badge&logo=autodesk&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

</div>

**Interfaces:** UART · RS-485 · I2C sensing · ESP-NOW · BLE · LoRa  
**Hardware craft:** multi-layer PCB design · differential routing · TVS protection · Kelvin sensing · 3D-printed enclosures

---

### 🎯 Now

- Bringing up flight-controller firmware for the search-and-rescue drone
- Building out payload electronics and telemetry for lightweight UAVs
- Learning in public: every board and firmware project here started as a self-taught build

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00e5a0,40:1c2541,100:0b132b&height=110&section=footer" alt="footer" />

</div>
