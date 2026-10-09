English | [Deutsch](../../../../de/06-multi-host/arduino/iic/README.md) | [Español](../../../../es/06-multi-host/arduino/iic/README.md) | [Français](../../../../fr/06-multi-host/arduino/iic/README.md) | [Italiano](../../../../it/06-multi-host/arduino/iic/README.md) | [日本語](../../../../ja/06-multi-host/arduino/iic/README.md) | [한국어](../../../../ko/06-multi-host/arduino/iic/README.md) | [Português (BR)](../../../../pt-br/06-multi-host/arduino/iic/README.md) | [Português (PT)](../../../../pt-pt/06-multi-host/arduino/iic/README.md) | [简体中文](../../../../zh-hans/06-multi-host/arduino/iic/README.md) | [繁體中文](../../../../zh-hant/06-multi-host/arduino/iic/README.md)

# IIC Voice Module BSP Version Tutorial

## 📁 File Structure

```
iic/
├── iic.ino    # 主程序
├── bsp_iic.hpp         # 头文件（地址和函数声明）
├── bsp_iic.cpp         # 实现文件
└── README.md            # 本教程
```

---

## 🔌 Hardware Connection

| Arduino | Voice Module |
|---------|----------|
| A4 (SDA) | SDA |
| A5 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

---

## 🔧 Compile and Upload

### Step 1: Open the Arduino IDE
1. Open the `IIC_Voice.ino` file
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
IIC Voice Module Initialized
```

Speak the wake word and command word to the module, and it will output the corresponding ID:
```
ID: 1
ID: 2
ID: 10
```

---

## 📚 Register Map

| Register | Address | Function | Description |
|--------|------|------|------|
| REG_RESULT | 0xDA | Read command ID | Read 1 byte, 0 = unrecognized |
| REG_PASSIVE | 0xD1 | Write passive broadcast | Write 1 byte, 0x00 = passive broadcast voice |
| REG_FUNCTION | 0xD2 | Write function-word broadcast | Write 1 byte, 0x00 = function-word broadcast voice |
| REG_COMMAND | 0xD3 | Write command-word broadcast | Write 1 byte, 0x00 = command-word broadcast voice |

---

## 📚 BSP Interface Reference

### 1. IIC_Init()
```cpp
void IIC_Init(void);
```
**Function**: Initialize the I2C bus

**Example**:
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
**Function**: Read the command ID recognized by the voice module

**Return value**:
- `0` - no command recognized
- `1~254` - command ID
- `-1` - communication error

**Example**:
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
**Function**: Set the passive broadcast voice

**Parameter**:
- `0x00` - passive broadcast voice type

**Example**:
```cpp
IIC_SetPassiveVoice(0x00);
delay(200);
```

---

### 4. IIC_SetFunctionVoice()
```cpp
void IIC_SetFunctionVoice(uint8_t voiceID);
```
**Function**: Set the function-word broadcast voice

**Parameter**:
- `0x00` - function-word broadcast voice type

**Example**:
```cpp
IIC_SetFunctionVoice(0x00);
delay(200);
```

---

### 5. IIC_SetCommandVoice()
```cpp
void IIC_SetCommandVoice(uint8_t voiceID);
```
**Function**: Set the command-word broadcast voice

**Parameter**:
- `0x00` - command-word broadcast voice type

**Example**:
```cpp
IIC_SetCommandVoice(0x00);
delay(200);
```

---

## 🎯 Main Program Logic

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

### Q1: The serial monitor only shows "IIC Read Error"

**Possible causes:**
1. Incorrect wiring, or not connected
2. Module not powered
3. Wrong I2C address

**Solutions:**
- Check whether SDA/SCL are reversed
- Check whether GND is common ground
- Check whether the 5V power supply is normal
- Use an I2C scanner program to confirm the device address

---

### Q2: No output at all

**Possible causes:**
1. Wrong serial baud rate
2. Module not woken up

**Solutions:**
- Confirm the serial baud rate is 115200
- Say the wake word first, then the command word

---

### Q3: Output shows "ID: 255" or "ID: 0"

**Explanation:** This is normal

- `0` = no command recognized
- `255` = no new data

These values are already filtered out in the code, so they are not normally output. If you do see them, the code is not taking effect.

---

## 💡 Advantages of the BSP Architecture

### 1. Clear code layering
- **bsp_iic.hpp** - declaration only, no implementation
- **bsp_iic.cpp** - concrete implementation details
- **IIC_Voice.ino** - only cares about business logic

### 2. Easy to port
If you switch to another platform (e.g., STM32, ESP32), you only need to modify the implementation in `bsp_iic.cpp`; the main program does not need to change.

### 3. Easy to maintain
Changes to I2C-related code are confined to `bsp_iic.cpp` — fix once, effective everywhere.

---

## 🚀 Extended Function Examples

### Example 1: Trigger different broadcasts based on different commands
```cpp
if (commandId == 1) {
  IIC_SetCommandVoice(0x00);      // 播报命令词
} else if (commandId == 2) {
  IIC_SetFunctionVoice(0x00);     // 播报功能词
} else if (commandId == 3) {
  IIC_SetPassiveVoice(0x00);      // 播报被动语
}
```

### Example 2: Control an LED
```cpp
if (commandId == 10) {
  digitalWrite(LED_PIN, LOW);    // 关灯
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```

### Example 3: Control a motor
```cpp
if (commandId == 11) {
  motor_stop();
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```
