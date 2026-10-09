[English](../../../../en/06-multi-host/arduino/uart/README.md) | Deutsch | [Español](../../../../es/06-multi-host/arduino/uart/README.md) | [Français](../../../../fr/06-multi-host/arduino/uart/README.md) | [Italiano](../../../../it/06-multi-host/arduino/uart/README.md) | [日本語](../../../../ja/06-multi-host/arduino/uart/README.md) | [한국어](../../../../ko/06-multi-host/arduino/uart/README.md) | [Português (BR)](../../../../pt-br/06-multi-host/arduino/uart/README.md) | [Português (PT)](../../../../pt-pt/06-multi-host/arduino/uart/README.md) | [简体中文](../../../../zh-hans/06-multi-host/arduino/uart/README.md) | [繁體中文](../../../../zh-hant/06-multi-host/arduino/uart/README.md)

# Tutorial zur BSP-Version des UART-Sprachmoduls

## 📁 Dateistruktur

```
uart/
├── uart.ino    # 主程序
├── bsp_uart.hpp         # 头文件（协议帧和函数声明）
├── bsp_uart.cpp         # 实现文件
└── README.md              # 本教程
```

---

## 🔌 Hardware-Anschluss

### Anschluss an das Sprachmodul
| Arduino | Sprachmodul |
|---------|----------|
| D10 (RX) | TX |
| D11 (TX) | RX |
| GND | GND |
| 5V | 5V |

> 💡 **Hinweis:** RX und TX müssen über Kreuz verbunden werden!

---

## 🔧 Kompilieren und Hochladen

### Schritt 1: Arduino IDE öffnen
1. Öffnen Sie die Datei `UART_Voice.ino`
2. Wählen Sie Ihr Board-Modell (z. B. Arduino Uno)
3. Wählen Sie die entsprechende serielle Schnittstelle

### Schritt 2: Kompilieren und Hochladen
1. Klicken Sie auf die Schaltfläche ✔️, um zu kompilieren
2. Klicken Sie auf die Schaltfläche ➡️, um auf das Board hochzuladen

---

## 📡 Serieller Test

### Den seriellen Monitor in der Arduino IDE öffnen
- Baudrate: **115200**
- Zeilenende: **None**

### Erwartete Ausgabe

Nach dem Einschalten sollten Sie Folgendes sehen:
```
UART Voice Module Initialized
```

Sprechen Sie das Weckwort und das Befehlswort zum Modul, und es gibt die entsprechende ID aus:
```
ID: 1
ID: 2
ID: 10
```

---

## 📚 Format des Protokollrahmens

| Byte | Inhalt | Beschreibung |
|------|------|------|
| 1 | 0xFE | Rahmenkopf 1 |
| 2 | 0xEF | Rahmenkopf 2 |
| 3 | Funktionscode | 0xD1 = passive Wiedergabe, 0xD2 = Funktionswort, 0xD3 = Befehlswort |
| 4 | Daten | Befehls-ID oder Wiedergabe-ID |
| 5 | 0xEE | Rahmenende |

**Beispiel:** Befehls-ID = 10 lesen
```
FE EF 00 0A EE
```

**Beispiel:** Befehlswort-Wiedergabe senden
```
FE EF D3 00 EE
```

---

## 📚 Referenz der BSP-Schnittstellen

### 1. UART_Init()
```cpp
void UART_Init(void);
```
**Funktion**: Initialisiert die serielle Schnittstelle (Baudrate 115200)

**Beispiel**:
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
**Funktion**: Liest die vom Sprachmodul erkannte Befehls-ID

**Rückgabewert**:
- `0` - kein Befehl erkannt
- `1~254` - Befehls-ID
- `-1` - keine neuen Daten

**Beispiel**:
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
**Funktion**: Legt die passive Wiedergabestimme fest

**Parameter**:
- `0x00` - Typ der passiven Wiedergabestimme

**Beispiel**:
```cpp
UART_SetPassiveVoice(0x00);
delay(200);
```

