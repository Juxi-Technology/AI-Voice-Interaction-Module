[English](../../../../en/06-multi-host/arduino/uart/README.md) | [Deutsch](../../../../de/06-multi-host/arduino/uart/README.md) | Español | [Français](../../../../fr/06-multi-host/arduino/uart/README.md) | [Italiano](../../../../it/06-multi-host/arduino/uart/README.md) | [日本語](../../../../ja/06-multi-host/arduino/uart/README.md) | [한국어](../../../../ko/06-multi-host/arduino/uart/README.md) | [Português (BR)](../../../../pt-br/06-multi-host/arduino/uart/README.md) | [Português (PT)](../../../../pt-pt/06-multi-host/arduino/uart/README.md) | [简体中文](../../../../zh-hans/06-multi-host/arduino/uart/README.md) | [繁體中文](../../../../zh-hant/06-multi-host/arduino/uart/README.md)

# Tutorial de la versión BSP del módulo de voz UART

## 📁 Estructura de archivos

```
uart/
├── uart.ino    # 主程序
├── bsp_uart.hpp         # 头文件（协议帧和函数声明）
├── bsp_uart.cpp         # 实现文件
└── README.md              # 本教程
```

---

## 🔌 Conexión de hardware

### Conexión al módulo de voz
| Arduino | Módulo de voz |
|---------|----------|
| D10 (RX) | TX |
| D11 (TX) | RX |
| GND | GND |
| 5V | 5V |

> 💡 **Nota:** ¡RX y TX deben conectarse de forma cruzada!

---

## 🔧 Compilar y subir

### Paso 1: Abrir el Arduino IDE
1. Abre el archivo `UART_Voice.ino`
2. Selecciona tu modelo de placa (por ejemplo, Arduino Uno)
3. Selecciona el puerto serie correspondiente

### Paso 2: Compilar y subir
1. Haz clic en el botón ✔️ para compilar
2. Haz clic en el botón ➡️ para subir a la placa

---

## 📡 Prueba serie

### Abre el Monitor Serie en el Arduino IDE
- Velocidad en baudios: **115200**
- Fin de línea: **Ninguno**

### Salida esperada

Tras encender, deberías ver:
```
UART Voice Module Initialized
```

Di la palabra de activación y la palabra de comando al módulo y emitirá el ID correspondiente:
```
ID: 1
ID: 2
ID: 10
```

---

## 📚 Formato de trama del protocolo

| Byte | Contenido | Descripción |
|------|------|------|
| 1 | 0xFE | Cabecera de trama 1 |
| 2 | 0xEF | Cabecera de trama 2 |
| 3 | Código de función | 0xD1 = reproducción pasiva, 0xD2 = palabra de función, 0xD3 = palabra de comando |
| 4 | Datos | ID de comando o ID de reproducción |
| 5 | 0xEE | Cola de trama |

**Ejemplo:** Leer el ID de comando = 10
```
FE EF 00 0A EE
```

**Ejemplo:** Enviar reproducción de palabra de comando
```
FE EF D3 00 EE
```

---

## 📚 Referencia de la interfaz BSP

### 1. UART_Init()
```cpp
void UART_Init(void);
```
**Función**: Inicializa el puerto serie (velocidad en baudios 115200)

**Ejemplo**:
```cpp
void setup() {
  UART_Init();
}
```

---

### 2. UART_ReadCommand()
```cpp
int UART_ReadCommand(void);
```
**Función**: Lee el ID de comando reconocido por el módulo de voz

**Valor de retorno**:
- `0` - no se ha reconocido ningún comando
- `1~254` - ID del comando
- `-1` - no hay datos nuevos

**Ejemplo**:
```cpp
int id = UART_ReadCommand();
if (id > 0) {
  Serial.print("识别到命令: ");
  Serial.println(id);
}
```

---

### 3. UART_SetPassiveVoice()
```cpp
void UART_SetPassiveVoice(uint8_t voiceID);
```
**Función**: Establece la voz de reproducción pasiva

**Parámetro**:
- `0x00` - tipo de voz de reproducción pasiva

**Ejemplo**:
```cpp
UART_SetPassiveVoice(0x00);
delay(200);
```

---

### 4. UART_SetFunctionVoice()
```cpp
void UART_SetFunctionVoice(uint8_t voiceID);
```
**Función**: Establece la voz de reproducción de palabra de función

