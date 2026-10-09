[English](../../../en/06-multi-host/raspberry-pi/README.md) | [Deutsch](../../../de/06-multi-host/raspberry-pi/README.md) | [Español](../../../es/06-multi-host/raspberry-pi/README.md) | [Français](../../../fr/06-multi-host/raspberry-pi/README.md) | [Italiano](../../../it/06-multi-host/raspberry-pi/README.md) | [日本語](../../../ja/06-multi-host/raspberry-pi/README.md) | [한국어](../../../ko/06-multi-host/raspberry-pi/README.md) | [Português (BR)](../../../pt-br/06-multi-host/raspberry-pi/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/raspberry-pi/README.md) | [简体中文](../../../zh-hans/06-multi-host/raspberry-pi/README.md) | 繁體中文

# 樹莓派語音互動模組使用說明

## 安裝依賴

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## 啟用I2C

```bash
sudo raspi-config
```
選擇 `Interface Options` -> `I2C` -> `Yes`

重啟樹莓派

## IIC版本

### 檔案位置
`IIC_Voice/iic_voice.py

### 接線說明
| 樹莓派 | 語音模組 |
|-------|----------|
| GPIO2 (SDA) | SDA |
| GPIO3 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

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
`UART_Voice/uart_voice.py

### 啟用序列埠
編輯 `/boot/firmware/config.txt` 或 `/boot/config.txt`，確保以下配置：
```
enable_uart=1
dtoverlay=disable-bt
```

然後重啟樹莓派。

```
sudo reboot
```

### 接線說明

Type直連樹莓派時，取消註解SERIAL_PORT = '/dev/ttyUSB0'，註解掉SERIAL_PORT = '/dev/ttyAMA0'

![](C:\Users\qq141\AppData\Roaming\Typora\typora-user-images\image-20260701162405794.png)

透過UART針腳連接樹莓派

| 樹莓派 | 語音模組 |
|-------|----------|
| GPIO14 (TXD) | RX |
| GPIO15 (RXD) | TX |
| GND | GND |
| 5V | 5V |

註解掉SERIAL_PORT = '/dev/ttyUSB0'
取消註解SERIAL_PORT = '/dev/ttyAMA0'

![](C:\Users\qq141\AppData\Roaming\Typora\typora-user-images\image-20260701162229241.png)

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
