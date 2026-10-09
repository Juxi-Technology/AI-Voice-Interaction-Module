[English](../../../en/06-multi-host/jetson/README.md) | [Deutsch](../../../de/06-multi-host/jetson/README.md) | Español | [Français](../../../fr/06-multi-host/jetson/README.md) | [Italiano](../../../it/06-multi-host/jetson/README.md) | [日本語](../../../ja/06-multi-host/jetson/README.md) | [한국어](../../../ko/06-multi-host/jetson/README.md) | [Português (BR)](../../../pt-br/06-multi-host/jetson/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/jetson/README.md) | [简体中文](../../../zh-hans/06-multi-host/jetson/README.md) | [繁體中文](../../../zh-hant/06-multi-host/jetson/README.md)

# Guía de usuario del módulo de interacción por voz para Jetson

## Instalar dependencias

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## Comprobar los grupos de usuarios

```bash
sudo usermod -aG i2c $USER
sudo usermod -aG dialout $USER
```

Cierra sesión y vuelve a iniciarla para que los cambios surtan efecto.

## Versión IIC

### Ubicación del archivo
`IIC_Voice/iic_voice.py`

### Instrucciones de cableado

| Jetson | Módulo de voz |
|--------|--------------|
| Pin 27 (I2C1 SDA) | SDA |
| Pin 28 (I2C1 SCL) | SCL |
| Pin 6 (GND) | GND |
| Pin 4 (5V) | 5V |

### Comprobar el dispositivo I2C

```bash
sudo i2cdetect -y -r 1
```

Deberías ver la dirección 0x2A

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

### Conexión mediante los pines UART

Al conectar el módulo al Jetson mediante los pines UART, comenta `SERIAL_PORT = '/dev/ttyUSB0'` y descomenta `SERIAL_PORT = '/dev/ttyTHS1'`

#### Instrucciones de cableado

| Jetson | Módulo de voz |
|--------|--------------|
| Pin 8 (UART1 TX) | RX |
| Pin 10 (UART1 RX) | TX |
| Pin 6 (GND) | GND |
| Pin 4 (5V) | 5V |

### Comprobar el puerto serie

```bash
ls /dev/ttyTHS*
```

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

### Conexión mediante cable Type-C

Al conectar el módulo al Jetson mediante un cable Type-C, descomenta `SERIAL_PORT = '/dev/ttyUSB0'` y comenta `SERIAL_PORT = '/dev/ttyTHS1'`

### Comprobar el puerto serie

```bash
ls /dev/ttyUSB*
```

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

## Preguntas frecuentes

### Problema de permisos de I2C

```bash
sudo chmod 666 /dev/i2c-1
```

### Puerto serie ocupado

Si no se puede abrir el puerto serie, comprueba si está ocupado por otros servicios:

```bash
sudo systemctl stop nvgetty
sudo systemctl disable nvgetty
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
