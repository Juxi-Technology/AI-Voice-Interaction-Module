[English](../../../en/06-multi-host/rdk-x5/README.md) | [Deutsch](../../../de/06-multi-host/rdk-x5/README.md) | [Español](../../../es/06-multi-host/rdk-x5/README.md) | [Français](../../../fr/06-multi-host/rdk-x5/README.md) | [Italiano](../../../it/06-multi-host/rdk-x5/README.md) | [日本語](../../../ja/06-multi-host/rdk-x5/README.md) | 한국어 | [Português (BR)](../../../pt-br/06-multi-host/rdk-x5/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/rdk-x5/README.md) | [简体中文](../../../zh-hans/06-multi-host/rdk-x5/README.md) | [繁體中文](../../../zh-hant/06-multi-host/rdk-x5/README.md)

# AI 음성 상호작용 모듈 - RDK X5 (Python) 사용 가이드

## 목차

1. [소개](#소개)
2. [하드웨어 연결](#하드웨어-연결)
3. [환경 설정](#환경-설정)
4. [IIC 버전 사용](#iic-버전-사용)
5. [UART 버전 사용](#uart-버전-사용)
6. [FAQ](#faq)

---

## 소개

이 저장소는 RDK X5(Raspberry Pi) 플랫폼에서 AI 음성 상호작용 모듈과 통신하기 위한 Python 예제 코드를 제공하며, I2C와 UART 두 가지 통신 방식을 모두 지원합니다.

- **음성 인식 모듈**: 오프라인 음성 인식을 지원하며, 인식 후 명령 ID를 출력합니다
- **방송 기능**: 수동 방송, 기능어 방송, 명령어 방송을 지원합니다
- **통신 프로토콜**: I2C 주소 0x2A, UART 보드 레이트 115200
- **프로그래밍 언어**: Python 3

---

## 하드웨어 연결

### 일반 연결

| RDK X5 핀 | 음성 모듈 | 설명 |
|------------|-------------|-------------|
| 5V (Pin 2/4) | 5V | 전원 양극 |
| GND (Pin 6/9) | GND | 전원 접지 |

> **중요**: 모든 장치가 공통 접지를 공유하도록 하십시오!

---

### I2C 버전 연결

| RDK X5 핀 | 음성 모듈 | 설명 |
|------------|-------------|-------------|
| SDA (GPIO3, Pin 3) | SDA | I2C 데이터선 |
| SCL (GPIO5, Pin 5) | SCL | I2C 클록선 |

**참고**: 기본적으로 I2C 버스 5를 사용합니다(BCM 번호 기준)

---

### UART 버전 연결

| RDK X5 핀 | 음성 모듈 | 설명 |
|------------|-------------|-------------|
| GPIO14 (TXD, Pin 8) | RX | 시리얼 송신 |
| GPIO15 (RXD, Pin 10) | TX | 시리얼 수신 |

**참고**: 기본적으로 `/dev/ttyAMA0` 시리얼 장치를 사용합니다

---

### Type-C 케이블 연결(UART 대안)

USB-TTL 어댑터 모듈을 사용하는 경우:

| RDK X5 | USB-TTL 모듈 | 음성 모듈 |
|--------|---------------|-------------|
| USB 포트 | USB | - |
| - | RX | TX |
| - | TX | RX |
| GND | GND | GND |

**참고**: 이 경우 시리얼 장치는 일반적으로 `/dev/ttyUSB0`입니다

---

## 환경 설정

### 1. 시스템 요구 사항

- RDK X5 (또는 Raspberry Pi 3/4/5)
- Ubuntu / Debian 시스템
- Python 3.7+

### 2. 의존성 설치

```bash
# Update packages
sudo apt update
sudo apt upgrade -y

# Install Python libraries
sudo apt install -y python3-pip python3-smbus i2c-tools

# Install pyserial
pip3 install pyserial
```

### 3. I2C 인터페이스 활성화

```bash
# Open configuration tool
sudo raspi-config

# Select Interface Options → I2C → Enable
# Reboot to take effect
sudo reboot
```

### 4. 시리얼 인터페이스 활성화

```bash
# Open configuration tool
sudo raspi-config

# Select Interface Options → Serial
# Select: No (shell) → Yes (hardware serial port)
# Reboot to take effect
sudo reboot
```

### 5. 하드웨어 인터페이스 테스트

```bash
# Test I2C device
sudo i2cdetect -y 5

# Test serial port
ls /dev/ttyAMA0
ls /dev/ttyUSB0  # If using USB-TTL
```

---

## IIC 버전 사용

### 1. 코드 파일 확인

```bash
cd IIC_Voice
ls -la
# Should see iic_voice.py
```

### 2. I2C 버스 구성

`iic_voice.py` 파일을 편집하여 필요에 따라 매개변수를 수정합니다:

```python
# I2C device address
DEVICE_ADDRESS = 0x2A

# Register address
REG_RESULT = 0xDA

# I2C bus number (modify according to actual connection)
bus = smbus.SMBus(5)  # I2C bus 5
```

### 3. 프로그램 실행

```bash
# Make executable
chmod +x iic_voice.py

# Run (sudo required for I2C access)
sudo python3 iic_voice.py
```

### 4. 테스트 실행

정상적으로 시작되면 다음이 표시됩니다:

```
Speech Serial Opened! Baudrate=115200
```

음성 모듈에 명령어를 말하면 해당 ID가 표시됩니다:

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. 프로그램 중지

`Ctrl + C`를 눌러 프로그램을 중지합니다:

```
Program terminated
```

---

## UART 버전 사용

### 1. 코드 파일 확인

```bash
cd UART_Voice
ls -la
# Should see uart_voice.py
```

### 2. 시리얼 포트 구성

`uart_voice.py` 파일을 편집하여 시리얼 장치를 수정합니다:

```python
# UART direct connection (default)
SERIAL_PORT = '/dev/ttyAMA0'

# Or use USB-TTL
# SERIAL_PORT = '/dev/ttyUSB0'

# Baud rate
BAUD_RATE = 115200
```

### 3. 프로그램 실행

```bash
# Make executable
chmod +x uart_voice.py

# Run (sudo required for serial port access)
sudo python3 uart_voice.py
```

### 4. 테스트 실행

정상적으로 시작되면 다음이 표시됩니다:

```
Speech Serial Opened! Baudrate=115200
```

음성 모듈에 명령어를 말하면 해당 ID가 표시됩니다:

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. 프로그램 중지

`Ctrl + C`를 눌러 프로그램을 중지합니다

---

## FAQ

### Q1: I2C 작업 권한 부족

**A: 사용자를 I2C 사용자 그룹에 추가합니다:**
```bash
sudo usermod -aG i2c $USER
# Re-login to take effect
```
또는 `sudo`로 실행합니다

---

### Q2: 시리얼 장치를 찾을 수 없음

**A: 확인하십시오:**
1. 시리얼 포트가 활성화되었는지 확인합니다(raspi-config)
2. 장치 이름이 올바른지 확인합니다
   - UART 직결: `/dev/ttyAMA0`
   - USB-TTL: `/dev/ttyUSB0` 또는 `/dev/ttyUSB1`
3. 하드웨어 연결이 올바른지 확인합니다
4. 시리얼 포트가 다른 프로그램에 의해 점유되었는지 확인합니다

```bash
# List available serial ports
ls /dev/tty* | grep tty
```

---

### Q3: 스캔에서 I2C 장치가 감지되지 않음

**A: 확인하십시오:**
1. I2C가 활성화되었는지 확인합니다(raspi-config)
2. SDA/SCL이 반대로 연결되지 않았는지 확인합니다
3. 공통 접지가 연결되었는지 확인합니다
4. 장치에 전원이 공급되는지 확인합니다

```bash
# Scan I2C devices
sudo i2cdetect -y 5
```

0x2A가 표시되면 장치 연결이 정상입니다

---

### Q4: 명령 ID가 0만 표시되거나 아무것도 표시되지 않음

**A: 정상 동작입니다:**
- 0 = 유효한 명령이 인식되지 않음
- 유효한 명령어를 말할 때만 ID가 출력됩니다
- 먼저 모듈을 깨운 다음 명령을 말합니다

---

### Q5: 인식 정확도가 높지 않음

**A: 최적화 제안:**
- 조용한 환경을 유지하고 배경 소음이 너무 크지 않도록 합니다
- 마이크와 적절한 거리를 유지합니다(10-50cm)
- 적당한 속도로 명확하게 발음합니다

---

### Q6: 시리얼 통신 이상

**A: 확인하십시오:**
1. TX/RX가 올바르게 교차 연결되었는지 확인합니다(모듈 TX → RPi RX)
2. 보드 레이트가 115200인지 확인합니다
3. 공통 접지가 연결되었는지 확인합니다
4. 시리얼 포트가 다른 프로세스에 의해 점유되었는지 확인합니다

```bash
# Check serial port occupancy
sudo lsof /dev/ttyAMA0
```

---

## 기술 지원

문제가 발생하면 다음을 확인하십시오:
1. 하드웨어 연결이 올바른지(공통 접지는 매우 중요합니다!)
2. 시리얼 보드 레이트가 115200인지
3. I2C 주소가 올바른지(0x2A)
4. 하드웨어 인터페이스에 접근할 권한이 충분한지

```bash
# Useful debugging commands
ls -l /dev/i2c*      # List I2C devices
ls -l /dev/ttyAMA0   # List serial device
groups                # List user group permissions
```
