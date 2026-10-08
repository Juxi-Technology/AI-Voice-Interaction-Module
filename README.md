English | [简体中文](README_CN.md)

# AI Voice Interaction Module

An offline voice recognition module based on the **CI1302** chip. It recognises wake words and command words on-device — no network connection and no cloud service required — and reports the recognised command to a host over **I2C** or **UART**. Announcement phrases can also be played on demand from the host.

This repository collects the module documentation, per-platform example code and firmware, with tutorials in English and Simplified Chinese.

## 📦 Repository layout

| Path | Contents |
|------|----------|
| `docs/` | Tutorials, each in English and Simplified Chinese |
| `docs/01-quick-start/` | Quick start |
| `docs/02-module-overview/` | Module overview |
| `docs/03-wake-words/` | Changing the wake word and command words |
| `docs/04-custom-protocol/` | Creating custom protocol entries |
| `docs/05-firmware-flashing/` | Flashing firmware to the module |
| `docs/06-multi-host/` | Connecting a host — Arduino, Raspberry Pi, Jetson, RDK X5 |
| `docs/07-pc-serial/` | Talking to the module from a PC over serial |
| `docs/command-words-v1-zh.xlsx` | Command word / announcement phrase list (Chinese) |
| `protocols/` | I2C and UART protocol reference |
| `examples/` | Source code per platform, plus ROS 1 and ROS 2 packages |
| `firmware/` | Factory firmware and STC8 firmware |
| `tools/` | Firmware flashing tool and serial assistant |

Every tutorial exists in two versions and they link to each other — `*.md` is English, `*_CN.md` is Simplified Chinese.

## 🔌 Interfaces

| Interface | Details |
|-----------|---------|
| I2C | Slave address `0x2A` |
| UART | The factory firmware is built for UART1 at 115200 baud — see `firmware/factory/` |

Protocol details are in [protocols/](protocols/).

## 🚀 Quick start

1. Flash the firmware if necessary — see [firmware flashing](docs/05-firmware-flashing/firmware-flashing.md).
2. Wire the module to your host board over I2C or UART.
3. Follow the tutorial for your platform under [docs/06-multi-host/](docs/06-multi-host/), or use the matching code in [examples/](examples/).

## 📡 Talking to the module

Over I2C, the host reads and writes these registers:

| Register | Purpose |
|----------|---------|
| `0xDA` | ID of the recognised command word (`0x00` = nothing recognised) |
| `0xD1` | Play a passive announcement phrase |
| `0xD2` | Play a function word phrase |
| `0xD3` | Play a command word phrase |

Over UART the module sends a five-byte frame — `FE EF <type> <id> EE`. See [protocols/uart/](protocols/uart/) for the full description.

## 📄 Note on `tools/`

The firmware flashing tool and the serial assistant are third-party utilities, redistributed here for convenience. They remain the property of their authors.
