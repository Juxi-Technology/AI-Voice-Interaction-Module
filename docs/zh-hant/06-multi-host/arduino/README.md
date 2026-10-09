[English](../../../en/06-multi-host/arduino/README.md) | [Deutsch](../../../de/06-multi-host/arduino/README.md) | [Español](../../../es/06-multi-host/arduino/README.md) | [Français](../../../fr/06-multi-host/arduino/README.md) | [Italiano](../../../it/06-multi-host/arduino/README.md) | [日本語](../../../ja/06-multi-host/arduino/README.md) | [한국어](../../../ko/06-multi-host/arduino/README.md) | [Português (BR)](../../../pt-br/06-multi-host/arduino/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/arduino/README.md) | [简体中文](../../../zh-hans/06-multi-host/arduino/README.md) | 繁體中文

# AI 語音互動模組 - Arduino 使用教學

## 目錄

1. [簡介](#簡介)
2. [硬體連接](#硬體連接)
3. [開發環境配置](#開發環境配置)
4. [IIC 版本使用](#iic-版本使用)
5. [UART 版本使用](#uart-版本使用)
6. [常見問題](#常見問題)

---

## 簡介

本儲存庫提供了 Arduino 平台與 AI 語音互動模組通訊的範例程式碼，支援 I2C 和 UART 兩種通訊方式。

- **語音辨識模組**：支援離線語音辨識，辨識後輸出命令ID
- **播報功能**：支援被動播報、功能詞播報、命令詞播報
- **通訊協定**：I2C 位址 0x2A，UART 鮑率 115200

---

## 硬體連接

### 通用連接

| Arduino 腳位 | 語音模組 | 說明 |
|-------------|---------|------|
| 5V | 5V | 電源正極 |
| GND | GND | 電源負極 |

---

### I2C 版本連接

| Arduino 腳位 | 語音模組 | 說明 |
|-------------|---------|------|
| A4 (SDA) | SDA | I2C 資料線 |
| A5 (SCL) | SCL | I2C 時鐘線 |

---

### UART 版本連接

| Arduino 腳位 | 語音模組 | 說明 |
|-------------|---------|------|
| D10 (RX) | TX | 序列埠接收（軟序列埠） |
| D11 (TX) | RX | 序列埠發送（軟序列埠） |

---

### 序列埠除錯連接

| Arduino 腳位 | USB-TTL | 說明 |
|-------------|---------|------|
| TX (D1) | RX | 除錯輸出 |
| RX (D0) | TX | 除錯輸入（可選） |
| GND | GND | 共地 |

---

## 開發環境配置

### 1. 安裝 Arduino IDE

- 下載位址：https://www.arduino.cc/en/software
- 安裝最新版本即可

### 2. 安裝板級支援套件

- 打開 Arduino IDE
- 工具 → 開發板 → 開發板管理器
- 搜尋並安裝對應你的 Arduino 型號的支援套件
- 推薦：Arduino Uno / Nano

---

## IIC 版本使用

### 1. 打開工程

- 在 Arduino IDE 中打開 `IIC_Voice/IIC_Voice.ino`

### 2. 上傳程式碼

- 選擇正確的開發板型號（工具 → 開發板）
- 選擇正確的連接埠號（工具 → 連接埠）
- 點擊上傳按鈕（→）
- 等待上傳完成

### 3. 執行測試

1. 打開序列埠監視器（工具 → 序列埠監視器）
2. 設定鮑率為 **115200**
3. 正常啟動後會顯示：

```
IIC Voice Module Initialized
```

4. 對語音模組說出命令詞，會顯示對應的 ID：

```
IIC Voice Module Initialized
ID: 1
ID: 4
ID: 10
```

### 4. 程式碼說明

```cpp
// 初始化 I2C
IIC_Init();

// 读取命令 ID
int commandId = IIC_ReadCommand();

// 设置播报
IIC_SetCommandVoice(0x00);  // 命令词播报
```

---

## UART 版本使用

### 1. 打開工程

- 在 Arduino IDE 中打開 `UART_Voice/UART_Voice.ino`

### 2. 上傳程式碼

- 選擇正確的開發板型號
- 選擇正確的連接埠號
- 點擊上傳按鈕
- 等待上傳完成

### 3. 執行測試

1. 打開序列埠監視器
2. 設定鮑率為 **115200**
3. 正常啟動後會顯示：

```
UART Voice Module Initialized
```

4. 對語音模組說出命令詞，會顯示對應的 ID：

```
UART Voice Module Initialized
ID: 1
ID: 4
ID: 10
```

### 4. 程式碼說明

```cpp
// 初始化串口（软串口 D10/D11）
UART_Init();

// 读取命令 ID
int commandId = UART_ReadCommand();

// 设置播报
UART_SetCommandVoice(0x00);  // 命令词播报
```

---

## 常見問題

### Q1: 序列埠監視器沒有任何輸出

**A: 檢查以下幾點：**
- 檢查序列埠鮑率是否為 115200
- 檢查是否選擇了正確的連接埠
- 檢查 TX/RX 是否接反
- 檢查 GND 是否共地

### Q2: I2C 版本顯示 "IIC Read Error"

**A: 檢查 I2C 連接：**
- 檢查 SDA/SCL 是否接反
- 檢查裝置位址是否正確（0x2A）
- 檢查是否共地

### Q3: 命令 ID 只顯示 0 或 255

**A: 正常現象：**
- 0 = 未辨識到有效命令
- 255 = 無新資料
- 正常辨識後才會輸出有效 ID

### Q4: 辨識準確率不高

**A: 最佳化建議：**
- 確保環境安靜，背景噪音不要太大
- 離麥克風距離適中（10-50cm）
- 語速適中，發音清晰

### Q5: UART 版本接收不到資料

**A: 檢查：**
- 確認語音模組 TX 接 Arduino D10 (RX)
- 確認語音模組 RX 接 Arduino D11 (TX)
- 檢查鮑率是否為 115200

---

## 技術支援

如有問題，請檢查：
1. 硬體接線是否正確
2. 序列埠鮑率是否相符
3. I2C 位址是否正確
4. 是否共地（非常重要！）
