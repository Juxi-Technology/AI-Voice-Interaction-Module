[English](../../../en/06-multi-host/arduino/README.md) | [Deutsch](../../../de/06-multi-host/arduino/README.md) | [Español](../../../es/06-multi-host/arduino/README.md) | [Français](../../../fr/06-multi-host/arduino/README.md) | [Italiano](../../../it/06-multi-host/arduino/README.md) | 日本語 | [한국어](../../../ko/06-multi-host/arduino/README.md) | [Português (BR)](../../../pt-br/06-multi-host/arduino/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/arduino/README.md) | [简体中文](../../../zh-hans/06-multi-host/arduino/README.md) | [繁體中文](../../../zh-hant/06-multi-host/arduino/README.md)

# AI 音声対話モジュール - Arduino ユーザーガイド

## 目次

1. [はじめに](#introduction)
2. [ハードウェア接続](#hardware-connection)
3. [開発環境のセットアップ](#development-environment-setup)
4. [IIC 版の使用方法](#iic-version-usage)
5. [UART 版の使用方法](#uart-version-usage)
6. [FAQ](#faq)

---

## はじめに

本リポジトリは、AI 音声対話モジュールと通信するための Arduino プラットフォーム向けサンプルコードを提供し、I2C と UART の両方の通信方式をサポートしています。

- **音声認識モジュール**：オフライン音声認識をサポートし、認識後にコマンド ID を出力します
- **読み上げ機能**：受動読み上げ、機能ワード読み上げ、コマンドワード読み上げをサポートします
- **通信プロトコル**：I2C アドレス 0x2A、UART ボーレート 115200

---

## ハードウェア接続

### 共通接続

| Arduino ピン | 音声モジュール | 説明 |
|-------------|-------------|-------------|
| 5V | 5V | 電源プラス |
| GND | GND | 電源グラウンド |

---

### I2C 版の接続

| Arduino ピン | 音声モジュール | 説明 |
|-------------|-------------|-------------|
| A4 (SDA) | SDA | I2C データライン |
| A5 (SCL) | SCL | I2C クロックライン |

---

### UART 版の接続

| Arduino ピン | 音声モジュール | 説明 |
|-------------|-------------|-------------|
| D10 (RX) | TX | シリアル受信（ソフトウェアシリアル） |
| D11 (TX) | RX | シリアル送信（ソフトウェアシリアル） |

---

### シリアルデバッグ接続

| Arduino ピン | USB-TTL | 説明 |
|-------------|---------|-------------|
| TX (D1) | RX | デバッグ出力 |
| RX (D0) | TX | デバッグ入力（任意） |
| GND | GND | 共通グラウンド |

---

## 開発環境のセットアップ

### 1. Arduino IDE のインストール

- ダウンロード：https://www.arduino.cc/en/software
- 最新バージョンをインストールします

### 2. ボードサポートパッケージのインストール

- Arduino IDE を開きます
- ツール → ボード → ボードマネージャ
- お使いの Arduino ボードのサポートパッケージを検索してインストールします
- 推奨：Arduino Uno / Nano

---

## IIC 版の使用方法

### 1. プロジェクトを開く

- Arduino IDE で `IIC_Voice/IIC_Voice.ino` を開きます

### 2. コードをアップロード

- 正しいボードモデルを選択します（ツール → ボード）
- 正しいポートを選択します（ツール → ポート）
- アップロードボタン（→）をクリックします
- アップロードが完了するのを待ちます

### 3. テスト実行

1. シリアルモニタを開きます（ツール → シリアルモニタ）
2. ボーレートを **115200** に設定します
3. 正常に起動すると、次のように表示されます：

```
IIC Voice Module Initialized
```

4. 音声モジュールにコマンドワードを話しかけると、対応する ID が表示されます：

```
IIC Voice Module Initialized
ID: 1
ID: 4
ID: 10
```

### 4. コードの説明

```cpp
// Initialize I2C
IIC_Init();

// Read command ID
int commandId = IIC_ReadCommand();

// Set broadcast
IIC_SetCommandVoice(0x00);  // Command word broadcast
```

---

## UART 版の使用方法

### 1. プロジェクトを開く

- Arduino IDE で `UART_Voice/UART_Voice.ino` を開きます

### 2. コードをアップロード

- 正しいボードモデルを選択します
- 正しいポートを選択します
- アップロードボタンをクリックします
- アップロードが完了するのを待ちます

### 3. テスト実行

1. シリアルモニタを開きます
2. ボーレートを **115200** に設定します
3. 正常に起動すると、次のように表示されます：

```
UART Voice Module Initialized
```

4. 音声モジュールにコマンドワードを話しかけると、対応する ID が表示されます：

```
UART Voice Module Initialized
ID: 1
ID: 4
ID: 10
```

### 4. コードの説明

```cpp
// Initialize serial (Software Serial D10/D11)
UART_Init();

// Read command ID
int commandId = UART_ReadCommand();

// Set broadcast
UART_SetCommandVoice(0x00);  // Command word broadcast
```

---

## FAQ

### Q1: シリアルモニタに出力がない

**A: 以下を確認してください：**
- シリアルのボーレートが 115200 かどうかを確認します
- 正しいポートが選択されているか確認します
- TX/RX が逆になっていないか確認します
- GND が接続されているか確認します

---

### Q2: I2C 版で "IIC Read Error" が表示される

**A: I2C 接続を確認してください：**
- SDA/SCL が逆になっていないか確認します
- デバイスアドレスが正しいか確認します（0x2A）
- GND が接続されているか確認します

---

### Q3: コマンド ID が 0 または 255 しか表示されない

**A: 正常な動作です：**
- 0 = 有効なコマンドが認識されていない
- 255 = 新しいデータがない
- 有効な ID は正常に認識された後にのみ出力されます

---

### Q4: 認識精度が高くない

**A: 最適化の提案：**
- 静かな環境を確保し、背景ノイズが多すぎないようにします
- マイクから適切な距離を保ちます（10～50cm）
- 適度な速さで、はっきりと発音します

---

### Q5: UART 版でデータを受信できない

**A: 確認してください：**
- 音声モジュールの TX が Arduino の D10（RX）に接続されていることを確認します
- 音声モジュールの RX が Arduino の D11（TX）に接続されていることを確認します
- ボーレートが 115200 かどうかを確認します

---

## テクニカルサポート

問題が発生した場合は、以下を確認してください：
1. ハードウェア接続が正しい
2. シリアルのボーレートが一致している
3. I2C アドレスが正しい
4. GND が接続されている（非常に重要です！）
