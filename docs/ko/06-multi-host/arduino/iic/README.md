[English](../../../../en/06-multi-host/arduino/iic/README.md) | [Deutsch](../../../../de/06-multi-host/arduino/iic/README.md) | [Español](../../../../es/06-multi-host/arduino/iic/README.md) | [Français](../../../../fr/06-multi-host/arduino/iic/README.md) | [Italiano](../../../../it/06-multi-host/arduino/iic/README.md) | [日本語](../../../../ja/06-multi-host/arduino/iic/README.md) | 한국어 | [Português (BR)](../../../../pt-br/06-multi-host/arduino/iic/README.md) | [Português (PT)](../../../../pt-pt/06-multi-host/arduino/iic/README.md) | [简体中文](../../../../zh-hans/06-multi-host/arduino/iic/README.md) | [繁體中文](../../../../zh-hant/06-multi-host/arduino/iic/README.md)

# IIC 음성 모듈 BSP 버전 튜토리얼

## 📁 파일 구조

```
iic/
├── iic.ino    # 主程序
├── bsp_iic.hpp         # 头文件（地址和函数声明）
├── bsp_iic.cpp         # 实现文件
└── README.md            # 本教程
```

---

## 🔌 하드웨어 연결

| Arduino | 음성 모듈 |
|---------|----------|
| A4 (SDA) | SDA |
| A5 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

---

## 🔧 컴파일 및 업로드

### 1단계: Arduino IDE 열기
1. `IIC_Voice.ino` 파일을 엽니다
2. 사용하는 보드 모델을 선택합니다(예: Arduino Uno)
3. 해당 시리얼 포트를 선택합니다

### 2단계: 컴파일 및 업로드
1. ✔️ 버튼을 클릭하여 컴파일합니다
2. ➡️ 버튼을 클릭하여 보드에 업로드합니다

---

## 📡 시리얼 테스트

### Arduino IDE에서 시리얼 모니터 열기
- 보드 레이트: **115200**
- 줄 바꿈: **None**

### 예상 출력

전원을 켜면 다음이 표시됩니다:
```
IIC Voice Module Initialized
```

모듈에 웨이크 워드와 명령어를 말하면 해당 ID를 출력합니다:
```
ID: 1
ID: 2
ID: 10
```

---

## 📚 레지스터 맵

| 레지스터 | 주소 | 기능 | 설명 |
|--------|------|------|------|
| REG_RESULT | 0xDA | 명령 ID 읽기 | 1바이트 읽기, 0 = 미인식 |
| REG_PASSIVE | 0xD1 | 수동 방송 쓰기 | 1바이트 쓰기, 0x00 = 수동 방송 음성 |
| REG_FUNCTION | 0xD2 | 기능어 방송 쓰기 | 1바이트 쓰기, 0x00 = 기능어 방송 음성 |
| REG_COMMAND | 0xD3 | 명령어 방송 쓰기 | 1바이트 쓰기, 0x00 = 명령어 방송 음성 |

---

## 📚 BSP 인터페이스 레퍼런스

### 1. IIC_Init()
```cpp
void IIC_Init(void);
```
**기능**: I2C 버스를 초기화합니다

**예시**:
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
**기능**: 음성 모듈이 인식한 명령 ID를 읽습니다

**반환 값**:
- `0` - 인식된 명령 없음
- `1~254` - 명령 ID
- `-1` - 통신 오류

**예시**:
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
**기능**: 수동 방송 음성을 설정합니다

**매개변수**:
- `0x00` - 수동 방송 음성 유형

**예시**:
```cpp
IIC_SetPassiveVoice(0x00);
delay(200);
```

---

### 4. IIC_SetFunctionVoice()
```cpp
void IIC_SetFunctionVoice(uint8_t voiceID);
```
**기능**: 기능어 방송 음성을 설정합니다

**매개변수**:
- `0x00` - 기능어 방송 음성 유형

**예시**:
```cpp
IIC_SetFunctionVoice(0x00);
delay(200);
```

---

### 5. IIC_SetCommandVoice()
```cpp
void IIC_SetCommandVoice(uint8_t voiceID);
```
**기능**: 명령어 방송 음성을 설정합니다

**매개변수**:
- `0x00` - 명령어 방송 음성 유형

**예시**:
```cpp
IIC_SetCommandVoice(0x00);
delay(200);
```

---

## 🎯 메인 프로그램 로직

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

### Q1: 시리얼 모니터에 "IIC Read Error"만 표시됨

**가능한 원인:**
1. 배선이 잘못되었거나 연결되지 않음
2. 모듈에 전원이 공급되지 않음
3. I2C 주소가 잘못됨

**해결 방법:**
- SDA/SCL이 반대로 연결되지 않았는지 확인합니다
- GND가 공통 접지인지 확인합니다
- 5V 전원 공급이 정상인지 확인합니다
- I2C 스캐너 프로그램을 사용하여 장치 주소를 확인합니다

---

### Q2: 출력이 전혀 없음

**가능한 원인:**
1. 시리얼 보드 레이트가 잘못됨
2. 모듈이 깨어나지 않음

**해결 방법:**
- 시리얼 보드 레이트가 115200인지 확인합니다
- 먼저 웨이크 워드를 말한 다음 명령어를 말합니다

---

### Q3: 출력에 "ID: 255" 또는 "ID: 0"이 표시됨

**설명:** 정상입니다

- `0` = 인식된 명령 없음
- `255` = 새로운 데이터 없음

이 값들은 코드에서 이미 필터링되므로 일반적으로 출력되지 않습니다. 만약 이 값이 보인다면 코드가 적용되지 않은 것입니다.

---

## 💡 BSP 아키텍처의 장점

### 1. 명확한 코드 계층화
- **bsp_iic.hpp** - 선언만 있고 구현 없음
- **bsp_iic.cpp** - 구체적인 구현 세부 사항
- **IIC_Voice.ino** - 비즈니스 로직만 담당

### 2. 이식 용이
다른 플랫폼(예: STM32, ESP32)으로 전환하더라도 `bsp_iic.cpp`의 구현만 수정하면 되며, 메인 프로그램은 변경할 필요가 없습니다.

### 3. 유지보수 용이
I2C 관련 코드의 변경은 `bsp_iic.cpp`에 국한됩니다 — 한 번 수정하면 어디서나 적용됩니다.

---

## 🚀 확장 기능 예시

### 예시 1: 서로 다른 명령에 따라 서로 다른 방송 트리거
```cpp
if (commandId == 1) {
  IIC_SetCommandVoice(0x00);      // 播报命令词
} else if (commandId == 2) {
  IIC_SetFunctionVoice(0x00);     // 播报功能词
} else if (commandId == 3) {
  IIC_SetPassiveVoice(0x00);      // 播报被动语
}
```

### 예시 2: LED 제어
```cpp
if (commandId == 10) {
  digitalWrite(LED_PIN, LOW);    // 关灯
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```

### 예시 3: 모터 제어
```cpp
if (commandId == 11) {
  motor_stop();
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```
