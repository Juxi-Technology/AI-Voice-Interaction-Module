[English](../../../en/06-multi-host/rdk-x5/README.md) | [Deutsch](../../../de/06-multi-host/rdk-x5/README.md) | [Español](../../../es/06-multi-host/rdk-x5/README.md) | [Français](../../../fr/06-multi-host/rdk-x5/README.md) | [Italiano](../../../it/06-multi-host/rdk-x5/README.md) | [日本語](../../../ja/06-multi-host/rdk-x5/README.md) | [한국어](../../../ko/06-multi-host/rdk-x5/README.md) | [Português (BR)](../../../pt-br/06-multi-host/rdk-x5/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/rdk-x5/README.md) | [简体中文](../../../zh-hans/06-multi-host/rdk-x5/README.md) | 繁體中文

# AI 語音互動模組 - RDK X5 (Python) 使用教學

## 目錄

1. [簡介](#簡介)
2. [硬體連接](#硬體連接)
3. [環境配置](#環境配置)
4. [IIC 版本使用](#iic-版本使用)
5. [UART 版本使用](#uart-版本使用)
6. [常見問題](#常見問題)

---

## 簡介

本儲存庫提供了 RDK X5（Raspberry Pi）平台與 AI 語音互動模組通訊的 Python 範例程式碼，支援 I2C 和 UART 兩種通訊方式。

- **語音辨識模組**：支援離線語音辨識，辨識後輸出命令ID
- **播報功能**：支援被動播報、功能詞播報、命令詞播報
- **通訊協定**：I2C 位址 0x2A，UART 鮑率 115200
- **程式語言**：Python 3

---

## 硬體連接

### 通用連接

| RDK X5 腳位 | 語音模組 | 說明 |
|------------|---------|------|
| 5V (Pin 2/4) | 5V | 電源正極 |
| GND (Pin 6/9) | GND | 電源負極 |

> **重要提示**：確保所有裝置共地！

---

### I2C 版本連接

| RDK X5 腳位 | 語音模組 | 說明 |
|------------|---------|------|
| SDA (GPIO3, Pin 3) | SDA | I2C 資料線 |
| SCL (GPIO5, Pin 5) | SCL | I2C 時鐘線 |

**注意**：預設使用 I2C 匯流排 5（BCM 編號）

---

### UART 版本連接

| RDK X5 腳位 | 語音模組 | 說明 |
|------------|---------|------|
| GPIO14 (TXD, Pin 8) | RX | 序列埠發送 |
| GPIO15 (RXD, Pin 10) | TX | 序列埠接收 |

**注意**：預設使用 `/dev/ttyAMA0` 序列埠裝置

---

### Type-C 傳輸線連接（UART 備選）

如果使用 USB-TTL 轉接模組：

| RDK X5 | USB-TTL 模組 | 語音模組 |
|--------|------------|---------|
| USB 埠 | USB | - |
| - | RX | TX |
| - | TX | RX |
| GND | GND | GND |

**注意**：此時序列埠裝置通常為 `/dev/ttyUSB0`

---

## 環境配置

### 1. 系統要求

- RDK X5（或 Raspberry Pi 3/4/5）
- Ubuntu / Debian 系統
- Python 3.7+

### 2. 安裝依賴套件

```bash
# 更新软件包
sudo apt update
sudo apt upgrade -y

# 安装 Python 库
sudo apt install -y python3-pip python3-smbus i2c-tools

# 安装 pyserial
pip3 install pyserial
```

### 3. 啟用 I2C 介面

```bash
# 打开配置工具
sudo raspi-config

# 选择 Interface Options → I2C → Enable
# 重启生效
sudo reboot
```

### 4. 啟用序列埠介面

```bash
# 打开配置工具
sudo raspi-config

# 选择 Interface Options → Serial
# Select: No (shell) → Yes (hardware serial port)
# 重启生效
sudo reboot
```

### 5. 測試硬體介面

```bash
# 测试 I2C 设备
sudo i2cdetect -y 5

# 测试串口
ls /dev/ttyAMA0
ls /dev/ttyUSB0  # 如果用 USB-TTL
```

---

## IIC 版本使用

### 1. 檢查程式碼檔案

```bash
cd IIC_Voice
ls -la
# 应该看到 iic_voice.py
```

### 2. 配置 I2C 匯流排

編輯 `iic_voice.py` 檔案，修改需要的參數：

```python
# I2C 设备地址
DEVICE_ADDRESS = 0x2A

# 寄存器地址
REG_RESULT = 0xDA

# I2C 总线编号（根据实际连接修改）
bus = smbus.SMBus(5)  # I2C 总线 5
```

### 3. 執行程式

```bash
# 赋予执行权限
chmod +x iic_voice.py

# 运行（需要 sudo 权限访问 I2C）
sudo python3 iic_voice.py
```

### 4. 執行測試

正常啟動後會顯示：

```
Speech Serial Opened! Baudrate=115200
```

對語音模組說出命令詞，會顯示對應的 ID：

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. 停止程式

按 `Ctrl + C` 停止程式：

```
Program terminated
```

---

## UART 版本使用

### 1. 檢查程式碼檔案

```bash
cd UART_Voice
ls -la
# 应该看到 uart_voice.py
```

### 2. 配置序列埠裝置

編輯 `uart_voice.py` 檔案，修改序列埠裝置：

```python
# UART 直连（默认）
SERIAL_PORT = '/dev/ttyAMA0'

# 或者使用 USB-TTL
# SERIAL_PORT = '/dev/ttyUSB0'

# 波特率
BAUD_RATE = 115200
```

### 3. 執行程式

```bash
# 赋予执行权限
chmod +x uart_voice.py

# 运行（需要 sudo 权限访问串口）
sudo python3 uart_voice.py
```

### 4. 執行測試

正常啟動後會顯示：

```
Speech Serial Opened! Baudrate=115200
```

對語音模組說出命令詞，會顯示對應的 ID：

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. 停止程式

按 `Ctrl + C` 停止程式

---

## 常見問題

### Q1: I2C 操作權限不足

**A: 新增使用者到 I2C 群組：**
```bash
sudo usermod -aG i2c $USER
# 重新登录生效
```
或者使用 `sudo` 執行程式

---

### Q2: 序列埠裝置找不到

**A: 檢查：**
1. 檢查序列埠是否啟用（raspi-config）
2. 檢查裝置名稱是否正確
   - UART 直連：`/dev/ttyAMA0`
   - USB-TTL：`/dev/ttyUSB0` 或 `/dev/ttyUSB1`
3. 檢查硬體連接是否正確
4. 檢查序列埠是否被其他程式佔用

```bash
# 查看可用串口
ls /dev/tty* | grep tty
```

---

### Q3: I2C 裝置掃描不到

**A: 檢查：**
1. 確認 I2C 已啟用（raspi-config）
2. 檢查 SDA/SCL 是否接反
3. 檢查是否共地
4. 檢查裝置是否上電

```bash
# 扫描 I2C 设备
sudo i2cdetect -y 5
```

如果看到 0x2A，說明裝置連接正常

---

### Q4: 命令 ID 只顯示 0 或不顯示

**A: 正常現象：**
- 0 = 未辨識到有效命令
- 只有說出有效命令詞才會輸出 ID
- 先喚醒模組，再說命令

---

### Q5: 辨識準確率不高

**A: 最佳化建議：**
- 確保環境安靜，背景噪音不要太大
- 離麥克風距離適中（10-50cm）
- 語速適中，發音清晰

---

### Q6: 序列埠通訊異常

**A: 檢查：**
1. TX/RX 是否交叉連接（模組 TX → RPi RX）
2. 鮑率是否為 115200
3. 是否共地
4. 序列埠是否被其他行程佔用

```bash
# 检查串口占用
sudo lsof /dev/ttyAMA0
```

---

## 技術支援

如有問題，請檢查：
1. 硬體接線是否正確（共地非常重要！）
2. 序列埠鮑率是否為 115200
3. I2C 位址是否正確（0x2A）
4. 是否有足夠的權限存取硬體介面

```bash
# 常用调试命令
ls -l /dev/i2c*      # 查看 I2C 设备
ls -l /dev/ttyAMA0   # 查看串口设备
groups                # 查看用户组权限
```
