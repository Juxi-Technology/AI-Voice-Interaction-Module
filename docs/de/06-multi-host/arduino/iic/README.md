[English](../../../../en/06-multi-host/arduino/iic/README.md) | Deutsch | [Español](../../../../es/06-multi-host/arduino/iic/README.md) | [Français](../../../../fr/06-multi-host/arduino/iic/README.md) | [Italiano](../../../../it/06-multi-host/arduino/iic/README.md) | [日本語](../../../../ja/06-multi-host/arduino/iic/README.md) | [한국어](../../../../ko/06-multi-host/arduino/iic/README.md) | [Português (BR)](../../../../pt-br/06-multi-host/arduino/iic/README.md) | [Português (PT)](../../../../pt-pt/06-multi-host/arduino/iic/README.md) | [简体中文](../../../../zh-hans/06-multi-host/arduino/iic/README.md) | [繁體中文](../../../../zh-hant/06-multi-host/arduino/iic/README.md)

# Tutorial zur BSP-Version des IIC-Sprachmoduls

## 📁 Dateistruktur

```
iic/
├── iic.ino    # 主程序
├── bsp_iic.hpp         # 头文件（地址和函数声明）
├── bsp_iic.cpp         # 实现文件
└── README.md            # 本教程
```

---

## 🔌 Hardware-Anschluss

| Arduino | Sprachmodul |
|---------|----------|
| A4 (SDA) | SDA |
| A5 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

---

## 🔧 Kompilieren und Hochladen

### Schritt 1: Arduino IDE öffnen
1. Öffnen Sie die Datei `IIC_Voice.ino`
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
IIC Voice Module Initialized
```

Sprechen Sie das Weckwort und das Befehlswort zum Modul, und es gibt die entsprechende ID aus:
```
ID: 1
ID: 2
ID: 10
```

---

## 📚 Registerübersicht

| Register | Adresse | Funktion | Beschreibung |
|--------|------|------|------|
| REG_RESULT | 0xDA | Befehls-ID lesen | Liest 1 Byte, 0 = nicht erkannt |
| REG_PASSIVE | 0xD1 | Passive Wiedergabe schreiben | Schreibt 1 Byte, 0x00 = passive Wiedergabestimme |
| REG_FUNCTION | 0xD2 | Funktionswort-Wiedergabe schreiben | Schreibt 1 Byte, 0x00 = Funktionswort-Wiedergabestimme |
| REG_COMMAND | 0xD3 | Befehlswort-Wiedergabe schreiben | Schreibt 1 Byte, 0x00 = Befehlswort-Wiedergabestimme |

---

## 📚 Referenz der BSP-Schnittstellen

### 1. IIC_Init()
```cpp
void IIC_Init(void);
```
**Funktion**: Initialisiert den I2C-Bus

**Beispiel**:
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
**Funktion**: Liest die vom Sprachmodul erkannte Befehls-ID

**Rückgabewert**:
- `0` - kein Befehl erkannt
- `1~254` - Befehls-ID
- `-1` - Kommunikationsfehler

**Beispiel**:
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
**Funktion**: Legt die passive Wiedergabestimme fest

**Parameter**:
- `0x00` - Typ der passiven Wiedergabestimme

**Beispiel**:
```cpp
IIC_SetPassiveVoice(0x00);
delay(200);
```

---

### 4. IIC_SetFunctionVoice()
```cpp
void IIC_SetFunctionVoice(uint8_t voiceID);
```
**Funktion**: Legt die Funktionswort-Wiedergabestimme fest

**Parameter**:
- `0x00` - Typ der Funktionswort-Wiedergabestimme

**Beispiel**:
```cpp
IIC_SetFunctionVoice(0x00);
delay(200);
```

---

### 5. IIC_SetCommandVoice()
```cpp
void IIC_SetCommandVoice(uint8_t voiceID);
```
**Funktion**: Legt die Befehlswort-Wiedergabestimme fest

**Parameter**:
- `0x00` - Typ der Befehlswort-Wiedergabestimme

**Beispiel**:
```cpp
IIC_SetCommandVoice(0x00);
delay(200);
```

---

## 🎯 Logik des Hauptprogramms

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

## 🔍 FAQ

### Q1: Der serielle Monitor zeigt nur „IIC Read Error“

**Mögliche Ursachen:**
1. Falsche Verdrahtung oder nicht angeschlossen
2. Modul nicht mit Strom versorgt
3. Falsche I2C-Adresse

**Lösungen:**
- Prüfen Sie, ob SDA/SCL vertauscht sind
- Prüfen Sie, ob GND mit der gemeinsamen Masse verbunden ist
- Prüfen Sie, ob die 5V-Stromversorgung normal ist
- Verwenden Sie ein I2C-Scanner-Programm, um die Geräteadresse zu bestätigen

---

### Q2: Überhaupt keine Ausgabe

**Mögliche Ursachen:**
1. Falsche serielle Baudrate
2. Modul nicht aufgeweckt

**Lösungen:**
- Stellen Sie sicher, dass die serielle Baudrate 115200 beträgt
- Sagen Sie zuerst das Weckwort und dann das Befehlswort

---

### Q3: Die Ausgabe zeigt „ID: 255“ oder „ID: 0“

**Erklärung:** Dies ist normal

- `0` = kein Befehl erkannt
- `255` = keine neuen Daten

Diese Werte werden bereits im Code herausgefiltert und daher normalerweise nicht ausgegeben. Wenn Sie sie dennoch sehen, greift der Code nicht.

---

## 💡 Vorteile der BSP-Architektur

### 1. Klare Code-Schichtung
- **bsp_iic.hpp** - nur Deklaration, keine Implementierung
- **bsp_iic.cpp** - konkrete Implementierungsdetails
- **IIC_Voice.ino** - kümmert sich nur um die Geschäftslogik

### 2. Einfache Portierung
Wenn Sie auf eine andere Plattform wechseln (z. B. STM32, ESP32), müssen Sie nur die Implementierung in `bsp_iic.cpp` ändern; das Hauptprogramm muss nicht angepasst werden.

### 3. Einfache Wartung
Änderungen am I2C-bezogenen Code sind auf `bsp_iic.cpp` beschränkt — einmal korrigieren, überall wirksam.

---

## 🚀 Beispiele für erweiterte Funktionen

### Beispiel 1: Unterschiedliche Wiedergaben je nach Befehl auslösen
```cpp
if (commandId == 1) {
  IIC_SetCommandVoice(0x00);      // 播报命令词
} else if (commandId == 2) {
  IIC_SetFunctionVoice(0x00);     // 播报功能词
} else if (commandId == 3) {
  IIC_SetPassiveVoice(0x00);      // 播报被动语
}
```

### Beispiel 2: Eine LED ansteuern
```cpp
if (commandId == 10) {
  digitalWrite(LED_PIN, LOW);    // 关灯
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```

### Beispiel 3: Einen Motor ansteuern
```cpp
if (commandId == 11) {
  motor_stop();
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```
