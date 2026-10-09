[English](../../../en/06-multi-host/arduino/README.md) | [Deutsch](../../../de/06-multi-host/arduino/README.md) | [Español](../../../es/06-multi-host/arduino/README.md) | [Français](../../../fr/06-multi-host/arduino/README.md) | Italiano | [日本語](../../../ja/06-multi-host/arduino/README.md) | [한국어](../../../ko/06-multi-host/arduino/README.md) | [Português (BR)](../../../pt-br/06-multi-host/arduino/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/arduino/README.md) | [简体中文](../../../zh-hans/06-multi-host/arduino/README.md) | [繁體中文](../../../zh-hant/06-multi-host/arduino/README.md)

# Modulo di interazione vocale AI - Guida utente per Arduino

## Indice

1. [Introduzione](#introduzione)
2. [Collegamento hardware](#collegamento-hardware)
3. [Configurazione dell'ambiente di sviluppo](#configurazione-dellambiente-di-sviluppo)
4. [Utilizzo della versione IIC](#utilizzo-della-versione-iic)
5. [Utilizzo della versione UART](#utilizzo-della-versione-uart)
6. [FAQ](#faq)

---

## Introduzione

Questo repository fornisce codice di esempio per la piattaforma Arduino per comunicare con il modulo di interazione vocale AI, supportando sia il metodo di comunicazione I2C sia quello UART.

- **Modulo di riconoscimento vocale**: supporta il riconoscimento vocale offline e restituisce l'ID del comando dopo il riconoscimento
- **Funzione di riproduzione**: supporta la riproduzione passiva, la riproduzione di parole di funzione e la riproduzione di parole di comando
- **Protocollo di comunicazione**: indirizzo I2C 0x2A, baud rate UART 115200

---

## Collegamento hardware

### Collegamento generale

| Pin Arduino | Modulo vocale | Descrizione |
|-------------|-------------|-------------|
| 5V | 5V | Positivo dell'alimentazione |
| GND | GND | Massa dell'alimentazione |

---

### Collegamento versione I2C

| Pin Arduino | Modulo vocale | Descrizione |
|-------------|-------------|-------------|
| A4 (SDA) | SDA | Linea dati I2C |
| A5 (SCL) | SCL | Linea di clock I2C |

---

### Collegamento versione UART

| Pin Arduino | Modulo vocale | Descrizione |
|-------------|-------------|-------------|
| D10 (RX) | TX | Ricezione seriale (Software Serial) |
| D11 (TX) | RX | Trasmissione seriale (Software Serial) |

---

### Collegamento per il debug seriale

| Pin Arduino | USB-TTL | Descrizione |
|-------------|---------|-------------|
| TX (D1) | RX | Output di debug |
| RX (D0) | TX | Input di debug (opzionale) |
| GND | GND | Massa comune |

---

## Configurazione dell'ambiente di sviluppo

### 1. Installare Arduino IDE

- Download: https://www.arduino.cc/en/software
- Installa la versione più recente

### 2. Installare il pacchetto di supporto per la scheda

- Apri Arduino IDE
- Strumenti → Scheda → Gestione schede
- Cerca e installa il pacchetto di supporto per la tua scheda Arduino
- Consigliato: Arduino Uno / Nano

---

## Utilizzo della versione IIC

### 1. Aprire il progetto

- Apri `IIC_Voice/IIC_Voice.ino` in Arduino IDE

### 2. Caricare il codice

- Seleziona il modello di scheda corretto (Strumenti → Scheda)
- Seleziona la porta corretta (Strumenti → Porta)
- Clicca sul pulsante di caricamento (→)
- Attendi il completamento del caricamento

### 3. Eseguire il test

1. Apri il monitor seriale (Strumenti → Monitor seriale)
2. Imposta il baud rate su **115200**
3. Dopo l'avvio normale, verrà visualizzato:

```
IIC Voice Module Initialized
```

4. Pronuncia le parole di comando verso il modulo vocale e verranno visualizzati gli ID corrispondenti:

```
IIC Voice Module Initialized
ID: 1
ID: 4
ID: 10
```

### 4. Spiegazione del codice

```cpp
// Initialize I2C
IIC_Init();

// Read command ID
int commandId = IIC_ReadCommand();

// Set broadcast
IIC_SetCommandVoice(0x00);  // Command word broadcast
```

---

## Utilizzo della versione UART

### 1. Aprire il progetto

- Apri `UART_Voice/UART_Voice.ino` in Arduino IDE

### 2. Caricare il codice

- Seleziona il modello di scheda corretto
- Seleziona la porta corretta
- Clicca sul pulsante di caricamento
- Attendi il completamento del caricamento

### 3. Eseguire il test

1. Apri il monitor seriale
2. Imposta il baud rate su **115200**
3. Dopo l'avvio normale, verrà visualizzato:

```
UART Voice Module Initialized
```

4. Pronuncia le parole di comando verso il modulo vocale e verranno visualizzati gli ID corrispondenti:

```
UART Voice Module Initialized
ID: 1
ID: 4
ID: 10
```

### 4. Spiegazione del codice

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

### D1: Nessun output nel monitor seriale

**R: Controlla quanto segue:**
- Verifica che il baud rate seriale sia 115200
- Verifica che sia selezionata la porta corretta
- Verifica che TX/RX non siano invertiti
- Verifica che il GND sia collegato

---

### D2: La versione I2C mostra "IIC Read Error"

**R: Controlla il collegamento I2C:**
- Verifica che SDA/SCL non siano invertiti
- Verifica che l'indirizzo del dispositivo sia corretto (0x2A)
- Verifica che il GND sia collegato

---

### D3: L'ID del comando mostra solo 0 o 255

**R: Comportamento normale:**
- 0 = Nessun comando valido riconosciuto
- 255 = Nessun nuovo dato
- Gli ID validi vengono restituiti solo dopo un riconoscimento corretto

---

### D4: La precisione di riconoscimento non è elevata

**R: Suggerimenti di ottimizzazione:**
- Assicurati che l'ambiente sia silenzioso e che non vi sia troppo rumore di fondo
- Mantieni una distanza adeguata dal microfono (10-50 cm)
- Parla a velocità moderata con pronuncia chiara

---

### D5: La versione UART non riceve dati

**R: Controlla:**
- Verifica che il TX del modulo vocale sia collegato al D10 (RX) di Arduino
- Verifica che il RX del modulo vocale sia collegato al D11 (TX) di Arduino
- Verifica che il baud rate sia 115200

---

## Supporto tecnico

Se riscontri problemi, controlla:
1. Che il collegamento hardware sia corretto
2. Che il baud rate seriale corrisponda
3. Che l'indirizzo I2C sia corretto
4. Che il GND sia collegato (molto importante!)
