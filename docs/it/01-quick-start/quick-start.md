[English](../../en/01-quick-start/quick-start.md) | [Deutsch](../../de/01-quick-start/quick-start.md) | [Español](../../es/01-quick-start/quick-start.md) | [Français](../../fr/01-quick-start/quick-start.md) | Italiano | [日本語](../../ja/01-quick-start/quick-start.md) | [한국어](../../ko/01-quick-start/quick-start.md) | [Português (BR)](../../pt-br/01-quick-start/quick-start.md) | [Português (PT)](../../pt-pt/01-quick-start/quick-start.md) | [简体中文](../../zh-hans/01-quick-start/quick-start.md) | [繁體中文](../../zh-hant/01-quick-start/quick-start.md)

# Guida rapida

Il firmware di fabbrica include già la funzionalità di riconoscimento vocale, quindi gli utenti possono provarla rapidamente senza eseguire il flashing. Se hai bisogno di aggiungere altre voci di riconoscimento, eseguire il flashing di un altro firmware o personalizzare le voci, consulta il tutorial "3. Creazione di voci con protocollo personalizzato" per le istruzioni su come personalizzare le voci.

# 1. Preparazione

1. Un cavo dati Type-C
2. Modulo di interazione vocale

# 2. Collegamento del dispositivo

![1](../../en/01-quick-start/images/1.png)

# 3. Riconoscimento vocale e riproduzione

Dopo aver alimentato il modulo di interazione vocale tramite Type-C, risveglia il modulo dicendo "你好，小犀" (Ciao, Xiao Xi). Al risveglio riuscito, il modulo risponde "我在" (Sono qui), indicando che si trova attualmente nello stato di riconoscimento vocale. Se entro 15 secondi non viene riconosciuta alcuna voce di comando, il modulo entra in modalità riposo e annuncia "我去休息了" (Vado a riposare). Per risvegliare nuovamente il modulo, è sufficiente ripetere la parola di risveglio.

Il firmware di fabbrica include parole di comando e parole di riproduzione integrate. Puoi consultare l'elenco dei protocolli negli allegati della documentazione forniti. La tabella seguente mostra un estratto parziale dell'elenco dei protocolli delle parole di comando e delle parole di riproduzione. Puoi controllare il tipo di funzione per vedere cosa rappresenta ciascuna parola di comando. Le parole di riproduzione contrassegnate come "passive" devono essere attivate inviando il comando corrispondente al modulo di interazione vocale tramite una porta seriale del PC, un microcontrollore o un altro dispositivo host. Vedi i dettagli di seguito.

Parole di funzione:

| Etichetta semantica | Parola di comando | Tipo di funzione | Frase di riproduzione | Modalità di riproduzione | Protocollo di invio | Protocollo di ricezione |
| -------------- | ------------ | ------------- | --------------- | ------------- | --------------- | ---------------- |
| 1              | 欢迎语       | Benvenuto     | 欢迎使用小犀    | Passiva       | FE EF 01 00 EE  | FE EF 01 00 EE   |
| 2              | 休息语       | Riposo        | 我去休息啦      | Attiva        | FE EF 02 00 EE  | FE EF 02 00 EE   |
| 3              | 你好小犀     | Parola di risveglio | 我在      | Attiva        | FE EF 03 00 EE  | FE EF 03 00 EE   |
| 4              | 增大音量     | Aumenta volume | 增大音量       | Attiva        | FE EF 04 00 EE  | FE EF 04 00 EE   |
| 5              | 减小音量     | Riduci volume | 减小音量        | Attiva        | FE EF 05 00 EE  | FE EF 05 00 EE   |
| 6              | 最大音量     | Volume massimo | 最大音量       | Attiva        | FE EF 06 00 EE  | FE EF 06 00 EE   |
| 7              | 中等音量     | Volume medio  | 中等音量        | Attiva        | FE EF 07 00 EE  | FE EF 07 00 EE   |
| 8              | 最小音量     | Volume minimo | 最小音量        | Attiva        | FE EF 08 00 EE  | FE EF 08 00 EE   |
| 9              | 开启播报     | Attiva riproduzione | 开启播报   | Attiva        | FE EF 09 00 EE  | FE EF 09 00 EE   |
| 10             | 关闭播报     | Disattiva riproduzione | 关闭播报 | Attiva      | FE EF 0A 00 EE  | FE EF 0A 00 EE   |

