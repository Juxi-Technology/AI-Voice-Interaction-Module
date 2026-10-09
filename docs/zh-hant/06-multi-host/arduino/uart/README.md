[English](../../../../en/06-multi-host/arduino/uart/README.md) | [Deutsch](../../../../de/06-multi-host/arduino/uart/README.md) | [Español](../../../../es/06-multi-host/arduino/uart/README.md) | [Français](../../../../fr/06-multi-host/arduino/uart/README.md) | [Italiano](../../../../it/06-multi-host/arduino/uart/README.md) | [日本語](../../../../ja/06-multi-host/arduino/uart/README.md) | [한국어](../../../../ko/06-multi-host/arduino/uart/README.md) | [Português (BR)](../../../../pt-br/06-multi-host/arduino/uart/README.md) | [Português (PT)](../../../../pt-pt/06-multi-host/arduino/uart/README.md) | [简体中文](../../../../zh-hans/06-multi-host/arduino/uart/README.md) | 繁體中文

# UART 語音模組 BSP 版本 使用教學

## 📁 檔案結構

```
uart/
├── uart.ino    # 主程序
├── bsp_uart.hpp         # 头文件（协议帧和函数声明）
├── bsp_uart.cpp         # 实现文件
└── README.md              # 本教程
```

---

## 🔌 硬體連接

### 連接到語音模組
| Arduino | 語音模組 |
|---------|----------|
| D10 (RX) | TX |
| D11 (TX) | RX |
| GND | GND |
| 5V | 5V |

> 💡 **注意：** RX 和 TX 需要交叉連接！

---

## 🔧 編譯上傳

### 第一步：打開 Arduino IDE
1. 打開 `UART_Voice.ino` 檔案
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
UART Voice Module Initialized
```

對模組說出喚醒詞和命令詞，會輸出對應的ID：
```
ID: 1
ID: 2
ID: 10
```

---

## 📚 協定幀格式

| 位元組 | 內容 | 說明 |
|------|------|------|
| 1 | 0xFE | 幀頭1 |
| 2 | 0xEF | 幀頭2 |
| 3 | 功能碼 | 0xD1=被動播報, 0xD2=功能詞, 0xD3=命令詞 |
| 4 | 資料 | 命令ID 或 播報ID |
| 5 | 0xEE | 幀尾 |

**範例：** 讀取到命令ID=10
```
FE EF 00 0A EE
```

**範例：** 發送命令詞播報
```
FE EF D3 00 EE
```

---

## 📚 BSP 介面說明

### 1. UART_Init()
```cpp
void UART_Init(void);
```
**功能**：初始化序列埠（鮑率 115200）

**範例**：
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
**功能**：讀取語音模組辨識到的命令ID

**傳回值**：
- `0` - 未辨識到命令
- `1~254` - 命令ID
- `-1` - 無新資料

**範例**：
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
**功能**：設定被動播報語音

**參數**：
- `0x00` - 被動播報語類型

**範例**：
```cpp
UART_SetPassiveVoice(0x00);
delay(200);
```

---

### 4. UART_SetFunctionVoice()
```cpp
void UART_SetFunctionVoice(uint8_t voiceID);
```
**功能**：設定功能詞播報語音

**參數**：
- `0x00` - 功能詞播報語類型

**範例**：
```cpp
UART_SetFunctionVoice(0x00);
delay(200);
```

---

### 5. UART_SetCommandVoice()
```cpp
void UART_SetCommandVoice(uint8_t voiceID);
```
**功能**：設定命令詞播報語音

**參數**：
- `0x00` - 命令詞播報語類型

**範例**：
```cpp
UART_SetCommandVoice(0x00);
delay(200);
```

---

## 🎯 主程式邏輯說明

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

## 🔍 常見問題

### Q1: 沒有任何輸出

**可能原因：**
1. RX/TX 接反了
2. GND 沒共地
3. 模組沒上電
4. 鮑率不對

**解決方法：**
- 確認 D10 接 模組 TX，D11 接 模組 RX（交叉連接）
- 確認 GND 連接
- 確認 5V 供電正常
- 確認序列埠鮑率是 115200

---

### Q2: 序列埠只顯示亂碼

**可能原因：**
1. 鮑率不相符
2. 模組上電不正常

**解決方法：**
- 確認序列埠監視器鮑率是 115200
- 按一下模組重置鍵

---

### Q3: 輸出 "ID: 255" 或 "ID: 0"

**說明：** 這是正常現象
- `0` = 未辨識到命令
- `255` = 無新資料

程式碼裡已經過濾掉這些值了，正常不會輸出。如果看到輸出，說明程式碼沒生效。

---

## 💡 BSP 架構的優點

### 1. 程式碼分層清晰
- **bsp_uart.hpp** - 只看宣告，不看實作
- **bsp_uart.cpp** - 具體實作細節
- **UART_Voice.ino** - 只關心業務邏輯

### 2. 易於移植
如果換其他平台（如 STM32、ESP32），只需要修改 `bsp_uart.cpp` 的實作，主程式不用改。

### 3. 易於維護
修改 UART 相關程式碼只在 `bsp_uart.cpp` 裡，一處修改，處處生效。

---

## 🚀 擴充功能範例

### 範例1：根據不同命令觸發不同播報
```cpp
if (commandId == 1) {
  UART_SetCommandVoice(0x00);      // 播报命令词
} else if (commandId == 2) {
  UART_SetFunctionVoice(0x00);     // 播报功能词
} else if (commandId == 3) {
  UART_SetPassiveVoice(0x00);      // 播报被动语
}
```

### 範例2：控制 LED
```cpp
if (commandId == 10) {
  digitalWrite(LED_PIN, LOW);    // 关灯
  UART_SetCommandVoice(0x00);     // 播报确认
}
```

### 範例3：控制馬達
```cpp
if (commandId == 11) {
  motor_stop();
  UART_SetCommandVoice(0x00);     // 播报确认
}
```
