[English](../../../../en/06-multi-host/arduino/uart/README.md) | [Deutsch](../../../../de/06-multi-host/arduino/uart/README.md) | [Español](../../../../es/06-multi-host/arduino/uart/README.md) | [Français](../../../../fr/06-multi-host/arduino/uart/README.md) | [Italiano](../../../../it/06-multi-host/arduino/uart/README.md) | 日本語 | [한국어](../../../../ko/06-multi-host/arduino/uart/README.md) | [Português (BR)](../../../../pt-br/06-multi-host/arduino/uart/README.md) | [Português (PT)](../../../../pt-pt/06-multi-host/arduino/uart/README.md) | [简体中文](../../../../zh-hans/06-multi-host/arduino/uart/README.md) | [繁體中文](../../../../zh-hant/06-multi-host/arduino/uart/README.md)

# UART 音声モジュール BSP 版チュートリアル

## 📁 ファイル構成

```
uart/
├── uart.ino    # 主程序
├── bsp_uart.hpp         # 头文件（协议帧和函数声明）
├── bsp_uart.cpp         # 实现文件
└── README.md              # 本教程
```

---

## 🔌 ハードウェア接続

### 音声モジュールへの接続
| Arduino | 音声モジュール |
|---------|----------|
| D10 (RX) | TX |
| D11 (TX) | RX |
| GND | GND |
| 5V | 5V |

> 💡 **注意：** RX と TX はクロス接続する必要があります！

---

## 🔧 コンパイルとアップロード

### ステップ 1：Arduino IDE を開く
1. `UART_Voice.ino` ファイルを開きます
2. ボードモデルを選択します（例：Arduino Uno）
3. 対応するシリアルポートを選択します

### ステップ 2：コンパイルとアップロード
1. ✔️ ボタンをクリックしてコンパイルします
2. ➡️ ボタンをクリックしてボードにアップロードします

---

## 📡 シリアルテスト

### Arduino IDE でシリアルモニタを開く
- ボーレート：**115200**
- 行末記号：**None**

### 期待される出力

電源投入後、次のように表示されます：
```
UART Voice Module Initialized
```

ウェイクワードとコマンドワードをモジュールに話しかけると、対応する ID が出力されます：
```
ID: 1
ID: 2
ID: 10
```

---

## 📚 プロトコルフレーム形式

| バイト | 内容 | 説明 |
|------|------|------|
| 1 | 0xFE | フレームヘッダ 1 |
| 2 | 0xEF | フレームヘッダ 2 |
| 3 | 機能コード | 0xD1 = 受動読み上げ、0xD2 = 機能ワード、0xD3 = コマンドワード |
| 4 | データ | コマンド ID または読み上げ ID |
| 5 | 0xEE | フレームテール |

**例：** コマンド ID を読み取る = 10
```
FE EF 00 0A EE
```

**例：** コマンドワード読み上げを送信する
```
FE EF D3 00 EE
```

---

## 📚 BSP インターフェースリファレンス

### 1. UART_Init()
```cpp
void UART_Init(void);
```
**機能**：シリアルポートを初期化します（ボーレート 115200）

**例**：
```cpp
void setup() {
  UART_Init();
}
```

---

### 2. UART_ReadCommand()
```cpp
int UART_ReadCommand(void);
```
**機能**：音声モジュールが認識したコマンド ID を読み取ります

**戻り値**：
- `0` - コマンドが認識されていない
- `1~254` - コマンド ID
- `-1` - 新しいデータがない

**例**：
```cpp
int id = UART_ReadCommand();
if (id > 0) {
  Serial.print("识别到命令: ");
  Serial.println(id);
}
```

---

### 3. UART_SetPassiveVoice()
```cpp
void UART_SetPassiveVoice(uint8_t voiceID);
```
**機能**：受動読み上げ音声を設定します

**パラメータ**：
- `0x00` - 受動読み上げ音声タイプ

**例**：
```cpp
UART_SetPassiveVoice(0x00);
delay(200);
```

---

### 4. UART_SetFunctionVoice()
```cpp
void UART_SetFunctionVoice(uint8_t voiceID);
```
**機能**：機能ワード読み上げ音声を設定します

