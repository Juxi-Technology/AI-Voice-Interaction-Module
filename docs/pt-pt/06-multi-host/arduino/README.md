[English](../../../en/06-multi-host/arduino/README.md) | [Deutsch](../../../de/06-multi-host/arduino/README.md) | [Español](../../../es/06-multi-host/arduino/README.md) | [Français](../../../fr/06-multi-host/arduino/README.md) | [Italiano](../../../it/06-multi-host/arduino/README.md) | [日本語](../../../ja/06-multi-host/arduino/README.md) | [한국어](../../../ko/06-multi-host/arduino/README.md) | [Português (BR)](../../../pt-br/06-multi-host/arduino/README.md) | Português (PT) | [简体中文](../../../zh-hans/06-multi-host/arduino/README.md) | [繁體中文](../../../zh-hant/06-multi-host/arduino/README.md)

# Módulo de Interação por Voz IA - Guia do Utilizador para Arduino

## Índice

1. [Introdução](#introdução)
2. [Ligação de Hardware](#ligação-de-hardware)
3. [Configuração do Ambiente de Desenvolvimento](#configuração-do-ambiente-de-desenvolvimento)
4. [Utilização da Versão IIC](#utilização-da-versão-iic)
5. [Utilização da Versão UART](#utilização-da-versão-uart)
6. [FAQ](#faq)

---

## Introdução

Este repositório fornece código de exemplo para a plataforma Arduino comunicar com o módulo de interação por voz IA, suportando tanto o método de comunicação I2C como o UART.

- **Módulo de Reconhecimento de Voz**: suporta reconhecimento de voz offline, emitindo o ID do comando após o reconhecimento
- **Função de Transmissão**: suporta transmissão passiva, transmissão de palavras de função e transmissão de palavras de comando
- **Protocolo de Comunicação**: endereço I2C 0x2A, taxa de transferência UART 115200

---

## Ligação de Hardware

### Ligação Geral

| Pino do Arduino | Módulo de Voz | Descrição |
|-------------|-------------|-------------|
| 5V | 5V | Positivo da alimentação |
| GND | GND | Massa da alimentação |

---

### Ligação da Versão I2C

| Pino do Arduino | Módulo de Voz | Descrição |
|-------------|-------------|-------------|
| A4 (SDA) | SDA | Linha de dados I2C |
| A5 (SCL) | SCL | Linha de relógio I2C |

---

### Ligação da Versão UART

| Pino do Arduino | Módulo de Voz | Descrição |
|-------------|-------------|-------------|
| D10 (RX) | TX | Receção série (Software Serial) |
| D11 (TX) | RX | Transmissão série (Software Serial) |

---

### Ligação de Depuração Série

| Pino do Arduino | USB-TTL | Descrição |
|-------------|---------|-------------|
| TX (D1) | RX | Saída de depuração |
| RX (D0) | TX | Entrada de depuração (opcional) |
| GND | GND | Massa comum |

---

## Configuração do Ambiente de Desenvolvimento

### 1. Instalar o Arduino IDE

- Descarregar: https://www.arduino.cc/en/software
- Instalar a versão mais recente

### 2. Instalar o Pacote de Suporte da Placa

- Abrir o Arduino IDE
- Ferramentas → Placa → Gestor de Placas
- Pesquisar e instalar o pacote de suporte da sua placa Arduino
- Recomendado: Arduino Uno / Nano

---

## Utilização da Versão IIC

### 1. Abrir o Projeto

- Abra `IIC_Voice/IIC_Voice.ino` no Arduino IDE

### 2. Carregar o Código

- Selecione o modelo correto da placa (Ferramentas → Placa)
- Selecione a porta correta (Ferramentas → Porta)
- Clique no botão de carregamento (→)
- Aguarde que o carregamento termine

### 3. Executar o Teste

1. Abra o Monitor Série (Ferramentas → Monitor Série)
2. Defina a taxa de transferência para **115200**
3. Após um arranque normal, apresentará:

```
IIC Voice Module Initialized
```

4. Diga palavras de comando ao módulo de voz e os IDs correspondentes serão apresentados:

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

## Utilização da Versão UART

### 1. Abrir o Projeto

- Abra `UART_Voice/UART_Voice.ino` no Arduino IDE

### 2. Carregar o Código

- Selecione o modelo correto da placa
- Selecione a porta correta
- Clique no botão de carregamento
- Aguarde que o carregamento termine

### 3. Executar o Teste

1. Abra o Monitor Série
2. Defina a taxa de transferência para **115200**
3. Após um arranque normal, apresentará:

```
UART Voice Module Initialized
```

4. Diga palavras de comando ao módulo de voz e os IDs correspondentes serão apresentados:

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

## FAQ

### P1: Sem saída no Monitor Série

**R: Verifique o seguinte:**
- Verifique se a taxa de transferência série é 115200
- Verifique se a porta correta está selecionada
- Verifique se TX/RX estão invertidos
- Verifique se o GND está ligado

---

### P2: A versão I2C mostra "IIC Read Error"

**R: Verifique a ligação I2C:**
- Verifique se SDA/SCL estão invertidos
- Verifique se o endereço do dispositivo está correto (0x2A)
- Verifique se o GND está ligado

---

### P3: O ID do comando só mostra 0 ou 255

**R: Comportamento normal:**
- 0 = nenhum comando válido reconhecido
- 255 = nenhum dado novo
- Os IDs válidos só são emitidos após um reconhecimento normal

---

### P4: A precisão do reconhecimento não é elevada

**R: Sugestões de otimização:**
- Garanta um ambiente silencioso, sem demasiado ruído de fundo
- Mantenha uma distância adequada do microfone (10-50 cm)
- Fale a um ritmo moderado e com pronúncia clara

---

### P5: A versão UART não recebe dados

**R: Verifique:**
- Confirme que o TX do módulo de voz está ligado ao D10 (RX) do Arduino
- Confirme que o RX do módulo de voz está ligado ao D11 (TX) do Arduino
- Verifique se a taxa de transferência é 115200

---

## Apoio Técnico

Se encontrar problemas, verifique:
1. A ligação de hardware está correta
2. A taxa de transferência série corresponde
3. O endereço I2C está correto
4. O GND está ligado (muito importante!)
