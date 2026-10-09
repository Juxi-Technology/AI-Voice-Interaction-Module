[English](../../../en/06-multi-host/rdk-x5/README.md) | [Deutsch](../../../de/06-multi-host/rdk-x5/README.md) | [Español](../../../es/06-multi-host/rdk-x5/README.md) | [Français](../../../fr/06-multi-host/rdk-x5/README.md) | Italiano | [日本語](../../../ja/06-multi-host/rdk-x5/README.md) | [한국어](../../../ko/06-multi-host/rdk-x5/README.md) | [Português (BR)](../../../pt-br/06-multi-host/rdk-x5/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/rdk-x5/README.md) | [简体中文](../../../zh-hans/06-multi-host/rdk-x5/README.md) | [繁體中文](../../../zh-hant/06-multi-host/rdk-x5/README.md)

# Modulo di interazione vocale AI - Guida utente per RDK X5 (Python)

## Indice

1. [Introduzione](#introduzione)
2. [Collegamento hardware](#collegamento-hardware)
3. [Configurazione dell'ambiente](#configurazione-dellambiente)
4. [Utilizzo della versione IIC](#utilizzo-della-versione-iic)
5. [Utilizzo della versione UART](#utilizzo-della-versione-uart)
6. [FAQ](#faq)

---

## Introduzione

Questo repository fornisce codice di esempio in Python per la piattaforma RDK X5 (Raspberry Pi) per comunicare con il modulo di interazione vocale AI, supportando sia il metodo di comunicazione I2C sia quello UART.

- **Modulo di riconoscimento vocale**: supporta il riconoscimento vocale offline e restituisce l'ID del comando dopo il riconoscimento
- **Funzione di riproduzione**: supporta la riproduzione passiva, la riproduzione di parole di funzione e la riproduzione di parole di comando
- **Protocollo di comunicazione**: indirizzo I2C 0x2A, baud rate UART 115200
- **Linguaggio di programmazione**: Python 3

---

## Collegamento hardware

### Collegamento generale

| Pin RDK X5 | Modulo vocale | Descrizione |
|------------|-------------|-------------|
| 5V (Pin 2/4) | 5V | Positivo dell'alimentazione |
| GND (Pin 6/9) | GND | Massa dell'alimentazione |

> **Importante**: assicurati che tutti i dispositivi condividano una massa comune!

---

### Collegamento versione I2C

| Pin RDK X5 | Modulo vocale | Descrizione |
|------------|-------------|-------------|
| SDA (GPIO3, Pin 3) | SDA | Linea dati I2C |
| SCL (GPIO5, Pin 5) | SCL | Linea di clock I2C |

**Nota**: utilizza per impostazione predefinita il bus I2C 5 (numerazione BCM)

---

### Collegamento versione UART

| Pin RDK X5 | Modulo vocale | Descrizione |
|------------|-------------|-------------|
| GPIO14 (TXD, Pin 8) | RX | Trasmissione seriale |
| GPIO15 (RXD, Pin 10) | TX | Ricezione seriale |

**Nota**: utilizza per impostazione predefinita il dispositivo seriale `/dev/ttyAMA0`

---

### Collegamento tramite cavo Type-C (alternativa UART)

Se utilizzi un modulo adattatore USB-TTL:

| RDK X5 | Modulo USB-TTL | Modulo vocale |
|--------|---------------|-------------|
| Porta USB | USB | - |
| - | RX | TX |
| - | TX | RX |
| GND | GND | GND |

**Nota**: in questo caso il dispositivo seriale è solitamente `/dev/ttyUSB0`

---

## Configurazione dell'ambiente

### 1. Requisiti di sistema

- RDK X5 (o Raspberry Pi 3/4/5)
- Sistema Ubuntu / Debian
- Python 3.7+

### 2. Installazione delle dipendenze

```bash
# Update packages
sudo apt update
sudo apt upgrade -y

# Install Python libraries
sudo apt install -y python3-pip python3-smbus i2c-tools

# Install pyserial
pip3 install pyserial
```

### 3. Abilitazione dell'interfaccia I2C

```bash
# Open configuration tool
sudo raspi-config

# Select Interface Options → I2C → Enable
# Reboot to take effect
sudo reboot
```

### 4. Abilitazione dell'interfaccia seriale

```bash
# Open configuration tool
sudo raspi-config

# Select Interface Options → Serial
# Select: No (shell) → Yes (hardware serial port)
# Reboot to take effect
sudo reboot
```

### 5. Verifica delle interfacce hardware

```bash
# Test I2C device
sudo i2cdetect -y 5

# Test serial port
ls /dev/ttyAMA0
ls /dev/ttyUSB0  # If using USB-TTL
```

---

## Utilizzo della versione IIC

### 1. Verifica dei file di codice

```bash
cd IIC_Voice
ls -la
# Should see iic_voice.py
```

### 2. Configurazione del bus I2C

Modifica il file `iic_voice.py`, cambiando i parametri secondo necessità:

```python
# I2C device address
DEVICE_ADDRESS = 0x2A

# Register address
REG_RESULT = 0xDA

# I2C bus number (modify according to actual connection)
bus = smbus.SMBus(5)  # I2C bus 5
```

### 3. Esecuzione del programma

```bash
# Make executable
chmod +x iic_voice.py

# Run (sudo required for I2C access)
sudo python3 iic_voice.py
```

### 4. Esecuzione del test

Dopo l'avvio normale, verrà visualizzato:

```
Speech Serial Opened! Baudrate=115200
```

Pronuncia le parole di comando verso il modulo vocale; verranno visualizzati gli ID corrispondenti:

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. Arresto del programma

Premi `Ctrl + C` per arrestare il programma:

```
Program terminated
```

---

## Utilizzo della versione UART

### 1. Verifica dei file di codice

```bash
cd UART_Voice
ls -la
# Should see uart_voice.py
```

### 2. Configurazione della porta seriale

Modifica il file `uart_voice.py`, cambiando il dispositivo seriale:

```python
# UART direct connection (default)
SERIAL_PORT = '/dev/ttyAMA0'

# Or use USB-TTL
# SERIAL_PORT = '/dev/ttyUSB0'

# Baud rate
BAUD_RATE = 115200
```

### 3. Esecuzione del programma

```bash
# Make executable
chmod +x uart_voice.py

# Run (sudo required for serial port access)
sudo python3 uart_voice.py
```

### 4. Esecuzione del test

Dopo l'avvio normale, verrà visualizzato:

```
Speech Serial Opened! Baudrate=115200
```

Pronuncia le parole di comando verso il modulo vocale; verranno visualizzati gli ID corrispondenti:

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. Arresto del programma

Premi `Ctrl + C` per arrestare il programma

---

## FAQ

### D1: Permessi insufficienti per le operazioni I2C

**R: Aggiungi l'utente al gruppo utente I2C:**
```bash
sudo usermod -aG i2c $USER
# Re-login to take effect
```
Oppure esegui con `sudo`

---

### D2: Dispositivo seriale non trovato

**R: Controlla:**
1. Verifica se la porta seriale è abilitata (raspi-config)
2. Verifica se il nome del dispositivo è corretto
   - UART diretto: `/dev/ttyAMA0`
   - USB-TTL: `/dev/ttyUSB0` o `/dev/ttyUSB1`
3. Verifica se il collegamento hardware è corretto
4. Verifica se la porta seriale è occupata da altri programmi

```bash
# List available serial ports
ls /dev/tty* | grep tty
```

---

### D3: Dispositivo I2C non rilevato nella scansione

**R: Controlla:**
1. Conferma che I2C sia abilitato (raspi-config)
2. Verifica se SDA/SCL sono invertiti
3. Verifica se la massa comune è collegata
4. Verifica se il dispositivo è alimentato

```bash
# Scan I2C devices
sudo i2cdetect -y 5
```

Se vedi 0x2A, il collegamento del dispositivo è normale

---

### D4: L'ID del comando mostra solo 0 o nulla

**R: Comportamento normale:**
- 0 = Nessun comando valido riconosciuto
- Gli ID vengono restituiti solo quando si pronunciano parole di comando valide
- Risveglia prima il modulo, poi pronuncia il comando

---

### D5: Precisione di riconoscimento non elevata

**R: Suggerimenti di ottimizzazione:**
- Assicurati che l'ambiente sia silenzioso e che non vi sia troppo rumore di fondo
- Mantieni una distanza adeguata dal microfono (10-50 cm)
- Parla a velocità moderata con pronuncia chiara

---

### D6: Comunicazione seriale anomala

**R: Controlla:**
1. TX/RX sono collegati in modo incrociato corretto? (TX del modulo → RX del RPi)
2. Il baud rate è 115200
3. La massa comune è collegata
4. La porta seriale è occupata da altri processi

```bash
# Check serial port occupancy
sudo lsof /dev/ttyAMA0
```

---

## Supporto tecnico

Se riscontri problemi, controlla:
1. Che il collegamento hardware sia corretto (la massa comune è molto importante!)
2. Che il baud rate seriale sia 115200
3. Che l'indirizzo I2C sia corretto (0x2A)
4. Di avere permessi sufficienti per accedere alle interfacce hardware

```bash
# Useful debugging commands
ls -l /dev/i2c*      # List I2C devices
ls -l /dev/ttyAMA0   # List serial device
groups                # List user group permissions
```
