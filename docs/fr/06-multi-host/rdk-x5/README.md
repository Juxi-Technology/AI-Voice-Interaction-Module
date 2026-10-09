[English](../../../en/06-multi-host/rdk-x5/README.md) | [Deutsch](../../../de/06-multi-host/rdk-x5/README.md) | [Español](../../../es/06-multi-host/rdk-x5/README.md) | Français | [Italiano](../../../it/06-multi-host/rdk-x5/README.md) | [日本語](../../../ja/06-multi-host/rdk-x5/README.md) | [한국어](../../../ko/06-multi-host/rdk-x5/README.md) | [Português (BR)](../../../pt-br/06-multi-host/rdk-x5/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/rdk-x5/README.md) | [简体中文](../../../zh-hans/06-multi-host/rdk-x5/README.md) | [繁體中文](../../../zh-hant/06-multi-host/rdk-x5/README.md)

# Module d'interaction vocale IA - Guide utilisateur RDK X5 (Python)

## Table des matières

1. [Introduction](#introduction)
2. [Connexion matérielle](#connexion-matérielle)
3. [Configuration de l'environnement](#configuration-de-lenvironnement)
4. [Utilisation de la version IIC](#utilisation-de-la-version-iic)
5. [Utilisation de la version UART](#utilisation-de-la-version-uart)
6. [FAQ](#faq)

---

## Introduction

Ce dépôt fournit un exemple de code Python pour la plateforme RDK X5 (Raspberry Pi) permettant de communiquer avec le module d'interaction vocale IA, prenant en charge les méthodes de communication I2C et UART.

- **Module de reconnaissance vocale** : prend en charge la reconnaissance vocale hors ligne, génère l'ID de commande après reconnaissance
- **Fonction de diffusion** : prend en charge la diffusion passive, la diffusion de mots de fonction, la diffusion de mots de commande
- **Protocole de communication** : adresse I2C 0x2A, débit en bauds UART 115200
- **Langage de programmation** : Python 3

---

## Connexion matérielle

### Connexion générale

| Broche RDK X5 | Module vocal | Description |
|------------|-------------|-------------|
| 5V (Pin 2/4) | 5V | Alimentation positive |
| GND (Pin 6/9) | GND | Masse d'alimentation |

> **Important** : assurez-vous que tous les appareils partagent une masse commune !

---

### Connexion version I2C

| Broche RDK X5 | Module vocal | Description |
|------------|-------------|-------------|
| SDA (GPIO3, Pin 3) | SDA | Ligne de données I2C |
| SCL (GPIO5, Pin 5) | SCL | Ligne d'horloge I2C |

**Remarque** : utilise par défaut le bus I2C 5 (numérotation BCM)

---

### Connexion version UART

| Broche RDK X5 | Module vocal | Description |
|------------|-------------|-------------|
| GPIO14 (TXD, Pin 8) | RX | Émission série |
| GPIO15 (RXD, Pin 10) | TX | Réception série |

**Remarque** : utilise par défaut le périphérique série `/dev/ttyAMA0`

---

### Connexion par câble Type-C (alternative à l'UART)

Si vous utilisez un module adaptateur USB-TTL :

| RDK X5 | Module USB-TTL | Module vocal |
|--------|---------------|-------------|
| Port USB | USB | - |
| - | RX | TX |
| - | TX | RX |
| GND | GND | GND |

**Remarque** : le périphérique série est généralement `/dev/ttyUSB0` dans ce cas

---

## Configuration de l'environnement

### 1. Configuration système requise

- RDK X5 (ou Raspberry Pi 3/4/5)
- Système Ubuntu / Debian
- Python 3.7+

### 2. Installer les dépendances

```bash
# Update packages
sudo apt update
sudo apt upgrade -y

# Install Python libraries
sudo apt install -y python3-pip python3-smbus i2c-tools

# Install pyserial
pip3 install pyserial
```

### 3. Activer l'interface I2C

```bash
# Open configuration tool
sudo raspi-config

# Select Interface Options → I2C → Enable
# Reboot to take effect
sudo reboot
```

### 4. Activer l'interface série

```bash
# Open configuration tool
sudo raspi-config

# Select Interface Options → Serial
# Select: No (shell) → Yes (hardware serial port)
# Reboot to take effect
sudo reboot
```

### 5. Tester les interfaces matérielles

```bash
# Test I2C device
sudo i2cdetect -y 5

# Test serial port
ls /dev/ttyAMA0
ls /dev/ttyUSB0  # If using USB-TTL
```

---

## Utilisation de la version IIC

### 1. Vérifier les fichiers de code

```bash
cd IIC_Voice
ls -la
# Should see iic_voice.py
```

### 2. Configurer le bus I2C

Modifiez le fichier `iic_voice.py`, ajustez les paramètres au besoin :

```python
# I2C device address
DEVICE_ADDRESS = 0x2A

# Register address
REG_RESULT = 0xDA

# I2C bus number (modify according to actual connection)
bus = smbus.SMBus(5)  # I2C bus 5
```

### 3. Exécuter le programme

```bash
# Make executable
chmod +x iic_voice.py

# Run (sudo required for I2C access)
sudo python3 iic_voice.py
```

### 4. Exécuter le test

Après un démarrage normal, il affichera :

```
Speech Serial Opened! Baudrate=115200
```

Prononcez des mots de commande vers le module vocal, les ID correspondants s'afficheront :

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. Arrêter le programme

Appuyez sur `Ctrl + C` pour arrêter le programme :

```
Program terminated
```

---

## Utilisation de la version UART

### 1. Vérifier les fichiers de code

```bash
cd UART_Voice
ls -la
# Should see uart_voice.py
```

### 2. Configurer le port série

Modifiez le fichier `uart_voice.py`, ajustez le périphérique série :

```python
# UART direct connection (default)
SERIAL_PORT = '/dev/ttyAMA0'

# Or use USB-TTL
# SERIAL_PORT = '/dev/ttyUSB0'

# Baud rate
BAUD_RATE = 115200
```

### 3. Exécuter le programme

```bash
# Make executable
chmod +x uart_voice.py

# Run (sudo required for serial port access)
sudo python3 uart_voice.py
```

### 4. Exécuter le test

Après un démarrage normal, il affichera :

```
Speech Serial Opened! Baudrate=115200
```

Prononcez des mots de commande vers le module vocal, les ID correspondants s'afficheront :

```
Speech Serial Opened! Baudrate=115200
ID:1
ID:4
ID:10
```

### 5. Arrêter le programme

Appuyez sur `Ctrl + C` pour arrêter le programme

---

## FAQ

### Q1 : Permissions insuffisantes pour l'opération I2C

**R : Ajoutez l'utilisateur au groupe d'utilisateurs I2C :**
```bash
sudo usermod -aG i2c $USER
# Re-login to take effect
```
Ou exécutez avec `sudo`

---

### Q2 : Périphérique série introuvable

**R : Vérifiez :**
1. Vérifiez si le port série est activé (raspi-config)
2. Vérifiez si le nom du périphérique est correct
   - UART direct : `/dev/ttyAMA0`
   - USB-TTL : `/dev/ttyUSB0` ou `/dev/ttyUSB1`
3. Vérifiez si la connexion matérielle est correcte
4. Vérifiez si le port série est occupé par d'autres programmes

```bash
# List available serial ports
ls /dev/tty* | grep tty
```

---

### Q3 : Périphérique I2C non détecté lors du scan

**R : Vérifiez :**
1. Confirmez que I2C est activé (raspi-config)
2. Vérifiez si SDA/SCL sont inversés
3. Vérifiez si la masse commune est connectée
4. Vérifiez si l'appareil est sous tension

```bash
# Scan I2C devices
sudo i2cdetect -y 5
```

Si vous voyez 0x2A, la connexion de l'appareil est normale

---

### Q4 : L'ID de commande n'affiche que 0 ou rien

**R : Comportement normal :**
- 0 = aucune commande valide reconnue
- Les ID ne sont émis que lorsque des mots de commande valides sont prononcés
- Réveillez d'abord le module, puis prononcez la commande

---

### Q5 : Précision de reconnaissance peu élevée

**R : Suggestions d'optimisation :**
- Assurez un environnement calme, sans trop de bruit de fond
- Gardez une distance adéquate par rapport au microphone (10-50cm)
- Parlez à une vitesse modérée avec une prononciation claire

---

### Q6 : Communication série anormale

**R : Vérifiez :**
1. Les TX/RX sont-ils correctement croisés ? (TX du module → RX du RPi)
2. Le débit en bauds est-il 115200
3. La masse commune est-elle connectée
4. Le port série est-il occupé par d'autres processus

```bash
# Check serial port occupancy
sudo lsof /dev/ttyAMA0
```

---

## Support technique

Si vous rencontrez des problèmes, veuillez vérifier :
1. La connexion matérielle est correcte (la masse commune est très importante !)
2. Le débit en bauds série est 115200
3. L'adresse I2C est correcte (0x2A)
4. Vous disposez de permissions suffisantes pour accéder aux interfaces matérielles

```bash
# Useful debugging commands
ls -l /dev/i2c*      # List I2C devices
ls -l /dev/ttyAMA0   # List serial device
groups                # List user group permissions
```
