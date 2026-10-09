[English](../../../../en/06-multi-host/arduino/iic/README.md) | [Deutsch](../../../../de/06-multi-host/arduino/iic/README.md) | [Español](../../../../es/06-multi-host/arduino/iic/README.md) | [Français](../../../../fr/06-multi-host/arduino/iic/README.md) | [Italiano](../../../../it/06-multi-host/arduino/iic/README.md) | 日本語 | [한국어](../../../../ko/06-multi-host/arduino/iic/README.md) | [Português (BR)](../../../../pt-br/06-multi-host/arduino/iic/README.md) | [Português (PT)](../../../../pt-pt/06-multi-host/arduino/iic/README.md) | [简体中文](../../../../zh-hans/06-multi-host/arduino/iic/README.md) | [繁體中文](../../../../zh-hant/06-multi-host/arduino/iic/README.md)

# IIC 音声モジュール BSP 版チュートリアル

## 📁 ファイル構成

```
iic/
├── iic.ino    # 主程序
├── bsp_iic.hpp         # 头文件（地址和函数声明）
├── bsp_iic.cpp         # 实现文件
└── README.md            # 本教程
```

---

## 🔌 ハードウェア接続

| Arduino | 音声モジュール |
|---------|----------|
| A4 (SDA) | SDA |
| A5 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

---

## 🔧 コンパイルとアップロード

### ステップ 1：Arduino IDE を開く
1. `IIC_Voice.ino` ファイルを開きます
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
IIC Voice Module Initialized
```

ウェイクワードとコマンドワードをモジュールに話しかけると、対応する ID が出力されます：
```
ID: 1
ID: 2
ID: 10
```

---

## 📚 レジスタマップ

| レジスタ | アドレス | 機能 | 説明 |
|--------|------|------|------|
| REG_RESULT | 0xDA | コマンド ID を読み取る | 1 バイト読み取り、0 = 未認識 |
| REG_PASSIVE | 0xD1 | 受動読み上げを書き込む | 1 バイト書き込み、0x00 = 受動読み上げ音声 |
| REG_FUNCTION | 0xD2 | 機能ワード読み上げを書き込む | 1 バイト書き込み、0x00 = 機能ワード読み上げ音声 |
| REG_COMMAND | 0xD3 | コマンドワード読み上げを書き込む | 1 バイト書き込み、0x00 = コマンドワード読み上げ音声 |

---

## 📚 BSP インターフェースリファレンス

### 1. IIC_Init()
```cpp
void IIC_Init(void);
```
**機能**：I2C バスを初期化します

**例**：
```cpp
void setup() {
  IIC_Init();
}
```

---

### 2. IIC_ReadCommand()
```cpp
int IIC_ReadCommand(void);
```
**機能**：音声モジュールが認識したコマンド ID を読み取ります

**戻り値**：
- `0` - コマンドが認識されていない
- `1~254` - コマンド ID
- `-1` - 通信エラー

**例**：
```cpp
int id = IIC_ReadCommand();
if (id > 0) {
  Serial.print("识别到命令: ");
  Serial.println(id);
}
```

---

### 3. IIC_SetPassiveVoice()
```cpp
void IIC_SetPassiveVoice(uint8_t voiceID);
```
**機能**：受動読み上げ音声を設定します

**パラメータ**：
- `0x00` - 受動読み上げ音声タイプ

**例**：
```cpp
IIC_SetPassiveVoice(0x00);
delay(200);
```

---

### 4. IIC_SetFunctionVoice()
```cpp
void IIC_SetFunctionVoice(uint8_t voiceID);
```
**機能**：機能ワード読み上げ音声を設定します

**パラメータ**：
- `0x00` - 機能ワード読み上げ音声タイプ

**例**：
```cpp
IIC_SetFunctionVoice(0x00);
delay(200);
```

---

### 5. IIC_SetCommandVoice()
```cpp
void IIC_SetCommandVoice(uint8_t voiceID);
```
**機能**：コマンドワード読み上げ音声を設定します

**パラメータ**：
- `0x00` - コマンドワード読み上げ音声タイプ

**例**：
```cpp
IIC_SetCommandVoice(0x00);
delay(200);
```

---

## 🎯 メインプログラムのロジック

```cpp
void setup() {
  Serial.begin(115200);
  IIC_Init();
  
  Serial.println("IIC Voice Module Initialized");
  
  IIC_SetCommandVoice(0x00);  // 上电播报命令词语音
  delay(200);
}