Parole di comando:

| 11   | 小车停止     | Comando | 好的,已停止           | Attiva | FE EF 00 01 EE | FE EF 00 01 EE |
| ---- | ------------ | ------- | --------------------- | ------ | -------------- | -------------- |
| 12   | 停车         | Comando | 好的,已停止           | Attiva | FE EF 00 02 EE | FE EF 00 02 EE |
| 13   | 小车休眠     | Comando | 好的,已休眠           | Attiva | FE EF 00 03 EE | FE EF 00 03 EE |
| 14   | 小车前进     | Comando | 好的,正在前进         | Attiva | FE EF 00 04 EE | FE EF 00 04 EE |
| 15   | 小车后退     | Comando | 好的,正在后退         | Attiva | FE EF 00 05 EE | FE EF 00 05 EE |
| 16   | 小车左转     | Comando | 好的,正在向左转       | Attiva | FE EF 00 06 EE | FE EF 00 06 EE |
| 17   | 小车右转     | Comando | 好的,正在向右转       | Attiva | FE EF 00 07 EE | FE EF 00 07 EE |
| 18   | 小车左旋     | Comando | 好的,正在向左旋转     | Attiva | FE EF 00 08 EE | FE EF 00 08 EE |
| 19   | 小车右旋     | Comando | 好的,正在向右旋转     | Attiva | FE EF 00 09 EE | FE EF 00 09 EE |
| 20   | 关灯         | Comando | 好的,已关灯           | Attiva | FE EF 00 0A EE | FE EF 00 0A EE |
| 21   | 亮红灯       | Comando | 好的,已亮红灯         | Attiva | FE EF 00 0B EE | FE EF 00 0B EE |
| 22   | 亮绿灯       | Comando | 好的,已亮绿灯         | Attiva | FE EF 00 0C EE | FE EF 00 0C EE |
| 23   | 亮蓝灯       | Comando | 好的,已亮蓝灯         | Attiva | FE EF 00 0D EE | FE EF 00 0D EE |
| 24   | 亮黄灯       | Comando | 好的,已亮黄灯         | Attiva | FE EF 00 0E EE | FE EF 00 0E EE |
| 25   | 打开流水灯   | Comando | 好的,已打开流水灯     | Attiva | FE EF 00 0F EE | FE EF 00 0F EE |
| 26   | 打开渐变灯   | Comando | 好的,已打开渐变灯     | Attiva | FE EF 00 10 EE | FE EF 00 10 EE |
| 27   | 打开呼吸灯   | Comando | 好的,已打开呼吸灯     | Attiva | FE EF 00 11 EE | FE EF 00 11 EE |
| 28   | 显示电量     | Comando | 好的,已显示电量       | Attiva | FE EF 00 12 EE | FE EF 00 12 EE |
| 29   | 导航去一号位 | Comando | 好的,正在去一号位     | Attiva | FE EF 00 13 EE | FE EF 00 13 EE |
| 30   | 导航去二号位 | Comando | 好的,正在去二号位     | Attiva | FE EF 00 14 EE | FE EF 00 14 EE |
| 31   | 导航去三号位 | Comando | 好的,正在去三号位     | Attiva | FE EF 00 15 EE | FE EF 00 15 EE |
| 32   | 导航去四号位 | Comando | 好的,正在去四号位     | Attiva | FE EF 00 20 EE | FE EF 00 20 EE |
| 33   | 回到原点     | Comando | 好的,正在回到原点     | Attiva | FE EF 00 21 EE | FE EF 00 21 EE |
| 34   | 关闭巡线     | Comando | 好的,已关闭巡线功能   | Attiva | FE EF 00 16 EE | FE EF 00 16 EE |
| 35   | 巡红线       | Comando | 好的,已开启巡红线功能 | Attiva | FE EF 00 17 EE | FE EF 00 17 EE |
| 36   | 巡绿线       | Comando | 好的,已开启巡绿线功能 | Attiva | FE EF 00 18 EE | FE EF 00 18 EE |
| 37   | 巡蓝线       | Comando | 好的,已开启巡蓝线功能 | Attiva | FE EF 00 19 EE | FE EF 00 19 EE |
| 38   | 巡黄线       | Comando | 好的,已开启巡黄线功能 | Attiva | FE EF 00 1A EE | FE EF 00 1A EE |
| 39   | 开启跟随     | Comando | 好的,已开启跟随功能   | Attiva | FE EF 00 1B EE | FE EF 00 1B EE |
| 40   | 关闭跟随     | Comando | 好的,已关闭跟随功能   | Attiva | FE EF 00 1C EE | FE EF 00 1C EE |
| 41   | 报警         | Comando | 好的,已开启报警       | Attiva | FE EF 00 26 EE | FE EF 00 26 EE |
| 42   | 向上         | Comando | 好的,已控制向上       | Attiva | FE EF 00 27 EE | FE EF 00 27 EE |
| 43   | 向下         | Comando | 好的,已控制向下       | Attiva | FE EF 00 28 EE | FE EF 00 28 EE |
| 44   | 向左         | Comando | 好的,已控制向左       | Attiva | FE EF 00 29 EE | FE EF 00 29 EE |
| 45   | 向右         | Comando | 好的,已控制向右       | Attiva | FE EF 00 2A EE | FE EF 00 2A EE |
| 46   | 夹紧         | Comando | 好的,已控制夹紧       | Attiva | FE EF 00 2B EE | FE EF 00 2B EE |
| 47   | 松开         | Comando | 好的,已控制松开       | Attiva | FE EF 00 2C EE | FE EF 00 2C EE |

