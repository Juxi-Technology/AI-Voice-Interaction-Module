[English](../../../en/06-multi-host/arduino/README.md) | [Deutsch](../../../de/06-multi-host/arduino/README.md) | [Español](../../../es/06-multi-host/arduino/README.md) | Français | [Italiano](../../../it/06-multi-host/arduino/README.md) | [日本語](../../../ja/06-multi-host/arduino/README.md) | [한국어](../../../ko/06-multi-host/arduino/README.md) | [Português (BR)](../../../pt-br/06-multi-host/arduino/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/arduino/README.md) | [简体中文](../../../zh-hans/06-multi-host/arduino/README.md) | [繁體中文](../../../zh-hant/06-multi-host/arduino/README.md)

# Module d'interaction vocale IA - Guide utilisateur Arduino

## Table des matières

1. [Introduction](#introduction)
2. [Connexion matérielle](#connexion-matérielle)
3. [Configuration de l'environnement de développement](#configuration-de-lenvironnement-de-développement)
4. [Utilisation de la version IIC](#utilisation-de-la-version-iic)
5. [Utilisation de la version UART](#utilisation-de-la-version-uart)
6. [FAQ](#faq)

---

## Introduction

Ce dépôt fournit un exemple de code pour la plateforme Arduino permettant de communiquer avec le module d'interaction vocale IA, prenant en charge les méthodes de communication I2C et UART.

- **Module de reconnaissance vocale** : prend en charge la reconnaissance vocale hors ligne, génère l'ID de commande après reconnaissance
- **Fonction de diffusion** : prend en charge la diffusion passive, la diffusion de mots de fonction, la diffusion de mots de commande
- **Protocole de communication** : adresse I2C 0x2A, débit en bauds UART 115200

---

## Connexion matérielle

### Connexion générale

| Broche Arduino | Module vocal | Description |
|-------------|-------------|-------------|
| 5V | 5V | Alimentation positive |
| GND | GND | Masse d'alimentation |

---

### Connexion version I2C

| Broche Arduino | Module vocal | Description |
|-------------|-------------|-------------|
| A4 (SDA) | SDA | Ligne de données I2C |
| A5 (SCL) | SCL | Ligne d'horloge I2C |

---

### Connexion version UART

| Broche Arduino | Module vocal | Description |
|-------------|-------------|-------------|
| D10 (RX) | TX | Réception série (Software Serial) |
| D11 (TX) | RX | Émission série (Software Serial) |

---

### Connexion de débogage série

| Broche Arduino | USB-TTL | Description |
|-------------|---------|-------------|
| TX (D1) | RX | Sortie de débogage |
| RX (D0) | TX | Entrée de débogage (facultatif) |
| GND | GND | Masse commune |

---

## Configuration de l'environnement de développement

### 1. Installer l'IDE Arduino

- Téléchargement : https://www.arduino.cc/en/software
- Installez la dernière version

### 2. Installer le package de prise en charge de la carte

- Ouvrez l'IDE Arduino
- Outils → Type de carte → Gestionnaire de cartes
- Recherchez et installez le package de prise en charge de votre carte Arduino
- Recommandé : Arduino Uno / Nano

---

## Utilisation de la version IIC

### 1. Ouvrir le projet

- Ouvrez `IIC_Voice/IIC_Voice.ino` dans l'IDE Arduino

### 2. Téléverser le code

- Sélectionnez le modèle de carte correct (Outils → Type de carte)
- Sélectionnez le port correct (Outils → Port)
- Cliquez sur le bouton de téléversement (→)
- Attendez la fin du téléversement

### 3. Exécuter le test

1. Ouvrez le moniteur série (Outils → Moniteur série)
2. Réglez le débit en bauds sur **115200**
3. Après un démarrage normal, il affichera :

```
IIC Voice Module Initialized
```

4. Prononcez des mots de commande vers le module vocal, et les ID correspondants s'afficheront :

```
IIC Voice Module Initialized
ID: 1
ID: 4
ID: 10
```

### 4. Explication du code

```cpp
// Initialize I2C
IIC_Init();

// Read command ID
int commandId = IIC_ReadCommand();

// Set broadcast
IIC_SetCommandVoice(0x00);  // Command word broadcast
```

---

## Utilisation de la version UART

### 1. Ouvrir le projet

- Ouvrez `UART_Voice/UART_Voice.ino` dans l'IDE Arduino

### 2. Téléverser le code

- Sélectionnez le modèle de carte correct
- Sélectionnez le port correct
- Cliquez sur le bouton de téléversement
- Attendez la fin du téléversement

### 3. Exécuter le test

1. Ouvrez le moniteur série
2. Réglez le débit en bauds sur **115200**
3. Après un démarrage normal, il affichera :

```
UART Voice Module Initialized
```

4. Prononcez des mots de commande vers le module vocal, et les ID correspondants s'afficheront :

```
UART Voice Module Initialized
ID: 1
ID: 4
ID: 10
```

### 4. Explication du code

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

### Q1 : Aucune sortie dans le moniteur série

**R : Vérifiez les points suivants :**
- Vérifiez que le débit en bauds série est 115200
- Vérifiez que le port correct est sélectionné
- Vérifiez que TX/RX ne sont pas inversés
- Vérifiez que GND est connecté

---

### Q2 : La version I2C affiche « IIC Read Error »

**R : Vérifiez la connexion I2C :**
- Vérifiez que SDA/SCL ne sont pas inversés
- Vérifiez que l'adresse de l'appareil est correcte (0x2A)
- Vérifiez que GND est connecté

---

### Q3 : L'ID de commande n'affiche que 0 ou 255

**R : Comportement normal :**
- 0 = aucune commande valide reconnue
- 255 = aucune nouvelle donnée
- Les ID valides ne sont émis qu'après une reconnaissance normale

---

### Q4 : La précision de reconnaissance n'est pas élevée

**R : Suggestions d'optimisation :**
- Assurez un environnement calme, sans trop de bruit de fond
- Gardez une distance adéquate par rapport au microphone (10-50cm)
- Parlez à une vitesse modérée avec une prononciation claire

---

### Q5 : La version UART ne reçoit aucune donnée

**R : Vérifiez :**
- Confirmez que le TX du module vocal est connecté au D10 (RX) de l'Arduino
- Confirmez que le RX du module vocal est connecté au D11 (TX) de l'Arduino
- Vérifiez que le débit en bauds est 115200

---

## Support technique

Si vous rencontrez des problèmes, veuillez vérifier :
1. La connexion matérielle est correcte
2. Le débit en bauds série correspond
3. L'adresse I2C est correcte
4. GND est connecté (très important !)