**パラメータ**：
- `0x00` - 機能ワード読み上げ音声タイプ

**例**：
```cpp
UART_SetFunctionVoice(0x00);
delay(200);
```

---

### 5. UART_SetCommandVoice()
```cpp
void UART_SetCommandVoice(uint8_t voiceID);
```
**機能**：コマンドワード読み上げ音声を設定します

**パラメータ**：
- `0x00` - コマンドワード読み上げ音声タイプ

**例**：
```cpp
UART_SetCommandVoice(0x00);
delay(200);
```

---

## 🎯 メインプログラムのロジック

```cpp
void setup() {
  Serial.begin(115200);
  UART_Init();
  
  Serial.println("UART Voice Module Initialized");
  
  UART_SetCommandVoice(0x00);  // 上电播报命令词语音
  delay(200);
}

void loop() {
  int commandId = UART_ReadCommand();
  
  if (commandId >= 0) {
    // 过滤无效值，防止重复输出
    if (commandId != 0 && commandId != 255 && commandId != lastCommandId) {
      Serial.print("ID: ");
      Serial.println(commandId);
      lastCommandId = commandId;
      
      // 示例：根据识别到的命令控制播报
      if (commandId == 1) {
        UART_SetCommandVoice(0x00);  // 识别到命令1，播报命令词语音
      } else if (commandId == 2) {
        UART_SetCommandVoice(0x00);  // 识别到命令2，播报命令词语音
      }
    } else if (commandId == 0 || commandId == 255) {
      if (lastCommandId != 0) {
        lastCommandId = 0;  // 重置状态
      }
    }
  }
  
  delay(50);
}
```

---

## 🔍 FAQ

### Q1: まったく出力がない

**考えられる原因：**
1. RX/TX が逆になっている
2. GND が共通グラウンドになっていない
3. モジュールに電源が供給されていない
4. ボーレートが間違っている

**解決策：**
- D10 がモジュールの TX に、D11 がモジュールの RX に接続されていることを確認します（クロス接続）
- GND の接続を確認します
- 5V 電源が正常か確認します
- シリアルのボーレートが 115200 であることを確認します

---

### Q2: シリアルモニタに文字化けしか表示されない

**考えられる原因：**
1. ボーレートの不一致
2. モジュールの起動異常

**解決策：**
- シリアルモニタのボーレートが 115200 であることを確認します
- モジュールのリセットボタンを一度押します

---

### Q3: 出力に "ID: 255" または "ID: 0" が表示される

**説明：** これは正常です
- `0` = コマンドが認識されていない
- `255` = 新しいデータがない

これらの値はコード内ですでにフィルタリングされているため、通常は出力されません。もし表示される場合は、コードが有効になっていません。

---

## 💡 BSP アーキテクチャの利点

### 1. コードの階層化が明確
- **bsp_uart.hpp** - 宣言のみ、実装なし
- **bsp_uart.cpp** - 具体的な実装の詳細
- **UART_Voice.ino** - ビジネスロジックのみを担当

### 2. 移植が容易
別のプラットフォーム（例：STM32、ESP32）に切り替える場合、`bsp_uart.cpp` の実装を変更するだけで済み、メインプログラムを変更する必要はありません。

### 3. 保守が容易
UART 関連のコードの変更は `bsp_uart.cpp` に限定され、一度修正すればどこでも有効です。

---

## 🚀 拡張機能の例

### 例 1: コマンドごとに異なる読み上げをトリガーする
```cpp
if (commandId == 1) {
  UART_SetCommandVoice(0x00);      // 播报命令词
} else if (commandId == 2) {
  UART_SetFunctionVoice(0x00);     // 播报功能词
} else if (commandId == 3) {
  UART_SetPassiveVoice(0x00);      // 播报被动语
}
```

### 例 2: LED を制御する
```cpp
if (commandId == 10) {
  digitalWrite(LED_PIN, LOW);    // 关灯
  UART_SetCommandVoice(0x00);     // 播报确认
}
```

### 例 3: モーターを制御する
```cpp
if (commandId == 11) {
  motor_stop();
  UART_SetCommandVoice(0x00);     // 播报确认
}
```
