English | [Deutsch](../../../../de/06-multi-host/arduino/uart/README.md) | [Español](../../../../es/06-multi-host/arduino/uart/README.md) | [Français](../../../../fr/06-multi-host/arduino/uart/README.md) | [Italiano](../../../../it/06-multi-host/arduino/uart/README.md) | [日本語](../../../../ja/06-multi-host/arduino/uart/README.md) | [한국어](../../../../ko/06-multi-host/arduino/uart/README.md) | [Português (BR)](../../../../pt-br/06-multi-host/arduino/uart/README.md) | [Português (PT)](../../../../pt-pt/06-multi-host/arduino/uart/README.md) | [简体中文](../../../../zh-hans/06-multi-host/arduino/uart/README.md) | [繁體中文](../../../../zh-hant/06-multi-host/arduino/uart/README.md)

# UART Voice Module BSP Version Tutorial

## 📁 File Structure

```
uart/
├── uart.ino    # 主程序
├── bsp_uart.hpp         # 头文件（协议帧和函数声明）
├── bsp_uart.cpp         # 实现文件
└── README.md              # 本教程
```

---

## 🔌 Hardware Connection

### Connecting to the Voice Module
| Arduino | Voice Module |
|---------|----------|
| D10 (RX) | TX |
| D11 (TX) | RX |
| GND | GND |
| 5V | 5V |

> 💡 **Note:** RX and TX must be cross-connected!

---

## 🔧 Compile and Upload

### Step 1: Open the Arduino IDE
1. Open the `UART_Voice.ino` file
2. Select your board model (e.g., Arduino Uno)
3. Select the corresponding serial port

### Step 2: Compile and Upload
1. Click the ✔️ button to compile
2. Click the ➡️ button to upload to the board

---

## 📡 Serial Test

### Open the Serial Monitor in the Arduino IDE
- Baud rate: **115200**
- Line ending: **None**

### Expected Output

After power-up, you should see:
```
UART Voice Module Initialized
```

Speak the wake word and command word to the module, and it will output the corresponding ID:
```
ID: 1
ID: 2
ID: 10
```

---

## 📚 Protocol Frame Format

| Byte | Content | Description |
|------|------|------|
| 1 | 0xFE | Frame header 1 |
| 2 | 0xEF | Frame header 2 |
| 3 | Function code | 0xD1 = passive broadcast, 0xD2 = function word, 0xD3 = command word |
| 4 | Data | Command ID or broadcast ID |
| 5 | 0xEE | Frame tail |

**Example:** Read command ID = 10
```
FE EF 00 0A EE
```

**Example:** Send command-word broadcast
```
FE EF D3 00 EE
```

---

## 📚 BSP Interface Reference

### 1. UART_Init()
```cpp
void UART_Init(void);
```
**Function**: Initialize the serial port (baud rate 115200)

**Example**:
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
**Function**: Read the command ID recognized by the voice module

**Return value**:
- `0` - no command recognized
- `1~254` - command ID
- `-1` - no new data

**Example**:
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
**Function**: Set the passive broadcast voice

**Parameter**:
- `0x00` - passive broadcast voice type

**Example**:
```cpp
UART_SetPassiveVoice(0x00);
delay(200);
```

---

### 4. UART_SetFunctionVoice()
```cpp
void UART_SetFunctionVoice(uint8_t voiceID);
```
**Function**: Set the function-word broadcast voice

**Parameter**:
- `0x00` - function-word broadcast voice type

**Example**:
```cpp
UART_SetFunctionVoice(0x00);
delay(200);
```

---

### 5. UART_SetCommandVoice()
```cpp
void UART_SetCommandVoice(uint8_t voiceID);
```
**Function**: Set the command-word broadcast voice

**Parameter**:
- `0x00` - command-word broadcast voice type

**Example**:
```cpp
UART_SetCommandVoice(0x00);
delay(200);
```

---

## 🎯 Main Program Logic

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

### Q1: No output at all

**Possible causes:**
1. RX/TX are reversed
2. GND is not common ground
3. Module not powered
4. Wrong baud rate

**Solutions:**
- Confirm D10 connects to the module TX and D11 connects to the module RX (cross connection)
- Confirm the GND connection
- Confirm the 5V power supply is normal
- Confirm the serial baud rate is 115200

---

### Q2: The serial monitor shows only garbled text

**Possible causes:**
1. Baud rate mismatch
2. Abnormal module power-up

**Solutions:**
- Confirm the serial monitor baud rate is 115200
- Press the module reset button once

---

### Q3: Output shows "ID: 255" or "ID: 0"

**Explanation:** This is normal
- `0` = no command recognized
- `255` = no new data

These values are already filtered out in the code, so they are not normally output. If you do see them, the code is not taking effect.

---

## 💡 Advantages of the BSP Architecture

### 1. Clear code layering
- **bsp_uart.hpp** - declaration only, no implementation
- **bsp_uart.cpp** - concrete implementation details
- **UART_Voice.ino** - only cares about business logic

### 2. Easy to port
If you switch to another platform (e.g., STM32, ESP32), you only need to modify the implementation in `bsp_uart.cpp`; the main program does not need to change.

### 3. Easy to maintain
Changes to UART-related code are confined to `bsp_uart.cpp` — fix once, effective everywhere.

---

## 🚀 Extended Function Examples

### Example 1: Trigger different broadcasts based on different commands
```cpp
if (commandId == 1) {
  UART_SetCommandVoice(0x00);      // 播报命令词
} else if (commandId == 2) {
  UART_SetFunctionVoice(0x00);     // 播报功能词
} else if (commandId == 3) {
  UART_SetPassiveVoice(0x00);      // 播报被动语
}
```

### Example 2: Control an LED
```cpp
if (commandId == 10) {
  digitalWrite(LED_PIN, LOW);    // 关灯
  UART_SetCommandVoice(0x00);     // 播报确认
}
```

### Example 3: Control a motor
```cpp
if (commandId == 11) {
  motor_stop();
  UART_SetCommandVoice(0x00);     // 播报确认
}
```

