[English](../../../en/06-multi-host/raspberry-pi/README.md) | [Deutsch](../../../de/06-multi-host/raspberry-pi/README.md) | [Español](../../../es/06-multi-host/raspberry-pi/README.md) | [Français](../../../fr/06-multi-host/raspberry-pi/README.md) | [Italiano](../../../it/06-multi-host/raspberry-pi/README.md) | [日本語](../../../ja/06-multi-host/raspberry-pi/README.md) | 한국어 | [Português (BR)](../../../pt-br/06-multi-host/raspberry-pi/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/raspberry-pi/README.md) | [简体中文](../../../zh-hans/06-multi-host/raspberry-pi/README.md) | [繁體中文](../../../zh-hant/06-multi-host/raspberry-pi/README.md)

# Raspberry Pi 음성 상호작용 모듈 사용 가이드

## 의존성 설치

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## I2C 인터페이스 활성화

```bash
sudo raspi-config
```

`Interface Options` -> `I2C` -> `Yes`를 선택합니다

Raspberry Pi를 재부팅합니다

## IIC 버전

### 파일 위치
`IIC_Voice/iic_voice.py`

### 배선 안내

| Raspberry Pi | 음성 모듈 |
|--------------|--------------|
| GPIO2 (SDA) | SDA |
| GPIO3 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

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

### 시리얼 포트 활성화

`/boot/firmware/config.txt` 또는 `/boot/config.txt`를 편집하여 다음 구성이 포함되도록 합니다:

```
enable_uart=1
dtoverlay=disable-bt
```

그런 다음 Raspberry Pi를 재부팅합니다.

```bash
sudo reboot
```

### 배선 안내

#### Type-C 직결 사용

Type-C로 Raspberry Pi에 직결할 때는 `SERIAL_PORT = '/dev/ttyUSB0'`의 주석을 해제하고 `SERIAL_PORT = '/dev/ttyAMA0'`를 주석 처리합니다

#### UART 핀 사용

| Raspberry Pi | 음성 모듈 |
|--------------|--------------|
| GPIO14 (TXD) | RX |
| GPIO15 (RXD) | TX |
| GND | GND |
| 5V | 5V |

`SERIAL_PORT = '/dev/ttyUSB0'`를 주석 처리합니다

`SERIAL_PORT = '/dev/ttyAMA0'`의 주석을 해제합니다

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
