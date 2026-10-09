English | [Deutsch](../../../de/06-multi-host/raspberry-pi/README.md) | [Español](../../../es/06-multi-host/raspberry-pi/README.md) | [Français](../../../fr/06-multi-host/raspberry-pi/README.md) | [Italiano](../../../it/06-multi-host/raspberry-pi/README.md) | [日本語](../../../ja/06-multi-host/raspberry-pi/README.md) | [한국어](../../../ko/06-multi-host/raspberry-pi/README.md) | [Português (BR)](../../../pt-br/06-multi-host/raspberry-pi/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/raspberry-pi/README.md) | [简体中文](../../../zh-hans/06-multi-host/raspberry-pi/README.md) | [繁體中文](../../../zh-hant/06-multi-host/raspberry-pi/README.md)

# Raspberry Pi Voice Interaction Module User Guide

## Install Dependencies

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## Enable I2C Interface

```bash
sudo raspi-config
```

Select `Interface Options` -> `I2C` -> `Yes`

Reboot Raspberry Pi

## IIC Version

### File Location
`IIC_Voice/iic_voice.py`

### Wiring Instructions

| Raspberry Pi | Voice Module |
|--------------|--------------|
| GPIO2 (SDA) | SDA |
| GPIO3 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

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

### Enable Serial Port

Edit `/boot/firmware/config.txt` or `/boot/config.txt`, ensure the following configuration:

```
enable_uart=1
dtoverlay=disable-bt
```

Then reboot Raspberry Pi.

```bash
sudo reboot
```

### Wiring Instructions

#### Using Type-C Direct Connection

When using Type-C direct connection to Raspberry Pi, uncomment `SERIAL_PORT = '/dev/ttyUSB0'` and comment out `SERIAL_PORT = '/dev/ttyAMA0'`

#### Using UART Pins

| Raspberry Pi | Voice Module |
|--------------|--------------|
| GPIO14 (TXD) | RX |
| GPIO15 (RXD) | TX |
| GND | GND |
| 5V | 5V |

Comment out `SERIAL_PORT = '/dev/ttyUSB0'`

Uncomment `SERIAL_PORT = '/dev/ttyAMA0'`

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
