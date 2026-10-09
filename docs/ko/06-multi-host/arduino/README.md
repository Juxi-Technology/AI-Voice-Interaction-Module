[English](../../../en/06-multi-host/arduino/README.md) | [Deutsch](../../../de/06-multi-host/arduino/README.md) | [Español](../../../es/06-multi-host/arduino/README.md) | [Français](../../../fr/06-multi-host/arduino/README.md) | [Italiano](../../../it/06-multi-host/arduino/README.md) | [日本語](../../../ja/06-multi-host/arduino/README.md) | 한국어 | [Português (BR)](../../../pt-br/06-multi-host/arduino/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/arduino/README.md) | [简体中文](../../../zh-hans/06-multi-host/arduino/README.md) | [繁體中文](../../../zh-hant/06-multi-host/arduino/README.md)

# AI 음성 상호작용 모듈 - Arduino 사용 가이드

## 목차

1. [소개](#소개)
2. [하드웨어 연결](#하드웨어-연결)
3. [개발 환경 설정](#개발-환경-설정)
4. [IIC 버전 사용](#iic-버전-사용)
5. [UART 버전 사용](#uart-버전-사용)
6. [FAQ](#faq)

---

## 소개

이 저장소는 AI 음성 상호작용 모듈과 통신하기 위한 Arduino 플랫폼 예제 코드를 제공하며, I2C와 UART 두 가지 통신 방식을 모두 지원합니다.

- **음성 인식 모듈**: 오프라인 음성 인식을 지원하며, 인식 후 명령 ID를 출력합니다
- **방송 기능**: 수동 방송, 기능어 방송, 명령어 방송을 지원합니다
- **통신 프로토콜**: I2C 주소 0x2A, UART 보드 레이트 115200

---

## 하드웨어 연결

### 일반 연결

| Arduino 핀 | 음성 모듈 | 설명 |
|-------------|-------------|-------------|
| 5V | 5V | 전원 양극 |
| GND | GND | 전원 접지 |

---

### I2C 버전 연결

| Arduino 핀 | 음성 모듈 | 설명 |
|-------------|-------------|-------------|
| A4 (SDA) | SDA | I2C 데이터선 |
| A5 (SCL) | SCL | I2C 클록선 |

---

### UART 버전 연결

| Arduino 핀 | 음성 모듈 | 설명 |
|-------------|-------------|-------------|
| D10 (RX) | TX | 시리얼 수신(소프트웨어 시리얼) |
| D11 (TX) | RX | 시리얼 송신(소프트웨어 시리얼) |

---

### 시리얼 디버그 연결

| Arduino 핀 | USB-TTL | 설명 |
|-------------|---------|-------------|
| TX (D1) | RX | 디버그 출력 |
| RX (D0) | TX | 디버그 입력(선택 사항) |
| GND | GND | 공통 접지 |

---

## 개발 환경 설정

### 1. Arduino IDE 설치

- 다운로드: https://www.arduino.cc/en/software
- 최신 버전을 설치합니다

### 2. 보드 지원 패키지 설치

- Arduino IDE를 엽니다
- 도구 → 보드 → 보드 매니저
- 사용하는 Arduino 보드에 맞는 지원 패키지를 검색하여 설치합니다
- 권장: Arduino Uno / Nano

---

## IIC 버전 사용

### 1. 프로젝트 열기

- Arduino IDE에서 `IIC_Voice/IIC_Voice.ino`를 엽니다

### 2. 코드 업로드

- 올바른 보드 모델을 선택합니다(도구 → 보드)
- 올바른 포트를 선택합니다(도구 → 포트)
- 업로드 버튼(→)을 클릭합니다
- 업로드가 완료될 때까지 기다립니다

### 3. 테스트 실행

1. 시리얼 모니터를 엽니다(도구 → 시리얼 모니터)
2. 보드 레이트를 **115200**으로 설정합니다
3. 정상적으로 시작되면 다음이 표시됩니다:

```
IIC Voice Module Initialized
```

4. 음성 모듈에 명령어를 말하면 해당 ID가 표시됩니다:

```
IIC Voice Module Initialized
ID: 1
ID: 4
ID: 10
```

### 4. 코드 설명

```cpp
// Initialize I2C
IIC_Init();

// Read command ID
int commandId = IIC_ReadCommand();

// Set broadcast
IIC_SetCommandVoice(0x00);  // Command word broadcast
```

---

## UART 버전 사용

### 1. 프로젝트 열기

- Arduino IDE에서 `UART_Voice/UART_Voice.ino`를 엽니다

### 2. 코드 업로드

- 올바른 보드 모델을 선택합니다
- 올바른 포트를 선택합니다
- 업로드 버튼을 클릭합니다
- 업로드가 완료될 때까지 기다립니다

### 3. 테스트 실행

1. 시리얼 모니터를 엽니다
2. 보드 레이트를 **115200**으로 설정합니다
3. 정상적으로 시작되면 다음이 표시됩니다:

```
UART Voice Module Initialized
```

4. 음성 모듈에 명령어를 말하면 해당 ID가 표시됩니다:

```
UART Voice Module Initialized
ID: 1
ID: 4
ID: 10
```

### 4. 코드 설명

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

### Q1: 시리얼 모니터에 출력이 없음

**A: 다음을 확인하십시오:**
- 시리얼 보드 레이트가 115200인지 확인합니다
- 올바른 포트를 선택했는지 확인합니다
- TX/RX가 반대로 연결되지 않았는지 확인합니다
- GND가 연결되었는지 확인합니다

---

### Q2: I2C 버전에서 "IIC Read Error"가 표시됨

**A: I2C 연결을 확인하십시오:**
- SDA/SCL이 반대로 연결되지 않았는지 확인합니다
- 장치 주소가 올바른지 확인합니다(0x2A)
- GND가 연결되었는지 확인합니다

---

### Q3: 명령 ID가 0 또는 255만 표시됨

**A: 정상 동작입니다:**
- 0 = 유효한 명령이 인식되지 않음
- 255 = 새로운 데이터 없음
- 정상적으로 인식된 후에만 유효한 ID가 출력됩니다

---

### Q4: 인식 정확도가 높지 않음

**A: 최적화 제안:**
- 조용한 환경을 유지하고 배경 소음이 너무 크지 않도록 합니다
- 마이크와 적절한 거리를 유지합니다(10-50cm)
- 적당한 속도로 명확하게 발음합니다

---

### Q5: UART 버전에서 데이터를 수신하지 못함

**A: 확인하십시오:**
- 음성 모듈 TX가 Arduino D10 (RX)에 연결되었는지 확인합니다
- 음성 모듈 RX가 Arduino D11 (TX)에 연결되었는지 확인합니다
- 보드 레이트가 115200인지 확인합니다

---

## 기술 지원

문제가 발생하면 다음을 확인하십시오:
1. 하드웨어 연결이 올바른지
2. 시리얼 보드 레이트가 일치하는지
3. I2C 주소가 올바른지
4. GND가 연결되었는지(매우 중요합니다!)
