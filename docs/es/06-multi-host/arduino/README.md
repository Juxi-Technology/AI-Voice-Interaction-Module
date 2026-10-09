[English](../../../en/06-multi-host/arduino/README.md) | [Deutsch](../../../de/06-multi-host/arduino/README.md) | Español | [Français](../../../fr/06-multi-host/arduino/README.md) | [Italiano](../../../it/06-multi-host/arduino/README.md) | [日本語](../../../ja/06-multi-host/arduino/README.md) | [한국어](../../../ko/06-multi-host/arduino/README.md) | [Português (BR)](../../../pt-br/06-multi-host/arduino/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/arduino/README.md) | [简体中文](../../../zh-hans/06-multi-host/arduino/README.md) | [繁體中文](../../../zh-hant/06-multi-host/arduino/README.md)

# Módulo de interacción por voz con IA - Guía de usuario de Arduino

## Índice

1. [Introducción](#introducción)
2. [Conexión de hardware](#conexión-de-hardware)
3. [Configuración del entorno de desarrollo](#configuración-del-entorno-de-desarrollo)
4. [Uso de la versión IIC](#uso-de-la-versión-iic)
5. [Uso de la versión UART](#uso-de-la-versión-uart)
6. [Preguntas frecuentes](#faq)

---

## Introducción

Este repositorio proporciona código de ejemplo para que la plataforma Arduino se comunique con el módulo de interacción por voz con IA, compatible tanto con el método de comunicación I2C como con el UART.

- **Módulo de reconocimiento de voz**: Admite reconocimiento de voz offline y emite el ID del comando tras el reconocimiento
- **Función de reproducción**: Admite reproducción pasiva, reproducción de palabras de función y reproducción de palabras de comando
- **Protocolo de comunicación**: Dirección I2C 0x2A, velocidad en baudios UART 115200

---

## Conexión de hardware

### Conexión general

| Pin de Arduino | Módulo de voz | Descripción |
|-------------|-------------|-------------|
| 5V | 5V | Alimentación positiva |
| GND | GND | Masa de alimentación |

---

### Conexión de la versión I2C

| Pin de Arduino | Módulo de voz | Descripción |
|-------------|-------------|-------------|
| A4 (SDA) | SDA | Línea de datos I2C |
| A5 (SCL) | SCL | Línea de reloj I2C |

---

### Conexión de la versión UART

| Pin de Arduino | Módulo de voz | Descripción |
|-------------|-------------|-------------|
| D10 (RX) | TX | Recepción serie (Software Serial) |
| D11 (TX) | RX | Transmisión serie (Software Serial) |

---

### Conexión de depuración serie

| Pin de Arduino | USB-TTL | Descripción |
|-------------|---------|-------------|
| TX (D1) | RX | Salida de depuración |
| RX (D0) | TX | Entrada de depuración (opcional) |
| GND | GND | Masa común |

---

## Configuración del entorno de desarrollo

### 1. Instalar Arduino IDE

- Descarga: https://www.arduino.cc/en/software
- Instala la versión más reciente

### 2. Instalar el paquete de soporte de placas

- Abre Arduino IDE
- Herramientas → Placa → Gestor de placas
- Busca e instala el paquete de soporte para tu placa Arduino
- Recomendado: Arduino Uno / Nano

---

## Uso de la versión IIC

### 1. Abrir el proyecto

- Abre `IIC_Voice/IIC_Voice.ino` en Arduino IDE

### 2. Subir el código

- Selecciona el modelo de placa correcto (Herramientas → Placa)
- Selecciona el puerto correcto (Herramientas → Puerto)
- Haz clic en el botón de subir (→)
- Espera a que finalice la subida

### 3. Ejecutar la prueba

1. Abre el Monitor Serie (Herramientas → Monitor Serie)
2. Ajusta la velocidad en baudios a **115200**
3. Tras un arranque normal, mostrará:

```
IIC Voice Module Initialized
```

4. Di palabras de comando al módulo de voz y se mostrarán los ID correspondientes:

```
IIC Voice Module Initialized
ID: 1
ID: 4
ID: 10
```

### 4. Explicación del código

```cpp
// Initialize I2C
IIC_Init();

// Read command ID
int commandId = IIC_ReadCommand();

// Set broadcast
IIC_SetCommandVoice(0x00);  // Command word broadcast
```

---

## Uso de la versión UART

### 1. Abrir el proyecto

- Abre `UART_Voice/UART_Voice.ino` en Arduino IDE

### 2. Subir el código

- Selecciona el modelo de placa correcto
- Selecciona el puerto correcto
- Haz clic en el botón de subir
- Espera a que finalice la subida

### 3. Ejecutar la prueba

1. Abre el Monitor Serie
2. Ajusta la velocidad en baudios a **115200**
3. Tras un arranque normal, mostrará:

```
UART Voice Module Initialized
```

4. Di palabras de comando al módulo de voz y se mostrarán los ID correspondientes:

```
UART Voice Module Initialized
ID: 1
ID: 4
ID: 10
```

### 4. Explicación del código

```cpp
// Initialize serial (Software Serial D10/D11)
UART_Init();

// Read command ID
int commandId = UART_ReadCommand();

// Set broadcast
UART_SetCommandVoice(0x00);  // Command word broadcast
```

---

## Preguntas frecuentes

### Q1: No hay salida en el Monitor Serie

**R: Comprueba lo siguiente:**
- Comprueba si la velocidad en baudios del puerto serie es 115200
- Comprueba si se ha seleccionado el puerto correcto
- Comprueba si TX/RX están invertidos
- Comprueba si GND está conectado

---

### Q2: La versión I2C muestra "IIC Read Error"

**R: Comprueba la conexión I2C:**
- Comprueba si SDA/SCL están invertidos
- Comprueba si la dirección del dispositivo es correcta (0x2A)
- Comprueba si GND está conectado

---

### Q3: El ID del comando solo muestra 0 o 255

**R: Comportamiento normal:**
- 0 = No se ha reconocido ningún comando válido
- 255 = No hay datos nuevos
- Los ID válidos solo se emiten tras un reconocimiento normal

---

### Q4: La precisión de reconocimiento no es alta

**R: Sugerencias de optimización:**
- Asegura un entorno silencioso, con no demasiado ruido de fondo
- Mantén una distancia adecuada respecto al micrófono (10-50 cm)
- Habla a una velocidad moderada y con una pronunciación clara

---

### Q5: La versión UART no recibe datos

**R: Comprueba:**
- Confirma que TX del módulo de voz está conectado a Arduino D10 (RX)
- Confirma que RX del módulo de voz está conectado a Arduino D11 (TX)
- Comprueba si la velocidad en baudios es 115200

---

## Soporte técnico

Si encuentras problemas, comprueba:
1. Que la conexión de hardware sea correcta
2. Que la velocidad en baudios del puerto serie coincida
3. Que la dirección I2C sea correcta
4. Que GND esté conectado (¡muy importante!)
