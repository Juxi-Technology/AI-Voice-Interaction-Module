[English](../../../../en/06-multi-host/arduino/iic/README.md) | [Deutsch](../../../../de/06-multi-host/arduino/iic/README.md) | [Español](../../../../es/06-multi-host/arduino/iic/README.md) | Français | [Italiano](../../../../it/06-multi-host/arduino/iic/README.md) | [日本語](../../../../ja/06-multi-host/arduino/iic/README.md) | [한국어](../../../../ko/06-multi-host/arduino/iic/README.md) | [Português (BR)](../../../../pt-br/06-multi-host/arduino/iic/README.md) | [Português (PT)](../../../../pt-pt/06-multi-host/arduino/iic/README.md) | [简体中文](../../../../zh-hans/06-multi-host/arduino/iic/README.md) | [繁體中文](../../../../zh-hant/06-multi-host/arduino/iic/README.md)

# Tutoriel de la version BSP du module vocal IIC

## 📁 Structure des fichiers

```
iic/
├── iic.ino    # 主程序
├── bsp_iic.hpp         # 头文件（地址和函数声明）
├── bsp_iic.cpp         # 实现文件
└── README.md            # 本教程
```

---

## 🔌 Connexion matérielle

| Arduino | Module vocal |
|---------|----------|
| A4 (SDA) | SDA |
| A5 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

---

## 🔧 Compiler et téléverser

### Étape 1 : Ouvrir l'IDE Arduino
1. Ouvrez le fichier `IIC_Voice.ino`
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
IIC Voice Module Initialized
```

Prononcez le mot de réveil et le mot de commande vers le module, et il générera l'ID correspondant :
```
ID: 1
ID: 2
ID: 10
```

---

## 📚 Carte des registres

| Registre | Adresse | Fonction | Description |
|--------|------|------|------|
| REG_RESULT | 0xDA | Lire l'ID de commande | Lecture de 1 octet, 0 = non reconnu |
| REG_PASSIVE | 0xD1 | Écrire la diffusion passive | Écriture de 1 octet, 0x00 = voix de diffusion passive |
| REG_FUNCTION | 0xD2 | Écrire la diffusion de mot de fonction | Écriture de 1 octet, 0x00 = voix de diffusion de mot de fonction |
| REG_COMMAND | 0xD3 | Écrire la diffusion de mot de commande | Écriture de 1 octet, 0x00 = voix de diffusion de mot de commande |

---

## 📚 Référence de l'interface BSP

### 1. IIC_Init()
```cpp
void IIC_Init(void);
```
**Fonction** : initialise le bus I2C

**Exemple** :
```cpp
void setup() {
  IIC_Init();
}
```

---

### 2. IIC_ReadCommand()
```cpp
int IIC_ReadCommand(void);
```
**Fonction** : lit l'ID de commande reconnu par le module vocal

**Valeur de retour** :
- `0` - aucune commande reconnue
- `1~254` - ID de commande
- `-1` - erreur de communication

**Exemple** :
```cpp
int id = IIC_ReadCommand();
if (id > 0) {
  Serial.print("识别到命令: ");
  Serial.println(id);
}
```

---

### 3. IIC_SetPassiveVoice()
```cpp
void IIC_SetPassiveVoice(uint8_t voiceID);
```
**Fonction** : définit la voix de diffusion passive

**Paramètre** :
- `0x00` - type de voix de diffusion passive

**Exemple** :
```cpp
IIC_SetPassiveVoice(0x00);
delay(200);
```

---

### 4. IIC_SetFunctionVoice()
```cpp
void IIC_SetFunctionVoice(uint8_t voiceID);
```
**Fonction** : définit la voix de diffusion de mot de fonction

**Paramètre** :
- `0x00` - type de voix de diffusion de mot de fonction

**Exemple** :
```cpp
IIC_SetFunctionVoice(0x00);
delay(200);
```

---

### 5. IIC_SetCommandVoice()
```cpp
void IIC_SetCommandVoice(uint8_t voiceID);
```
**Fonction** : définit la voix de diffusion de mot de commande

**Paramètre** :
- `0x00` - type de voix de diffusion de mot de commande

**Exemple** :
```cpp
IIC_SetCommandVoice(0x00);
delay(200);
```

---

## 🎯 Logique du programme principal

```cpp
void setup() {
  Serial.begin(115200);
  IIC_Init();
  
  Serial.println("IIC Voice Module Initialized");
  
  IIC_SetCommandVoice(0x00);  // 上电播报命令词语音
  delay(200);
}

