
# Bluetooth Low Energy (BLE) Data Write Script

This repository contains a script designed to scan, connect, and write data to Bluetooth Low Energy (BLE) devices using the Bleak library.

## Prerequisites

- Python 3.6 or newer.
- [Bleak](https://github.com/hbldh/bleak) library: `pip install bleak`

## Setup

1. Clone this repository: `git clone <repository_url>`
2. Navigate to the repository directory: `cd <repository_directory>`
3. Run the script: `python btle_dos_attack.py`

## Detailed Explanation

The script follows these steps:

1. Scans for nearby BLE devices for 10 seconds.
2. Lists the detected devices and prompts the user to select a device to connect to.
3. Attempts to write data of varying sizes and formats to the device's characteristics to determine which formats are accepted.
4. Continuously writes data using the successful formats.

## Tested Devices and Their Behavior

The following devices have been tested with the script and here are their observed behaviors:

- **Fitbit Sense**: [Behavior]
- **Lookee Sleep ring**: [Behavior]
- **Powerlabs HR Monitor Arm band**: [Behavior]
- **Powerlabs HR Monitor Chest strap**: [Behavior]
- **COOSPO HW807 Armband**: [Behavior]
- **Livlov Heart Rate Sensor**: [Behavior]
- **Wellue O2 Ring**: [Behavior]
- **Lookee O2 Ring**: [Behavior]
- **Checkme BP2A**: Stores data on the device and sends it once Bluetooth is connected.
- **SleepU Sleep Oxygen Monitor**: [Behavior]
- **Rhythm+ 2.0 (Scosche)**: Device's gets overwhelmed and turns off.
- **Wellue Pulsebit EX**: [Behavior]
- **Checkme O2 Smart Wrist Pulse Oximeter**: [Behavior]
- **Kinsa Thermometer**: Can't turn off the thermometer to reset the connection until battery dead/attack stopped - it thinks it's already connected.
- **BabyO2 Babytone Oxygen monitor**: [Behavior]
- **Wellue Visual Oxy Wrist Pulse Oximeter**: [Behavior]

> **Note**: Where [Behavior] is mentioned, it indicates that the behavior for the particular device resisted the attack and behaved normally. Although further investigations might prove otherwise.

---

**Disclaimer**: This script is intended for educational and research purposes only. Please ensure you have the necessary permissions and consent before running this on any device.
