[English](../../../en/06-multi-host/rdk-x5/README.md) | [Deutsch](../../../de/06-multi-host/rdk-x5/README.md) | [Español](../../../es/06-multi-host/rdk-x5/README.md) | [Français](../../../fr/06-multi-host/rdk-x5/README.md) | [Italiano](../../../it/06-multi-host/rdk-x5/README.md) | 日本語 | [한국어](../../../ko/06-multi-host/rdk-x5/README.md) | [Português (BR)](../../../pt-br/06-multi-host/rdk-x5/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/rdk-x5/README.md) | [简体中文](../../../zh-hans/06-multi-host/rdk-x5/README.md) | [繁體中文](../../../zh-hant/06-multi-host/rdk-x5/README.md)

# AI 音声対話モジュール - RDK X5（Python）ユーザーガイド

## 目次

1. [はじめに](#introduction)
2. [ハードウェア接続](#hardware-connection)
3. [環境セットアップ](#environment-setup)
4. [IIC 版の使用方法](#iic-version-usage)
5. [UART 版の使用方法](#uart-version-usage)
6. [FAQ](#faq)

---

## はじめに

本リポジトリは、RDK X5（Raspberry Pi）プラットフォーム向けに、AI 音声対話モジュールと通信するための Python サンプルコードを提供し、I2C と UART の両方の通信方式をサポートしています。

- **音声認識モジュール**：オフライン音声認識をサポートし、認識後にコマンド ID を出力します
- **読み上げ機能**：受動読み上げ、機能ワード読み上げ、コマンドワード読み上げをサポートします
- **通信プロトコル**：I2C アドレス 0x2A、UART ボーレート 115200
- **プログラミング言語**：Python 3

---

## ハードウェア接続

### 共通接続

| RDK X5 ピン | 音声モジュール | 説明 |
|------------|-------------|-------------|
| 5V (Pin 2/4) | 5V | 電源プラス |
| GND (Pin 6/9) | GND | 電源グラウンド |

> **重要**：すべてのデバイスが共通のグラウンドを共有していることを確認してください！

---

### I2C 版の接続

| RDK X5 ピン | 音声モジュール | 説明 |
|------------|-------------|-------------|
| SDA (GPIO3, Pin 3) | SDA | I2C データライン |
| SCL (GPIO5, Pin 5) | SCL | I2C クロックライン |

**注**：デフォルトで I2C バス 5 を使用します（BCM 番号）

---

### UART 版の接続

| RDK X5 ピン | 音声モジュール | 説明 |
|------------|-------------|-------------|
| GPIO14 (TXD, Pin 8) | RX | シリアル送信 |
| GPIO15 (RXD, Pin 10) | TX | シリアル受信 |

**注**：デフォルトで `/dev/ttyAMA0` シリアルデバイスを使用します

---

### Type-C ケーブル接続（UART の代替）

USB-TTL アダプタモジュールを使用する場合：

| RDK X5 | USB-TTL モジュール | 音声モジュール |
|--------|---------------|-------------|
| USB ポート | USB | - |
| - | RX | TX |
| - | TX | RX |
| GND | GND | GND |

**注**：この場合、シリアルデバイスは通常 `/dev/ttyUSB0` です

---

## 環境セットアップ

### 1. システム要件

- RDK X5（または Raspberry Pi 3/4/5）
- Ubuntu / Debian システム
- Python 3.7 以上

### 2. 依存関係のインストール

```bash
# Update packages
sudo apt update
sudo apt upgrade -y

# Install Python libraries
sudo apt install -y python3-pip python3-smbus i2c-tools

# Install pyserial
pip3 install pyserial
```

### 3. I2C インターフェースの有効化

```bash
# Open configuration tool
sudo raspi-config

# Select Interface Options → I2C → Enable
# Reboot to take effect
sudo reboot
```

### 4. シリアルインターフェースの有効化

```bash
# Open configuration tool
sudo raspi-config

# Select Interface Options → Serial
# Select: No (shell) → Yes (hardware serial port)
# Reboot to take effect
sudo reboot
```

### 5. ハードウェアインターフェースのテスト

```bash
# Test I2C device
sudo i2cdetect -y 5

# Test serial port
ls /dev/ttyAMA0
ls /dev/ttyUSB0  # If using USB-TTL
```

---

## IIC 版の使用方法

### 1. コードファイルの確認

```bash
cd IIC_Voice
ls -la
# Should see iic_voice.py
```

### 2. I2C バスの設定

`iic_voice.py` ファイルを編集し、必要に応じてパラメータを変更します：

```python
# I2C device address
DEVICE_ADDRESS = 0x2A

# Register address
REG_RESULT = 0xDA

# I2C bus number (modify according to actual connection)
bus = smbus.SMBus(5)  # I2C bus 5
```

### 3. プログラムの実行

```bash
# Make executable
chmod +x iic_voice.py

# Run (sudo required for I2C access)
sudo python3 iic_voice.py
```

### 4. テスト実行

正常に起動すると、次のように表示されます：

```
Speech Serial Opened! Baudrate=115200
```

音声モジュールにコマンドワードを話しかけると、対応する ID が表示されます：

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. プログラムの停止

`Ctrl + C` を押してプログラムを停止します：

```
Program terminated
```

---

## UART 版の使用方法

### 1. コードファイルの確認

```bash
cd UART_Voice
ls -la
# Should see uart_voice.py
```

### 2. シリアルポートの設定

`uart_voice.py` ファイルを編集し、シリアルデバイスを変更します：

```python
# UART direct connection (default)
SERIAL_PORT = '/dev/ttyAMA0'

# Or use USB-TTL
# SERIAL_PORT = '/dev/ttyUSB0'

# Baud rate
BAUD_RATE = 115200
```

### 3. プログラムの実行

```bash
# Make executable
chmod +x uart_voice.py

# Run (sudo required for serial port access)
sudo python3 uart_voice.py
```

### 4. テスト実行

正常に起動すると、次のように表示されます：

```
Speech Serial Opened! Baudrate=115200
```

音声モジュールにコマンドワードを話しかけると、対応する ID が表示されます：

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. プログラムの停止

`Ctrl + C` を押してプログラムを停止します

---

## FAQ

### Q1: I2C の操作権限が不足している

**A: ユーザーを I2C ユーザーグループに追加します：**
```bash
sudo usermod -aG i2c $USER
# Re-login to take effect
```
または `sudo` で実行します

---

### Q2: シリアルデバイスが見つからない

**A: 確認してください：**
1. シリアルポートが有効になっているか確認します（raspi-config）
2. デバイス名が正しいか確認します
   - UART 直接接続：`/dev/ttyAMA0`
   - USB-TTL：`/dev/ttyUSB0` または `/dev/ttyUSB1`
3. ハードウェア接続が正しいか確認します
4. シリアルポートが他のプログラムに占有されていないか確認します

```bash
# List available serial ports
ls /dev/tty* | grep tty
```

---

### Q3: スキャンで I2C デバイスが検出されない

**A: 確認してください：**
1. I2C が有効になっていることを確認します（raspi-config）
2. SDA/SCL が逆になっていないか確認します
3. 共通グラウンドが接続されているか確認します
4. デバイスの電源が入っているか確認します

```bash
# Scan I2C devices
sudo i2cdetect -y 5
```

0x2A が表示されれば、デバイス接続は正常です

---

### Q4: コマンド ID が 0 しか表示されない、または何も表示されない

**A: 正常な動作です：**
- 0 = 有効なコマンドが認識されていない
- ID は有効なコマンドワードを話したときにのみ出力されます
- まずモジュールをウェイクアップし、それからコマンドを話してください

---

### Q5: 認識精度が高くない

**A: 最適化の提案：**
- 静かな環境を確保し、背景ノイズが多すぎないようにします
- マイクから適切な距離を保ちます（10～50cm）
- 適度な速さで、はっきりと発音します

---

### Q6: シリアル通信が異常

**A: 確認してください：**
1. TX/RX は正しくクロス接続されていますか？（モジュール TX → RPi RX）
2. ボーレートは 115200 ですか
3. 共通グラウンドは接続されていますか
4. シリアルポートは他のプロセスに占有されていませんか

```bash
# Check serial port occupancy
sudo lsof /dev/ttyAMA0
```

---

## テクニカルサポート

問題が発生した場合は、以下を確認してください：
1. ハードウェア接続が正しい（共通グラウンドは非常に重要です！）
2. シリアルのボーレートが 115200
3. I2C アドレスが正しい（0x2A）
4. ハードウェアインターフェースにアクセスするための十分な権限がある

```bash
# Useful debugging commands
ls -l /dev/i2c*      # List I2C devices
ls -l /dev/ttyAMA0   # List serial device
groups                # List user group permissions
```
