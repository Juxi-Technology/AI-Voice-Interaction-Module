[English](../../../en/06-multi-host/raspberry-pi/README.md) | [Deutsch](../../../de/06-multi-host/raspberry-pi/README.md) | [Español](../../../es/06-multi-host/raspberry-pi/README.md) | [Français](../../../fr/06-multi-host/raspberry-pi/README.md) | Italiano | [日本語](../../../ja/06-multi-host/raspberry-pi/README.md) | [한국어](../../../ko/06-multi-host/raspberry-pi/README.md) | [Português (BR)](../../../pt-br/06-multi-host/raspberry-pi/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/raspberry-pi/README.md) | [简体中文](../../../zh-hans/06-multi-host/raspberry-pi/README.md) | [繁體中文](../../../zh-hant/06-multi-host/raspberry-pi/README.md)

# Guida utente del modulo di interazione vocale per Raspberry Pi

## Installazione delle dipendenze

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## Abilitazione dell'interfaccia I2C

```bash
sudo raspi-config
```

Seleziona `Interface Options` -> `I2C` -> `Yes`

Riavvia il Raspberry Pi

## Versione IIC

### Posizione dei file
`IIC_Voice/iic_voice.py`

### Istruzioni di cablaggio

| Raspberry Pi | Modulo vocale |
|--------------|--------------|
| GPIO2 (SDA) | SDA |
| GPIO3 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

### Esecuzione

```bash
cd IIC_Voice
python3 iic_voice.py
```

### Formato dell'output

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## Versione UART

### Posizione dei file
`UART_Voice/uart_voice.py`

### Abilitazione della porta seriale

Modifica `/boot/firmware/config.txt` o `/boot/config.txt`, assicurandoti che contenga la seguente configurazione:

```
enable_uart=1
dtoverlay=disable-bt
```

Poi riavvia il Raspberry Pi.

```bash
sudo reboot
```

### Istruzioni di cablaggio

#### Utilizzo del collegamento diretto Type-C

Quando si utilizza il collegamento diretto Type-C al Raspberry Pi, rimuovi il commento da `SERIAL_PORT = '/dev/ttyUSB0'` e commenta `SERIAL_PORT = '/dev/ttyAMA0'`

#### Utilizzo dei pin UART

| Raspberry Pi | Modulo vocale |
|--------------|--------------|
| GPIO14 (TXD) | RX |
| GPIO15 (RXD) | TX |
| GND | GND |
| 5V | 5V |

Commenta `SERIAL_PORT = '/dev/ttyUSB0'`

Rimuovi il commento da `SERIAL_PORT = '/dev/ttyAMA0'`

### Esecuzione

```bash
cd UART_Voice
python3 uart_voice.py
```

### Formato dell'output

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## Descrizione del protocollo

### Protocollo UART

| Byte | Contenuto |
|------|---------|
| 1 | 0xFE (intestazione del frame) |
| 2 | 0xEF (intestazione del frame) |
| 3 | ID della parola di funzione |
| 4 | ID della parola di comando |
| 5 | 0xEE (fine del frame) |

### Protocollo IIC

- Indirizzo del dispositivo: 0x2A
- Registro di lettura: 0xDA (legge 1 byte)
  - 0x00: non riconosciuto
  - Altro: ID della parola di comando
