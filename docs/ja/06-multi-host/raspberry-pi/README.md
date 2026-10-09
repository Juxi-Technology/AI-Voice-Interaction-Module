[English](../../../en/06-multi-host/raspberry-pi/README.md) | [Deutsch](../../../de/06-multi-host/raspberry-pi/README.md) | [Español](../../../es/06-multi-host/raspberry-pi/README.md) | [Français](../../../fr/06-multi-host/raspberry-pi/README.md) | [Italiano](../../../it/06-multi-host/raspberry-pi/README.md) | 日本語 | [한국어](../../../ko/06-multi-host/raspberry-pi/README.md) | [Português (BR)](../../../pt-br/06-multi-host/raspberry-pi/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/raspberry-pi/README.md) | [简体中文](../../../zh-hans/06-multi-host/raspberry-pi/README.md) | [繁體中文](../../../zh-hant/06-multi-host/raspberry-pi/README.md)

# Raspberry Pi 音声対話モジュール ユーザーガイド

## 依存関係のインストール

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## I2C インターフェースの有効化

```bash
sudo raspi-config
```

`Interface Options` -> `I2C` -> `Yes` を選択します

Raspberry Pi を再起動します

## IIC 版

### ファイルの場所
`IIC_Voice/iic_voice.py`

### 配線手順

| Raspberry Pi | 音声モジュール |
|--------------|--------------|
| GPIO2 (SDA) | SDA |
| GPIO3 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

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

### シリアルポートの有効化

`/boot/firmware/config.txt` または `/boot/config.txt` を編集し、次の設定を確認します：

```
enable_uart=1
dtoverlay=disable-bt
```

その後、Raspberry Pi を再起動します。

```bash
sudo reboot
```

### 配線手順

#### Type-C 直接接続の使用

Type-C で Raspberry Pi に直接接続する場合、`SERIAL_PORT = '/dev/ttyUSB0'` をコメント解除し、`SERIAL_PORT = '/dev/ttyAMA0'` をコメントアウトします

#### UART ピンの使用

| Raspberry Pi | 音声モジュール |
|--------------|--------------|
| GPIO14 (TXD) | RX |
| GPIO15 (RXD) | TX |
| GND | GND |
| 5V | 5V |

`SERIAL_PORT = '/dev/ttyUSB0'` をコメントアウトします

`SERIAL_PORT = '/dev/ttyAMA0'` をコメント解除します

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
