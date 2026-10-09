English | [Deutsch](../../../de/06-multi-host/rdk-x5/README.md) | [Español](../../../es/06-multi-host/rdk-x5/README.md) | [Français](../../../fr/06-multi-host/rdk-x5/README.md) | [Italiano](../../../it/06-multi-host/rdk-x5/README.md) | [日本語](../../../ja/06-multi-host/rdk-x5/README.md) | [한국어](../../../ko/06-multi-host/rdk-x5/README.md) | [Português (BR)](../../../pt-br/06-multi-host/rdk-x5/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/rdk-x5/README.md) | [简体中文](../../../zh-hans/06-multi-host/rdk-x5/README.md) | [繁體中文](../../../zh-hant/06-multi-host/rdk-x5/README.md)

# AI Voice Interaction Module - RDK X5 (Python) User Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Hardware Connection](#hardware-connection)
3. [Environment Setup](#environment-setup)
4. [IIC Version Usage](#iic-version-usage)
5. [UART Version Usage](#uart-version-usage)
6. [FAQ](#faq)

---

## Introduction

This repository provides Python example code for RDK X5 (Raspberry Pi) platform to communicate with AI voice interaction module, supporting both I2C and UART communication methods.

- **Voice Recognition Module**: Supports offline voice recognition, outputs command ID after recognition
- **Broadcast Function**: Supports passive broadcast, function word broadcast, command word broadcast
- **Communication Protocol**: I2C address 0x2A, UART baud rate 115200
- **Programming Language**: Python 3

---

## Hardware Connection

### General Connection

| RDK X5 Pin | Voice Module | Description |
|------------|-------------|-------------|
| 5V (Pin 2/4) | 5V | Power positive |
| GND (Pin 6/9) | GND | Power ground |

> **Important**: Ensure all devices share a common ground!

---

### I2C Version Connection

| RDK X5 Pin | Voice Module | Description |
|------------|-------------|-------------|
| SDA (GPIO3, Pin 3) | SDA | I2C data line |
| SCL (GPIO5, Pin 5) | SCL | I2C clock line |

**Note**: Uses I2C bus 5 by default (BCM numbering)

---

### UART Version Connection

| RDK X5 Pin | Voice Module | Description |
|------------|-------------|-------------|
| GPIO14 (TXD, Pin 8) | RX | Serial transmit |
| GPIO15 (RXD, Pin 10) | TX | Serial receive |

**Note**: Uses `/dev/ttyAMA0` serial device by default

---

### Type-C Cable Connection (UART Alternative)

If using USB-TTL adapter module:

| RDK X5 | USB-TTL Module | Voice Module |
|--------|---------------|-------------|
| USB Port | USB | - |
| - | RX | TX |
| - | TX | RX |
| GND | GND | GND |

**Note**: Serial device is usually `/dev/ttyUSB0` in this case

---

## Environment Setup

### 1. System Requirements

- RDK X5 (or Raspberry Pi 3/4/5)
- Ubuntu / Debian system
- Python 3.7+

### 2. Install Dependencies

```bash
# Update packages
sudo apt update
sudo apt upgrade -y

# Install Python libraries
sudo apt install -y python3-pip python3-smbus i2c-tools

# Install pyserial
pip3 install pyserial
```

### 3. Enable I2C Interface

```bash
# Open configuration tool
sudo raspi-config

# Select Interface Options → I2C → Enable
# Reboot to take effect
sudo reboot
```

### 4. Enable Serial Interface

```bash
# Open configuration tool
sudo raspi-config

# Select Interface Options → Serial
# Select: No (shell) → Yes (hardware serial port)
# Reboot to take effect
sudo reboot
```

### 5. Test Hardware Interfaces

```bash
# Test I2C device
sudo i2cdetect -y 5

# Test serial port
ls /dev/ttyAMA0
ls /dev/ttyUSB0  # If using USB-TTL
```

---

## IIC Version Usage

### 1. Check Code Files

```bash
cd IIC_Voice
ls -la
# Should see iic_voice.py
```

### 2. Configure I2C Bus

Edit `iic_voice.py` file, modify parameters as needed:

```python
# I2C device address
DEVICE_ADDRESS = 0x2A

# Register address
REG_RESULT = 0xDA

# I2C bus number (modify according to actual connection)
bus = smbus.SMBus(5)  # I2C bus 5
```

### 3. Run Program

```bash
# Make executable
chmod +x iic_voice.py

# Run (sudo required for I2C access)
sudo python3 iic_voice.py
```

### 4. Run Test

After normal startup, it will display:

```
Speech Serial Opened! Baudrate=115200
```

Speak command words to the voice module, corresponding IDs will be displayed:

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. Stop Program

Press `Ctrl + C` to stop the program:

```
Program terminated
```

---

## UART Version Usage

### 1. Check Code Files

```bash
cd UART_Voice
ls -la
# Should see uart_voice.py
```

### 2. Configure Serial Port

Edit `uart_voice.py` file, modify serial device:

```python
# UART direct connection (default)
SERIAL_PORT = '/dev/ttyAMA0'

# Or use USB-TTL
# SERIAL_PORT = '/dev/ttyUSB0'

# Baud rate
BAUD_RATE = 115200
```

### 3. Run Program

```bash
# Make executable
chmod +x uart_voice.py

# Run (sudo required for serial port access)
sudo python3 uart_voice.py
```

### 4. Run Test

After normal startup, it will display:

```
Speech Serial Opened! Baudrate=115200
```

Speak command words to the voice module, corresponding IDs will be displayed:

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. Stop Program

Press `Ctrl + C` to stop the program

---

## FAQ

### Q1: Insufficient I2C operation permissions

**A: Add user to I2C user group:**
```bash
sudo usermod -aG i2c $USER
# Re-login to take effect
```
Or run with `sudo`

---

### Q2: Serial device not found

**A: Check:**
1. Check if serial port is enabled (raspi-config)
2. Check if device name is correct
   - UART direct: `/dev/ttyAMA0`
   - USB-TTL: `/dev/ttyUSB0` or `/dev/ttyUSB1`
3. Check if hardware connection is correct
4. Check if serial port is occupied by other programs

```bash
# List available serial ports
ls /dev/tty* | grep tty
```

---

### Q3: I2C device not detected in scan

**A: Check:**
1. Confirm I2C is enabled (raspi-config)
2. Check if SDA/SCL are reversed
3. Check if common ground is connected
4. Check if device is powered on

```bash
# Scan I2C devices
sudo i2cdetect -y 5
```

If you see 0x2A, device connection is normal

---

### Q4: Command ID only shows 0 or nothing

**A: Normal behavior:**
- 0 = No valid command recognized
- IDs are only output when valid command words are spoken
- Wake up module first, then speak command

---

### Q5: Recognition accuracy not high

**A: Optimization suggestions:**
- Ensure quiet environment, not too much background noise
- Keep proper distance from microphone (10-50cm)
- Speak at moderate speed with clear pronunciation

---

### Q6: Serial communication abnormal

**A: Check:**
1. Are TX/RX cross-connected correctly? (Module TX → RPi RX)
2. Is baud rate 115200
3. Is common ground connected
4. Is serial port occupied by other processes

```bash
# Check serial port occupancy
sudo lsof /dev/ttyAMA0
```

---

## Technical Support

If you encounter issues, please check:
1. Hardware connection is correct (common ground is very important!)
2. Serial baud rate is 115200
3. I2C address is correct (0x2A)
4. You have sufficient permissions to access hardware interfaces

```bash
# Useful debugging commands
ls -l /dev/i2c*      # List I2C devices
ls -l /dev/ttyAMA0   # List serial device
groups                # List user group permissions
```