---

### 4. UART_SetFunctionVoice()
```cpp
void UART_SetFunctionVoice(uint8_t voiceID);
```
**Funktion**: Legt die Funktionswort-Wiedergabestimme fest

**Parameter**:
- `0x00` - Typ der Funktionswort-Wiedergabestimme

**Beispiel**:
```cpp
UART_SetFunctionVoice(0x00);
delay(200);
```

---

### 5. UART_SetCommandVoice()
```cpp
void UART_SetCommandVoice(uint8_t voiceID);
```
**Funktion**: Legt die Befehlswort-Wiedergabestimme fest

**Parameter**:
- `0x00` - Typ der Befehlswort-Wiedergabestimme

**Beispiel**:
```cpp
UART_SetCommandVoice(0x00);
delay(200);
```

---

## 🎯 Logik des Hauptprogramms

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

## 🔍 FAQ

### Q1: Überhaupt keine Ausgabe

**Mögliche Ursachen:**
1. RX/TX sind vertauscht
2. GND ist nicht mit der gemeinsamen Masse verbunden
3. Modul nicht mit Strom versorgt
4. Falsche Baudrate

**Lösungen:**
- Stellen Sie sicher, dass D10 mit TX des Moduls und D11 mit RX des Moduls verbunden ist (Überkreuzverbindung)
- Bestätigen Sie den GND-Anschluss
- Bestätigen Sie, dass die 5V-Stromversorgung normal ist
- Stellen Sie sicher, dass die serielle Baudrate 115200 beträgt

---

### Q2: Der serielle Monitor zeigt nur unlesbaren Zeichensalat

**Mögliche Ursachen:**
1. Baudrate stimmt nicht überein
2. Anormales Einschalten des Moduls

**Lösungen:**
- Stellen Sie sicher, dass die Baudrate des seriellen Monitors 115200 beträgt
- Drücken Sie einmal die Reset-Taste des Moduls

---

### Q3: Die Ausgabe zeigt „ID: 255“ oder „ID: 0“

**Erklärung:** Dies ist normal
- `0` = kein Befehl erkannt
- `255` = keine neuen Daten

Diese Werte werden bereits im Code herausgefiltert und daher normalerweise nicht ausgegeben. Wenn Sie sie dennoch sehen, greift der Code nicht.

---

## 💡 Vorteile der BSP-Architektur

### 1. Klare Code-Schichtung
- **bsp_uart.hpp** - nur Deklaration, keine Implementierung
- **bsp_uart.cpp** - konkrete Implementierungsdetails
- **UART_Voice.ino** - kümmert sich nur um die Geschäftslogik

### 2. Einfache Portierung
Wenn Sie auf eine andere Plattform wechseln (z. B. STM32, ESP32), müssen Sie nur die Implementierung in `bsp_uart.cpp` ändern; das Hauptprogramm muss nicht angepasst werden.

### 3. Einfache Wartung
Änderungen am UART-bezogenen Code sind auf `bsp_uart.cpp` beschränkt — einmal korrigieren, überall wirksam.

---

## 🚀 Beispiele für erweiterte Funktionen

### Beispiel 1: Unterschiedliche Wiedergaben je nach Befehl auslösen
```cpp
if (commandId == 1) {
  UART_SetCommandVoice(0x00);      // 播报命令词
} else if (commandId == 2) {
  UART_SetFunctionVoice(0x00);     // 播报功能词
} else if (commandId == 3) {
  UART_SetPassiveVoice(0x00);      // 播报被动语
}
```

### Beispiel 2: Eine LED ansteuern
```cpp
if (commandId == 10) {
  digitalWrite(LED_PIN, LOW);    // 关灯
  UART_SetCommandVoice(0x00);     // 播报确认
}
```

### Beispiel 3: Einen Motor ansteuern
```cpp
if (commandId == 11) {
  motor_stop();
  UART_SetCommandVoice(0x00);     // 播报确认
}
```

