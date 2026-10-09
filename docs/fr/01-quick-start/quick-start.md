[English](../../en/01-quick-start/quick-start.md) | [Deutsch](../../de/01-quick-start/quick-start.md) | [Español](../../es/01-quick-start/quick-start.md) | Français | [Italiano](../../it/01-quick-start/quick-start.md) | [日本語](../../ja/01-quick-start/quick-start.md) | [한국어](../../ko/01-quick-start/quick-start.md) | [Português (BR)](../../pt-br/01-quick-start/quick-start.md) | [Português (PT)](../../pt-pt/01-quick-start/quick-start.md) | [简体中文](../../zh-hans/01-quick-start/quick-start.md) | [繁體中文](../../zh-hant/01-quick-start/quick-start.md)

# Démarrage rapide

Le firmware d'usine intègre déjà la fonction de reconnaissance vocale, ce qui permet aux utilisateurs de l'essayer rapidement sans avoir à le flasher. Si vous devez ajouter des entrées de reconnaissance supplémentaires, flasher un autre firmware ou personnaliser des entrées, consultez le tutoriel « 3. Création d'entrées de protocole personnalisées » pour savoir comment personnaliser des entrées.

# 1. Préparation

1. Un câble de données Type-C
2. Module d'interaction vocale

# 2. Connexion de l'appareil

![1](../../en/01-quick-start/images/1.png)

# 3. Reconnaissance vocale et lecture

Après avoir alimenté le module d'interaction vocale via Type-C, réveillez le module en prononçant « 你好，小犀 » (Bonjour, Xiao Xi). Une fois le réveil réussi, le module répond « 我在 » (Je suis là), ce qui indique qu'il se trouve actuellement en état de reconnaissance vocale. Si aucune entrée de commande n'est reconnue dans les 15 secondes, le module passe en mode veille et annonce « 我去休息了 » (Je vais me reposer). Pour réveiller à nouveau le module, prononcez simplement le mot de réveil.

Le firmware d'usine contient des mots de commande et des mots de lecture intégrés. Vous pouvez consulter la liste des protocoles dans les pièces jointes de la documentation fournie. Le tableau ci-dessous présente un extrait partiel de la liste des protocoles de mots de commande et de mots de lecture. Vous pouvez vérifier le type de fonction pour voir ce que représente chaque mot de commande. Les mots de lecture marqués « passive » doivent être déclenchés en envoyant la commande correspondante au module d'interaction vocale via un port série de PC, un microcontrôleur ou un autre appareil hôte. Voir les détails ci-dessous.

Mots de fonction :

| Étiquette sémantique | Mot de commande | Type de fonction | Phrase de lecture | Mode de lecture | Protocole d'envoi   | Protocole de réception |
| -------------- | ------------ | ------------- | --------------- | ------------- | --------------- | ---------------- |
| 1              | 欢迎语       | Accueil       | 欢迎使用小犀    | Passive       | FE EF 01 00 EE  | FE EF 01 00 EE   |
| 2              | 休息语       | Veille        | 我去休息啦      | Active        | FE EF 02 00 EE  | FE EF 02 00 EE   |
| 3              | 你好小犀     | Mot de réveil | 我在            | Active        | FE EF 03 00 EE  | FE EF 03 00 EE   |
| 4              | 增大音量     | Volume +      | 增大音量        | Active        | FE EF 04 00 EE  | FE EF 04 00 EE   |
| 5              | 减小音量     | Volume -      | 减小音量        | Active        | FE EF 05 00 EE  | FE EF 05 00 EE   |
| 6              | 最大音量     | Volume maximal | 最大音量        | Active        | FE EF 06 00 EE  | FE EF 06 00 EE   |
| 7              | 中等音量     | Volume moyen  | 中等音量        | Active        | FE EF 07 00 EE  | FE EF 07 00 EE   |
| 8              | 最小音量     | Volume minimal | 最小音量        | Active        | FE EF 08 00 EE  | FE EF 08 00 EE   |
| 9              | 开启播报     | Activer la lecture | 开启播报        | Active        | FE EF 09 00 EE  | FE EF 09 00 EE   |
| 10             | 关闭播报     | Désactiver la lecture | 关闭播报        | Active        | FE EF 0A 00 EE  | FE EF 0A 00 EE   |

Mots de commande :

