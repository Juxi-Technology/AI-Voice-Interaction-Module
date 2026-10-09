[English](../../../../en/06-multi-host/arduino/iic/README.md) | [Deutsch](../../../../de/06-multi-host/arduino/iic/README.md) | [Español](../../../../es/06-multi-host/arduino/iic/README.md) | [Français](../../../../fr/06-multi-host/arduino/iic/README.md) | [Italiano](../../../../it/06-multi-host/arduino/iic/README.md) | [日本語](../../../../ja/06-multi-host/arduino/iic/README.md) | [한국어](../../../../ko/06-multi-host/arduino/iic/README.md) | [Português (BR)](../../../../pt-br/06-multi-host/arduino/iic/README.md) | [Português (PT)](../../../../pt-pt/06-multi-host/arduino/iic/README.md) | 简体中文 | [繁體中文](../../../../zh-hant/06-multi-host/arduino/iic/README.md)

# IIC 语音模块 BSP 版本 使用教程

## 📁 文件结构

```
iic/
├── iic.ino    # 主程序
├── bsp_iic.hpp         # 头文件（地址和函数声明）
├── bsp_iic.cpp         # 实现文件
└── README.md            # 本教程
```

---

## 🔌 硬件连接

| Arduino | 语音模块 |
|---------|----------|
| A4 (SDA) | SDA |
| A5 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

---

## 🔧 编译上传

### 第一步：打开 Arduino IDE
1. 打开 `IIC_Voice.ino` 文件
2. 选择你的开发板型号（如 Arduino Uno）
3. 选择对应的串口

### 第二步：编译上传
1. 点击 ✔️ 按钮编译
2. 点击 ➡️ 按钮上传到开发板

---

## 📡 串口测试

### 打开Arduino IDE里的串口监视器
- 波特率：**115200**
- 结束符：**无**

### 预期输出

上电后应该看到：
```
IIC Voice Module Initialized
```

对模块说出唤醒词和命令词，会输出对应的ID：
```
ID: 1
ID: 2
ID: 10
```

---

## 📚 寄存器映射

| 寄存器 | 地址 | 功能 | 说明 |
|--------|------|------|------|
| REG_RESULT | 0xDA | 读命令ID | 读取1字节，0=未识别 |
| REG_PASSIVE | 0xD1 | 写被动播报 | 写1字节，0x00=被动播报语 |
| REG_FUNCTION | 0xD2 | 写功能词播报 | 写1字节，0x00=功能词播报语 |
| REG_COMMAND | 0xD3 | 写命令词播报 | 写1字节，0x00=命令词播报语 |

---

## 📚 BSP 接口说明

### 1. IIC_Init()
```cpp
void IIC_Init(void);
```
**功能**：初始化 I2C 总线

**示例**：
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
**功能**：读取语音模块识别到的命令ID

**返回值**：
- `0` - 未识别到命令
- `1~254` - 命令ID
- `-1` - 通信错误

**示例**：
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
**功能**：设置被动播报语音

**参数**：
- `0x00` - 被动播报语类型

**示例**：
```cpp
IIC_SetPassiveVoice(0x00);
delay(200);
```

---

### 4. IIC_SetFunctionVoice()
```cpp
void IIC_SetFunctionVoice(uint8_t voiceID);
```
**功能**：设置功能词播报语音

**参数**：
- `0x00` - 功能词播报语类型

**示例**：
```cpp
IIC_SetFunctionVoice(0x00);
delay(200);
```

---

### 5. IIC_SetCommandVoice()
```cpp
void IIC_SetCommandVoice(uint8_t voiceID);
```
**功能**：设置命令词播报语音

**参数**：
- `0x00` - 命令词播报语类型

**示例**：
```cpp
IIC_SetCommandVoice(0x00);
delay(200);
```

---

## 🎯 主程序逻辑说明

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

## 🔍 常见问题

### Q1: 串口只显示 "IIC Read Error"

**可能原因：**
1. 接线错误、没接上
2. 模块未上电
3. I2C 地址不对

**解决方法：**
- 检查 SDA/SCL 是否接反
- 检查 GND 是否共地
- 检查 5V 是否供电正常
- 用 I2C 扫描程序确认设备地址

---

### Q2: 没有任何输出

**可能原因：**
1. 串口波特率不对
2. 模块没唤醒

**解决方法：**
- 确认串口波特率是 115200
- 先说唤醒词，再说命令词

---

### Q3: 输出 "ID: 255" 或 "ID: 0"

**说明：** 这是正常现象

- `0` = 未识别到命令
- `255` = 无新数据

代码里已经过滤掉这些值了，正常不会输出。如果看到输出，说明代码没生效。

---

## 💡 BSP 架构的优点

### 1. 代码分层清晰
- **bsp_iic.hpp** - 只看声明，不看实现
- **bsp_iic.cpp** - 具体实现细节
- **IIC_Voice.ino** - 只关心业务逻辑

### 2. 易于移植
如果换其他平台（如 STM32、ESP32），只需要修改 `bsp_iic.cpp` 的实现，主程序不用改。

### 3. 易于维护
修改 I2C 相关代码只在 `bsp_iic.cpp` 里，一处修改，处处生效。

---

## 🚀 扩展功能示例

### 示例1：根据不同命令触发不同播报
```cpp
if (commandId == 1) {
  IIC_SetCommandVoice(0x00);      // 播报命令词
} else if (commandId == 2) {
  IIC_SetFunctionVoice(0x00);     // 播报功能词
} else if (commandId == 3) {
  IIC_SetPassiveVoice(0x00);      // 播报被动语
}
```

### 示例2：控制 LED
```cpp
if (commandId == 10) {
  digitalWrite(LED_PIN, LOW);    // 关灯
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```

### 示例3：控制电机
```cpp
if (commandId == 11) {
  motor_stop();
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```
