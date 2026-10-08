English | [简体中文](README_CN.md)

# Jetson Voice Interaction Module User Guide

## Install Dependencies

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## Check User Groups

```bash
sudo usermod -aG i2c $USER
sudo usermod -aG dialout $USER
```

Logout and login again for changes to take effect.

## IIC Version

### File Location
`IIC_Voice/iic_voice.py`

### Wiring Instructions

| Jetson | Voice Module |
|--------|--------------|
| Pin 27 (I2C1 SDA) | SDA |
| Pin 28 (I2C1 SCL) | SCL |
| Pin 6 (GND) | GND |
| Pin 4 (5V) | 5V |

### Check I2C Device

```bash
sudo i2cdetect -y -r 1
```

You should see address 0x2A

### Run

```bash
cd IIC_Voice
python3 iic_voice.py
```

### Output Format

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## UART Version

### File Location
`UART_Voice/uart_voice.py`

### Connection via UART Pins

When connecting module to Jetson via UART pins, comment out `SERIAL_PORT = '/dev/ttyUSB0'` and uncomment `SERIAL_PORT = '/dev/ttyTHS1'`

#### Wiring Instructions

| Jetson | Voice Module |
|--------|--------------|
| Pin 8 (UART1 TX) | RX |
| Pin 10 (UART1 RX) | TX |
| Pin 6 (GND) | GND |
| Pin 4 (5V) | 5V |

### Check Serial Port

```bash
ls /dev/ttyTHS*
```

### Run

```bash
cd UART_Voice
python3 uart_voice.py
```

### Output Format

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

### Connection via Type-C Cable

When connecting module to Jetson via Type-C cable, uncomment `SERIAL_PORT = '/dev/ttyUSB0'` and comment out `SERIAL_PORT = '/dev/ttyTHS1'`

### Check Serial Port

```bash
ls /dev/ttyUSB*
```

### Run

```bash
cd UART_Voice
python3 uart_voice.py
```

### Output Format

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## FAQ

### I2C Permission Issue

```bash
sudo chmod 666 /dev/i2c-1
```

### Serial Port Occupied

If serial port cannot be opened, check if it is occupied by other services:

```bash
sudo systemctl stop nvgetty
sudo systemctl disable nvgetty
```

## Protocol Description

### UART Protocol

| Byte | Content |
|------|---------|
| 1 | 0xFE (Frame Header) |
| 2 | 0xEF (Frame Header) |
| 3 | Function Word ID |
| 4 | Command Word ID |
| 5 | 0xEE (End Frame) |

### IIC Protocol

- Device Address: 0x2A
- Read Register: 0xDA (Read 1 byte)
  - 0x00: Not Recognized
  - Other: Command Word ID
