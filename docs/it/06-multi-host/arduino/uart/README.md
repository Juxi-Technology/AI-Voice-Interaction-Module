[English](../../../../en/06-multi-host/arduino/uart/README.md) | [Deutsch](../../../../de/06-multi-host/arduino/uart/README.md) | [Español](../../../../es/06-multi-host/arduino/uart/README.md) | [Français](../../../../fr/06-multi-host/arduino/uart/README.md) | Italiano | [日本語](../../../../ja/06-multi-host/arduino/uart/README.md) | [한국어](../../../../ko/06-multi-host/arduino/uart/README.md) | [Português (BR)](../../../../pt-br/06-multi-host/arduino/uart/README.md) | [Português (PT)](../../../../pt-pt/06-multi-host/arduino/uart/README.md) | [简体中文](../../../../zh-hans/06-multi-host/arduino/uart/README.md) | [繁體中文](../../../../zh-hant/06-multi-host/arduino/uart/README.md)

# Tutorial della versione BSP del modulo vocale UART

## 📁 Struttura dei file

```
uart/
├── uart.ino    # 主程序
├── bsp_uart.hpp         # 头文件（协议帧和函数声明）
├── bsp_uart.cpp         # 实现文件
└── README.md              # 本教程
```

---

## 🔌 Collegamento hardware

### Collegamento al modulo vocale
| Arduino | Modulo vocale |
|---------|----------|
| D10 (RX) | TX |
| D11 (TX) | RX |
| GND | GND |
| 5V | 5V |

> 💡 **Nota:** RX e TX devono essere collegati in modo incrociato!

---

## 🔧 Compilazione e caricamento

### Passaggio 1: apri Arduino IDE
1. Apri il file `UART_Voice.ino`
2. Seleziona il modello della tua scheda (ad es. Arduino Uno)
3. Seleziona la porta seriale corrispondente

### Passaggio 2: compila e carica
1. Clicca sul pulsante ✔️ per compilare
2. Clicca sul pulsante ➡️ per caricare sulla scheda

---

## 📡 Test seriale

### Apri il monitor seriale in Arduino IDE
- Baud rate: **115200**
- Terminazione di riga: **Nessuna**

### Output previsto

Dopo l'accensione dovresti vedere:
```
UART Voice Module Initialized
```

Pronuncia la parola di risveglio e la parola di comando verso il modulo; verrà restituito l'ID corrispondente:
```
ID: 1
ID: 2
ID: 10
```

---

## 📚 Formato del frame del protocollo

| Byte | Contenuto | Descrizione |
|------|------|------|
| 1 | 0xFE | Intestazione del frame 1 |
| 2 | 0xEF | Intestazione del frame 2 |
| 3 | Codice funzione | 0xD1 = riproduzione passiva, 0xD2 = parola di funzione, 0xD3 = parola di comando |
| 4 | Dati | ID del comando o ID di riproduzione |
| 5 | 0xEE | Coda del frame |

**Esempio:** legge l'ID del comando = 10
```
FE EF 00 0A EE
```

**Esempio:** invia la riproduzione della parola di comando
```
FE EF D3 00 EE
```

---

## 📚 Riferimento all'interfaccia BSP

### 1. UART_Init()
```cpp
void UART_Init(void);
```
**Funzione**: inizializza la porta seriale (baud rate 115200)

**Esempio**:
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
**Funzione**: legge l'ID del comando riconosciuto dal modulo vocale

**Valore restituito**:
- `0` - nessun comando riconosciuto
- `1~254` - ID del comando
- `-1` - nessun nuovo dato

**Esempio**:
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
**Funzione**: imposta la voce di riproduzione passiva

**Parametro**:
- `0x00` - tipo di voce di riproduzione passiva

**Esempio**:
```cpp
UART_SetPassiveVoice(0x00);
delay(200);
```

---

### 4. UART_SetFunctionVoice()
```cpp
void UART_SetFunctionVoice(uint8_t voiceID);
```
**Funzione**: imposta la voce di riproduzione della parola di funzione

**Parametro**:
- `0x00` - tipo di voce di riproduzione della parola di funzione

**Esempio**:
```cpp
UART_SetFunctionVoice(0x00);
delay(200);
```

---

### 5. UART_SetCommandVoice()
```cpp
void UART_SetCommandVoice(uint8_t voiceID);
```
**Funzione**: imposta la voce di riproduzione della parola di comando

**Parametro**:
- `0x00` - tipo di voce di riproduzione della parola di comando

**Esempio**:
```cpp
UART_SetCommandVoice(0x00);
delay(200);
```

---

## 🎯 Logica del programma principale

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

### D1: Nessun output

**Possibili cause:**
1. RX/TX invertiti
2. GND non è una massa comune
3. Modulo non alimentato
4. Baud rate errato

**Soluzioni:**
- Conferma che D10 sia collegato al TX del modulo e D11 al RX del modulo (collegamento incrociato)
- Conferma il collegamento del GND
- Conferma che l'alimentazione a 5V sia regolare
- Conferma che il baud rate seriale sia 115200

---

### D2: Il monitor seriale mostra solo testo illeggibile

**Possibili cause:**
1. Disallineamento del baud rate
2. Avvio anomalo del modulo

**Soluzioni:**
- Conferma che il baud rate del monitor seriale sia 115200
- Premi una volta il pulsante di reset del modulo

---

### D3: L'output mostra "ID: 255" o "ID: 0"

**Spiegazione:** Questo è normale
- `0` = nessun comando riconosciuto
- `255` = nessun nuovo dato

Questi valori sono già filtrati nel codice, quindi normalmente non vengono restituiti. Se li vedi comunque, significa che il codice non sta avendo effetto.

---

## 💡 Vantaggi dell'architettura BSP

### 1. Chiara suddivisione in livelli del codice
- **bsp_uart.hpp** - solo dichiarazioni, nessuna implementazione
- **bsp_uart.cpp** - dettagli concreti dell'implementazione
- **UART_Voice.ino** - si occupa solo della logica di business

### 2. Facile da portare su altre piattaforme
Se passi a un'altra piattaforma (ad es. STM32, ESP32), devi modificare solo l'implementazione in `bsp_uart.cpp`; il programma principale non deve essere cambiato.

### 3. Facile da mantenere
Le modifiche al codice relativo a UART sono confinate in `bsp_uart.cpp` — correggi una volta, l'effetto vale ovunque.

---

## 🚀 Esempi di funzionalità estese

### Esempio 1: attivare riproduzioni diverse in base a comandi diversi
```cpp
if (commandId == 1) {
  UART_SetCommandVoice(0x00);      // 播报命令词
} else if (commandId == 2) {
  UART_SetFunctionVoice(0x00);     // 播报功能词
} else if (commandId == 3) {
  UART_SetPassiveVoice(0x00);      // 播报被动语
}
```

### Esempio 2: controllare un LED
```cpp
if (commandId == 10) {
  digitalWrite(LED_PIN, LOW);    // 关灯
  UART_SetCommandVoice(0x00);     // 播报确认
}
```

### Esempio 3: controllare un motore
```cpp
if (commandId == 11) {
  motor_stop();
  UART_SetCommandVoice(0x00);     // 播报确认
}
```
