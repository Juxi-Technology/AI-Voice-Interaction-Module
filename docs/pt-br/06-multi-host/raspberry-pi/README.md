[English](../../../en/06-multi-host/raspberry-pi/README.md) | [Deutsch](../../../de/06-multi-host/raspberry-pi/README.md) | [Español](../../../es/06-multi-host/raspberry-pi/README.md) | [Français](../../../fr/06-multi-host/raspberry-pi/README.md) | [Italiano](../../../it/06-multi-host/raspberry-pi/README.md) | [日本語](../../../ja/06-multi-host/raspberry-pi/README.md) | [한국어](../../../ko/06-multi-host/raspberry-pi/README.md) | Português (BR) | [Português (PT)](../../../pt-pt/06-multi-host/raspberry-pi/README.md) | [简体中文](../../../zh-hans/06-multi-host/raspberry-pi/README.md) | [繁體中文](../../../zh-hant/06-multi-host/raspberry-pi/README.md)

# Guia do Usuário do Módulo de Interação de Voz para Raspberry Pi

## Instalar Dependências

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## Habilitar a Interface I2C

```bash
sudo raspi-config
```

Selecione `Interface Options` -> `I2C` -> `Yes`

Reinicie a Raspberry Pi

## Versão IIC

### Localização do Arquivo
`IIC_Voice/iic_voice.py`

### Instruções de Fiação

| Raspberry Pi | Módulo de Voz |
|--------------|--------------|
| GPIO2 (SDA) | SDA |
| GPIO3 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

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

### Habilitar a Porta Serial

Edite `/boot/firmware/config.txt` ou `/boot/config.txt`, garanta a seguinte configuração:

```
enable_uart=1
dtoverlay=disable-bt
```

Depois reinicie a Raspberry Pi.

```bash
sudo reboot
```

### Instruções de Fiação

#### Usando Conexão Direta Type-C

Ao usar conexão direta Type-C com a Raspberry Pi, descomente `SERIAL_PORT = '/dev/ttyUSB0'` e comente `SERIAL_PORT = '/dev/ttyAMA0'`

#### Usando os Pinos UART

| Raspberry Pi | Módulo de Voz |
|--------------|--------------|
| GPIO14 (TXD) | RX |
| GPIO15 (RXD) | TX |
| GND | GND |
| 5V | 5V |

Comente `SERIAL_PORT = '/dev/ttyUSB0'`

Descomente `SERIAL_PORT = '/dev/ttyAMA0'`

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
