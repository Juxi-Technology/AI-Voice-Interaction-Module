[English](../../../en/06-multi-host/jetson/README.md) | Deutsch | [Español](../../../es/06-multi-host/jetson/README.md) | [Français](../../../fr/06-multi-host/jetson/README.md) | [Italiano](../../../it/06-multi-host/jetson/README.md) | [日本語](../../../ja/06-multi-host/jetson/README.md) | [한국어](../../../ko/06-multi-host/jetson/README.md) | [Português (BR)](../../../pt-br/06-multi-host/jetson/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/jetson/README.md) | [简体中文](../../../zh-hans/06-multi-host/jetson/README.md) | [繁體中文](../../../zh-hant/06-multi-host/jetson/README.md)

# Benutzerhandbuch für das Jetson-Sprachinteraktionsmodul

## Abhängigkeiten installieren

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## Benutzergruppen prüfen

```bash
sudo usermod -aG i2c $USER
sudo usermod -aG dialout $USER
```

Melden Sie sich ab und erneut an, damit die Änderungen wirksam werden.

## IIC-Version

### Dateispeicherort
`IIC_Voice/iic_voice.py`

### Verdrahtungshinweise

| Jetson | Sprachmodul |
|--------|--------------|
| Pin 27 (I2C1 SDA) | SDA |
| Pin 28 (I2C1 SCL) | SCL |
| Pin 6 (GND) | GND |
| Pin 4 (5V) | 5V |

### I2C-Gerät prüfen

```bash
sudo i2cdetect -y -r 1
```

Sie sollten die Adresse 0x2A sehen

### Ausführen

```bash
cd IIC_Voice
python3 iic_voice.py
```

### Ausgabeformat

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## UART-Version

### Dateispeicherort
`UART_Voice/uart_voice.py`

### Verbindung über UART-Pins

Wenn Sie das Modul über die UART-Pins mit dem Jetson verbinden, kommentieren Sie `SERIAL_PORT = '/dev/ttyUSB0'` aus und entfernen Sie die Kommentierung von `SERIAL_PORT = '/dev/ttyTHS1'`

#### Verdrahtungshinweise

| Jetson | Sprachmodul |
|--------|--------------|
| Pin 8 (UART1 TX) | RX |
| Pin 10 (UART1 RX) | TX |
| Pin 6 (GND) | GND |
| Pin 4 (5V) | 5V |

### Serielle Schnittstelle prüfen

```bash
ls /dev/ttyTHS*
```

### Ausführen

```bash
cd UART_Voice
python3 uart_voice.py
```

### Ausgabeformat

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

### Verbindung über Type-C-Kabel

Wenn Sie das Modul über ein Type-C-Kabel mit dem Jetson verbinden, entfernen Sie die Kommentierung von `SERIAL_PORT = '/dev/ttyUSB0'` und kommentieren Sie `SERIAL_PORT = '/dev/ttyTHS1'` aus

### Serielle Schnittstelle prüfen

```bash
ls /dev/ttyUSB*
```

### Ausführen

```bash
cd UART_Voice
python3 uart_voice.py
```

### Ausgabeformat

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## FAQ

### I2C-Berechtigungsproblem

```bash
sudo chmod 666 /dev/i2c-1
```

### Serielle Schnittstelle belegt

Wenn die serielle Schnittstelle nicht geöffnet werden kann, prüfen Sie, ob sie von anderen Diensten belegt ist:

```bash
sudo systemctl stop nvgetty
sudo systemctl disable nvgetty
```

## Protokollbeschreibung

### UART-Protokoll

| Byte | Inhalt |
|------|---------|
| 1 | 0xFE (Rahmenkopf) |
| 2 | 0xEF (Rahmenkopf) |
| 3 | Funktionswort-ID |
| 4 | Befehlswort-ID |
| 5 | 0xEE (Rahmenende) |

### IIC-Protokoll

- Geräteadresse: 0x2A
- Leseregister: 0xDA (1 Byte lesen)
  - 0x00: Nicht erkannt
  - Andere: Befehlswort-ID
