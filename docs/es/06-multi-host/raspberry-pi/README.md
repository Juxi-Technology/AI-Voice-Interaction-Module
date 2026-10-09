[English](../../../en/06-multi-host/raspberry-pi/README.md) | [Deutsch](../../../de/06-multi-host/raspberry-pi/README.md) | Español | [Français](../../../fr/06-multi-host/raspberry-pi/README.md) | [Italiano](../../../it/06-multi-host/raspberry-pi/README.md) | [日本語](../../../ja/06-multi-host/raspberry-pi/README.md) | [한국어](../../../ko/06-multi-host/raspberry-pi/README.md) | [Português (BR)](../../../pt-br/06-multi-host/raspberry-pi/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/raspberry-pi/README.md) | [简体中文](../../../zh-hans/06-multi-host/raspberry-pi/README.md) | [繁體中文](../../../zh-hant/06-multi-host/raspberry-pi/README.md)

# Guía de usuario del módulo de interacción por voz para Raspberry Pi

## Instalar dependencias

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## Activar la interfaz I2C

```bash
sudo raspi-config
```

Selecciona `Interface Options` -> `I2C` -> `Yes`

Reinicia la Raspberry Pi

## Versión IIC

### Ubicación del archivo
`IIC_Voice/iic_voice.py`

### Instrucciones de cableado

| Raspberry Pi | Módulo de voz |
|--------------|--------------|
| GPIO2 (SDA) | SDA |
| GPIO3 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

### Ejecutar

```bash
cd IIC_Voice
python3 iic_voice.py
```

### Formato de salida

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## Versión UART

### Ubicación del archivo
`UART_Voice/uart_voice.py`

### Activar el puerto serie

Edita `/boot/firmware/config.txt` o `/boot/config.txt`, y asegúrate de la siguiente configuración:

```
enable_uart=1
dtoverlay=disable-bt
```

A continuación, reinicia la Raspberry Pi.

```bash
sudo reboot
```

### Instrucciones de cableado

#### Uso de conexión directa mediante Type-C

Al usar la conexión directa por Type-C a la Raspberry Pi, descomenta `SERIAL_PORT = '/dev/ttyUSB0'` y comenta `SERIAL_PORT = '/dev/ttyAMA0'`

#### Uso de los pines UART

| Raspberry Pi | Módulo de voz |
|--------------|--------------|
| GPIO14 (TXD) | RX |
| GPIO15 (RXD) | TX |
| GND | GND |
| 5V | 5V |

Comenta `SERIAL_PORT = '/dev/ttyUSB0'`

Descomenta `SERIAL_PORT = '/dev/ttyAMA0'`

### Ejecutar

```bash
cd UART_Voice
python3 uart_voice.py
```

### Formato de salida

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## Descripción del protocolo

### Protocolo UART

| Byte | Contenido |
|------|---------|
| 1 | 0xFE (cabecera de trama) |
| 2 | 0xEF (cabecera de trama) |
| 3 | ID de palabra de función |
| 4 | ID de palabra de comando |
| 5 | 0xEE (fin de trama) |

### Protocolo IIC

- Dirección del dispositivo: 0x2A
- Registro de lectura: 0xDA (leer 1 byte)
  - 0x00: no reconocido
  - Otro: ID de palabra de comando
