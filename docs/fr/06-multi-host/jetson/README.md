[English](../../../en/06-multi-host/jetson/README.md) | [Deutsch](../../../de/06-multi-host/jetson/README.md) | [Español](../../../es/06-multi-host/jetson/README.md) | Français | [Italiano](../../../it/06-multi-host/jetson/README.md) | [日本語](../../../ja/06-multi-host/jetson/README.md) | [한국어](../../../ko/06-multi-host/jetson/README.md) | [Português (BR)](../../../pt-br/06-multi-host/jetson/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/jetson/README.md) | [简体中文](../../../zh-hans/06-multi-host/jetson/README.md) | [繁體中文](../../../zh-hant/06-multi-host/jetson/README.md)

# Guide utilisateur du module d'interaction vocale Jetson

## Installer les dépendances

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## Vérifier les groupes d'utilisateurs

```bash
sudo usermod -aG i2c $USER
sudo usermod -aG dialout $USER
```

Déconnectez-vous puis reconnectez-vous pour que les modifications prennent effet.

## Version IIC

### Emplacement du fichier
`IIC_Voice/iic_voice.py`

### Instructions de câblage

| Jetson | Module vocal |
|--------|--------------|
| Pin 27 (I2C1 SDA) | SDA |
| Pin 28 (I2C1 SCL) | SCL |
| Pin 6 (GND) | GND |
| Pin 4 (5V) | 5V |

### Vérifier le périphérique I2C

```bash
sudo i2cdetect -y -r 1
```

Vous devriez voir l'adresse 0x2A

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

### Connexion via les broches UART

Lorsque vous connectez le module au Jetson via les broches UART, commentez `SERIAL_PORT = '/dev/ttyUSB0'` et décommentez `SERIAL_PORT = '/dev/ttyTHS1'`

#### Instructions de câblage

| Jetson | Module vocal |
|--------|--------------|
| Pin 8 (UART1 TX) | RX |
| Pin 10 (UART1 RX) | TX |
| Pin 6 (GND) | GND |
| Pin 4 (5V) | 5V |

### Vérifier le port série

```bash
ls /dev/ttyTHS*
```

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

### Connexion via un câble Type-C

Lorsque vous connectez le module au Jetson via un câble Type-C, décommentez `SERIAL_PORT = '/dev/ttyUSB0'` et commentez `SERIAL_PORT = '/dev/ttyTHS1'`

### Vérifier le port série

```bash
ls /dev/ttyUSB*
```

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

## FAQ

### Problème de permissions I2C

```bash
sudo chmod 666 /dev/i2c-1
```

### Port série occupé

Si le port série ne peut pas être ouvert, vérifiez s'il est occupé par d'autres services :

```bash
sudo systemctl stop nvgetty
sudo systemctl disable nvgetty
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
