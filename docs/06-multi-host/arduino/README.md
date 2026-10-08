English | [简体中文](README_CN.md)

# AI Voice Interaction Module - Arduino User Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Hardware Connection](#hardware-connection)
3. [Development Environment Setup](#development-environment-setup)
4. [IIC Version Usage](#iic-version-usage)
5. [UART Version Usage](#uart-version-usage)
6. [FAQ](#faq)

---

## Introduction

This repository provides example code for Arduino platform to communicate with AI voice interaction module, supporting both I2C and UART communication methods.

- **Voice Recognition Module**: Supports offline voice recognition, outputs command ID after recognition
- **Broadcast Function**: Supports passive broadcast, function word broadcast, command word broadcast
- **Communication Protocol**: I2C address 0x2A, UART baud rate 115200

---

## Hardware Connection

### General Connection

| Arduino Pin | Voice Module | Description |
|-------------|-------------|-------------|
| 5V | 5V | Power positive |
| GND | GND | Power ground |

---

### I2C Version Connection

| Arduino Pin | Voice Module | Description |
|-------------|-------------|-------------|
| A4 (SDA) | SDA | I2C data line |
| A5 (SCL) | SCL | I2C clock line |

---

### UART Version Connection

| Arduino Pin | Voice Module | Description |
|-------------|-------------|-------------|
| D10 (RX) | TX | Serial receive (Software Serial) |
| D11 (TX) | RX | Serial transmit (Software Serial) |

---

### Serial Debug Connection

| Arduino Pin | USB-TTL | Description |
|-------------|---------|-------------|
| TX (D1) | RX | Debug output |
| RX (D0) | TX | Debug input (optional) |
| GND | GND | Common ground |

---

## Development Environment Setup

### 1. Install Arduino IDE

- Download: https://www.arduino.cc/en/software
- Install the latest version

### 2. Install Board Support Package

- Open Arduino IDE
- Tools → Board → Boards Manager
- Search and install the support package for your Arduino board
- Recommended: Arduino Uno / Nano

---

## IIC Version Usage

### 1. Open Project

- Open `IIC_Voice/IIC_Voice.ino` in Arduino IDE

### 2. Upload Code

- Select correct board model (Tools → Board)
- Select correct port (Tools → Port)
- Click upload button (→)
- Wait for upload to complete

### 3. Run Test

1. Open Serial Monitor (Tools → Serial Monitor)
2. Set baud rate to **115200**
3. After normal startup, it will display:

```
IIC Voice Module Initialized
```

4. Speak command words to the voice module, and the corresponding IDs will be displayed:

```
IIC Voice Module Initialized
ID: 1
ID: 4
ID: 10
```

### 4. Code Explanation

```cpp
// Initialize I2C
IIC_Init();

// Read command ID
int commandId = IIC_ReadCommand();

// Set broadcast
IIC_SetCommandVoice(0x00);  // Command word broadcast
```

---

## UART Version Usage

### 1. Open Project

- Open `UART_Voice/UART_Voice.ino` in Arduino IDE

### 2. Upload Code

- Select correct board model
- Select correct port
- Click upload button
- Wait for upload to complete

### 3. Run Test

1. Open Serial Monitor
2. Set baud rate to **115200**
3. After normal startup, it will display:

```
UART Voice Module Initialized
```

4. Speak command words to the voice module, and the corresponding IDs will be displayed:

```
UART Voice Module Initialized
ID: 1
ID: 4
ID: 10
```

### 4. Code Explanation

```cpp
// Initialize serial (Software Serial D10/D11)
UART_Init();

// Read command ID
int commandId = UART_ReadCommand();

// Set broadcast
UART_SetCommandVoice(0x00);  // Command word broadcast
```

---

## FAQ

### Q1: No output in Serial Monitor

**A: Check the following:**
- Check if serial baud rate is 115200
- Check if correct port is selected
- Check if TX/RX are reversed
- Check if GND is connected

---

### Q2: I2C version shows "IIC Read Error"

**A: Check I2C connection:**
- Check if SDA/SCL are reversed
- Check if device address is correct (0x2A)
- Check if GND is connected

---

### Q3: Command ID only shows 0 or 255

**A: Normal behavior:**
- 0 = No valid command recognized
- 255 = No new data
- Valid IDs are output only after normal recognition

---

### Q4: Recognition accuracy is not high

**A: Optimization suggestions:**
- Ensure quiet environment, not too much background noise
- Keep proper distance from microphone (10-50cm)
- Speak at moderate speed with clear pronunciation

---

### Q5: UART version not receiving data

**A: Check:**
- Confirm voice module TX is connected to Arduino D10 (RX)
- Confirm voice module RX is connected to Arduino D11 (TX)
- Check if baud rate is 115200

---

## Technical Support

If you encounter issues, please check:
1. Hardware connection is correct
2. Serial baud rate matches
3. I2C address is correct
4. GND is connected (very important!)
