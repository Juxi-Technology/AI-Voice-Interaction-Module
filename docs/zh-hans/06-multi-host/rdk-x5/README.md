[English](../../../en/06-multi-host/rdk-x5/README.md) | [Deutsch](../../../de/06-multi-host/rdk-x5/README.md) | [Español](../../../es/06-multi-host/rdk-x5/README.md) | [Français](../../../fr/06-multi-host/rdk-x5/README.md) | [Italiano](../../../it/06-multi-host/rdk-x5/README.md) | [日本語](../../../ja/06-multi-host/rdk-x5/README.md) | [한국어](../../../ko/06-multi-host/rdk-x5/README.md) | [Português (BR)](../../../pt-br/06-multi-host/rdk-x5/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/rdk-x5/README.md) | 简体中文 | [繁體中文](../../../zh-hant/06-multi-host/rdk-x5/README.md)

# AI 语音交互模块 - RDK X5 (Python) 使用教程

## 目录

1. [简介](#简介)
2. [硬件连接](#硬件连接)
3. [环境配置](#环境配置)
4. [IIC 版本使用](#iic-版本使用)
5. [UART 版本使用](#uart-版本使用)
6. [常见问题](#常见问题)

---

## 简介

本仓库提供了 RDK X5（Raspberry Pi）平台与 AI 语音交互模块通信的 Python 示例代码，支持 I2C 和 UART 两种通信方式。

- **语音识别模块**：支持离线语音识别，识别后输出命令ID
- **播报功能**：支持被动播报、功能词播报、命令词播报
- **通信协议**：I2C 地址 0x2A，UART 波特率 115200
- **编程语言**：Python 3

---

## 硬件连接

### 通用连接

| RDK X5 引脚 | 语音模块 | 说明 |
|------------|---------|------|
| 5V (Pin 2/4) | 5V | 电源正极 |
| GND (Pin 6/9) | GND | 电源负极 |

> **重要提示**：确保所有设备共地！

---

### I2C 版本连接

| RDK X5 引脚 | 语音模块 | 说明 |
|------------|---------|------|
| SDA (GPIO3, Pin 3) | SDA | I2C 数据线 |
| SCL (GPIO5, Pin 5) | SCL | I2C 时钟线 |

**注意**：默认使用 I2C 总线 5（BCM 编号）

---

### UART 版本连接

| RDK X5 引脚 | 语音模块 | 说明 |
|------------|---------|------|
| GPIO14 (TXD, Pin 8) | RX | 串口发送 |
| GPIO15 (RXD, Pin 10) | TX | 串口接收 |

**注意**：默认使用 `/dev/ttyAMA0` 串口设备

---

### Type-C 数据线连接（UART 备选）

如果使用 USB-TTL 转接模块：

| RDK X5 | USB-TTL 模块 | 语音模块 |
|--------|------------|---------|
| USB 端口 | USB | - |
| - | RX | TX |
| - | TX | RX |
| GND | GND | GND |

**注意**：此时串口设备通常为 `/dev/ttyUSB0`

---

## 环境配置

### 1. 系统要求

- RDK X5（或 Raspberry Pi 3/4/5）
- Ubuntu / Debian 系统
- Python 3.7+

### 2. 安装依赖包

```bash
# 更新软件包
sudo apt update
sudo apt upgrade -y

# 安装 Python 库
sudo apt install -y python3-pip python3-smbus i2c-tools

# 安装 pyserial
pip3 install pyserial
```

### 3. 启用 I2C 接口

```bash
# 打开配置工具
sudo raspi-config

# 选择 Interface Options → I2C → Enable
# 重启生效
sudo reboot
```

### 4. 启用串口接口

```bash
# 打开配置工具
sudo raspi-config

# 选择 Interface Options → Serial
# Select: No (shell) → Yes (hardware serial port)
# 重启生效
sudo reboot
```

### 5. 测试硬件接口

```bash
# 测试 I2C 设备
sudo i2cdetect -y 5

# 测试串口
ls /dev/ttyAMA0
ls /dev/ttyUSB0  # 如果用 USB-TTL
```

---

## IIC 版本使用

### 1. 检查代码文件

```bash
cd IIC_Voice
ls -la
# 应该看到 iic_voice.py
```

### 2. 配置 I2C 总线

编辑 `iic_voice.py` 文件，修改需要的参数：

```python
# I2C 设备地址
DEVICE_ADDRESS = 0x2A

# 寄存器地址
REG_RESULT = 0xDA

# I2C 总线编号（根据实际连接修改）
bus = smbus.SMBus(5)  # I2C 总线 5
```

### 3. 运行程序

```bash
# 赋予执行权限
chmod +x iic_voice.py

# 运行（需要 sudo 权限访问 I2C）
sudo python3 iic_voice.py
```

### 4. 运行测试

正常启动后会显示：

```
Speech Serial Opened! Baudrate=115200
```

对语音模块说出命令词，会显示对应的 ID：

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. 停止程序

按 `Ctrl + C` 停止程序：

```
Program terminated
```

---

## UART 版本使用

### 1. 检查代码文件

```bash
cd UART_Voice
ls -la
# 应该看到 uart_voice.py
```

### 2. 配置串口设备

编辑 `uart_voice.py` 文件，修改串口设备：

```python
# UART 直连（默认）
SERIAL_PORT = '/dev/ttyAMA0'

# 或者使用 USB-TTL
# SERIAL_PORT = '/dev/ttyUSB0'

# 波特率
BAUD_RATE = 115200
```

### 3. 运行程序

```bash
# 赋予执行权限
chmod +x uart_voice.py

# 运行（需要 sudo 权限访问串口）
sudo python3 uart_voice.py
```

### 4. 运行测试

正常启动后会显示：

```
Speech Serial Opened! Baudrate=115200
```

对语音模块说出命令词，会显示对应的 ID：

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. 停止程序

按 `Ctrl + C` 停止程序

---

## 常见问题

### Q1: I2C 操作权限不足

**A: 添加用户到 I2C 用户组：**
```bash
sudo usermod -aG i2c $USER
# 重新登录生效
```
或者使用 `sudo` 运行程序

---

### Q2: 串口设备找不到

**A: 检查：**
1. 检查串口是否启用（raspi-config）
2. 检查设备名称是否正确
   - UART 直连：`/dev/ttyAMA0`
   - USB-TTL：`/dev/ttyUSB0` 或 `/dev/ttyUSB1`
3. 检查硬件连接是否正确
4. 检查串口是否被其他程序占用

```bash
# 查看可用串口
ls /dev/tty* | grep tty
```

---

### Q3: I2C 设备扫描不到

**A: 检查：**
1. 确认 I2C 已启用（raspi-config）
2. 检查 SDA/SCL 是否接反
3. 检查是否共地
4. 检查设备是否上电

```bash
# 扫描 I2C 设备
sudo i2cdetect -y 5
```

如果看到 0x2A，说明设备连接正常

---

### Q4: 命令 ID 只显示 0 或不显示

**A: 正常现象：**
- 0 = 未识别到有效命令
- 只有说出有效命令词才会输出 ID
- 先唤醒模块，再说命令

---

### Q5: 识别准确率不高

**A: 优化建议：**
- 确保环境安静，背景噪音不要太大
- 离麦克风距离适中（10-50cm）
- 语速适中，发音清晰

---

### Q6: 串口通信异常

**A: 检查：**
1. TX/RX 是否交叉连接（模块 TX → RPi RX）
2. 波特率是否为 115200
3. 是否共地
4. 串口是否被其他进程占用

```bash
# 检查串口占用
sudo lsof /dev/ttyAMA0
```

---

## 技术支持

如有问题，请检查：
1. 硬件接线是否正确（共地非常重要！）
2. 串口波特率是否为 115200
3. I2C 地址是否正确（0x2A）
4. 是否有足够的权限访问硬件接口

```bash
# 常用调试命令
ls -l /dev/i2c*      # 查看 I2C 设备
ls -l /dev/ttyAMA0   # 查看串口设备
groups                # 查看用户组权限
```