| 11   | 小车停止     | Commande | 好的,已停止           | Active | FE EF 00 01 EE | FE EF 00 01 EE |
| ---- | ------------ | ------- | --------------------- | ------ | -------------- | -------------- |
| 12   | 停车         | Commande | 好的,已停止           | Active | FE EF 00 02 EE | FE EF 00 02 EE |
| 13   | 小车休眠     | Commande | 好的,已休眠           | Active | FE EF 00 03 EE | FE EF 00 03 EE |
| 14   | 小车前进     | Commande | 好的,正在前进         | Active | FE EF 00 04 EE | FE EF 00 04 EE |
| 15   | 小车后退     | Commande | 好的,正在后退         | Active | FE EF 00 05 EE | FE EF 00 05 EE |
| 16   | 小车左转     | Commande | 好的,正在向左转       | Active | FE EF 00 06 EE | FE EF 00 06 EE |
| 17   | 小车右转     | Commande | 好的,正在向右转       | Active | FE EF 00 07 EE | FE EF 00 07 EE |
| 18   | 小车左旋     | Commande | 好的,正在向左旋转     | Active | FE EF 00 08 EE | FE EF 00 08 EE |
| 19   | 小车右旋     | Commande | 好的,正在向右旋转     | Active | FE EF 00 09 EE | FE EF 00 09 EE |
| 20   | 关灯         | Commande | 好的,已关灯           | Active | FE EF 00 0A EE | FE EF 00 0A EE |
| 21   | 亮红灯       | Commande | 好的,已亮红灯         | Active | FE EF 00 0B EE | FE EF 00 0B EE |
| 22   | 亮绿灯       | Commande | 好的,已亮绿灯         | Active | FE EF 00 0C EE | FE EF 00 0C EE |
| 23   | 亮蓝灯       | Commande | 好的,已亮蓝灯         | Active | FE EF 00 0D EE | FE EF 00 0D EE |
| 24   | 亮黄灯       | Commande | 好的,已亮黄灯         | Active | FE EF 00 0E EE | FE EF 00 0E EE |
| 25   | 打开流水灯   | Commande | 好的,已打开流水灯     | Active | FE EF 00 0F EE | FE EF 00 0F EE |
| 26   | 打开渐变灯   | Commande | 好的,已打开渐变灯     | Active | FE EF 00 10 EE | FE EF 00 10 EE |
| 27   | 打开呼吸灯   | Commande | 好的,已打开呼吸灯     | Active | FE EF 00 11 EE | FE EF 00 11 EE |
| 28   | 显示电量     | Commande | 好的,已显示电量       | Active | FE EF 00 12 EE | FE EF 00 12 EE |
| 29   | 导航去一号位 | Commande | 好的,正在去一号位     | Active | FE EF 00 13 EE | FE EF 00 13 EE |
| 30   | 导航去二号位 | Commande | 好的,正在去二号位     | Active | FE EF 00 14 EE | FE EF 00 14 EE |
| 31   | 导航去三号位 | Commande | 好的,正在去三号位     | Active | FE EF 00 15 EE | FE EF 00 15 EE |
| 32   | 导航去四号位 | Commande | 好的,正在去四号位     | Active | FE EF 00 20 EE | FE EF 00 20 EE |
| 33   | 回到原点     | Commande | 好的,正在回到原点     | Active | FE EF 00 21 EE | FE EF 00 21 EE |
| 34   | 关闭巡线     | Commande | 好的,已关闭巡线功能   | Active | FE EF 00 16 EE | FE EF 00 16 EE |
| 35   | 巡红线       | Commande | 好的,已开启巡红线功能 | Active | FE EF 00 17 EE | FE EF 00 17 EE |
| 36   | 巡绿线       | Commande | 好的,已开启巡绿线功能 | Active | FE EF 00 18 EE | FE EF 00 18 EE |
| 37   | 巡蓝线       | Commande | 好的,已开启巡蓝线功能 | Active | FE EF 00 19 EE | FE EF 00 19 EE |
| 38   | 巡黄线       | Commande | 好的,已开启巡黄线功能 | Active | FE EF 00 1A EE | FE EF 00 1A EE |
| 39   | 开启跟随     | Commande | 好的,已开启跟随功能   | Active | FE EF 00 1B EE | FE EF 00 1B EE |
| 40   | 关闭跟随     | Commande | 好的,已关闭跟随功能   | Active | FE EF 00 1C EE | FE EF 00 1C EE |
| 41   | 报警         | Commande | 好的,已开启报警       | Active | FE EF 00 26 EE | FE EF 00 26 EE |
| 42   | 向上         | Commande | 好的,已控制向上       | Active | FE EF 00 27 EE | FE EF 00 27 EE |
| 43   | 向下         | Commande | 好的,已控制向下       | Active | FE EF 00 28 EE | FE EF 00 28 EE |
| 44   | 向左         | Commande | 好的,已控制向左       | Active | FE EF 00 29 EE | FE EF 00 29 EE |
| 45   | 向右         | Commande | 好的,已控制向右       | Active | FE EF 00 2A EE | FE EF 00 2A EE |
| 46   | 夹紧         | Commande | 好的,已控制夹紧       | Active | FE EF 00 2B EE | FE EF 00 2B EE |
| 47   | 松开         | Commande | 好的,已控制松开       | Active | FE EF 00 2C EE | FE EF 00 2C EE |

Mots de lecture :

