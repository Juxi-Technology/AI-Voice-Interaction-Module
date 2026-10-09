English | [简体中文](README_CN.md)

# AI Voice Interaction Module

An offline voice recognition module based on the **CI1302** chip. It recognises wake words and command words on-device — no network connection and no cloud service required — and reports the recognised command to a host over **I2C** or **UART**. Announcement phrases can also be played on demand from the host.

This repository collects the module documentation, per-platform example code and firmware. The `docs/` tutorials are available in 11 languages.

## 📦 Repository layout

| Path | Contents |
|------|----------|
| `docs/` | Tutorials — one folder per language, 11 languages in total |
| `docs/en/01-quick-start/` | Quick start |
| `docs/en/02-module-overview/` | Module overview |
| `docs/en/03-wake-words/` | Changing the wake word and command words |
| `docs/en/04-custom-protocol/` | Creating custom protocol entries |
| `docs/en/05-firmware-flashing/` | Flashing firmware to the module |
| `docs/en/06-multi-host/` | Connecting a host — Arduino, Raspberry Pi, Jetson, RDK X5 |
| `docs/en/07-pc-serial/` | Talking to the module from a PC over serial |
| `docs/command-words-v1-zh.xlsx` | Command word / announcement phrase list (Chinese) |
| `protocols/` | I2C and UART protocol reference |
| `examples/` | Source code per platform, plus ROS 1 and ROS 2 packages |
| `firmware/` | Factory firmware and STC8 firmware |
| `tools/` | Firmware flashing tool and serial assistant |

Stage folders keep the same name in every language, so `docs/en/05-firmware-flashing/` has a counterpart at `docs/<lang>/05-firmware-flashing/`.

| Language | Folder |
|----------|--------|
| English | [`docs/en/`](docs/en/) |
| Deutsch | [`docs/de/`](docs/de/) |
| Español | [`docs/es/`](docs/es/) |
| Français | [`docs/fr/`](docs/fr/) |
| Italiano | [`docs/it/`](docs/it/) |
| 日本語 | [`docs/ja/`](docs/ja/) |
| 한국어 | [`docs/ko/`](docs/ko/) |
| Português (BR) | [`docs/pt-br/`](docs/pt-br/) |
| Português (PT) | [`docs/pt-pt/`](docs/pt-pt/) |
| 简体中文 | [`docs/zh-hans/`](docs/zh-hans/) |
| 繁體中文 | [`docs/zh-hant/`](docs/zh-hant/) |

Every `docs/` page carries a language switcher in its first line. The screenshots are stored once under `docs/en/` and referenced from every language, so a language folder is not self-contained on its own. The tutorials under `examples/` and `protocols/` remain English + Simplified Chinese — `*.md` is English, `*_CN.md` is Simplified Chinese.

## 🔌 Interfaces

| Interface | Details |
|-----------|---------|
| I2C | Slave address `0x2A` |
| UART | The factory firmware is built for UART1 at 115200 baud — see `firmware/factory/` |

Protocol details are in [protocols/](protocols/).

## 🚀 Quick start

1. Flash the firmware if necessary — see [firmware flashing](docs/en/05-firmware-flashing/firmware-flashing.md).
2. Wire the module to your host board over I2C or UART.
3. Follow the tutorial for your platform under [docs/en/06-multi-host/](docs/en/06-multi-host/), or use the matching code in [examples/](examples/).

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
