[English](../../../en/06-multi-host/rdk-x5/README.md) | [Deutsch](../../../de/06-multi-host/rdk-x5/README.md) | [Español](../../../es/06-multi-host/rdk-x5/README.md) | [Français](../../../fr/06-multi-host/rdk-x5/README.md) | [Italiano](../../../it/06-multi-host/rdk-x5/README.md) | [日本語](../../../ja/06-multi-host/rdk-x5/README.md) | [한국어](../../../ko/06-multi-host/rdk-x5/README.md) | [Português (BR)](../../../pt-br/06-multi-host/rdk-x5/README.md) | Português (PT) | [简体中文](../../../zh-hans/06-multi-host/rdk-x5/README.md) | [繁體中文](../../../zh-hant/06-multi-host/rdk-x5/README.md)

# Módulo de Interação por Voz IA - Guia do Utilizador para RDK X5 (Python)

## Índice

1. [Introdução](#introdução)
2. [Ligação de Hardware](#ligação-de-hardware)
3. [Configuração do Ambiente](#configuração-do-ambiente)
4. [Utilização da Versão IIC](#utilização-da-versão-iic)
5. [Utilização da Versão UART](#utilização-da-versão-uart)
6. [FAQ](#faq)

---

## Introdução

Este repositório fornece código de exemplo em Python para a plataforma RDK X5 (Raspberry Pi) comunicar com o módulo de interação por voz IA, suportando tanto o método de comunicação I2C como o UART.

- **Módulo de Reconhecimento de Voz**: suporta reconhecimento de voz offline, emitindo o ID do comando após o reconhecimento
- **Função de Transmissão**: suporta transmissão passiva, transmissão de palavras de função e transmissão de palavras de comando
- **Protocolo de Comunicação**: endereço I2C 0x2A, taxa de transferência UART 115200
- **Linguagem de Programação**: Python 3

---

## Ligação de Hardware

### Ligação Geral

| Pino do RDK X5 | Módulo de Voz | Descrição |
|------------|-------------|-------------|
| 5V (Pino 2/4) | 5V | Positivo da alimentação |
| GND (Pino 6/9) | GND | Massa da alimentação |

> **Importante**: Garanta que todos os dispositivos partilham uma massa comum!

---

### Ligação da Versão I2C

| Pino do RDK X5 | Módulo de Voz | Descrição |
|------------|-------------|-------------|
| SDA (GPIO3, Pino 3) | SDA | Linha de dados I2C |
| SCL (GPIO5, Pino 5) | SCL | Linha de relógio I2C |

**Nota**: Utiliza o barramento I2C 5 por predefinição (numeração BCM)

---

### Ligação da Versão UART

| Pino do RDK X5 | Módulo de Voz | Descrição |
|------------|-------------|-------------|
| GPIO14 (TXD, Pino 8) | RX | Transmissão série |
| GPIO15 (RXD, Pino 10) | TX | Receção série |

**Nota**: Utiliza o dispositivo série `/dev/ttyAMA0` por predefinição

---

### Ligação por Cabo Type-C (Alternativa ao UART)

Se utilizar um módulo adaptador USB-TTL:

| RDK X5 | Módulo USB-TTL | Módulo de Voz |
|--------|---------------|-------------|
| Porta USB | USB | - |
| - | RX | TX |
| - | TX | RX |
| GND | GND | GND |

**Nota**: Neste caso, o dispositivo série é normalmente `/dev/ttyUSB0`

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

### 3. Ativar a Interface I2C

```bash
# Open configuration tool
sudo raspi-config

# Select Interface Options → I2C → Enable
# Reboot to take effect
sudo reboot
```

### 4. Ativar a Interface Série

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

## Utilização da Versão IIC

### 1. Verificar os Ficheiros de Código

```bash
cd IIC_Voice
ls -la
# Should see iic_voice.py
```

### 2. Configurar o Barramento I2C

Edite o ficheiro `iic_voice.py` e modifique os parâmetros conforme necessário:

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

Após um arranque normal, apresentará:

```
Speech Serial Opened! Baudrate=115200
```

Diga palavras de comando ao módulo de voz e os IDs correspondentes serão apresentados:

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. Parar o Programa

Prima `Ctrl + C` para parar o programa:

```
Program terminated
```

---

## Utilização da Versão UART

### 1. Verificar os Ficheiros de Código

```bash
cd UART_Voice
ls -la
# Should see uart_voice.py
```

### 2. Configurar a Porta Série

Edite o ficheiro `uart_voice.py` e modifique o dispositivo série:

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

Após um arranque normal, apresentará:

```
Speech Serial Opened! Baudrate=115200
```

Diga palavras de comando ao módulo de voz e os IDs correspondentes serão apresentados:

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. Parar o Programa

Prima `Ctrl + C` para parar o programa

---

## FAQ

### P1: Permissões insuficientes para operações I2C

**R: Adicione o utilizador ao grupo de utilizadores I2C:**
```bash
sudo usermod -aG i2c $USER
# Re-login to take effect
```
Ou execute com `sudo`

---

### P2: Dispositivo série não encontrado

**R: Verifique:**
1. Verifique se a porta série está ativada (raspi-config)
2. Verifique se o nome do dispositivo está correto
   - UART direto: `/dev/ttyAMA0`
   - USB-TTL: `/dev/ttyUSB0` ou `/dev/ttyUSB1`
3. Verifique se a ligação de hardware está correta
4. Verifique se a porta série está ocupada por outros programas

```bash
# List available serial ports
ls /dev/tty* | grep tty
```

---

### P3: Dispositivo I2C não detetado no varrimento

**R: Verifique:**
1. Confirme que o I2C está ativado (raspi-config)
2. Verifique se SDA/SCL estão invertidos
3. Verifique se a massa comum está ligada
4. Verifique se o dispositivo está ligado

```bash
# Scan I2C devices
sudo i2cdetect -y 5
```

Se vir 0x2A, a ligação do dispositivo está normal

---

### P4: O ID do comando só mostra 0 ou nada

**R: Comportamento normal:**
- 0 = nenhum comando válido reconhecido
- Os IDs só são emitidos quando são ditas palavras de comando válidas
- Acorde primeiro o módulo e só depois diga o comando

---

### P5: Precisão do reconhecimento não elevada

**R: Sugestões de otimização:**
- Garanta um ambiente silencioso, sem demasiado ruído de fundo
- Mantenha uma distância adequada do microfone (10-50 cm)
- Fale a um ritmo moderado e com pronúncia clara

---

### P6: Comunicação série anormal

**R: Verifique:**
1. O TX/RX estão ligados de forma cruzada corretamente? (TX do módulo → RX da RPi)
2. A taxa de transferência é 115200
3. A massa comum está ligada
4. A porta série está ocupada por outros processos

```bash
# Check serial port occupancy
sudo lsof /dev/ttyAMA0
```

---

## Apoio Técnico

Se encontrar problemas, verifique:
1. A ligação de hardware está correta (a massa comum é muito importante!)
2. A taxa de transferência série é 115200
3. O endereço I2C está correto (0x2A)
4. Tem permissões suficientes para aceder às interfaces de hardware

```bash
# Useful debugging commands
ls -l /dev/i2c*      # List I2C devices
ls -l /dev/ttyAMA0   # List serial device
groups                # List user group permissions
```
