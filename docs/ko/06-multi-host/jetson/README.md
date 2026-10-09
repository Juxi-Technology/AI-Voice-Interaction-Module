[English](../../../en/06-multi-host/jetson/README.md) | [Deutsch](../../../de/06-multi-host/jetson/README.md) | [Español](../../../es/06-multi-host/jetson/README.md) | [Français](../../../fr/06-multi-host/jetson/README.md) | [Italiano](../../../it/06-multi-host/jetson/README.md) | [日本語](../../../ja/06-multi-host/jetson/README.md) | 한국어 | [Português (BR)](../../../pt-br/06-multi-host/jetson/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/jetson/README.md) | [简体中文](../../../zh-hans/06-multi-host/jetson/README.md) | [繁體中文](../../../zh-hant/06-multi-host/jetson/README.md)

# Jetson 음성 상호작용 모듈 사용 가이드

## 의존성 설치

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## 사용자 그룹 확인

```bash
sudo usermod -aG i2c $USER
sudo usermod -aG dialout $USER
```

로그아웃한 후 다시 로그인해야 변경 사항이 적용됩니다.

## IIC 버전

### 파일 위치
`IIC_Voice/iic_voice.py`

### 배선 안내

| Jetson | 음성 모듈 |
|--------|--------------|
| Pin 27 (I2C1 SDA) | SDA |
| Pin 28 (I2C1 SCL) | SCL |
| Pin 6 (GND) | GND |
| Pin 4 (5V) | 5V |

### I2C 장치 확인

```bash
sudo i2cdetect -y -r 1
```

주소 0x2A가 표시되어야 합니다

### 실행

```bash
cd IIC_Voice
python3 iic_voice.py
```

### 출력 형식

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## UART 버전

### 파일 위치
`UART_Voice/uart_voice.py`

### UART 핀을 통한 연결

UART 핀을 통해 모듈을 Jetson에 연결할 때는 `SERIAL_PORT = '/dev/ttyUSB0'`를 주석 처리하고 `SERIAL_PORT = '/dev/ttyTHS1'`의 주석을 해제합니다

#### 배선 안내

| Jetson | 음성 모듈 |
|--------|--------------|
| Pin 8 (UART1 TX) | RX |
| Pin 10 (UART1 RX) | TX |
| Pin 6 (GND) | GND |
| Pin 4 (5V) | 5V |

### 시리얼 포트 확인

```bash
ls /dev/ttyTHS*
```

### 실행

```bash
cd UART_Voice
python3 uart_voice.py
```

### 출력 형식

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

### Type-C 케이블을 통한 연결

Type-C 케이블을 통해 모듈을 Jetson에 연결할 때는 `SERIAL_PORT = '/dev/ttyUSB0'`의 주석을 해제하고 `SERIAL_PORT = '/dev/ttyTHS1'`를 주석 처리합니다

### 시리얼 포트 확인

```bash
ls /dev/ttyUSB*
```

### 실행

```bash
cd UART_Voice
python3 uart_voice.py
```

### 출력 형식

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## FAQ

### I2C 권한 문제

```bash
sudo chmod 666 /dev/i2c-1
```

### 시리얼 포트 점유됨

시리얼 포트를 열 수 없으면 다른 서비스가 점유하고 있는지 확인하십시오:

```bash
sudo systemctl stop nvgetty
sudo systemctl disable nvgetty
```

## 프로토콜 설명

### UART 프로토콜

| 바이트 | 내용 |
|------|---------|
| 1 | 0xFE (프레임 헤더) |
| 2 | 0xEF (프레임 헤더) |
| 3 | 기능어 ID |
| 4 | 명령어 ID |
| 5 | 0xEE (프레임 종료) |

### IIC 프로토콜

- 장치 주소: 0x2A
- 읽기 레지스터: 0xDA (1바이트 읽기)
  - 0x00: 미인식
  - 기타: 명령어 ID
