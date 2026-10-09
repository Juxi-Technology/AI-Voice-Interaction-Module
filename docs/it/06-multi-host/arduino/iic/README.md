[English](../../../../en/06-multi-host/arduino/iic/README.md) | [Deutsch](../../../../de/06-multi-host/arduino/iic/README.md) | [Español](../../../../es/06-multi-host/arduino/iic/README.md) | [Français](../../../../fr/06-multi-host/arduino/iic/README.md) | Italiano | [日本語](../../../../ja/06-multi-host/arduino/iic/README.md) | [한국어](../../../../ko/06-multi-host/arduino/iic/README.md) | [Português (BR)](../../../../pt-br/06-multi-host/arduino/iic/README.md) | [Português (PT)](../../../../pt-pt/06-multi-host/arduino/iic/README.md) | [简体中文](../../../../zh-hans/06-multi-host/arduino/iic/README.md) | [繁體中文](../../../../zh-hant/06-multi-host/arduino/iic/README.md)

# Tutorial della versione BSP del modulo vocale IIC

## 📁 Struttura dei file

```
iic/
├── iic.ino    # 主程序
├── bsp_iic.hpp         # 头文件（地址和函数声明）
├── bsp_iic.cpp         # 实现文件
└── README.md            # 本教程
```

---

## 🔌 Collegamento hardware

| Arduino | Modulo vocale |
|---------|----------|
| A4 (SDA) | SDA |
| A5 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

---

## 🔧 Compilazione e caricamento

### Passaggio 1: apri Arduino IDE
1. Apri il file `IIC_Voice.ino`
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
IIC Voice Module Initialized
```

Pronuncia la parola di risveglio e la parola di comando verso il modulo; verrà restituito l'ID corrispondente:
```
ID: 1
ID: 2
ID: 10
```

---

## 📚 Mappa dei registri

| Registro | Indirizzo | Funzione | Descrizione |
|--------|------|------|------|
| REG_RESULT | 0xDA | Legge l'ID del comando | Legge 1 byte, 0 = non riconosciuto |
| REG_PASSIVE | 0xD1 | Scrive la riproduzione passiva | Scrive 1 byte, 0x00 = voce di riproduzione passiva |
| REG_FUNCTION | 0xD2 | Scrive la riproduzione della parola di funzione | Scrive 1 byte, 0x00 = voce di riproduzione della parola di funzione |
| REG_COMMAND | 0xD3 | Scrive la riproduzione della parola di comando | Scrive 1 byte, 0x00 = voce di riproduzione della parola di comando |

---

## 📚 Riferimento all'interfaccia BSP

### 1. IIC_Init()
```cpp
void IIC_Init(void);
```
**Funzione**: inizializza il bus I2C

**Esempio**:
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
**Funzione**: legge l'ID del comando riconosciuto dal modulo vocale

**Valore restituito**:
- `0` - nessun comando riconosciuto
- `1~254` - ID del comando
- `-1` - errore di comunicazione

**Esempio**:
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
**Funzione**: imposta la voce di riproduzione passiva

**Parametro**:
- `0x00` - tipo di voce di riproduzione passiva

**Esempio**:
```cpp
IIC_SetPassiveVoice(0x00);
delay(200);
```

---

### 4. IIC_SetFunctionVoice()
```cpp
void IIC_SetFunctionVoice(uint8_t voiceID);
```
**Funzione**: imposta la voce di riproduzione della parola di funzione

**Parametro**:
- `0x00` - tipo di voce di riproduzione della parola di funzione

**Esempio**:
```cpp
IIC_SetFunctionVoice(0x00);
delay(200);
```

---

### 5. IIC_SetCommandVoice()
```cpp
void IIC_SetCommandVoice(uint8_t voiceID);
```
**Funzione**: imposta la voce di riproduzione della parola di comando

**Parametro**:
- `0x00` - tipo di voce di riproduzione della parola di comando

**Esempio**:
```cpp
IIC_SetCommandVoice(0x00);
delay(200);
```

---

## 🎯 Logica del programma principale

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

### D1: Il monitor seriale mostra solo "IIC Read Error"

**Possibili cause:**
1. Cablaggio errato o non collegato
2. Modulo non alimentato
3. Indirizzo I2C errato

**Soluzioni:**
- Verifica se SDA/SCL sono invertiti
- Verifica se il GND è una massa comune
- Verifica se l'alimentazione a 5V è regolare
- Usa un programma di scansione I2C per confermare l'indirizzo del dispositivo

---

### D2: Nessun output

**Possibili cause:**
1. Baud rate seriale errato
2. Modulo non risvegliato

**Soluzioni:**
- Conferma che il baud rate seriale sia 115200
- Di' prima la parola di risveglio, poi la parola di comando

---

### D3: L'output mostra "ID: 255" o "ID: 0"

**Spiegazione:** Questo è normale

- `0` = nessun comando riconosciuto
- `255` = nessun nuovo dato

Questi valori sono già filtrati nel codice, quindi normalmente non vengono restituiti. Se li vedi comunque, significa che il codice non sta avendo effetto.

---

## 💡 Vantaggi dell'architettura BSP

### 1. Chiara suddivisione in livelli del codice
- **bsp_iic.hpp** - solo dichiarazioni, nessuna implementazione
- **bsp_iic.cpp** - dettagli concreti dell'implementazione
- **IIC_Voice.ino** - si occupa solo della logica di business

### 2. Facile da portare su altre piattaforme
Se passi a un'altra piattaforma (ad es. STM32, ESP32), devi modificare solo l'implementazione in `bsp_iic.cpp`; il programma principale non deve essere cambiato.

### 3. Facile da mantenere
Le modifiche al codice relativo a I2C sono confinate in `bsp_iic.cpp` — correggi una volta, l'effetto vale ovunque.

---

## 🚀 Esempi di funzionalità estese

### Esempio 1: attivare riproduzioni diverse in base a comandi diversi
```cpp
if (commandId == 1) {
  IIC_SetCommandVoice(0x00);      // 播报命令词
} else if (commandId == 2) {
  IIC_SetFunctionVoice(0x00);     // 播报功能词
} else if (commandId == 3) {
  IIC_SetPassiveVoice(0x00);      // 播报被动语
}
```

### Esempio 2: controllare un LED
```cpp
if (commandId == 10) {
  digitalWrite(LED_PIN, LOW);    // 关灯
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```

### Esempio 3: controllare un motore
```cpp
if (commandId == 11) {
  motor_stop();
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```
