[English](../../../en/06-multi-host/jetson/README.md) | [Deutsch](../../../de/06-multi-host/jetson/README.md) | [Español](../../../es/06-multi-host/jetson/README.md) | [Français](../../../fr/06-multi-host/jetson/README.md) | Italiano | [日本語](../../../ja/06-multi-host/jetson/README.md) | [한국어](../../../ko/06-multi-host/jetson/README.md) | [Português (BR)](../../../pt-br/06-multi-host/jetson/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/jetson/README.md) | [简体中文](../../../zh-hans/06-multi-host/jetson/README.md) | [繁體中文](../../../zh-hant/06-multi-host/jetson/README.md)

# Guida utente del modulo di interazione vocale per Jetson

## Installazione delle dipendenze

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## Verifica dei gruppi utente

```bash
sudo usermod -aG i2c $USER
sudo usermod -aG dialout $USER
```

Esci e accedi di nuovo perché le modifiche abbiano effetto.

## Versione IIC

### Posizione dei file
`IIC_Voice/iic_voice.py`

### Istruzioni di cablaggio

| Jetson | Modulo vocale |
|--------|--------------|
| Pin 27 (I2C1 SDA) | SDA |
| Pin 28 (I2C1 SCL) | SCL |
| Pin 6 (GND) | GND |
| Pin 4 (5V) | 5V |

### Verifica del dispositivo I2C

```bash
sudo i2cdetect -y -r 1
```

Dovresti vedere l'indirizzo 0x2A

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

### Collegamento tramite i pin UART

Quando si collega il modulo al Jetson tramite i pin UART, commenta `SERIAL_PORT = '/dev/ttyUSB0'` e rimuovi il commento da `SERIAL_PORT = '/dev/ttyTHS1'`

#### Istruzioni di cablaggio

| Jetson | Modulo vocale |
|--------|--------------|
| Pin 8 (UART1 TX) | RX |
| Pin 10 (UART1 RX) | TX |
| Pin 6 (GND) | GND |
| Pin 4 (5V) | 5V |

### Verifica della porta seriale

```bash
ls /dev/ttyTHS*
```

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

### Collegamento tramite cavo Type-C

Quando si collega il modulo al Jetson tramite cavo Type-C, rimuovi il commento da `SERIAL_PORT = '/dev/ttyUSB0'` e commenta `SERIAL_PORT = '/dev/ttyTHS1'`

### Verifica della porta seriale

```bash
ls /dev/ttyUSB*
```

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

## FAQ

### Problema di permessi I2C

```bash
sudo chmod 666 /dev/i2c-1
```

### Porta seriale occupata

Se la porta seriale non può essere aperta, controlla se è occupata da altri servizi:

```bash
sudo systemctl stop nvgetty
sudo systemctl disable nvgetty
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
