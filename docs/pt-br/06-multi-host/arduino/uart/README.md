[English](../../../../en/06-multi-host/arduino/uart/README.md) | [Deutsch](../../../../de/06-multi-host/arduino/uart/README.md) | [Español](../../../../es/06-multi-host/arduino/uart/README.md) | [Français](../../../../fr/06-multi-host/arduino/uart/README.md) | [Italiano](../../../../it/06-multi-host/arduino/uart/README.md) | [日本語](../../../../ja/06-multi-host/arduino/uart/README.md) | [한국어](../../../../ko/06-multi-host/arduino/uart/README.md) | Português (BR) | [Português (PT)](../../../../pt-pt/06-multi-host/arduino/uart/README.md) | [简体中文](../../../../zh-hans/06-multi-host/arduino/uart/README.md) | [繁體中文](../../../../zh-hant/06-multi-host/arduino/uart/README.md)

# Tutorial da Versão BSP do Módulo de Voz UART

## 📁 Estrutura de Arquivos

```
uart/
├── uart.ino    # 主程序
├── bsp_uart.hpp         # 头文件（协议帧和函数声明）
├── bsp_uart.cpp         # 实现文件
└── README.md              # 本教程
```

---

## 🔌 Conexão de Hardware

### Conectando ao Módulo de Voz
| Arduino | Módulo de Voz |
|---------|----------|
| D10 (RX) | TX |
| D11 (TX) | RX |
| GND | GND |
| 5V | 5V |

> 💡 **Observação:** RX e TX devem ser conectados de forma cruzada!

---

## 🔧 Compilar e Enviar

### Passo 1: Abra o Arduino IDE
1. Abra o arquivo `UART_Voice.ino`
2. Selecione o modelo da sua placa (por exemplo, Arduino Uno)
3. Selecione a porta serial correspondente

### Passo 2: Compilar e Enviar
1. Clique no botão ✔️ para compilar
2. Clique no botão ➡️ para enviar para a placa

---

## 📡 Teste Serial

### Abra o Monitor Serial no Arduino IDE
- Taxa de transmissão (baud rate): **115200**
- Fim de linha: **None**

### Saída Esperada

Após energizar, você deverá ver:
```
UART Voice Module Initialized
```

Fale a palavra de ativação e a palavra de comando ao módulo, e ele emitirá o ID correspondente:
```
ID: 1
ID: 2
ID: 10
```

---

## 📚 Formato do Quadro de Protocolo

| Byte | Conteúdo | Descrição |
|------|------|------|
| 1 | 0xFE | Cabeçalho de quadro 1 |
| 2 | 0xEF | Cabeçalho de quadro 2 |
| 3 | Código de função | 0xD1 = transmissão passiva, 0xD2 = palavra de função, 0xD3 = palavra de comando |
| 4 | Dados | ID do comando ou ID da transmissão |
| 5 | 0xEE | Final do quadro |

**Exemplo:** Ler ID do comando = 10
```
FE EF 00 0A EE
```

**Exemplo:** Enviar transmissão de palavra de comando
```
FE EF D3 00 EE
```

---

## 📚 Referência da Interface BSP

### 1. UART_Init()
```cpp
void UART_Init(void);
```
**Função**: Inicializa a porta serial (taxa de transmissão (baud rate) 115200)

**Exemplo**:
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
**Função**: Lê o ID do comando reconhecido pelo módulo de voz

**Valor de retorno**:
- `0` - nenhum comando reconhecido
- `1~254` - ID do comando
- `-1` - nenhum dado novo

**Exemplo**:
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
**Função**: Define a voz de transmissão passiva

**Parâmetro**:
- `0x00` - tipo de voz de transmissão passiva

**Exemplo**:
```cpp
UART_SetPassiveVoice(0x00);
delay(200);
```

---

### 4. UART_SetFunctionVoice()
```cpp
void UART_SetFunctionVoice(uint8_t voiceID);
```
**Função**: Define a voz de transmissão de palavra de função

**Parâmetro**:
- `0x00` - tipo de voz de transmissão de palavra de função

**Exemplo**:
```cpp
UART_SetFunctionVoice(0x00);
delay(200);
```

---

### 5. UART_SetCommandVoice()
```cpp
void UART_SetCommandVoice(uint8_t voiceID);
```
**Função**: Define a voz de transmissão de palavra de comando

**Parâmetro**:
- `0x00` - tipo de voz de transmissão de palavra de comando

**Exemplo**:
```cpp
UART_SetCommandVoice(0x00);
delay(200);
```

---

## 🎯 Lógica do Programa Principal

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

## 🔍 Perguntas Frequentes

### Q1: Nenhuma saída

**Possíveis causas:**
1. RX/TX estão invertidos
2. O GND não é terra comum
3. Módulo sem alimentação
4. Taxa de transmissão (baud rate) errada

**Soluções:**
- Confirme se o D10 conecta ao TX do módulo e o D11 conecta ao RX do módulo (conexão cruzada)
- Confirme a conexão do GND
- Confirme se a alimentação de 5V está normal
- Confirme se a taxa de transmissão serial (baud rate) é 115200

---

### Q2: O monitor serial mostra apenas texto embaralhado

**Possíveis causas:**
1. Incompatibilidade de taxa de transmissão (baud rate)
2. Inicialização anormal do módulo

**Soluções:**
- Confirme se a taxa de transmissão (baud rate) do monitor serial é 115200
- Pressione o botão de reset do módulo uma vez

---

### Q3: A saída mostra "ID: 255" ou "ID: 0"

**Explicação:** Isso é normal
- `0` = nenhum comando reconhecido
- `255` = nenhum dado novo

Esses valores já são filtrados no código, então normalmente não são emitidos. Se você realmente os vir, o código não está sendo aplicado.

---

## 💡 Vantagens da Arquitetura BSP

### 1. Camadas de código claras
- **bsp_uart.hpp** - apenas declaração, sem implementação
- **bsp_uart.cpp** - detalhes concretos de implementação
- **UART_Voice.ino** - cuida apenas da lógica de negócio

### 2. Fácil de portar
Se você mudar para outra plataforma (por exemplo, STM32, ESP32), você só precisa modificar a implementação em `bsp_uart.cpp`; o programa principal não precisa mudar.

### 3. Fácil de manter
As alterações no código relacionado ao UART ficam confinadas a `bsp_uart.cpp` — corrige uma vez, vale em todos os lugares.

---

## 🚀 Exemplos de Funções Estendidas

### Exemplo 1: Acionar transmissões diferentes com base em comandos diferentes
```cpp
if (commandId == 1) {
  UART_SetCommandVoice(0x00);      // 播报命令词
} else if (commandId == 2) {
  UART_SetFunctionVoice(0x00);     // 播报功能词
} else if (commandId == 3) {
  UART_SetPassiveVoice(0x00);      // 播报被动语
}
```

### Exemplo 2: Controlar um LED
```cpp
if (commandId == 10) {
  digitalWrite(LED_PIN, LOW);    // 关灯
  UART_SetCommandVoice(0x00);     // 播报确认
}
```

### Exemplo 3: Controlar um motor
```cpp
if (commandId == 11) {
  motor_stop();
  UART_SetCommandVoice(0x00);     // 播报确认
}
```
