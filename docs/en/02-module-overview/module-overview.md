English | [Deutsch](../../de/02-module-overview/module-overview.md) | [Español](../../es/02-module-overview/module-overview.md) | [Français](../../fr/02-module-overview/module-overview.md) | [Italiano](../../it/02-module-overview/module-overview.md) | [日本語](../../ja/02-module-overview/module-overview.md) | [한국어](../../ko/02-module-overview/module-overview.md) | [Português (BR)](../../pt-br/02-module-overview/module-overview.md) | [Português (PT)](../../pt-pt/02-module-overview/module-overview.md) | [简体中文](../../zh-hans/02-module-overview/module-overview.md) | [繁體中文](../../zh-hant/02-module-overview/module-overview.md)

# Product Information

## 1. Voice Interaction Module Introduction

CI1302 is a new generation high-performance neural network intelligent voice chip developed by ChipIntelli. It integrates ChipIntelli's self-developed Brain Neural Network Processor BNPU V3 and CPU core, with a system clock frequency of up to 220MHz, built-in up to 640KB of SRAM, integrated PMU power management unit and RC oscillator, and integrated dual-channel high-performance low-power Audio Codec and multiple peripheral control interfaces such as UART, IIC, IIS, PWM, GPIO, and PDM. The chip requires only a few external components such as resistors and capacitors to implement various intelligent voice product hardware solutions, offering exceptional cost-effectiveness.

Utilizing 3rd-generation hardware BNPU technology, it supports DNN, TDNN, RNN, CNN and other neural networks as well as parallel vector operations, enabling functions such as voice recognition, voiceprint recognition, command word self-learning, voice detection, and deep learning noise reduction. The chip solution also supports multiple global languages including Chinese, English, and Japanese, making it widely applicable in home appliances, lighting, toys, wearable devices, industrial, automotive and other product fields for voice interaction, control, and various intelligent voice solution applications.

The CI1302 chip features a Brain Neural Network Processor core (BNPU), supporting offline NN acceleration computation and voice signal processing hardware acceleration. The CPU clock speed reaches up to 220MHz, enabling offline far-field voice recognition, with built-in 2MB FLASH storage supporting up to 300 command words.

## 2. Product Features

- Preloaded with 110+ voice commands, supporting customizable Chinese and English command words.

Users can modify command words through our provided web interface, generate new firmware files, and write the firmware to the module via PC software, after which the module will recognize the new commands. Built-in 2MB storage space supports writing up to approximately 120 command words.

- Built-in high-fidelity speaker and high-performance microphone.

It integrates advanced algorithms and circuit noise reduction technology to effectively filter environmental background noise, achieving a 99% recognition rate within a 5-meter range, enabling natural conversation and echo cancellation. It delivers clear audio output and accurately reproduces voice details.

- Onboard co-processor and IIC/Serial/UART/Type-C interfaces.

It integrates the STC8H chip, which can automatically convert voice data into serial or IIC data formats, simplifying the communication process with external host devices. A variety of connection cables are provided free of charge, allowing users to connect to MCU development boards and embedded host devices to enable communication and create their own DIY projects.

- Provides usage tutorials based on various development boards.

Provides development board information such as STM32, ESP32, MSPM0, Raspberry Pi, Jetson series development boards, RDK, etc. Also provides SDK files for ROS1 and ROS2 systems.

## 3. Working Principle

The module adopts a keyword wake-up mode. The user needs to speak the preset wake word to activate the voice interaction module first. After activation, voice recognition can be performed. The factory firmware default wake-up keyword is "你好，小犀" (Hello, Xiao Xi). If no voice is detected within 15 seconds, the module will enter sleep mode and must be woken up again for subsequent use.

When the CI1302 chip recognizes the corresponding voice entry, it sends it out via the serial port and IIC interface, along with feedback playback. The IIC chip stores the received voice commands and sends them out via the IIC slave protocol.

The module supports wake word modification, command word modification, and custom entries. You can learn how to operate these in the tutorials "Modifying Wake Words and Command Words" and "Custom Protocol Entry Creation".

## 4. Precautions

1. Use 5V voltage for power supply; exceeding 5V will damage the module.
2. The usage environment should be quiet; noisy environments will affect recognition performance.
3. When speaking entries, voice should be loud and not too fast. It is recommended to stay within 5 meters of the module.

## 5. Hardware Interface Description

![2](images/2.png)

| No. | Hardware Name         | Description                                                                 |
| --- | --------------------- | --------------------------------------------------------------------------- |
| 1   | Speaker               | Converts analog signals into sound                                         |
| 2   | Slide Switch          | Switches serial port mode for firmware flashing                            |
| 3   | Microphone            | Converts sound into analog signals                                         |
| 4   | RST Button            | Reset button                                                                |
| 5   | Power Indicator (Blue)| Stays on when power is normal                                               |
| 6   | Type-C Port           | Used for power supply and CI1302/STC8 firmware update and download          |
| 7   | Audio Amplifier Chip  | Converts digital signals into analog signals to drive the speaker           |
| 8   | CI1302 Chip           | High-performance voice recognition chip; recognizes voice and outputs signals |
| 9   | Reverse Polarity Protection | 5V/GND reverse connection protection                                 |
| 10  | IIC Interface         | Acts as slave for power supply and communication with host device           |
| 11  | Serial Interface      | External serial port provided; can control playback via protocol            |
| 12  | STC8H Chip            | Converts voice chip commands into IIC protocol commands and serial commands |
