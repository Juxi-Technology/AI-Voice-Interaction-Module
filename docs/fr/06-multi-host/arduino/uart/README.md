[English](../../../../en/06-multi-host/arduino/uart/README.md) | [Deutsch](../../../../de/06-multi-host/arduino/uart/README.md) | [Español](../../../../es/06-multi-host/arduino/uart/README.md) | Français | [Italiano](../../../../it/06-multi-host/arduino/uart/README.md) | [日本語](../../../../ja/06-multi-host/arduino/uart/README.md) | [한국어](../../../../ko/06-multi-host/arduino/uart/README.md) | [Português (BR)](../../../../pt-br/06-multi-host/arduino/uart/README.md) | [Português (PT)](../../../../pt-pt/06-multi-host/arduino/uart/README.md) | [简体中文](../../../../zh-hans/06-multi-host/arduino/uart/README.md) | [繁體中文](../../../../zh-hant/06-multi-host/arduino/uart/README.md)

# Tutoriel de la version BSP du module vocal UART

## 📁 Structure des fichiers

```
uart/
├── uart.ino    # 主程序
├── bsp_uart.hpp         # 头文件（协议帧和函数声明）
├── bsp_uart.cpp         # 实现文件
└── README.md              # 本教程
```

---

## 🔌 Connexion matérielle

### Connexion au module vocal
| Arduino | Module vocal |
|---------|----------|
| D10 (RX) | TX |
| D11 (TX) | RX |
| GND | GND |
| 5V | 5V |

> 💡 **Remarque :** RX et TX doivent être croisés !

---

## 🔧 Compiler et téléverser

### Étape 1 : Ouvrir l'IDE Arduino
1. Ouvrez le fichier `UART_Voice.ino`
2. Sélectionnez le modèle de votre carte (par ex., Arduino Uno)
3. Sélectionnez le port série correspondant

### Étape 2 : Compiler et téléverser
1. Cliquez sur le bouton ✔️ pour compiler
2. Cliquez sur le bouton ➡️ pour téléverser sur la carte

---

## 📡 Test série

### Ouvrez le moniteur série dans l'IDE Arduino
- Débit en bauds : **115200**
- Fin de ligne : **None**

### Sortie attendue

Après la mise sous tension, vous devriez voir :
```
UART Voice Module Initialized
```

Prononcez le mot de réveil et le mot de commande vers le module, et il générera l'ID correspondant :
```
ID: 1
ID: 2
ID: 10
```

---

## 📚 Format de trame du protocole

| Octet | Contenu | Description |
|------|------|------|
| 1 | 0xFE | En-tête de trame 1 |
| 2 | 0xEF | En-tête de trame 2 |
| 3 | Code de fonction | 0xD1 = diffusion passive, 0xD2 = mot de fonction, 0xD3 = mot de commande |
| 4 | Données | ID de commande ou ID de diffusion |
| 5 | 0xEE | Fin de trame |

**Exemple :** lecture de l'ID de commande = 10
```
FE EF 00 0A EE
```

**Exemple :** envoyer une diffusion de mot de commande
```
FE EF D3 00 EE
```

---

## 📚 Référence de l'interface BSP

### 1. UART_Init()
```cpp
void UART_Init(void);
```
**Fonction** : initialise le port série (débit en bauds 115200)

**Exemple** :
```cpp
void setup() {
  UART_Init();
}
```

---

### 2. UART_ReadCommand()
```cpp
int UART_ReadCommand(void);
```
**Fonction** : lit l'ID de commande reconnu par le module vocal

**Valeur de retour** :
- `0` - aucune commande reconnue
- `1~254` - ID de commande
- `-1` - aucune nouvelle donnée

**Exemple** :
```cpp
int id = UART_ReadCommand();
if (id > 0) {
  Serial.print("识别到命令: ");
  Serial.println(id);
}
```

---

### 3. UART_SetPassiveVoice()
```cpp
void UART_SetPassiveVoice(uint8_t voiceID);
```
**Fonction** : définit la voix de diffusion passive

**Paramètre** :
- `0x00` - type de voix de diffusion passive

**Exemple** :
```cpp
UART_SetPassiveVoice(0x00);
delay(200);
```

---

### 4. UART_SetFunctionVoice()
```cpp
void UART_SetFunctionVoice(uint8_t voiceID);
```
**Fonction** : définit la voix de diffusion de mot de fonction

