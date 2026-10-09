[English](../../../en/06-multi-host/raspberry-pi/README.md) | Deutsch | [Español](../../../es/06-multi-host/raspberry-pi/README.md) | [Français](../../../fr/06-multi-host/raspberry-pi/README.md) | [Italiano](../../../it/06-multi-host/raspberry-pi/README.md) | [日本語](../../../ja/06-multi-host/raspberry-pi/README.md) | [한국어](../../../ko/06-multi-host/raspberry-pi/README.md) | [Português (BR)](../../../pt-br/06-multi-host/raspberry-pi/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/raspberry-pi/README.md) | [简体中文](../../../zh-hans/06-multi-host/raspberry-pi/README.md) | [繁體中文](../../../zh-hant/06-multi-host/raspberry-pi/README.md)

# Benutzerhandbuch für das Raspberry Pi-Sprachinteraktionsmodul

## Abhängigkeiten installieren

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## I2C-Schnittstelle aktivieren

```bash
sudo raspi-config
```

Wählen Sie `Interface Options` -> `I2C` -> `Yes`

Starten Sie den Raspberry Pi neu

## IIC-Version

### Dateispeicherort
`IIC_Voice/iic_voice.py`

### Verdrahtungshinweise

| Raspberry Pi | Sprachmodul |
|--------------|--------------|
| GPIO2 (SDA) | SDA |
| GPIO3 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

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

### Serielle Schnittstelle aktivieren

Bearbeiten Sie `/boot/firmware/config.txt` oder `/boot/config.txt` und stellen Sie sicher, dass die folgende Konfiguration vorhanden ist:

```
enable_uart=1
dtoverlay=disable-bt
```

Starten Sie anschließend den Raspberry Pi neu.

```bash
sudo reboot
```

### Verdrahtungshinweise

#### Verwendung der direkten Type-C-Verbindung

Wenn Sie eine direkte Type-C-Verbindung zum Raspberry Pi verwenden, entfernen Sie die Kommentierung von `SERIAL_PORT = '/dev/ttyUSB0'` und kommentieren Sie `SERIAL_PORT = '/dev/ttyAMA0'` aus

#### Verwendung der UART-Pins

| Raspberry Pi | Sprachmodul |
|--------------|--------------|
| GPIO14 (TXD) | RX |
| GPIO15 (RXD) | TX |
| GND | GND |
| 5V | 5V |

Kommentieren Sie `SERIAL_PORT = '/dev/ttyUSB0'` aus

Entfernen Sie die Kommentierung von `SERIAL_PORT = '/dev/ttyAMA0'`

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
