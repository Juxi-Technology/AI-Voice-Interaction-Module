[English](../../../../en/06-multi-host/arduino/iic/README.md) | [Deutsch](../../../../de/06-multi-host/arduino/iic/README.md) | [Español](../../../../es/06-multi-host/arduino/iic/README.md) | [Français](../../../../fr/06-multi-host/arduino/iic/README.md) | [Italiano](../../../../it/06-multi-host/arduino/iic/README.md) | [日本語](../../../../ja/06-multi-host/arduino/iic/README.md) | [한국어](../../../../ko/06-multi-host/arduino/iic/README.md) | [Português (BR)](../../../../pt-br/06-multi-host/arduino/iic/README.md) | [Português (PT)](../../../../pt-pt/06-multi-host/arduino/iic/README.md) | [简体中文](../../../../zh-hans/06-multi-host/arduino/iic/README.md) | 繁體中文

# IIC 語音模組 BSP 版本 使用教學

## 📁 檔案結構

```
iic/
├── iic.ino    # 主程序
├── bsp_iic.hpp         # 头文件（地址和函数声明）
├── bsp_iic.cpp         # 实现文件
└── README.md            # 本教程
```

---

## 🔌 硬體連接

| Arduino | 語音模組 |
|---------|----------|
| A4 (SDA) | SDA |
| A5 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

---

## 🔧 編譯上傳

### 第一步：打開 Arduino IDE
1. 打開 `IIC_Voice.ino` 檔案
2. 選擇你的開發板型號（如 Arduino Uno）
3. 選擇對應的序列埠

### 第二步：編譯上傳
1. 點擊 ✔️ 按鈕編譯
2. 點擊 ➡️ 按鈕上傳到開發板

---

## 📡 序列埠測試

### 打開Arduino IDE裡的序列埠監視器
- 鮑率：**115200**
- 結束符：**無**

### 預期輸出

上電後應該看到：
```
IIC Voice Module Initialized
```

對模組說出喚醒詞和命令詞，會輸出對應的ID：
```
ID: 1
ID: 2
ID: 10
```

---

## 📚 暫存器映射

| 暫存器 | 位址 | 功能 | 說明 |
|--------|------|------|------|
| REG_RESULT | 0xDA | 讀命令ID | 讀取1位元組，0=未辨識 |
| REG_PASSIVE | 0xD1 | 寫被動播報 | 寫1位元組，0x00=被動播報語 |
| REG_FUNCTION | 0xD2 | 寫功能詞播報 | 寫1位元組，0x00=功能詞播報語 |
| REG_COMMAND | 0xD3 | 寫命令詞播報 | 寫1位元組，0x00=命令詞播報語 |

---

## 📚 BSP 介面說明

### 1. IIC_Init()
```cpp
void IIC_Init(void);
```
**功能**：初始化 I2C 匯流排

**範例**：
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
**功能**：讀取語音模組辨識到的命令ID

**傳回值**：
- `0` - 未辨識到命令
- `1~254` - 命令ID
- `-1` - 通訊錯誤

**範例**：
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
**功能**：設定被動播報語音

**參數**：
- `0x00` - 被動播報語類型

**範例**：
```cpp
IIC_SetPassiveVoice(0x00);
delay(200);
```

---

### 4. IIC_SetFunctionVoice()
```cpp
void IIC_SetFunctionVoice(uint8_t voiceID);
```
**功能**：設定功能詞播報語音

**參數**：
- `0x00` - 功能詞播報語類型

**範例**：
```cpp
IIC_SetFunctionVoice(0x00);
delay(200);
```

---

### 5. IIC_SetCommandVoice()
```cpp
void IIC_SetCommandVoice(uint8_t voiceID);
```
**功能**：設定命令詞播報語音

**參數**：
- `0x00` - 命令詞播報語類型

**範例**：
```cpp
IIC_SetCommandVoice(0x00);
delay(200);
```

---

## 🎯 主程式邏輯說明

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

## 🔍 常見問題

### Q1: 序列埠只顯示 "IIC Read Error"

**可能原因：**
1. 接線錯誤、沒接上
2. 模組未上電
3. I2C 位址不對

**解決方法：**
- 檢查 SDA/SCL 是否接反
- 檢查 GND 是否共地
- 檢查 5V 是否供電正常
- 用 I2C 掃描程式確認裝置位址

---

### Q2: 沒有任何輸出

**可能原因：**
1. 序列埠鮑率不對
2. 模組沒喚醒

**解決方法：**
- 確認序列埠鮑率是 115200
- 先說喚醒詞，再說命令詞

---

### Q3: 輸出 "ID: 255" 或 "ID: 0"

**說明：** 這是正常現象

- `0` = 未辨識到命令
- `255` = 無新資料

程式碼裡已經過濾掉這些值了，正常不會輸出。如果看到輸出，說明程式碼沒生效。

---

## 💡 BSP 架構的優點

### 1. 程式碼分層清晰
- **bsp_iic.hpp** - 只看宣告，不看實作
- **bsp_iic.cpp** - 具體實作細節
- **IIC_Voice.ino** - 只關心業務邏輯

### 2. 易於移植
如果換其他平台（如 STM32、ESP32），只需要修改 `bsp_iic.cpp` 的實作，主程式不用改。

### 3. 易於維護
修改 I2C 相關程式碼只在 `bsp_iic.cpp` 裡，一處修改，處處生效。

---

## 🚀 擴充功能範例

### 範例1：根據不同命令觸發不同播報
```cpp
if (commandId == 1) {
  IIC_SetCommandVoice(0x00);      // 播报命令词
} else if (commandId == 2) {
  IIC_SetFunctionVoice(0x00);     // 播报功能词
} else if (commandId == 3) {
  IIC_SetPassiveVoice(0x00);      // 播报被动语
}
```

### 範例2：控制 LED
```cpp
if (commandId == 10) {
  digitalWrite(LED_PIN, LOW);    // 关灯
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```

### 範例3：控制馬達
```cpp
if (commandId == 11) {
  motor_stop();
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```
