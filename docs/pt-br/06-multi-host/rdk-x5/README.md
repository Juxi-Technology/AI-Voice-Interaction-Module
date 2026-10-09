[English](../../../en/06-multi-host/rdk-x5/README.md) | [Deutsch](../../../de/06-multi-host/rdk-x5/README.md) | [Español](../../../es/06-multi-host/rdk-x5/README.md) | [Français](../../../fr/06-multi-host/rdk-x5/README.md) | [Italiano](../../../it/06-multi-host/rdk-x5/README.md) | [日本語](../../../ja/06-multi-host/rdk-x5/README.md) | [한국어](../../../ko/06-multi-host/rdk-x5/README.md) | Português (BR) | [Português (PT)](../../../pt-pt/06-multi-host/rdk-x5/README.md) | [简体中文](../../../zh-hans/06-multi-host/rdk-x5/README.md) | [繁體中文](../../../zh-hant/06-multi-host/rdk-x5/README.md)

# Módulo de Interação de Voz com IA - Guia do Usuário do RDK X5 (Python)

## Índice

1. [Introdução](#introdução)
2. [Conexão de Hardware](#conexão-de-hardware)
3. [Configuração do Ambiente](#configuração-do-ambiente)
4. [Uso da Versão IIC](#uso-da-versão-iic)
5. [Uso da Versão UART](#uso-da-versão-uart)
6. [Perguntas Frequentes](#perguntas-frequentes)

---

## Introdução

Este repositório fornece código de exemplo em Python para a plataforma RDK X5 (Raspberry Pi) se comunicar com o módulo de interação de voz com IA, com suporte tanto ao método de comunicação I2C quanto ao UART.

- **Módulo de Reconhecimento de Voz**: Suporta reconhecimento de voz offline, emite o ID do comando após o reconhecimento
- **Função de Transmissão (Broadcast)**: Suporta transmissão passiva, transmissão de palavras de função e transmissão de palavras de comando
- **Protocolo de Comunicação**: Endereço I2C 0x2A, taxa de transmissão (baud rate) UART 115200
- **Linguagem de Programação**: Python 3

---

## Conexão de Hardware

### Conexão Geral

| Pino do RDK X5 | Módulo de Voz | Descrição |
|------------|-------------|-------------|
| 5V (Pino 2/4) | 5V | Positivo da alimentação |
| GND (Pino 6/9) | GND | Terra da alimentação |

> **Importante**: Garanta que todos os dispositivos compartilhem um terra comum!

---

### Conexão da Versão I2C

| Pino do RDK X5 | Módulo de Voz | Descrição |
|------------|-------------|-------------|
| SDA (GPIO3, Pino 3) | SDA | Linha de dados I2C |
| SCL (GPIO5, Pino 5) | SCL | Linha de clock I2C |

**Observação**: Usa o barramento I2C 5 por padrão (numeração BCM)

---

### Conexão da Versão UART

| Pino do RDK X5 | Módulo de Voz | Descrição |
|------------|-------------|-------------|
| GPIO14 (TXD, Pino 8) | RX | Transmissão serial |
| GPIO15 (RXD, Pino 10) | TX | Recepção serial |

**Observação**: Usa o dispositivo serial `/dev/ttyAMA0` por padrão

---

### Conexão por Cabo Type-C (Alternativa ao UART)

Se você usar um módulo adaptador USB-TTL:

| RDK X5 | Módulo USB-TTL | Módulo de Voz |
|--------|---------------|-------------|
| Porta USB | USB | - |
| - | RX | TX |
| - | TX | RX |
| GND | GND | GND |

**Observação**: Neste caso, o dispositivo serial geralmente é `/dev/ttyUSB0`

---

## Configuração do Ambiente

### 1. Requisitos do Sistema

- RDK X5 (ou Raspberry Pi 3/4/5)
- Sistema Ubuntu / Debian
- Python 3.7+

### 2. Instalar Dependências

```bash
# Update packages
sudo apt update
sudo apt upgrade -y

# Install Python libraries
sudo apt install -y python3-pip python3-smbus i2c-tools

# Install pyserial
pip3 install pyserial
```

### 3. Habilitar a Interface I2C

```bash
# Open configuration tool
sudo raspi-config

# Select Interface Options → I2C → Enable
# Reboot to take effect
sudo reboot
```

### 4. Habilitar a Interface Serial

```bash
# Open configuration tool
sudo raspi-config

# Select Interface Options → Serial
# Select: No (shell) → Yes (hardware serial port)
# Reboot to take effect
sudo reboot
```

### 5. Testar as Interfaces de Hardware

```bash
# Test I2C device
sudo i2cdetect -y 5

# Test serial port
ls /dev/ttyAMA0
ls /dev/ttyUSB0  # If using USB-TTL
```

---

## Uso da Versão IIC

### 1. Verificar os Arquivos de Código

```bash
cd IIC_Voice
ls -la
# Should see iic_voice.py
```

### 2. Configurar o Barramento I2C

Edite o arquivo `iic_voice.py`, modifique os parâmetros conforme necessário:

```python
# I2C device address
DEVICE_ADDRESS = 0x2A

# Register address
REG_RESULT = 0xDA

# I2C bus number (modify according to actual connection)
bus = smbus.SMBus(5)  # I2C bus 5
```

### 3. Executar o Programa

```bash
# Make executable
chmod +x iic_voice.py

# Run (sudo required for I2C access)
sudo python3 iic_voice.py
```

### 4. Executar o Teste

Após a inicialização normal, ele exibirá:

```
Speech Serial Opened! Baudrate=115200
```

Fale palavras de comando ao módulo de voz e os IDs correspondentes serão exibidos:

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. Parar o Programa

Pressione `Ctrl + C` para parar o programa:

```
Program terminated
```

---

## Uso da Versão UART

### 1. Verificar os Arquivos de Código

```bash
cd UART_Voice
ls -la
# Should see uart_voice.py
```

### 2. Configurar a Porta Serial

Edite o arquivo `uart_voice.py`, modifique o dispositivo serial:

```python
# UART direct connection (default)
SERIAL_PORT = '/dev/ttyAMA0'

# Or use USB-TTL
# SERIAL_PORT = '/dev/ttyUSB0'

# Baud rate
BAUD_RATE = 115200
```

### 3. Executar o Programa

```bash
# Make executable
chmod +x uart_voice.py

# Run (sudo required for serial port access)
sudo python3 uart_voice.py
```

### 4. Executar o Teste

Após a inicialização normal, ele exibirá:

```
Speech Serial Opened! Baudrate=115200
```

Fale palavras de comando ao módulo de voz e os IDs correspondentes serão exibidos:

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. Parar o Programa

Pressione `Ctrl + C` para parar o programa

---

## Perguntas Frequentes

### Q1: Permissões insuficientes para operar o I2C

**R: Adicione o usuário ao grupo de usuários do I2C:**
```bash
sudo usermod -aG i2c $USER
# Re-login to take effect
```
Ou execute com `sudo`

---

### Q2: Dispositivo serial não encontrado

**R: Verifique:**
1. Verifique se a porta serial está habilitada (raspi-config)
2. Verifique se o nome do dispositivo está correto
   - UART direto: `/dev/ttyAMA0`
   - USB-TTL: `/dev/ttyUSB0` ou `/dev/ttyUSB1`
3. Verifique se a conexão de hardware está correta
4. Verifique se a porta serial está ocupada por outros programas

```bash
# List available serial ports
ls /dev/tty* | grep tty
```

---

### Q3: Dispositivo I2C não detectado na varredura

**R: Verifique:**
1. Confirme se o I2C está habilitado (raspi-config)
2. Verifique se SDA/SCL estão invertidos
3. Verifique se o terra comum está conectado
4. Verifique se o dispositivo está energizado

```bash
# Scan I2C devices
sudo i2cdetect -y 5
```

Se você vir 0x2A, a conexão do dispositivo está normal

---

### Q4: O ID do comando mostra apenas 0 ou nada

**R: Comportamento normal:**
- 0 = Nenhum comando válido reconhecido
- Os IDs só são emitidos quando palavras de comando válidas são faladas
- Ative o módulo primeiro, depois fale o comando

---

### Q5: A precisão do reconhecimento não é alta

**R: Sugestões de otimização:**
- Garanta um ambiente silencioso, sem muito ruído de fundo
- Mantenha uma distância adequada do microfone (10-50cm)
- Fale em velocidade moderada e com pronúncia clara

---

### Q6: Comunicação serial anormal

**R: Verifique:**
1. TX/RX estão conectados de forma cruzada corretamente? (TX do Módulo → RX da RPi)
2. A taxa de transmissão (baud rate) é 115200
3. O terra comum está conectado
4. A porta serial está ocupada por outros processos

```bash
# Check serial port occupancy
sudo lsof /dev/ttyAMA0
```

---

## Suporte Técnico

Se você encontrar problemas, verifique:
1. A conexão de hardware está correta (o terra comum é muito importante!)
2. A taxa de transmissão serial (baud rate) é 115200
3. O endereço I2C está correto (0x2A)
4. Você tem permissões suficientes para acessar as interfaces de hardware

```bash
# Useful debugging commands
ls -l /dev/i2c*      # List I2C devices
ls -l /dev/ttyAMA0   # List serial device
groups                # List user group permissions
```
