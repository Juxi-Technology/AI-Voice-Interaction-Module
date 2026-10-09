[English](../../../en/06-multi-host/raspberry-pi/README.md) | [Deutsch](../../../de/06-multi-host/raspberry-pi/README.md) | [Español](../../../es/06-multi-host/raspberry-pi/README.md) | [Français](../../../fr/06-multi-host/raspberry-pi/README.md) | [Italiano](../../../it/06-multi-host/raspberry-pi/README.md) | [日本語](../../../ja/06-multi-host/raspberry-pi/README.md) | [한국어](../../../ko/06-multi-host/raspberry-pi/README.md) | [Português (BR)](../../../pt-br/06-multi-host/raspberry-pi/README.md) | Português (PT) | [简体中文](../../../zh-hans/06-multi-host/raspberry-pi/README.md) | [繁體中文](../../../zh-hant/06-multi-host/raspberry-pi/README.md)

# Guia do Utilizador do Módulo de Interação por Voz para Raspberry Pi

## Instalar Dependências

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## Ativar a Interface I2C

```bash
sudo raspi-config
```

Selecione `Interface Options` -> `I2C` -> `Yes`

Reinicie a Raspberry Pi

## Versão IIC

### Localização dos Ficheiros
`IIC_Voice/iic_voice.py`

### Instruções de Cablagem

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

### Formato da Saída

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## Versão UART

### Localização dos Ficheiros
`UART_Voice/uart_voice.py`

### Ativar a Porta Série

Edite `/boot/firmware/config.txt` ou `/boot/config.txt` e garanta a seguinte configuração:

```
enable_uart=1
dtoverlay=disable-bt
```

De seguida, reinicie a Raspberry Pi.

```bash
sudo reboot
```

### Instruções de Cablagem

#### Utilização da Ligação Direta por Type-C

Ao utilizar a ligação direta por Type-C à Raspberry Pi, descomente `SERIAL_PORT = '/dev/ttyUSB0'` e comente `SERIAL_PORT = '/dev/ttyAMA0'`

#### Utilização dos Pinos UART

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

### Formato da Saída

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
| 1 | 0xFE (Cabeçalho do Frame) |
| 2 | 0xEF (Cabeçalho do Frame) |
| 3 | ID da Palavra de Função |
| 4 | ID da Palavra de Comando |
| 5 | 0xEE (Fim do Frame) |

### Protocolo IIC

- Endereço do Dispositivo: 0x2A
- Registo de Leitura: 0xDA (Lê 1 byte)
  - 0x00: Não Reconhecido
  - Outro: ID da Palavra de Comando
