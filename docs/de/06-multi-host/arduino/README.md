[English](../../../en/06-multi-host/arduino/README.md) | Deutsch | [Español](../../../es/06-multi-host/arduino/README.md) | [Français](../../../fr/06-multi-host/arduino/README.md) | [Italiano](../../../it/06-multi-host/arduino/README.md) | [日本語](../../../ja/06-multi-host/arduino/README.md) | [한국어](../../../ko/06-multi-host/arduino/README.md) | [Português (BR)](../../../pt-br/06-multi-host/arduino/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/arduino/README.md) | [简体中文](../../../zh-hans/06-multi-host/arduino/README.md) | [繁體中文](../../../zh-hant/06-multi-host/arduino/README.md)

# AI-Sprachinteraktionsmodul - Arduino-Benutzerhandbuch

## Inhaltsverzeichnis

1. [Einführung](#einführung)
2. [Hardware-Anschluss](#hardware-anschluss)
3. [Einrichtung der Entwicklungsumgebung](#einrichtung-der-entwicklungsumgebung)
4. [Verwendung der IIC-Version](#verwendung-der-iic-version)
5. [Verwendung der UART-Version](#verwendung-der-uart-version)
6. [FAQ](#faq)

---

## Einführung

Dieses Repository stellt Beispielcode für die Kommunikation der Arduino-Plattform mit dem AI-Sprachinteraktionsmodul bereit und unterstützt sowohl die I2C- als auch die UART-Kommunikation.

- **Spracherkennungsmodul**: Unterstützt Offline-Spracherkennung und gibt nach der Erkennung eine Befehls-ID aus
- **Wiedergabefunktion**: Unterstützt passive Wiedergabe, Funktionswort-Wiedergabe, Befehlswort-Wiedergabe
- **Kommunikationsprotokoll**: I2C-Adresse 0x2A, UART-Baudrate 115200

---

## Hardware-Anschluss

### Allgemeiner Anschluss

| Arduino-Pin | Sprachmodul | Beschreibung |
|-------------|-------------|-------------|
| 5V | 5V | Stromversorgung Plus |
| GND | GND | Masse |

---

### I2C-Versionsanschluss

| Arduino-Pin | Sprachmodul | Beschreibung |
|-------------|-------------|-------------|
| A4 (SDA) | SDA | I2C-Datenleitung |
| A5 (SCL) | SCL | I2C-Taktleitung |

---

### UART-Versionsanschluss

| Arduino-Pin | Sprachmodul | Beschreibung |
|-------------|-------------|-------------|
| D10 (RX) | TX | Serieller Empfang (Software-Seriell) |
| D11 (TX) | RX | Serielle Übertragung (Software-Seriell) |

---

### Serieller Debug-Anschluss

| Arduino-Pin | USB-TTL | Beschreibung |
|-------------|---------|-------------|
| TX (D1) | RX | Debug-Ausgabe |
| RX (D0) | TX | Debug-Eingabe (optional) |
| GND | GND | Gemeinsame Masse |

---

## Einrichtung der Entwicklungsumgebung

### 1. Arduino IDE installieren

- Download: https://www.arduino.cc/en/software
- Installieren Sie die neueste Version

### 2. Board-Support-Paket installieren

- Arduino IDE öffnen
- Werkzeuge → Board → Boardverwalter
- Suchen Sie das Support-Paket für Ihr Arduino-Board und installieren Sie es
- Empfohlen: Arduino Uno / Nano

---

## Verwendung der IIC-Version

### 1. Projekt öffnen

- Öffnen Sie `IIC_Voice/IIC_Voice.ino` in der Arduino IDE

### 2. Code hochladen

- Wählen Sie das richtige Board-Modell (Werkzeuge → Board)
- Wählen Sie den richtigen Port (Werkzeuge → Port)
- Klicken Sie auf die Schaltfläche zum Hochladen (→)
- Warten Sie, bis der Upload abgeschlossen ist

### 3. Test ausführen

1. Öffnen Sie den seriellen Monitor (Werkzeuge → Serieller Monitor)
2. Stellen Sie die Baudrate auf **115200** ein
3. Nach dem normalen Start wird Folgendes angezeigt:

```
IIC Voice Module Initialized
```

4. Sprechen Sie Befehlswörter zum Sprachmodul, und die entsprechenden IDs werden angezeigt:

```
IIC Voice Module Initialized
ID: 1
ID: 4
ID: 10
```

### 4. Code-Erklärung

```cpp
// Initialize I2C
IIC_Init();

// Read command ID
int commandId = IIC_ReadCommand();

// Set broadcast
IIC_SetCommandVoice(0x00);  // Command word broadcast
```

---

## Verwendung der UART-Version

### 1. Projekt öffnen

- Öffnen Sie `UART_Voice/UART_Voice.ino` in der Arduino IDE

### 2. Code hochladen

- Wählen Sie das richtige Board-Modell
- Wählen Sie den richtigen Port
- Klicken Sie auf die Schaltfläche zum Hochladen
- Warten Sie, bis der Upload abgeschlossen ist

### 3. Test ausführen

1. Öffnen Sie den seriellen Monitor
2. Stellen Sie die Baudrate auf **115200** ein
3. Nach dem normalen Start wird Folgendes angezeigt:

```
UART Voice Module Initialized
```

4. Sprechen Sie Befehlswörter zum Sprachmodul, und die entsprechenden IDs werden angezeigt:

```
UART Voice Module Initialized
ID: 1
ID: 4
ID: 10
```

### 4. Code-Erklärung

```cpp
// Initialize serial (Software Serial D10/D11)
UART_Init();

// Read command ID
int commandId = UART_ReadCommand();

// Set broadcast
UART_SetCommandVoice(0x00);  // Command word broadcast
```

---

## FAQ

### Q1: Keine Ausgabe im seriellen Monitor

**A: Prüfen Sie Folgendes:**
- Prüfen Sie, ob die serielle Baudrate 115200 beträgt
- Prüfen Sie, ob der richtige Port ausgewählt ist
- Prüfen Sie, ob TX/RX vertauscht sind
- Prüfen Sie, ob GND angeschlossen ist

---

### Q2: I2C-Version zeigt „IIC Read Error“

**A: Prüfen Sie den I2C-Anschluss:**
- Prüfen Sie, ob SDA/SCL vertauscht sind
- Prüfen Sie, ob die Geräteadresse korrekt ist (0x2A)
- Prüfen Sie, ob GND angeschlossen ist

---

### Q3: Befehls-ID zeigt nur 0 oder 255

**A: Normales Verhalten:**
- 0 = Kein gültiger Befehl erkannt
- 255 = Keine neuen Daten
- Gültige IDs werden nur nach einer normalen Erkennung ausgegeben

---

### Q4: Erkennungsgenauigkeit ist nicht hoch

**A: Optimierungsvorschläge:**
- Sorgen Sie für eine ruhige Umgebung mit nicht zu vielen Hintergrundgeräuschen
- Halten Sie einen angemessenen Abstand zum Mikrofon ein (10-50 cm)
- Sprechen Sie in mäßigem Tempo und mit klarer Aussprache

---

### Q5: UART-Version empfängt keine Daten

**A: Prüfen Sie:**
- Stellen Sie sicher, dass TX des Sprachmoduls mit Arduino D10 (RX) verbunden ist
- Stellen Sie sicher, dass RX des Sprachmoduls mit Arduino D11 (TX) verbunden ist
- Prüfen Sie, ob die Baudrate 115200 beträgt

---

## Technischer Support

Wenn Sie auf Probleme stoßen, prüfen Sie bitte:
1. Ob der Hardware-Anschluss korrekt ist
2. Ob die serielle Baudrate übereinstimmt
3. Ob die I2C-Adresse korrekt ist
4. Ob GND angeschlossen ist (sehr wichtig!)
