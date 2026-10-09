[English](../../../en/06-multi-host/rdk-x5/README.md) | Deutsch | [Español](../../../es/06-multi-host/rdk-x5/README.md) | [Français](../../../fr/06-multi-host/rdk-x5/README.md) | [Italiano](../../../it/06-multi-host/rdk-x5/README.md) | [日本語](../../../ja/06-multi-host/rdk-x5/README.md) | [한국어](../../../ko/06-multi-host/rdk-x5/README.md) | [Português (BR)](../../../pt-br/06-multi-host/rdk-x5/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/rdk-x5/README.md) | [简体中文](../../../zh-hans/06-multi-host/rdk-x5/README.md) | [繁體中文](../../../zh-hant/06-multi-host/rdk-x5/README.md)

# AI-Sprachinteraktionsmodul - RDK X5 (Python) Benutzerhandbuch

## Inhaltsverzeichnis

1. [Einführung](#einführung)
2. [Hardware-Anschluss](#hardware-anschluss)
3. [Einrichtung der Umgebung](#einrichtung-der-umgebung)
4. [Verwendung der IIC-Version](#verwendung-der-iic-version)
5. [Verwendung der UART-Version](#verwendung-der-uart-version)
6. [FAQ](#faq)

---

## Einführung

Dieses Repository stellt Python-Beispielcode für die Kommunikation der RDK X5 (Raspberry Pi)-Plattform mit dem AI-Sprachinteraktionsmodul bereit und unterstützt sowohl die I2C- als auch die UART-Kommunikation.

- **Spracherkennungsmodul**: Unterstützt Offline-Spracherkennung und gibt nach der Erkennung eine Befehls-ID aus
- **Wiedergabefunktion**: Unterstützt passive Wiedergabe, Funktionswort-Wiedergabe, Befehlswort-Wiedergabe
- **Kommunikationsprotokoll**: I2C-Adresse 0x2A, UART-Baudrate 115200
- **Programmiersprache**: Python 3

---

## Hardware-Anschluss

### Allgemeiner Anschluss

| RDK X5-Pin | Sprachmodul | Beschreibung |
|------------|-------------|-------------|
| 5V (Pin 2/4) | 5V | Stromversorgung Plus |
| GND (Pin 6/9) | GND | Masse |

> **Wichtig**: Stellen Sie sicher, dass alle Geräte eine gemeinsame Masse teilen!

---

### I2C-Versionsanschluss

| RDK X5-Pin | Sprachmodul | Beschreibung |
|------------|-------------|-------------|
| SDA (GPIO3, Pin 3) | SDA | I2C-Datenleitung |
| SCL (GPIO5, Pin 5) | SCL | I2C-Taktleitung |

**Hinweis**: Verwendet standardmäßig I2C-Bus 5 (BCM-Nummerierung)

---

### UART-Versionsanschluss

| RDK X5-Pin | Sprachmodul | Beschreibung |
|------------|-------------|-------------|
| GPIO14 (TXD, Pin 8) | RX | Serielle Übertragung |
| GPIO15 (RXD, Pin 10) | TX | Serieller Empfang |

**Hinweis**: Verwendet standardmäßig das serielle Gerät `/dev/ttyAMA0`

---

### Type-C-Kabelverbindung (UART-Alternative)

Wenn Sie ein USB-TTL-Adaptermodul verwenden:

| RDK X5 | USB-TTL-Modul | Sprachmodul |
|--------|---------------|-------------|
| USB-Port | USB | - |
| - | RX | TX |
| - | TX | RX |
| GND | GND | GND |

**Hinweis**: Das serielle Gerät ist in diesem Fall normalerweise `/dev/ttyUSB0`

---

## Einrichtung der Umgebung

### 1. Systemanforderungen

- RDK X5 (oder Raspberry Pi 3/4/5)
- Ubuntu-/Debian-System
- Python 3.7+

### 2. Abhängigkeiten installieren

```bash
# Update packages
sudo apt update
sudo apt upgrade -y

# Install Python libraries
sudo apt install -y python3-pip python3-smbus i2c-tools

# Install pyserial
pip3 install pyserial
```

### 3. I2C-Schnittstelle aktivieren

```bash
# Open configuration tool
sudo raspi-config

# Select Interface Options → I2C → Enable
# Reboot to take effect
sudo reboot
```

### 4. Serielle Schnittstelle aktivieren

```bash
# Open configuration tool
sudo raspi-config

# Select Interface Options → Serial
# Select: No (shell) → Yes (hardware serial port)
# Reboot to take effect
sudo reboot
```

### 5. Hardware-Schnittstellen testen

```bash
# Test I2C device
sudo i2cdetect -y 5

# Test serial port
ls /dev/ttyAMA0
ls /dev/ttyUSB0  # If using USB-TTL
```

---

## Verwendung der IIC-Version

### 1. Codedateien prüfen

```bash
cd IIC_Voice
ls -la
# Should see iic_voice.py
```

### 2. I2C-Bus konfigurieren

Bearbeiten Sie die Datei `iic_voice.py` und passen Sie die Parameter nach Bedarf an:

```python
# I2C device address
DEVICE_ADDRESS = 0x2A

# Register address
REG_RESULT = 0xDA

# I2C bus number (modify according to actual connection)
bus = smbus.SMBus(5)  # I2C bus 5
```

### 3. Programm ausführen

```bash
# Make executable
chmod +x iic_voice.py

# Run (sudo required for I2C access)
sudo python3 iic_voice.py
```

### 4. Test ausführen

Nach dem normalen Start wird Folgendes angezeigt:

```
Speech Serial Opened! Baudrate=115200
```

Sprechen Sie Befehlswörter zum Sprachmodul, die entsprechenden IDs werden angezeigt:

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. Programm beenden

Drücken Sie `Ctrl + C`, um das Programm zu beenden:

```
Program terminated
```

---

## Verwendung der UART-Version

### 1. Codedateien prüfen

```bash
cd UART_Voice
ls -la
# Should see uart_voice.py
```

### 2. Serielle Schnittstelle konfigurieren

Bearbeiten Sie die Datei `uart_voice.py` und ändern Sie das serielle Gerät:

```python
# UART direct connection (default)
SERIAL_PORT = '/dev/ttyAMA0'

# Or use USB-TTL
# SERIAL_PORT = '/dev/ttyUSB0'

# Baud rate
BAUD_RATE = 115200
```

### 3. Programm ausführen

```bash
# Make executable
chmod +x uart_voice.py

# Run (sudo required for serial port access)
sudo python3 uart_voice.py
```

### 4. Test ausführen

Nach dem normalen Start wird Folgendes angezeigt:

```
Speech Serial Opened! Baudrate=115200
```

Sprechen Sie Befehlswörter zum Sprachmodul, die entsprechenden IDs werden angezeigt:

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. Programm beenden

Drücken Sie `Ctrl + C`, um das Programm zu beenden

---

## FAQ

### Q1: Unzureichende Berechtigungen für I2C-Operationen

**A: Fügen Sie den Benutzer zur I2C-Benutzergruppe hinzu:**
```bash
sudo usermod -aG i2c $USER
# Re-login to take effect
```
Oder führen Sie es mit `sudo` aus

---

### Q2: Serielles Gerät nicht gefunden

**A: Prüfen Sie:**
1. Ob die serielle Schnittstelle aktiviert ist (raspi-config)
2. Ob der Gerätename korrekt ist
   - UART direkt: `/dev/ttyAMA0`
   - USB-TTL: `/dev/ttyUSB0` oder `/dev/ttyUSB1`
3. Ob der Hardware-Anschluss korrekt ist
4. Ob die serielle Schnittstelle von anderen Programmen belegt ist

```bash
# List available serial ports
ls /dev/tty* | grep tty
```

---

### Q3: I2C-Gerät wird beim Scan nicht erkannt

**A: Prüfen Sie:**
1. Ob I2C aktiviert ist (raspi-config)
2. Ob SDA/SCL vertauscht sind
3. Ob die gemeinsame Masse angeschlossen ist
4. Ob das Gerät eingeschaltet ist

```bash
# Scan I2C devices
sudo i2cdetect -y 5
```

Wenn Sie 0x2A sehen, ist der Geräteanschluss normal

---

### Q4: Befehls-ID zeigt nur 0 oder nichts

**A: Normales Verhalten:**
- 0 = Kein gültiger Befehl erkannt
- IDs werden nur ausgegeben, wenn gültige Befehlswörter gesprochen werden
- Wecken Sie das Modul zuerst auf und sprechen Sie dann den Befehl

---

### Q5: Erkennungsgenauigkeit nicht hoch

**A: Optimierungsvorschläge:**
- Sorgen Sie für eine ruhige Umgebung mit nicht zu vielen Hintergrundgeräuschen
- Halten Sie einen angemessenen Abstand zum Mikrofon ein (10-50 cm)
- Sprechen Sie in mäßigem Tempo und mit klarer Aussprache

---

### Q6: Serielle Kommunikation anomal

**A: Prüfen Sie:**
1. Sind TX/RX korrekt über Kreuz verbunden? (Modul TX → RPi RX)
2. Beträgt die Baudrate 115200
3. Ist die gemeinsame Masse angeschlossen
4. Ist die serielle Schnittstelle von anderen Prozessen belegt

```bash
# Check serial port occupancy
sudo lsof /dev/ttyAMA0
```

---

## Technischer Support

Wenn Sie auf Probleme stoßen, prüfen Sie bitte:
1. Ob der Hardware-Anschluss korrekt ist (gemeinsame Masse ist sehr wichtig!)
2. Ob die serielle Baudrate 115200 beträgt
3. Ob die I2C-Adresse korrekt ist (0x2A)
4. Ob Sie über ausreichende Berechtigungen für den Zugriff auf die Hardware-Schnittstellen verfügen

```bash
# Useful debugging commands
ls -l /dev/i2c*      # List I2C devices
ls -l /dev/ttyAMA0   # List serial device
groups                # List user group permissions
```
