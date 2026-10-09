[English](../../../en/06-multi-host/jetson/README.md) | [Deutsch](../../../de/06-multi-host/jetson/README.md) | [Español](../../../es/06-multi-host/jetson/README.md) | [Français](../../../fr/06-multi-host/jetson/README.md) | [Italiano](../../../it/06-multi-host/jetson/README.md) | [日本語](../../../ja/06-multi-host/jetson/README.md) | [한국어](../../../ko/06-multi-host/jetson/README.md) | [Português (BR)](../../../pt-br/06-multi-host/jetson/README.md) | Português (PT) | [简体中文](../../../zh-hans/06-multi-host/jetson/README.md) | [繁體中文](../../../zh-hant/06-multi-host/jetson/README.md)

# Guia do Utilizador do Módulo de Interação por Voz para Jetson

## Instalar Dependências

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## Verificar os Grupos de Utilizadores

```bash
sudo usermod -aG i2c $USER
sudo usermod -aG dialout $USER
```

Termine a sessão e inicie-a novamente para que as alterações tenham efeito.

## Versão IIC

### Localização dos Ficheiros
`IIC_Voice/iic_voice.py`

### Instruções de Cablagem

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

Deverá ver o endereço 0x2A

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

### Ligação através dos Pinos UART

Ao ligar o módulo ao Jetson através dos pinos UART, comente `SERIAL_PORT = '/dev/ttyUSB0'` e descomente `SERIAL_PORT = '/dev/ttyTHS1'`

#### Instruções de Cablagem

| Jetson | Módulo de Voz |
|--------|--------------|
| Pino 8 (UART1 TX) | RX |
| Pino 10 (UART1 RX) | TX |
| Pino 6 (GND) | GND |
| Pino 4 (5V) | 5V |

### Verificar a Porta Série

```bash
ls /dev/ttyTHS*
```

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

### Ligação através do Cabo Type-C

Ao ligar o módulo ao Jetson através de um cabo Type-C, descomente `SERIAL_PORT = '/dev/ttyUSB0'` e comente `SERIAL_PORT = '/dev/ttyTHS1'`

### Verificar a Porta Série

```bash
ls /dev/ttyUSB*
```

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

## FAQ

### Problema de Permissões do I2C

```bash
sudo chmod 666 /dev/i2c-1
```

### Porta Série Ocupada

Se a porta série não puder ser aberta, verifique se está ocupada por outros serviços:

```bash
sudo systemctl stop nvgetty
sudo systemctl disable nvgetty
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