**Parámetro**:
- `0x00` - tipo de voz de reproducción de palabra de función

**Ejemplo**:
```cpp
UART_SetFunctionVoice(0x00);
delay(200);
```

---

### 5. UART_SetCommandVoice()
```cpp
void UART_SetCommandVoice(uint8_t voiceID);
```
**Función**: Establece la voz de reproducción de palabra de comando

**Parámetro**:
- `0x00` - tipo de voz de reproducción de palabra de comando

**Ejemplo**:
```cpp
UART_SetCommandVoice(0x00);
delay(200);
```

---

## 🎯 Lógica del programa principal

```cpp
void setup() {
  Serial.begin(115200);
  UART_Init();
  
  Serial.println("UART Voice Module Initialized");
  
  UART_SetCommandVoice(0x00);  // 上电播报命令词语音
  delay(200);
}

void loop() {
  int commandId = UART_ReadCommand();
  
  if (commandId >= 0) {
    // 过滤无效值，防止重复输出
    if (commandId != 0 && commandId != 255 && commandId != lastCommandId) {
      Serial.print("ID: ");
      Serial.println(commandId);
      lastCommandId = commandId;
      
      // 示例：根据识别到的命令控制播报
      if (commandId == 1) {
        UART_SetCommandVoice(0x00);  // 识别到命令1，播报命令词语音
      } else if (commandId == 2) {
        UART_SetCommandVoice(0x00);  // 识别到命令2，播报命令词语音
      }
    } else if (commandId == 0 || commandId == 255) {
      if (lastCommandId != 0) {
        lastCommandId = 0;  // 重置状态
      }
    }
  }
  
  delay(50);
}
```

---

## 🔍 Preguntas frecuentes

### Q1: No hay salida en absoluto

**Posibles causas:**
1. RX/TX están invertidos
2. GND no es masa común
3. Módulo sin alimentación
4. Velocidad en baudios incorrecta

**Soluciones:**
- Confirma que D10 se conecta al TX del módulo y D11 al RX del módulo (conexión cruzada)
- Confirma la conexión de GND
- Confirma que la alimentación de 5V es normal
- Confirma que la velocidad en baudios del puerto serie es 115200

---

### Q2: El monitor serie solo muestra caracteres ilegibles

**Posibles causas:**
1. Discrepancia en la velocidad en baudios
2. Encendido anómalo del módulo

**Soluciones:**
- Confirma que la velocidad en baudios del monitor serie es 115200
- Pulsa una vez el botón de reinicio del módulo

---

### Q3: La salida muestra "ID: 255" o "ID: 0"

**Explicación:** Esto es normal
- `0` = no se ha reconocido ningún comando
- `255` = no hay datos nuevos

Estos valores ya se filtran en el código, por lo que normalmente no se emiten. Si los ves, significa que el código no está surtiendo efecto.

---

## 💡 Ventajas de la arquitectura BSP

### 1. Capas de código claras
- **bsp_uart.hpp** - solo declaraciones, sin implementación
- **bsp_uart.cpp** - detalles concretos de implementación
- **UART_Voice.ino** - solo se ocupa de la lógica de negocio

### 2. Fácil de portar
Si cambias a otra plataforma (por ejemplo, STM32, ESP32), solo necesitas modificar la implementación en `bsp_uart.cpp`; el programa principal no necesita cambios.

### 3. Fácil de mantener
Los cambios en el código relacionado con UART quedan confinados en `bsp_uart.cpp`: se corrige una vez y es efectivo en todas partes.

---

## 🚀 Ejemplos de funciones ampliadas

### Ejemplo 1: Activar distintas reproducciones según distintos comandos
```cpp
if (commandId == 1) {
  UART_SetCommandVoice(0x00);      // 播报命令词
} else if (commandId == 2) {
  UART_SetFunctionVoice(0x00);     // 播报功能词
} else if (commandId == 3) {
  UART_SetPassiveVoice(0x00);      // 播报被动语
}
```

### Ejemplo 2: Controlar un LED
```cpp
if (commandId == 10) {
  digitalWrite(LED_PIN, LOW);    // 关灯
  UART_SetCommandVoice(0x00);     // 播报确认
}
```

### Ejemplo 3: Controlar un motor
```cpp
if (commandId == 11) {
  motor_stop();
  UART_SetCommandVoice(0x00);     // 播报确认
}
```
