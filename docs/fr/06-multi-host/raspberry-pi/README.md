[English](../../../en/06-multi-host/raspberry-pi/README.md) | [Deutsch](../../../de/06-multi-host/raspberry-pi/README.md) | [Español](../../../es/06-multi-host/raspberry-pi/README.md) | Français | [Italiano](../../../it/06-multi-host/raspberry-pi/README.md) | [日本語](../../../ja/06-multi-host/raspberry-pi/README.md) | [한국어](../../../ko/06-multi-host/raspberry-pi/README.md) | [Português (BR)](../../../pt-br/06-multi-host/raspberry-pi/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/raspberry-pi/README.md) | [简体中文](../../../zh-hans/06-multi-host/raspberry-pi/README.md) | [繁體中文](../../../zh-hant/06-multi-host/raspberry-pi/README.md)

# Guide utilisateur du module d'interaction vocale Raspberry Pi

## Installer les dépendances

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## Activer l'interface I2C

```bash
sudo raspi-config
```

Sélectionnez `Interface Options` -> `I2C` -> `Yes`

Redémarrez le Raspberry Pi

## Version IIC

### Emplacement du fichier
`IIC_Voice/iic_voice.py`

### Instructions de câblage

| Raspberry Pi | Module vocal |
|--------------|--------------|
| GPIO2 (SDA) | SDA |
| GPIO3 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

### Exécution

```bash
cd IIC_Voice
python3 iic_voice.py
```

### Format de sortie

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## Version UART

### Emplacement du fichier
`UART_Voice/uart_voice.py`

### Activer le port série

Modifiez `/boot/firmware/config.txt` ou `/boot/config.txt`, assurez-vous de la configuration suivante :

```
enable_uart=1
dtoverlay=disable-bt
```

Redémarrez ensuite le Raspberry Pi.

```bash
sudo reboot
```

### Instructions de câblage

#### Utilisation de la connexion directe Type-C

Lorsque vous utilisez la connexion directe Type-C au Raspberry Pi, décommentez `SERIAL_PORT = '/dev/ttyUSB0'` et commentez `SERIAL_PORT = '/dev/ttyAMA0'`

#### Utilisation des broches UART

| Raspberry Pi | Module vocal |
|--------------|--------------|
| GPIO14 (TXD) | RX |
| GPIO15 (RXD) | TX |
| GND | GND |
| 5V | 5V |

Commentez `SERIAL_PORT = '/dev/ttyUSB0'`

Décommentez `SERIAL_PORT = '/dev/ttyAMA0'`

### Exécution

```bash
cd UART_Voice
python3 uart_voice.py
```

### Format de sortie

```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## Description du protocole

### Protocole UART

| Octet | Contenu |
|------|---------|
| 1 | 0xFE (En-tête de trame) |
| 2 | 0xEF (En-tête de trame) |
| 3 | ID de mot de fonction |
| 4 | ID de mot de commande |
| 5 | 0xEE (Fin de trame) |

### Protocole IIC

- Adresse de l'appareil : 0x2A
- Registre de lecture : 0xDA (lecture de 1 octet)
  - 0x00 : non reconnu
  - Autre : ID de mot de commande