| 84   | 这是红色                    | Commande | 这是红色                    | Passive | FE EF FF 5F EE | FE EF FF 5F EE |
| ---- | --------------------------- | ------- | --------------------------- | ------- | -------------- | -------------- |
| 85   | 这是蓝色                    | Commande | 这是蓝色                    | Passive | FE EF FF 60 EE | FE EF FF 60 EE |
| 86   | 这是绿色                    | Commande | 这是绿色                    | Passive | FE EF FF 61 EE | FE EF FF 61 EE |
| 87   | 这是黄色                    | Commande | 这是黄色                    | Passive | FE EF FF 62 EE | FE EF FF 62 EE |
| 88   | 识别到黄色                  | Commande | 识别到黄色                  | Passive | FE EF FF 63 EE | FE EF FF 63 EE |
| 89   | 识别到绿色                  | Commande | 识别到绿色                  | Passive | FE EF FF 64 EE | FE EF FF 64 EE |
| 90   | 识别到蓝色                  | Commande | 识别到蓝色                  | Passive | FE EF FF 65 EE | FE EF FF 65 EE |
| 91   | 识别到红色                  | Commande | 识别到红色                  | Passive | FE EF FF 66 EE | FE EF FF 66 EE |
| 92   | 初始化完成                  | Commande | 初始化完成                  | Passive | FE EF FF 67 EE | FE EF FF 67 EE |
| 93   | 第一个要排序的颜色是        | Commande | 第一个要排序的颜色是        | Passive | FE EF FF 68 EE | FE EF FF 68 EE |
| 94   | 第二个要排序的颜色是        | Commande | 第二个要排序的颜色是        | Passive | FE EF FF 69 EE | FE EF FF 69 EE |
| 95   | 第三个要排序的颜色是        | Commande | 第三个要排序的颜色是        | Passive | FE EF FF 6A EE | FE EF FF 6A EE |
| 96   | 第四个要排序的颜色是        | Commande | 第四个要排序的颜色是        | Passive | FE EF FF 6B EE | FE EF FF 6B EE |
| 97   | 这是易拉罐,属于可回收垃圾   | Commande | 这是易拉罐,属于可回收垃圾   | Passive | FE EF FF 6C EE | FE EF FF 6C EE |
| 98   | 这是旧书包,属于可回收垃圾   | Commande | 这是旧书包,属于可回收垃圾   | Passive | FE EF FF 6D EE | FE EF FF 6D EE |
| 99   | 这是报纸,属于可回收垃圾     | Commande | 这是报纸,属于可回收垃圾     | Passive | FE EF FF 6E EE | FE EF FF 6E EE |
| 100  | 这是书本,属于可回收垃圾     | Commande | 这是书本,属于可回收垃圾     | Passive | FE EF FF 6F EE | FE EF FF 6F EE |
| 101  | 这是注射器,属于有毒垃圾     | Commande | 这是注射器,属于有毒垃圾     | Passive | FE EF FF 70 EE | FE EF FF 70 EE |
| 102  | 这是废旧电池,属于有毒垃圾   | Commande | 这是废旧电池,属于有毒垃圾   | Passive | FE EF FF 71 EE | FE EF FF 71 EE |
| 103  | 这是过期化妆品,属于有毒垃圾 | Commande | 这是过期化妆品,属于有毒垃圾 | Passive | FE EF FF 72 EE | FE EF FF 72 EE |
| 104  | 这是过期药品,属于有毒垃圾   | Commande | 这是过期药品,属于有毒垃圾   | Passive | FE EF FF 73 EE | FE EF FF 73 EE |
| 105  | 这是鱼骨,属于湿垃圾         | Commande | 这是鱼骨,属于湿垃圾         | Passive | FE EF FF 74 EE | FE EF FF 74 EE |
| 106  | 这是西瓜皮,属于湿垃圾       | Commande | 这是西瓜皮,属于湿垃圾       | Passive | FE EF FF 75 EE | FE EF FF 75 EE |
| 107  | 这是苹果核,属于湿垃圾       | Commande | 这是苹果核,属于湿垃圾       | Passive | FE EF FF 76 EE | FE EF FF 76 EE |
| 108  | 这是鸡蛋壳,属于湿垃圾       | Commande | 这是鸡蛋壳,属于湿垃圾       | Passive | FE EF FF 77 EE | FE EF FF 77 EE |
| 109  | 这是一次性筷子,属于干垃圾   | Commande | 这是一次性筷子,属于干垃圾   | Passive | FE EF FF 78 EE | FE EF FF 78 EE |
| 110  | 这是烟蒂,属于干垃圾         | Commande | 这是烟蒂,属于干垃圾         | Passive | FE EF FF 79 EE | FE EF FF 79 EE |
| 111  | 这是桃核,属于干垃圾         | Commande | 这是桃核,属于干垃圾         | Passive | FE EF FF 80 EE | FE EF FF 80 EE |
| 112  | 这是卫生纸,属于干垃圾       | Commande | 这是卫生纸,属于干垃圾       | Passive | FE EF FF 8A EE | FE EF FF 8A EE |

Il existe deux modes de lecture : active et passive.

Lecture active : lorsque nous prononçons le mot de commande conformément au tableau, le module lit activement la phrase correspondante. Après le réveil, si nous disons « 小车前进 » (Voiture avance), le module diffuse activement « 好的，正在前进 » (OK, en marche avant).

Lecture passive : la commande du tableau de protocole doit être envoyée au module vocal via le port série pour que le module lise la phrase correspondante. Elle peut également être déclenchée en écrivant les données de lecture correspondantes dans le registre de lecture passive via le protocole IIC. Pour plus de détails, voir « 3. Communication multi-hôtes ».
