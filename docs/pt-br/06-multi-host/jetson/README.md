[English](../../../en/06-multi-host/jetson/README.md) | [Deutsch](../../../de/06-multi-host/jetson/README.md) | [Español](../../../es/06-multi-host/jetson/README.md) | [Français](../../../fr/06-multi-host/jetson/README.md) | [Italiano](../../../it/06-multi-host/jetson/README.md) | [日本語](../../../ja/06-multi-host/jetson/README.md) | [한국어](../../../ko/06-multi-host/jetson/README.md) | Português (BR) | [Português (PT)](../../../pt-pt/06-multi-host/jetson/README.md) | [简体中文](../../../zh-hans/06-multi-host/jetson/README.md) | [繁體中文](../../../zh-hant/06-multi-host/jetson/README.md)

# Guia do Usuário do Módulo de Interação de Voz para Jetson

## Instalar Dependências

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## Verificar os Grupos do Usuário

```bash
sudo usermod -aG i2c $USER
sudo usermod -aG dialout $USER
```

Faça logout e login novamente para que as alterações tenham efeito.

## Versão IIC

### Localização do Arquivo
`IIC_Voice/iic_voice.py`

### Instruções de Fiação

| Jetson | Módulo de Voz |
|--------|--------------|
| Pino 27 (I2C1 SDA) | SDA |
| Pino 28 (I2C1 SCL) | SCL |
| Pino 6 (GND) | GND |
| Pino 4 (5V) | 5V |

### Verificar o Dispositivo I2C

```bash
sudo i2cdetect -y -r 1
```

Você deverá ver o endereço 0x2A

### Executar

```bash
cd IIC_Voice
python3 iic_voice.py
```

### Formato de Saída

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## Versão UART

### Localização do Arquivo
`UART_Voice/uart_voice.py`

### Conexão via Pinos UART

Ao conectar o módulo ao Jetson pelos pinos UART, comente `SERIAL_PORT = '/dev/ttyUSB0'` e descomente `SERIAL_PORT = '/dev/ttyTHS1'`

#### Instruções de Fiação

| Jetson | Módulo de Voz |
|--------|--------------|
| Pino 8 (UART1 TX) | RX |
| Pino 10 (UART1 RX) | TX |
| Pino 6 (GND) | GND |
| Pino 4 (5V) | 5V |

### Verificar a Porta Serial

```bash
ls /dev/ttyTHS*
```

### Executar

```bash
cd UART_Voice
python3 uart_voice.py
```

### Formato de Saída

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

### Conexão via Cabo Type-C

Ao conectar o módulo ao Jetson por cabo Type-C, descomente `SERIAL_PORT = '/dev/ttyUSB0'` e comente `SERIAL_PORT = '/dev/ttyTHS1'`

### Verificar a Porta Serial

```bash
ls /dev/ttyUSB*
```

### Executar

```bash
cd UART_Voice
python3 uart_voice.py
```

### Formato de Saída

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## Perguntas Frequentes

### Problema de Permissão do I2C

```bash
sudo chmod 666 /dev/i2c-1
```

### Porta Serial Ocupada

Se a porta serial não puder ser aberta, verifique se ela está ocupada por outros serviços:

```bash
sudo systemctl stop nvgetty
sudo systemctl disable nvgetty
```

## Descrição do Protocolo

### Protocolo UART

| Byte | Conteúdo |
|------|---------|
| 1 | 0xFE (Cabeçalho do Quadro) |
| 2 | 0xEF (Cabeçalho do Quadro) |
| 3 | ID da Palavra de Função |
| 4 | ID da Palavra de Comando |
| 5 | 0xEE (Final do Quadro) |

### Protocolo IIC

- Endereço do Dispositivo: 0x2A
- Registrador de Leitura: 0xDA (Lê 1 byte)
  - 0x00: Não Reconhecido
  - Outro: ID da Palavra de Comando
