[English](README.md) | 简体中文

# AI 语音交互模块

基于 **CI1302** 芯片的离线语音识别模块。唤醒词与命令词均在模块本地识别——无需联网、不依赖云端服务——识别结果通过 **I2C** 或 **UART** 上报给主控。播报语也可由主控按需触发播放。

本仓库汇集了模块文档、各平台示例代码与固件，教程均提供中英双语版本。

## 📦 仓库结构

| 路径 | 内容 |
|------|------|
| `docs/` | 教程，每篇均有中英两个版本 |
| `docs/01-quick-start/` | 快速上手 |
| `docs/02-module-overview/` | 模块简介 |
| `docs/03-wake-words/` | 修改唤醒词与命令词 |
| `docs/04-custom-protocol/` | 自定义协议词条制作 |
| `docs/05-firmware-flashing/` | 固件烧录 |
| `docs/06-multi-host/` | 接入主控——Arduino、树莓派、Jetson、RDK X5 |
| `docs/07-pc-serial/` | 在 PC 上通过串口与模块通讯 |
| `docs/command-words-v1-zh.xlsx` | 命令词 / 播报词协议列表（中文） |
| `protocols/` | I2C 与 UART 通信协议参考 |
| `examples/` | 各平台源码，以及 ROS 1 与 ROS 2 功能包 |
| `firmware/` | 出厂固件与 STC8 固件 |
| `tools/` | 固件烧录工具与串口调试助手 |

每篇教程都有中英两个版本并互相跳转——`*.md` 是英文，`*_CN.md` 是简体中文。

## 🔌 接口

| 接口 | 说明 |
|------|------|
| I2C | 从机地址 `0x2A` |
| UART | 出厂固件为 UART1、115200 波特率——见 `firmware/factory/` |

协议细节见 [protocols/](protocols/)。

## 🚀 快速开始

1. 如有需要，先烧录固件——见[固件烧录](docs/05-firmware-flashing/firmware-flashing_CN.md)。
2. 用 I2C 或 UART 把模块接到主控板。
3. 按平台参考 [docs/06-multi-host/](docs/06-multi-host/) 下对应教程，或直接使用 [examples/](examples/) 里的代码。

## 📡 与模块通讯

通过 I2C，主控读写以下寄存器：

| 寄存器 | 作用 |
|--------|------|
| `0xDA` | 识别到的命令词 ID（`0x00` 表示未识别到） |
| `0xD1` | 播报被动播报语 |
| `0xD2` | 播报功能词 |
| `0xD3` | 播报命令词 |

通过 UART，模块发送 5 字节帧——`FE EF <类型> <ID> EE`。完整说明见 [protocols/uart/](protocols/uart/)。

## 📄 关于 `tools/`

`tools/` 下的固件烧录工具与串口调试助手均为第三方工具，此处仅为方便分发。版权归各自权利人所有。
