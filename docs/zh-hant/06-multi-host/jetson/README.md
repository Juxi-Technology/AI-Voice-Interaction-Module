[English](../../../en/06-multi-host/jetson/README.md) | [Deutsch](../../../de/06-multi-host/jetson/README.md) | [Español](../../../es/06-multi-host/jetson/README.md) | [Français](../../../fr/06-multi-host/jetson/README.md) | [Italiano](../../../it/06-multi-host/jetson/README.md) | [日本語](../../../ja/06-multi-host/jetson/README.md) | [한국어](../../../ko/06-multi-host/jetson/README.md) | [Português (BR)](../../../pt-br/06-multi-host/jetson/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/jetson/README.md) | [简体中文](../../../zh-hans/06-multi-host/jetson/README.md) | 繁體中文

# Jetson語音互動模組使用說明

## 安裝依賴

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## 檢查使用者群組

```bash
sudo usermod -aG i2c $USER
sudo usermod -aG dialout $USER
```
登出並重新登入生效。

## IIC版本

### 檔案位置
`IIC_Voice/iic_voice.py`

### 接線說明
| Jetson | 語音模組 |
|--------|----------|
| Pin 27 (I2C1 SDA) | SDA |
| Pin 28 (I2C1 SCL) | SCL |
| Pin 6 (GND) | GND |
| Pin 4 (5V) | 5V |

### 檢查I2C裝置
```bash
sudo i2cdetect -y -r 1
```
應能看到位址 0x2A

### 執行
```bash
cd IIC_Voice
python3 iic_voice.py
```

### 輸出格式
```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## UART版本

### 檔案位置
`UART_Voice/uart_voice.py`

模組透過UART針腳連接到Jetson，註解掉SERIAL_PORT = '/dev/ttyUSB0'，取消註解SERIAL_PORT = '/dev/ttyTHS1'

![image-20260701185853347](C:\Users\qq141\AppData\Roaming\Typora\typora-user-images\image-20260701185853347.png)

### 接線說明

| Jetson | 語音模組 |
|--------|----------|
| Pin 8 (UART1 TX) | RX |
| Pin 10 (UART1 RX) | TX |
| Pin 6 (GND) | GND |
| Pin 4 (5V) | 5V |

### 檢查序列埠
```bash
ls /dev/ttyTHS*
```

### 執行
```bash
cd UART_Voice
python3 uart_voice.py
```

### 輸出格式
```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

模組透過Type傳輸線連接到Jetson，取消註解SERIAL_PORT = '/dev/ttyUSB0'，註解掉SERIAL_PORT = '/dev/ttyTHS1'

![image-20260701185812787](C:\Users\qq141\AppData\Roaming\Typora\typora-user-images\image-20260701185812787.png)

### 檢查序列埠

```bash
ls /dev/ttyUSB*
```

### 執行

```bash
cd UART_Voice
python3 uart_voice.py
```

### 輸出格式

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## 常見問題

### I2C權限問題
```bash
sudo chmod 666 /dev/i2c-1
```

### 序列埠被佔用
如果序列埠無法打開，請檢查是否被其他服務佔用：
```bash
sudo systemctl stop nvgetty
sudo systemctl disable nvgetty
```

## 協定說明

### UART協定
| 位元組 | 內容 |
|------|------|
| 1 | 0xFE (幀頭) |
| 2 | 0xEF (幀頭) |
| 3 | 功能詞ID |
| 4 | 命令詞ID |
| 5 | 0xEE (結束幀) |

### IIC協定
- 裝置位址: 0x2A
- 讀取暫存器: 0xDA (讀取1位元組)
  - 0x00: 未辨識
  - 其他: 命令詞ID