void loop() {
  int commandId = IIC_ReadCommand();
  
  if (commandId >= 0) {
    // 过滤无效值，防止重复输出
    if (commandId != 0 && commandId != 255 && commandId != lastCommandId) {
      Serial.print("ID: ");
      Serial.println(commandId);
      lastCommandId = commandId;
      
      // 示例：根据识别到的命令控制播报
      if (commandId == 1) {
        IIC_SetCommandVoice(0x00);  // 识别到命令1，播报命令词语音
      } else if (commandId == 2) {
        IIC_SetCommandVoice(0x00);  // 识别到命令2，播报命令词语音
      }
    } else if (commandId == 0 || commandId == 255) {
      if (lastCommandId != 0) {
        lastCommandId = 0;  // 重置状态
      }
    }
  } else {
    Serial.println("IIC Read Error");
    delay(1000);
  }
  
  delay(50);
}
```

---

## 🔍 FAQ

### Q1: シリアルモニタに "IIC Read Error" しか表示されない

**考えられる原因：**
1. 配線が間違っている、または接続されていない
2. モジュールに電源が供給されていない
3. I2C アドレスが間違っている

**解決策：**
- SDA/SCL が逆になっていないか確認します
- GND が共通グラウンドになっているか確認します
- 5V 電源が正常か確認します
- I2C スキャナプログラムを使ってデバイスアドレスを確認します

---

### Q2: まったく出力がない

**考えられる原因：**
1. シリアルのボーレートが間違っている
2. モジュールがウェイクアップしていない

**解決策：**
- シリアルのボーレートが 115200 であることを確認します
- 先にウェイクワードを言い、その後でコマンドワードを言います

---

### Q3: 出力に "ID: 255" または "ID: 0" が表示される

**説明：** これは正常です

- `0` = コマンドが認識されていない
- `255` = 新しいデータがない

これらの値はコード内ですでにフィルタリングされているため、通常は出力されません。もし表示される場合は、コードが有効になっていません。

---

## 💡 BSP アーキテクチャの利点

### 1. コードの階層化が明確
- **bsp_iic.hpp** - 宣言のみ、実装なし
- **bsp_iic.cpp** - 具体的な実装の詳細
- **IIC_Voice.ino** - ビジネスロジックのみを担当

### 2. 移植が容易
別のプラットフォーム（例：STM32、ESP32）に切り替える場合、`bsp_iic.cpp` の実装を変更するだけで済み、メインプログラムを変更する必要はありません。

### 3. 保守が容易
I2C 関連のコードの変更は `bsp_iic.cpp` に限定され、一度修正すればどこでも有効です。

---

## 🚀 拡張機能の例

### 例 1: コマンドごとに異なる読み上げをトリガーする
```cpp
if (commandId == 1) {
  IIC_SetCommandVoice(0x00);      // 播报命令词
} else if (commandId == 2) {
  IIC_SetFunctionVoice(0x00);     // 播报功能词
} else if (commandId == 3) {
  IIC_SetPassiveVoice(0x00);      // 播报被动语
}
```

### 例 2: LED を制御する
```cpp
if (commandId == 10) {
  digitalWrite(LED_PIN, LOW);    // 关灯
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```

### 例 3: モーターを制御する
```cpp
if (commandId == 11) {
  motor_stop();
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```