void loop() {
  int commandId = IIC_ReadCommand();
  
  if (commandId >= 0) {
    // 过滤无效值，防止重复输出
    if (commandId != 0 && commandId != 255 && commandId != lastCommandId) {
      Serial.print("ID: ");
      Serial.println(commandId);
      lastCommandId = commandId;
      
      // 示例：根据识别到的命令控制播报
      if (commandId == 1) {
        IIC_SetCommandVoice(0x00);  // 识别到命令1，播报命令词语音
      } else if (commandId == 2) {
        IIC_SetCommandVoice(0x00);  // 识别到命令2，播报命令词语音
      }
    } else if (commandId == 0 || commandId == 255) {
      if (lastCommandId != 0) {
        lastCommandId = 0;  // 重置状态
      }
    }
  } else {
    Serial.println("IIC Read Error");
    delay(1000);
  }
  
  delay(50);
}
```

---

## 🔍 FAQ

### Q1 : Le moniteur série n'affiche que « IIC Read Error »

**Causes possibles :**
1. Câblage incorrect, ou non connecté
2. Module non alimenté
3. Adresse I2C incorrecte

**Solutions :**
- Vérifiez si SDA/SCL sont inversés
- Vérifiez si GND est une masse commune
- Vérifiez si l'alimentation 5V est normale
- Utilisez un programme de scan I2C pour confirmer l'adresse de l'appareil

---

### Q2 : Aucune sortie du tout

**Causes possibles :**
1. Débit en bauds série incorrect
2. Module non réveillé

**Solutions :**
- Confirmez que le débit en bauds série est 115200
- Prononcez d'abord le mot de réveil, puis le mot de commande

---

### Q3 : La sortie affiche « ID: 255 » ou « ID: 0 »

**Explication :** c'est normal

- `0` = aucune commande reconnue
- `255` = aucune nouvelle donnée

Ces valeurs sont déjà filtrées dans le code, elles ne sont donc normalement pas affichées. Si vous les voyez réellement, c'est que le code ne prend pas effet.

---

## 💡 Avantages de l'architecture BSP

### 1. Une organisation claire du code
- **bsp_iic.hpp** - déclaration uniquement, aucune implémentation
- **bsp_iic.cpp** - détails concrets de l'implémentation
- **IIC_Voice.ino** - ne s'occupe que de la logique métier

### 2. Portage facile
Si vous passez à une autre plateforme (par ex., STM32, ESP32), vous devez uniquement modifier l'implémentation dans `bsp_iic.cpp` ; le programme principal n'a pas besoin de changer.

### 3. Maintenance facile
Les modifications du code lié à I2C sont confinées à `bsp_iic.cpp` — corrigez une fois, efficace partout.

---

## 🚀 Exemples de fonctions étendues

### Exemple 1 : Déclencher différentes diffusions selon différentes commandes
```cpp
if (commandId == 1) {
  IIC_SetCommandVoice(0x00);      // 播报命令词
} else if (commandId == 2) {
  IIC_SetFunctionVoice(0x00);     // 播报功能词
} else if (commandId == 3) {
  IIC_SetPassiveVoice(0x00);      // 播报被动语
}
```

### Exemple 2 : Contrôler une LED
```cpp
if (commandId == 10) {
  digitalWrite(LED_PIN, LOW);    // 关灯
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```

### Exemple 3 : Contrôler un moteur
```cpp
if (commandId == 11) {
  motor_stop();
  IIC_SetCommandVoice(0x00);     // 播报确认
}
```
