[English](../../../../en/06-multi-host/arduino/iic/README.md) | [Deutsch](../../../../de/06-multi-host/arduino/iic/README.md) | [Español](../../../../es/06-multi-host/arduino/iic/README.md) | [Français](../../../../fr/06-multi-host/arduino/iic/README.md) | [Italiano](../../../../it/06-multi-host/arduino/iic/README.md) | [日本語](../../../../ja/06-multi-host/arduino/iic/README.md) | [한국어](../../../../ko/06-multi-host/arduino/iic/README.md) | [Português (BR)](../../../../pt-br/06-multi-host/arduino/iic/README.md) | Português (PT) | [简体中文](../../../../zh-hans/06-multi-host/arduino/iic/README.md) | [繁體中文](../../../../zh-hant/06-multi-host/arduino/iic/README.md)

# Tutorial da Versão BSP do Módulo de Voz IIC

## 📁 Estrutura de Ficheiros

```
iic/
├── iic.ino    # 主程序
├── bsp_iic.hpp         # 头文件（地址和函数声明）
├── bsp_iic.cpp         # 实现文件
└── README.md            # 本教程
```

---

## 🔌 Ligação de Hardware

| Arduino | Módulo de Voz |
|---------|----------|
| A4 (SDA) | SDA |
| A5 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

---

## 🔧 Compilar e Carregar

### Passo 1: Abrir o Arduino IDE
1. Abra o ficheiro `IIC_Voice.ino`
2. Selecione o modelo da sua placa (por exemplo, Arduino Uno)
3. Selecione a porta série correspondente

### Passo 2: Compilar e Carregar
1. Clique no botão ✔️ para compilar
2. Clique no botão ➡️ para carregar para a placa

---

## 📡 Teste Série

### Abra o Monitor Série no Arduino IDE
- Taxa de transferência: **115200**
- Fim de linha: **None**

### Saída Esperada

Após a alimentação, deverá ver:
```
IIC Voice Module Initialized
```

Diga a palavra de despertar e a palavra de comando ao módulo, e este emitirá o ID correspondente:
```
ID: 1
ID: 2
ID: 10
```

---

## 📚 Mapa de Registos

| Registo | Endereço | Função | Descrição |
|--------|------|------|------|
| REG_RESULT | 0xDA | Ler o ID do comando | Lê 1 byte, 0 = não reconhecido |
| REG_PASSIVE | 0xD1 | Escrever transmissão passiva | Escreve 1 byte, 0x00 = voz de transmissão passiva |
| REG_FUNCTION | 0xD2 | Escrever transmissão de palavras de função | Escreve 1 byte, 0x00 = voz de transmissão de palavras de função |
| REG_COMMAND | 0xD3 | Escrever transmissão de palavras de comando | Escreve 1 byte, 0x00 = voz de transmissão de palavras de comando |

---

## 📚 Referência da Interface BSP

### 1. IIC_Init()
```cpp
void IIC_Init(void);
```
**Função**: Inicializa o barramento I2C

**Exemplo**:
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
**Função**: Lê o ID do comando reconhecido pelo módulo de voz

**Valor de retorno**:
- `0` - nenhum comando reconhecido
- `1~254` - ID do comando
- `-1` - erro de comunicação

**Exemplo**:
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
**Função**: Define a voz de transmissão passiva

**Parâmetro**:
- `0x00` - tipo de voz de transmissão passiva

**Exemplo**:
```cpp
IIC_SetPassiveVoice(0x00);
delay(200);
```

---

### 4. IIC_SetFunctionVoice()
```cpp
void IIC_SetFunctionVoice(uint8_t voiceID);
```
**Função**: Define a voz de transmissão de palavras de função

**Parâmetro**:
- `0x00` - tipo de voz de transmissão de palavras de função

**Exemplo**:
```cpp
IIC_SetFunctionVoice(0x00);
delay(200);
```

---

### 5. IIC_SetCommandVoice()
```cpp
void IIC_SetCommandVoice(uint8_t voiceID);
```
**Função**: Define a voz de transmissão de palavras de comando

**Parâmetro**:
- `0x00` - tipo de voz de transmissão de palavras de comando

**Exemplo**:
```cpp
IIC_SetCommandVoice(0x00);
delay(200);
```

---

## 🎯 Lógica do Programa Principal

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

### P1: O monitor série só mostra "IIC Read Error"

**Causas possíveis:**
1. Cablagem incorreta ou não ligada
2. Módulo sem alimentação
3. Endereço I2C errado

**Soluções:**
- Verifique se SDA/SCL estão invertidos
- Verifique se o GND é massa comum
- Verifique se a alimentação de 5V está normal
- Utilize um programa de varrimento I2C para confirmar o endereço do dispositivo

---

### P2: Sem qualquer saída

**Causas possíveis:**
1. Taxa de transferência série errada
2. Módulo não acordado

**Soluções:**
- Confirme que a taxa de transferência série é 115200
- Diga primeiro a palavra de despertar e depois a palavra de comando

---

### P3: A saída mostra "ID: 255" ou "ID: 0"

**Explicação:** Isto é normal

- `0` = nenhum comando reconhecido
- `255` = nenhum dado novo

Estes valores já são filtrados no código, pelo que normalmente não são emitidos. Se os vir, o código não está a fazer efeito.

---

## 💡 Vantagens da Arquitetura BSP

### 1. Camadas de código claras
- **bsp_iic.hpp** - apenas declaração, sem implementação
- **bsp_iic.cpp** - detalhes concretos da implementação
- **IIC_Voice.ino** - apenas se preocupa com a lógica de negócio

### 2. Fácil de portar
Se mudar para outra plataforma (por exemplo, STM32, ESP32), só precisa de modificar a implementação em `bsp_iic.cpp`; o programa principal não precisa de ser alterado.

### 3. Fácil de manter
As alterações ao código relacionado com I2C estão confinadas a `bsp_iic.cpp` — corrigir uma vez, com efeito em todo o lado.

---

## 🚀 Exemplos de Funções Alargadas

### Exemplo 1: Acionar transmissões diferentes com base em comandos diferentes
```cpp
if (commandId == 1) {
  IIC_SetCommandVoice(0x00);      // 播报命令词
} else if (commandId == 2) {
  IIC_SetFunctionVoice(0x00);     // 播报功能词
} else if (commandId == 3) {
  IIC_SetPassiveVoice(0x00);      // 播报被动语
}
```

### Exemplo 2: Controlar um LED
```cpp
if (commandId == 10) {
  digitalWrite(LED_PIN, LOW);    // 关灯
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```

### Exemplo 3: Controlar um motor
```cpp
if (commandId == 11) {
  motor_stop();
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```
