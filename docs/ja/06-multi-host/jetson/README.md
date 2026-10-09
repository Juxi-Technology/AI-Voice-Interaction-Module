[English](../../../en/06-multi-host/jetson/README.md) | [Deutsch](../../../de/06-multi-host/jetson/README.md) | [Español](../../../es/06-multi-host/jetson/README.md) | [Français](../../../fr/06-multi-host/jetson/README.md) | [Italiano](../../../it/06-multi-host/jetson/README.md) | 日本語 | [한국어](../../../ko/06-multi-host/jetson/README.md) | [Português (BR)](../../../pt-br/06-multi-host/jetson/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/jetson/README.md) | [简体中文](../../../zh-hans/06-multi-host/jetson/README.md) | [繁體中文](../../../zh-hant/06-multi-host/jetson/README.md)

# Jetson 音声対話モジュール ユーザーガイド

## 依存関係のインストール

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## ユーザーグループの確認

```bash
sudo usermod -aG i2c $USER
sudo usermod -aG dialout $USER
```

ログアウトして再度ログインすると、変更が反映されます。

## IIC 版

### ファイルの場所
`IIC_Voice/iic_voice.py`

### 配線手順

| Jetson | 音声モジュール |
|--------|--------------|
| Pin 27 (I2C1 SDA) | SDA |
| Pin 28 (I2C1 SCL) | SCL |
| Pin 6 (GND) | GND |
| Pin 4 (5V) | 5V |

### I2C デバイスの確認

```bash
sudo i2cdetect -y -r 1
```

アドレス 0x2A が表示されるはずです

### 実行

```bash
cd IIC_Voice
python3 iic_voice.py
```

### 出力形式

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## UART 版

### ファイルの場所
`UART_Voice/uart_voice.py`

### UART ピンによる接続

UART ピンでモジュールを Jetson に接続する場合、`SERIAL_PORT = '/dev/ttyUSB0'` をコメントアウトし、`SERIAL_PORT = '/dev/ttyTHS1'` をコメント解除します

#### 配線手順

| Jetson | 音声モジュール |
|--------|--------------|
| Pin 8 (UART1 TX) | RX |
| Pin 10 (UART1 RX) | TX |
| Pin 6 (GND) | GND |
| Pin 4 (5V) | 5V |

### シリアルポートの確認

```bash
ls /dev/ttyTHS*
```

### 実行

```bash
cd UART_Voice
python3 uart_voice.py
```

### 出力形式

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

### Type-C ケーブルによる接続

Type-C ケーブルでモジュールを Jetson に接続する場合、`SERIAL_PORT = '/dev/ttyUSB0'` をコメント解除し、`SERIAL_PORT = '/dev/ttyTHS1'` をコメントアウトします

### シリアルポートの確認

```bash
ls /dev/ttyUSB*
```

### 実行

```bash
cd UART_Voice
python3 uart_voice.py
```

### 出力形式

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## FAQ

### I2C の権限の問題

```bash
sudo chmod 666 /dev/i2c-1
```

### シリアルポートが使用中

シリアルポートを開けない場合は、他のサービスに占有されていないか確認してください：

```bash
sudo systemctl stop nvgetty
sudo systemctl disable nvgetty
```

## プロトコル説明

### UART プロトコル

| バイト | 内容 |
|------|---------|
| 1 | 0xFE（フレームヘッダ） |
| 2 | 0xEF（フレームヘッダ） |
| 3 | 機能ワード ID |
| 4 | コマンドワード ID |
| 5 | 0xEE（終了フレーム） |

### IIC プロトコル

- デバイスアドレス：0x2A
- 読み取りレジスタ：0xDA（1 バイト読み取り）
  - 0x00：未認識
  - その他：コマンドワード ID
