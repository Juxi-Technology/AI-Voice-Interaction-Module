[English](../../../../en/06-multi-host/arduino/iic/README.md) | [Deutsch](../../../../de/06-multi-host/arduino/iic/README.md) | Español | [Français](../../../../fr/06-multi-host/arduino/iic/README.md) | [Italiano](../../../../it/06-multi-host/arduino/iic/README.md) | [日本語](../../../../ja/06-multi-host/arduino/iic/README.md) | [한국어](../../../../ko/06-multi-host/arduino/iic/README.md) | [Português (BR)](../../../../pt-br/06-multi-host/arduino/iic/README.md) | [Português (PT)](../../../../pt-pt/06-multi-host/arduino/iic/README.md) | [简体中文](../../../../zh-hans/06-multi-host/arduino/iic/README.md) | [繁體中文](../../../../zh-hant/06-multi-host/arduino/iic/README.md)

# Tutorial de la versión BSP del módulo de voz IIC

## 📁 Estructura de archivos

```
iic/
├── iic.ino    # 主程序
├── bsp_iic.hpp         # 头文件（地址和函数声明）
├── bsp_iic.cpp         # 实现文件
└── README.md            # 本教程
```

---

## 🔌 Conexión de hardware

| Arduino | Módulo de voz |
|---------|----------|
| A4 (SDA) | SDA |
| A5 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

---

## 🔧 Compilar y subir

### Paso 1: Abrir el Arduino IDE
1. Abre el archivo `IIC_Voice.ino`
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
IIC Voice Module Initialized
```

Di la palabra de activación y la palabra de comando al módulo y emitirá el ID correspondiente:
```
ID: 1
ID: 2
ID: 10
```

---

## 📚 Mapa de registros

| Registro | Dirección | Función | Descripción |
|--------|------|------|------|
| REG_RESULT | 0xDA | Leer el ID del comando | Lee 1 byte, 0 = no reconocido |
| REG_PASSIVE | 0xD1 | Escribir reproducción pasiva | Escribe 1 byte, 0x00 = voz de reproducción pasiva |
| REG_FUNCTION | 0xD2 | Escribir reproducción de palabra de función | Escribe 1 byte, 0x00 = voz de reproducción de palabra de función |
| REG_COMMAND | 0xD3 | Escribir reproducción de palabra de comando | Escribe 1 byte, 0x00 = voz de reproducción de palabra de comando |

---

## 📚 Referencia de la interfaz BSP

### 1. IIC_Init()
```cpp
void IIC_Init(void);
```
**Función**: Inicializa el bus I2C

**Ejemplo**:
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
**Función**: Lee el ID de comando reconocido por el módulo de voz

**Valor de retorno**:
- `0` - no se ha reconocido ningún comando
- `1~254` - ID del comando
- `-1` - error de comunicación

**Ejemplo**:
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
**Función**: Establece la voz de reproducción pasiva

**Parámetro**:
- `0x00` - tipo de voz de reproducción pasiva

**Ejemplo**:
```cpp
IIC_SetPassiveVoice(0x00);
delay(200);
```

---

### 4. IIC_SetFunctionVoice()
```cpp
void IIC_SetFunctionVoice(uint8_t voiceID);
```
**Función**: Establece la voz de reproducción de palabra de función

**Parámetro**:
- `0x00` - tipo de voz de reproducción de palabra de función

**Ejemplo**:
```cpp
IIC_SetFunctionVoice(0x00);
delay(200);
```

---

### 5. IIC_SetCommandVoice()
```cpp
void IIC_SetCommandVoice(uint8_t voiceID);
```
**Función**: Establece la voz de reproducción de palabra de comando

**Parámetro**:
- `0x00` - tipo de voz de reproducción de palabra de comando

**Ejemplo**:
```cpp
IIC_SetCommandVoice(0x00);
delay(200);
```

---

## 🎯 Lógica del programa principal

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

## 🔍 Preguntas frecuentes

### Q1: El monitor serie solo muestra "IIC Read Error"

**Posibles causas:**
1. Cableado incorrecto, o sin conexión
2. Módulo sin alimentación
3. Dirección I2C incorrecta

**Soluciones:**
- Comprueba si SDA/SCL están invertidos
- Comprueba si GND es masa común
- Comprueba si la alimentación de 5V es normal
- Usa un programa escáner de I2C para confirmar la dirección del dispositivo

---

### Q2: No hay salida en absoluto

**Posibles causas:**
1. Velocidad en baudios del puerto serie incorrecta
2. Módulo sin despertar

**Soluciones:**
- Confirma que la velocidad en baudios del puerto serie es 115200
- Di primero la palabra de activación y después la palabra de comando

---

### Q3: La salida muestra "ID: 255" o "ID: 0"

**Explicación:** Esto es normal

- `0` = no se ha reconocido ningún comando
- `255` = no hay datos nuevos

Estos valores ya se filtran en el código, por lo que normalmente no se emiten. Si los ves, significa que el código no está surtiendo efecto.

---

## 💡 Ventajas de la arquitectura BSP

### 1. Capas de código claras
- **bsp_iic.hpp** - solo declaraciones, sin implementación
- **bsp_iic.cpp** - detalles concretos de implementación
- **IIC_Voice.ino** - solo se ocupa de la lógica de negocio

### 2. Fácil de portar
Si cambias a otra plataforma (por ejemplo, STM32, ESP32), solo necesitas modificar la implementación en `bsp_iic.cpp`; el programa principal no necesita cambios.

### 3. Fácil de mantener
Los cambios en el código relacionado con I2C quedan confinados en `bsp_iic.cpp`: se corrige una vez y es efectivo en todas partes.

---

## 🚀 Ejemplos de funciones ampliadas

### Ejemplo 1: Activar distintas reproducciones según distintos comandos
```cpp
if (commandId == 1) {
  IIC_SetCommandVoice(0x00);      // 播报命令词
} else if (commandId == 2) {
  IIC_SetFunctionVoice(0x00);     // 播报功能词
} else if (commandId == 3) {
  IIC_SetPassiveVoice(0x00);      // 播报被动语
}
```

### Ejemplo 2: Controlar un LED
```cpp
if (commandId == 10) {
  digitalWrite(LED_PIN, LOW);    // 关灯
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```

### Ejemplo 3: Controlar un motor
```cpp
if (commandId == 11) {
  motor_stop();
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```
