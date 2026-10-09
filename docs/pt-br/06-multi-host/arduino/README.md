[English](../../../en/06-multi-host/arduino/README.md) | [Deutsch](../../../de/06-multi-host/arduino/README.md) | [Español](../../../es/06-multi-host/arduino/README.md) | [Français](../../../fr/06-multi-host/arduino/README.md) | [Italiano](../../../it/06-multi-host/arduino/README.md) | [日本語](../../../ja/06-multi-host/arduino/README.md) | [한국어](../../../ko/06-multi-host/arduino/README.md) | Português (BR) | [Português (PT)](../../../pt-pt/06-multi-host/arduino/README.md) | [简体中文](../../../zh-hans/06-multi-host/arduino/README.md) | [繁體中文](../../../zh-hant/06-multi-host/arduino/README.md)

# Módulo de Interação de Voz com IA - Guia do Usuário do Arduino

## Índice

1. [Introdução](#introdução)
2. [Conexão de Hardware](#conexão-de-hardware)
3. [Configuração do Ambiente de Desenvolvimento](#configuração-do-ambiente-de-desenvolvimento)
4. [Uso da Versão IIC](#uso-da-versão-iic)
5. [Uso da Versão UART](#uso-da-versão-uart)
6. [Perguntas Frequentes](#perguntas-frequentes)

---

## Introdução

Este repositório fornece código de exemplo para a plataforma Arduino se comunicar com o módulo de interação de voz com IA, com suporte tanto ao método de comunicação I2C quanto ao UART.

- **Módulo de Reconhecimento de Voz**: Suporta reconhecimento de voz offline, emite o ID do comando após o reconhecimento
- **Função de Transmissão (Broadcast)**: Suporta transmissão passiva, transmissão de palavras de função e transmissão de palavras de comando
- **Protocolo de Comunicação**: Endereço I2C 0x2A, taxa de transmissão (baud rate) UART 115200

---

## Conexão de Hardware

### Conexão Geral

| Pino do Arduino | Módulo de Voz | Descrição |
|-------------|-------------|-------------|
| 5V | 5V | Positivo da alimentação |
| GND | GND | Terra da alimentação |

---

### Conexão da Versão I2C

| Pino do Arduino | Módulo de Voz | Descrição |
|-------------|-------------|-------------|
| A4 (SDA) | SDA | Linha de dados I2C |
| A5 (SCL) | SCL | Linha de clock I2C |

---

### Conexão da Versão UART

| Pino do Arduino | Módulo de Voz | Descrição |
|-------------|-------------|-------------|
| D10 (RX) | TX | Recepção serial (Software Serial) |
| D11 (TX) | RX | Transmissão serial (Software Serial) |

---

### Conexão de Depuração Serial

| Pino do Arduino | USB-TTL | Descrição |
|-------------|---------|-------------|
| TX (D1) | RX | Saída de depuração |
| RX (D0) | TX | Entrada de depuração (opcional) |
| GND | GND | Terra comum |

---

## Configuração do Ambiente de Desenvolvimento

### 1. Instalar o Arduino IDE

- Download: https://www.arduino.cc/en/software
- Instale a versão mais recente

### 2. Instalar o Pacote de Suporte da Placa

- Abra o Arduino IDE
- Ferramentas → Placa → Gerenciador de Placas
- Pesquise e instale o pacote de suporte para a sua placa Arduino
- Recomendado: Arduino Uno / Nano

---

## Uso da Versão IIC

### 1. Abrir o Projeto

- Abra `IIC_Voice/IIC_Voice.ino` no Arduino IDE

### 2. Enviar o Código

- Selecione o modelo correto da placa (Ferramentas → Placa)
- Selecione a porta correta (Ferramentas → Porta)
- Clique no botão de envio (→)
- Aguarde a conclusão do envio

### 3. Executar o Teste

1. Abra o Monitor Serial (Ferramentas → Monitor Serial)
2. Defina a taxa de transmissão (baud rate) como **115200**
3. Após a inicialização normal, ele exibirá:

```
IIC Voice Module Initialized
```

4. Fale palavras de comando ao módulo de voz e os IDs correspondentes serão exibidos:

```
IIC Voice Module Initialized
ID: 1
ID: 4
ID: 10
```

### 4. Explicação do Código

```cpp
// Initialize I2C
IIC_Init();

// Read command ID
int commandId = IIC_ReadCommand();

// Set broadcast
IIC_SetCommandVoice(0x00);  // Command word broadcast
```

---

## Uso da Versão UART

### 1. Abrir o Projeto

- Abra `UART_Voice/UART_Voice.ino` no Arduino IDE

### 2. Enviar o Código

- Selecione o modelo correto da placa
- Selecione a porta correta
- Clique no botão de envio
- Aguarde a conclusão do envio

### 3. Executar o Teste

1. Abra o Monitor Serial
2. Defina a taxa de transmissão (baud rate) como **115200**
3. Após a inicialização normal, ele exibirá:

```
UART Voice Module Initialized
```

4. Fale palavras de comando ao módulo de voz e os IDs correspondentes serão exibidos:

```
UART Voice Module Initialized
ID: 1
ID: 4
ID: 10
```

### 4. Explicação do Código

```cpp
// Initialize serial (Software Serial D10/D11)
UART_Init();

// Read command ID
int commandId = UART_ReadCommand();

// Set broadcast
UART_SetCommandVoice(0x00);  // Command word broadcast
```

---

## Perguntas Frequentes

### Q1: Nenhuma saída no Monitor Serial

**R: Verifique o seguinte:**
- Verifique se a taxa de transmissão serial (baud rate) é 115200
- Verifique se a porta correta está selecionada
- Verifique se TX/RX estão invertidos
- Verifique se o GND está conectado

---

### Q2: A versão I2C mostra "IIC Read Error"

**R: Verifique a conexão I2C:**
- Verifique se SDA/SCL estão invertidos
- Verifique se o endereço do dispositivo está correto (0x2A)
- Verifique se o GND está conectado

---

### Q3: O ID do comando mostra apenas 0 ou 255

**R: Comportamento normal:**
- 0 = Nenhum comando válido reconhecido
- 255 = Nenhum dado novo
- Os IDs válidos só são emitidos após o reconhecimento normal

---

### Q4: A precisão do reconhecimento não é alta

**R: Sugestões de otimização:**
- Garanta um ambiente silencioso, sem muito ruído de fundo
- Mantenha uma distância adequada do microfone (10-50cm)
- Fale em velocidade moderada e com pronúncia clara

---

### Q5: A versão UART não recebe dados

**R: Verifique:**
- Confirme se o TX do módulo de voz está conectado ao D10 (RX) do Arduino
- Confirme se o RX do módulo de voz está conectado ao D11 (TX) do Arduino
- Verifique se a taxa de transmissão (baud rate) é 115200

---

## Suporte Técnico

Se você encontrar problemas, verifique:
1. A conexão de hardware está correta
2. A taxa de transmissão serial (baud rate) corresponde
3. O endereço I2C está correto
4. O GND está conectado (muito importante!)