Parole di riproduzione:

| 84   | 这是红色                    | Comando | 这是红色                    | Passiva | FE EF FF 5F EE | FE EF FF 5F EE |
| ---- | --------------------------- | ------- | --------------------------- | ------- | -------------- | -------------- |
| 85   | 这是蓝色                    | Comando | 这是蓝色                    | Passiva | FE EF FF 60 EE | FE EF FF 60 EE |
| 86   | 这是绿色                    | Comando | 这是绿色                    | Passiva | FE EF FF 61 EE | FE EF FF 61 EE |
| 87   | 这是黄色                    | Comando | 这是黄色                    | Passiva | FE EF FF 62 EE | FE EF FF 62 EE |
| 88   | 识别到黄色                  | Comando | 识别到黄色                  | Passiva | FE EF FF 63 EE | FE EF FF 63 EE |
| 89   | 识别到绿色                  | Comando | 识别到绿色                  | Passiva | FE EF FF 64 EE | FE EF FF 64 EE |
| 90   | 识别到蓝色                  | Comando | 识别到蓝色                  | Passiva | FE EF FF 65 EE | FE EF FF 65 EE |
| 91   | 识别到红色                  | Comando | 识别到红色                  | Passiva | FE EF FF 66 EE | FE EF FF 66 EE |
| 92   | 初始化完成                  | Comando | 初始化完成                  | Passiva | FE EF FF 67 EE | FE EF FF 67 EE |
| 93   | 第一个要排序的颜色是        | Comando | 第一个要排序的颜色是        | Passiva | FE EF FF 68 EE | FE EF FF 68 EE |
| 94   | 第二个要排序的颜色是        | Comando | 第二个要排序的颜色是        | Passiva | FE EF FF 69 EE | FE EF FF 69 EE |
| 95   | 第三个要排序的颜色是        | Comando | 第三个要排序的颜色是        | Passiva | FE EF FF 6A EE | FE EF FF 6A EE |
| 96   | 第四个要排序的颜色是        | Comando | 第四个要排序的颜色是        | Passiva | FE EF FF 6B EE | FE EF FF 6B EE |
| 97   | 这是易拉罐,属于可回收垃圾   | Comando | 这是易拉罐,属于可回收垃圾   | Passiva | FE EF FF 6C EE | FE EF FF 6C EE |
| 98   | 这是旧书包,属于可回收垃圾   | Comando | 这是旧书包,属于可回收垃圾   | Passiva | FE EF FF 6D EE | FE EF FF 6D EE |
| 99   | 这是报纸,属于可回收垃圾     | Comando | 这是报纸,属于可回收垃圾     | Passiva | FE EF FF 6E EE | FE EF FF 6E EE |
| 100  | 这是书本,属于可回收垃圾     | Comando | 这是书本,属于可回收垃圾     | Passiva | FE EF FF 6F EE | FE EF FF 6F EE |
| 101  | 这是注射器,属于有毒垃圾     | Comando | 这是注射器,属于有毒垃圾     | Passiva | FE EF FF 70 EE | FE EF FF 70 EE |
| 102  | 这是废旧电池,属于有毒垃圾   | Comando | 这是废旧电池,属于有毒垃圾   | Passiva | FE EF FF 71 EE | FE EF FF 71 EE |
| 103  | 这是过期化妆品,属于有毒垃圾 | Comando | 这是过期化妆品,属于有毒垃圾 | Passiva | FE EF FF 72 EE | FE EF FF 72 EE |
| 104  | 这是过期药品,属于有毒垃圾   | Comando | 这是过期药品,属于有毒垃圾   | Passiva | FE EF FF 73 EE | FE EF FF 73 EE |
| 105  | 这是鱼骨,属于湿垃圾         | Comando | 这是鱼骨,属于湿垃圾         | Passiva | FE EF FF 74 EE | FE EF FF 74 EE |
| 106  | 这是西瓜皮,属于湿垃圾       | Comando | 这是西瓜皮,属于湿垃圾       | Passiva | FE EF FF 75 EE | FE EF FF 75 EE |
| 107  | 这是苹果核,属于湿垃圾       | Comando | 这是苹果核,属于湿垃圾       | Passiva | FE EF FF 76 EE | FE EF FF 76 EE |
| 108  | 这是鸡蛋壳,属于湿垃圾       | Comando | 这是鸡蛋壳,属于湿垃圾       | Passiva | FE EF FF 77 EE | FE EF FF 77 EE |
| 109  | 这是一次性筷子,属于干垃圾   | Comando | 这是一次性筷子,属于干垃圾   | Passiva | FE EF FF 78 EE | FE EF FF 78 EE |
| 110  | 这是烟蒂,属于干垃圾         | Comando | 这是烟蒂,属于干垃圾         | Passiva | FE EF FF 79 EE | FE EF FF 79 EE |
| 111  | 这是桃核,属于干垃圾         | Comando | 这是桃核,属于干垃圾         | Passiva | FE EF FF 80 EE | FE EF FF 80 EE |
| 112  | 这是卫生纸,属于干垃圾       | Comando | 这是卫生纸,属于干垃圾       | Passiva | FE EF FF 8A EE | FE EF FF 8A EE |

Esistono due modalità di riproduzione: attiva e passiva.

Riproduzione attiva: quando pronunciamo la parola di comando secondo la tabella, il modulo riproduce attivamente la frase corrispondente. Dopo il risveglio, se diciamo "小车前进" (Il carrello avanza), il modulo trasmette attivamente "好的，正在前进" (Bene, avanzamento in corso).

Riproduzione passiva: il comando della tabella dei protocolli deve essere inviato al modulo vocale tramite la porta seriale affinché il modulo riproduca la frase corrispondente. Può anche essere attivato scrivendo i dati di riproduzione corrispondenti nel registro di riproduzione passiva tramite il protocollo IIC. Per maggiori dettagli, vedi "3. Comunicazione multi-host".