**Paramètre** :
- `0x00` - type de voix de diffusion de mot de fonction

**Exemple** :
```cpp
UART_SetFunctionVoice(0x00);
delay(200);
```

---

### 5. UART_SetCommandVoice()
```cpp
void UART_SetCommandVoice(uint8_t voiceID);
```
**Fonction** : définit la voix de diffusion de mot de commande

**Paramètre** :
- `0x00` - type de voix de diffusion de mot de commande

**Exemple** :
```cpp
UART_SetCommandVoice(0x00);
delay(200);
```

---

## 🎯 Logique du programme principal

```cpp
void setup() {
  Serial.begin(115200);
  UART_Init();
  
  Serial.println("UART Voice Module Initialized");
  
  UART_SetCommandVoice(0x00);  // 上电播报命令词语音
  delay(200);
}

void loop() {
  int commandId = UART_ReadCommand();
  
  if (commandId >= 0) {
    // 过滤无效值，防止重复输出
    if (commandId != 0 && commandId != 255 && commandId != lastCommandId) {
      Serial.print("ID: ");
      Serial.println(commandId);
      lastCommandId = commandId;
      
      // 示例：根据识别到的命令控制播报
      if (commandId == 1) {
        UART_SetCommandVoice(0x00);  // 识别到命令1，播报命令词语音
      } else if (commandId == 2) {
        UART_SetCommandVoice(0x00);  // 识别到命令2，播报命令词语音
      }
    } else if (commandId == 0 || commandId == 255) {
      if (lastCommandId != 0) {
        lastCommandId = 0;  // 重置状态
      }
    }
  }
  
  delay(50);
}
```

---

## 🔍 FAQ

### Q1 : Aucune sortie du tout

**Causes possibles :**
1. RX/TX sont inversés
2. GND n'est pas une masse commune
3. Module non alimenté
4. Débit en bauds incorrect

**Solutions :**
- Confirmez que D10 se connecte au TX du module et D11 au RX du module (connexion croisée)
- Confirmez la connexion GND
- Confirmez que l'alimentation 5V est normale
- Confirmez que le débit en bauds série est 115200

---

### Q2 : Le moniteur série n'affiche que du texte illisible

**Causes possibles :**
1. Incompatibilité de débit en bauds
2. Démarrage anormal du module

**Solutions :**
- Confirmez que le débit en bauds du moniteur série est 115200
- Appuyez une fois sur le bouton de réinitialisation du module

---

### Q3 : La sortie affiche « ID: 255 » ou « ID: 0 »

**Explication :** c'est normal
- `0` = aucune commande reconnue
- `255` = aucune nouvelle donnée

Ces valeurs sont déjà filtrées dans le code, elles ne sont donc normalement pas affichées. Si vous les voyez réellement, c'est que le code ne prend pas effet.

---

## 💡 Avantages de l'architecture BSP

### 1. Une organisation claire du code
- **bsp_uart.hpp** - déclaration uniquement, aucune implémentation
- **bsp_uart.cpp** - détails concrets de l'implémentation
- **UART_Voice.ino** - ne s'occupe que de la logique métier

### 2. Portage facile
Si vous passez à une autre plateforme (par ex., STM32, ESP32), vous devez uniquement modifier l'implémentation dans `bsp_uart.cpp` ; le programme principal n'a pas besoin de changer.

### 3. Maintenance facile
Les modifications du code lié à UART sont confinées à `bsp_uart.cpp` — corrigez une fois, efficace partout.

---

## 🚀 Exemples de fonctions étendues

### Exemple 1 : Déclencher différentes diffusions selon différentes commandes
```cpp
if (commandId == 1) {
  UART_SetCommandVoice(0x00);      // 播报命令词
} else if (commandId == 2) {
  UART_SetFunctionVoice(0x00);     // 播报功能词
} else if (commandId == 3) {
  UART_SetPassiveVoice(0x00);      // 播报被动语
}
```

### Exemple 2 : Contrôler une LED
```cpp
if (commandId == 10) {
  digitalWrite(LED_PIN, LOW);    // 关灯
  UART_SetCommandVoice(0x00);     // 播报确认
}
```

### Exemple 3 : Contrôler un moteur
```cpp
if (commandId == 11) {
  motor_stop();
  UART_SetCommandVoice(0x00);     // 播报确认
}
```
