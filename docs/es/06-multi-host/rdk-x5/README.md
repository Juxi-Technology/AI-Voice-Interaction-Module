[English](../../../en/06-multi-host/rdk-x5/README.md) | [Deutsch](../../../de/06-multi-host/rdk-x5/README.md) | Español | [Français](../../../fr/06-multi-host/rdk-x5/README.md) | [Italiano](../../../it/06-multi-host/rdk-x5/README.md) | [日本語](../../../ja/06-multi-host/rdk-x5/README.md) | [한국어](../../../ko/06-multi-host/rdk-x5/README.md) | [Português (BR)](../../../pt-br/06-multi-host/rdk-x5/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/rdk-x5/README.md) | [简体中文](../../../zh-hans/06-multi-host/rdk-x5/README.md) | [繁體中文](../../../zh-hant/06-multi-host/rdk-x5/README.md)

# Módulo de interacción por voz con IA - Guía de usuario de RDK X5 (Python)

## Índice

1. [Introducción](#introducción)
2. [Conexión de hardware](#conexión-de-hardware)
3. [Configuración del entorno](#configuración-del-entorno)
4. [Uso de la versión IIC](#uso-de-la-versión-iic)
5. [Uso de la versión UART](#uso-de-la-versión-uart)
6. [Preguntas frecuentes](#faq)

---

## Introducción

Este repositorio proporciona código de ejemplo en Python para que la plataforma RDK X5 (Raspberry Pi) se comunique con el módulo de interacción por voz con IA, compatible tanto con el método de comunicación I2C como con el UART.

- **Módulo de reconocimiento de voz**: Admite reconocimiento de voz offline y emite el ID del comando tras el reconocimiento
- **Función de reproducción**: Admite reproducción pasiva, reproducción de palabras de función y reproducción de palabras de comando
- **Protocolo de comunicación**: Dirección I2C 0x2A, velocidad en baudios UART 115200
- **Lenguaje de programación**: Python 3

---

## Conexión de hardware

### Conexión general

| Pin de RDK X5 | Módulo de voz | Descripción |
|------------|-------------|-------------|
| 5V (Pin 2/4) | 5V | Alimentación positiva |
| GND (Pin 6/9) | GND | Masa de alimentación |

> **Importante**: ¡Asegúrate de que todos los dispositivos compartan una masa común!

---

### Conexión de la versión I2C

| Pin de RDK X5 | Módulo de voz | Descripción |
|------------|-------------|-------------|
| SDA (GPIO3, Pin 3) | SDA | Línea de datos I2C |
| SCL (GPIO5, Pin 5) | SCL | Línea de reloj I2C |

**Nota**: Utiliza el bus I2C 5 por defecto (numeración BCM)

---

### Conexión de la versión UART

| Pin de RDK X5 | Módulo de voz | Descripción |
|------------|-------------|-------------|
| GPIO14 (TXD, Pin 8) | RX | Transmisión serie |
| GPIO15 (RXD, Pin 10) | TX | Recepción serie |

**Nota**: Utiliza el dispositivo serie `/dev/ttyAMA0` por defecto

---

### Conexión mediante cable Type-C (alternativa a UART)

Si se utiliza un módulo adaptador USB-TTL:

| RDK X5 | Módulo USB-TTL | Módulo de voz |
|--------|---------------|-------------|
| Puerto USB | USB | - |
| - | RX | TX |
| - | TX | RX |
| GND | GND | GND |

**Nota**: En este caso, el dispositivo serie suele ser `/dev/ttyUSB0`

---

## Configuración del entorno

### 1. Requisitos del sistema

- RDK X5 (o Raspberry Pi 3/4/5)
- Sistema Ubuntu / Debian
- Python 3.7+

### 2. Instalar dependencias

```bash
# Update packages
sudo apt update
sudo apt upgrade -y

# Install Python libraries
sudo apt install -y python3-pip python3-smbus i2c-tools

# Install pyserial
pip3 install pyserial
```

### 3. Activar la interfaz I2C

```bash
# Open configuration tool
sudo raspi-config

# Select Interface Options → I2C → Enable
# Reboot to take effect
sudo reboot
```

### 4. Activar la interfaz serie

```bash
# Open configuration tool
sudo raspi-config

# Select Interface Options → Serial
# Select: No (shell) → Yes (hardware serial port)
# Reboot to take effect
sudo reboot
```

### 5. Probar las interfaces de hardware

```bash
# Test I2C device
sudo i2cdetect -y 5

# Test serial port
ls /dev/ttyAMA0
ls /dev/ttyUSB0  # If using USB-TTL
```

---

## Uso de la versión IIC

### 1. Comprobar los archivos de código

```bash
cd IIC_Voice
ls -la
# Should see iic_voice.py
```

### 2. Configurar el bus I2C

Edita el archivo `iic_voice.py` y modifica los parámetros según sea necesario:

```python
# I2C device address
DEVICE_ADDRESS = 0x2A

# Register address
REG_RESULT = 0xDA

# I2C bus number (modify according to actual connection)
bus = smbus.SMBus(5)  # I2C bus 5
```

### 3. Ejecutar el programa

```bash
# Make executable
chmod +x iic_voice.py

# Run (sudo required for I2C access)
sudo python3 iic_voice.py
```

### 4. Ejecutar la prueba

Tras un arranque normal, mostrará:

```
Speech Serial Opened! Baudrate=115200
```

Di palabras de comando al módulo de voz y se mostrarán los ID correspondientes:

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. Detener el programa

Pulsa `Ctrl + C` para detener el programa:

```
Program terminated
```

---

## Uso de la versión UART

### 1. Comprobar los archivos de código

```bash
cd UART_Voice
ls -la
# Should see uart_voice.py
```

### 2. Configurar el puerto serie

Edita el archivo `uart_voice.py` y modifica el dispositivo serie:

```python
# UART direct connection (default)
SERIAL_PORT = '/dev/ttyAMA0'

# Or use USB-TTL
# SERIAL_PORT = '/dev/ttyUSB0'

# Baud rate
BAUD_RATE = 115200
```

### 3. Ejecutar el programa

```bash
# Make executable
chmod +x uart_voice.py

# Run (sudo required for serial port access)
sudo python3 uart_voice.py
```

### 4. Ejecutar la prueba

Tras un arranque normal, mostrará:

```
Speech Serial Opened! Baudrate=115200
```

Di palabras de comando al módulo de voz y se mostrarán los ID correspondientes:

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. Detener el programa

Pulsa `Ctrl + C` para detener el programa

---

## Preguntas frecuentes

### Q1: Permisos insuficientes para operar con I2C

**R: Añade el usuario al grupo de usuarios de I2C:**
```bash
sudo usermod -aG i2c $USER
# Re-login to take effect
```
O ejecuta con `sudo`

---

### Q2: No se encuentra el dispositivo serie

**R: Comprueba:**
1. Si el puerto serie está activado (raspi-config)
2. Si el nombre del dispositivo es correcto
   - UART directo: `/dev/ttyAMA0`
   - USB-TTL: `/dev/ttyUSB0` o `/dev/ttyUSB1`
3. Si la conexión de hardware es correcta
4. Si el puerto serie está ocupado por otros programas

```bash
# List available serial ports
ls /dev/tty* | grep tty
```

---

### Q3: El dispositivo I2C no se detecta en el escaneo

**R: Comprueba:**
1. Confirma que I2C está activado (raspi-config)
2. Comprueba si SDA/SCL están invertidos
3. Comprueba si la masa común está conectada
4. Comprueba si el dispositivo está encendido

```bash
# Scan I2C devices
sudo i2cdetect -y 5
```

Si ves 0x2A, la conexión del dispositivo es correcta

---

### Q4: El ID del comando solo muestra 0 o nada

**R: Comportamiento normal:**
- 0 = No se ha reconocido ningún comando válido
- Los ID solo se emiten cuando se pronuncian palabras de comando válidas
- Despierta primero el módulo y luego di el comando

---

### Q5: La precisión de reconocimiento no es alta

**R: Sugerencias de optimización:**
- Asegura un entorno silencioso, con no demasiado ruido de fondo
- Mantén una distancia adecuada respecto al micrófono (10-50 cm)
- Habla a una velocidad moderada y con una pronunciación clara

---

### Q6: Comunicación serie anómala

**R: Comprueba:**
1. ¿Están TX/RX conectados de forma cruzada correctamente? (TX del módulo → RX de la RPi)
2. ¿La velocidad en baudios es 115200?
3. ¿Está conectada la masa común?
4. ¿Está el puerto serie ocupado por otros procesos?

```bash
# Check serial port occupancy
sudo lsof /dev/ttyAMA0
```

---

## Soporte técnico

Si encuentras problemas, comprueba:
1. Que la conexión de hardware sea correcta (¡la masa común es muy importante!)
2. Que la velocidad en baudios del puerto serie sea 115200
3. Que la dirección I2C sea correcta (0x2A)
4. Que tengas permisos suficientes para acceder a las interfaces de hardware

```bash
# Useful debugging commands
ls -l /dev/i2c*      # List I2C devices
ls -l /dev/ttyAMA0   # List serial device
groups                # List user group permissions
```
