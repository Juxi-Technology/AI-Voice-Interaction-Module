[English](../../en/01-quick-start/quick-start.md) | Deutsch | [Español](../../es/01-quick-start/quick-start.md) | [Français](../../fr/01-quick-start/quick-start.md) | [Italiano](../../it/01-quick-start/quick-start.md) | [日本語](../../ja/01-quick-start/quick-start.md) | [한국어](../../ko/01-quick-start/quick-start.md) | [Português (BR)](../../pt-br/01-quick-start/quick-start.md) | [Português (PT)](../../pt-pt/01-quick-start/quick-start.md) | [简体中文](../../zh-hans/01-quick-start/quick-start.md) | [繁體中文](../../zh-hant/01-quick-start/quick-start.md)

# Schnellstart

Die Werks-Firmware enthält bereits eine Spracherkennungsfunktion, sodass Anwender sie ohne Flashen schnell ausprobieren können. Wenn Sie zusätzliche Erkennungseinträge hinzufügen, andere Firmware neu aufspielen oder Einträge anpassen möchten, lesen Sie bitte das Tutorial „3. Benutzerdefinierte Protokolleinträge erstellen“, um zu erfahren, wie Sie Einträge anpassen.

# 1. Vorbereitung

1. Ein Type-C-Datenkabel
2. Sprachinteraktionsmodul

# 2. Geräteanschluss

![1](../../en/01-quick-start/images/1.png)

# 3. Spracherkennung und Wiedergabe

Versorgen Sie das Sprachinteraktionsmodul über Type-C mit Strom und wecken Sie es anschließend auf, indem Sie „你好，小犀“ (Hallo, Xiao Xi) sagen. Nach erfolgreichem Aufwecken antwortet das Modul mit „我在“ (Ich bin hier), was anzeigt, dass es sich derzeit im Spracherkennungszustand befindet. Wird innerhalb von 15 Sekunden kein Befehlseintrag erkannt, wechselt das Modul in den Schlafmodus und sagt „我去休息了“ (Ich gehe jetzt schlafen). Um das Modul erneut aufzuwecken, sagen Sie einfach wieder das Weckwort.

Die Werks-Firmware enthält bereits integrierte Befehlswörter und Wiedergabewörter. Die Protokollliste finden Sie in den mitgelieferten Dokumentationsanhängen. Die folgende Tabelle zeigt einen Teilauszug der Protokollliste für Befehlswörter und Wiedergabewörter. Anhand des Funktionstyps können Sie erkennen, wofür jedes Befehlswort steht. Wiedergabewörter, die als „passiv“ gekennzeichnet sind, müssen ausgelöst werden, indem der entsprechende Befehl über eine serielle PC-Schnittstelle, einen Mikrocontroller oder ein anderes Hostgerät an das Sprachinteraktionsmodul gesendet wird. Einzelheiten siehe unten.

Funktionswörter:

| Semantisches Label | Befehlswort | Funktionstyp | Wiedergabesatz | Wiedergabemodus | Sende-Protokoll | Empfangsprotokoll |
| -------------- | ------------ | ------------- | --------------- | ------------- | --------------- | ---------------- |
| 1              | 欢迎语       | Begrüßung     | 欢迎使用小犀    | Passiv        | FE EF 01 00 EE  | FE EF 01 00 EE   |
| 2              | 休息语       | Schlaf        | 我去休息啦      | Aktiv         | FE EF 02 00 EE  | FE EF 02 00 EE   |
| 3              | 你好小犀     | Weckwort      | 我在            | Aktiv         | FE EF 03 00 EE  | FE EF 03 00 EE   |
| 4              | 增大音量     | Lautstärke erhöhen | 增大音量   | Aktiv         | FE EF 04 00 EE  | FE EF 04 00 EE   |
| 5              | 减小音量     | Lautstärke verringern | 减小音量 | Aktiv       | FE EF 05 00 EE  | FE EF 05 00 EE   |
| 6              | 最大音量     | Maximale Lautstärke | 最大音量  | Aktiv        | FE EF 06 00 EE  | FE EF 06 00 EE   |
| 7              | 中等音量     | Mittlere Lautstärke | 中等音量  | Aktiv        | FE EF 07 00 EE  | FE EF 07 00 EE   |
| 8              | 最小音量     | Minimale Lautstärke | 最小音量  | Aktiv        | FE EF 08 00 EE  | FE EF 08 00 EE   |
| 9              | 开启播报     | Wiedergabe aktivieren | 开启播报 | Aktiv       | FE EF 09 00 EE  | FE EF 09 00 EE   |
| 10             | 关闭播报     | Wiedergabe deaktivieren | 关闭播报 | Aktiv     | FE EF 0A 00 EE  | FE EF 0A 00 EE   |

Befehlswörter:

| 11   | 小车停止     | Befehl | 好的,已停止           | Aktiv | FE EF 00 01 EE | FE EF 00 01 EE |
| ---- | ------------ | ------- | --------------------- | ------ | -------------- | -------------- |
| 12   | 停车         | Befehl | 好的,已停止           | Aktiv | FE EF 00 02 EE | FE EF 00 02 EE |
| 13   | 小车休眠     | Befehl | 好的,已休眠           | Aktiv | FE EF 00 03 EE | FE EF 00 03 EE |
| 14   | 小车前进     | Befehl | 好的,正在前进         | Aktiv | FE EF 00 04 EE | FE EF 00 04 EE |
| 15   | 小车后退     | Befehl | 好的,正在后退         | Aktiv | FE EF 00 05 EE | FE EF 00 05 EE |
| 16   | 小车左转     | Befehl | 好的,正在向左转       | Aktiv | FE EF 00 06 EE | FE EF 00 06 EE |
| 17   | 小车右转     | Befehl | 好的,正在向右转       | Aktiv | FE EF 00 07 EE | FE EF 00 07 EE |
| 18   | 小车左旋     | Befehl | 好的,正在向左旋转     | Aktiv | FE EF 00 08 EE | FE EF 00 08 EE |
| 19   | 小车右旋     | Befehl | 好的,正在向右旋转     | Aktiv | FE EF 00 09 EE | FE EF 00 09 EE |
| 20   | 关灯         | Befehl | 好的,已关灯           | Aktiv | FE EF 00 0A EE | FE EF 00 0A EE |
| 21   | 亮红灯       | Befehl | 好的,已亮红灯         | Aktiv | FE EF 00 0B EE | FE EF 00 0B EE |
| 22   | 亮绿灯       | Befehl | 好的,已亮绿灯         | Aktiv | FE EF 00 0C EE | FE EF 00 0C EE |
| 23   | 亮蓝灯       | Befehl | 好的,已亮蓝灯         | Aktiv | FE EF 00 0D EE | FE EF 00 0D EE |
| 24   | 亮黄灯       | Befehl | 好的,已亮黄灯         | Aktiv | FE EF 00 0E EE | FE EF 00 0E EE |
| 25   | 打开流水灯   | Befehl | 好的,已打开流水灯     | Aktiv | FE EF 00 0F EE | FE EF 00 0F EE |
| 26   | 打开渐变灯   | Befehl | 好的,已打开渐变灯     | Aktiv | FE EF 00 10 EE | FE EF 00 10 EE |
| 27   | 打开呼吸灯   | Befehl | 好的,已打开呼吸灯     | Aktiv | FE EF 00 11 EE | FE EF 00 11 EE |
| 28   | 显示电量     | Befehl | 好的,已显示电量       | Aktiv | FE EF 00 12 EE | FE EF 00 12 EE |
| 29   | 导航去一号位 | Befehl | 好的,正在去一号位     | Aktiv | FE EF 00 13 EE | FE EF 00 13 EE |
| 30   | 导航去二号位 | Befehl | 好的,正在去二号位     | Aktiv | FE EF 00 14 EE | FE EF 00 14 EE |
| 31   | 导航去三号位 | Befehl | 好的,正在去三号位     | Aktiv | FE EF 00 15 EE | FE EF 00 15 EE |
| 32   | 导航去四号位 | Befehl | 好的,正在去四号位     | Aktiv | FE EF 00 20 EE | FE EF 00 20 EE |
| 33   | 回到原点     | Befehl | 好的,正在回到原点     | Aktiv | FE EF 00 21 EE | FE EF 00 21 EE |
| 34   | 关闭巡线     | Befehl | 好的,已关闭巡线功能   | Aktiv | FE EF 00 16 EE | FE EF 00 16 EE |
| 35   | 巡红线       | Befehl | 好的,已开启巡红线功能 | Aktiv | FE EF 00 17 EE | FE EF 00 17 EE |
| 36   | 巡绿线       | Befehl | 好的,已开启巡绿线功能 | Aktiv | FE EF 00 18 EE | FE EF 00 18 EE |
| 37   | 巡蓝线       | Befehl | 好的,已开启巡蓝线功能 | Aktiv | FE EF 00 19 EE | FE EF 00 19 EE |
| 38   | 巡黄线       | Befehl | 好的,已开启巡黄线功能 | Aktiv | FE EF 00 1A EE | FE EF 00 1A EE |
| 39   | 开启跟随     | Befehl | 好的,已开启跟随功能   | Aktiv | FE EF 00 1B EE | FE EF 00 1B EE |
| 40   | 关闭跟随     | Befehl | 好的,已关闭跟随功能   | Aktiv | FE EF 00 1C EE | FE EF 00 1C EE |
| 41   | 报警         | Befehl | 好的,已开启报警       | Aktiv | FE EF 00 26 EE | FE EF 00 26 EE |
| 42   | 向上         | Befehl | 好的,已控制向上       | Aktiv | FE EF 00 27 EE | FE EF 00 27 EE |
| 43   | 向下         | Befehl | 好的,已控制向下       | Aktiv | FE EF 00 28 EE | FE EF 00 28 EE |
| 44   | 向左         | Befehl | 好的,已控制向左       | Aktiv | FE EF 00 29 EE | FE EF 00 29 EE |
| 45   | 向右         | Befehl | 好的,已控制向右       | Aktiv | FE EF 00 2A EE | FE EF 00 2A EE |
| 46   | 夹紧         | Befehl | 好的,已控制夹紧       | Aktiv | FE EF 00 2B EE | FE EF 00 2B EE |
| 47   | 松开         | Befehl | 好的,已控制松开       | Aktiv | FE EF 00 2C EE | FE EF 00 2C EE |

Wiedergabewörter:

| 84   | 这是红色                    | Befehl | 这是红色                    | Passiv | FE EF FF 5F EE | FE EF FF 5F EE |
| ---- | --------------------------- | ------- | --------------------------- | ------- | -------------- | -------------- |
| 85   | 这是蓝色                    | Befehl | 这是蓝色                    | Passiv | FE EF FF 60 EE | FE EF FF 60 EE |
| 86   | 这是绿色                    | Befehl | 这是绿色                    | Passiv | FE EF FF 61 EE | FE EF FF 61 EE |
| 87   | 这是黄色                    | Befehl | 这是黄色                    | Passiv | FE EF FF 62 EE | FE EF FF 62 EE |
| 88   | 识别到黄色                  | Befehl | 识别到黄色                  | Passiv | FE EF FF 63 EE | FE EF FF 63 EE |
| 89   | 识别到绿色                  | Befehl | 识别到绿色                  | Passiv | FE EF FF 64 EE | FE EF FF 64 EE |
| 90   | 识别到蓝色                  | Befehl | 识别到蓝色                  | Passiv | FE EF FF 65 EE | FE EF FF 65 EE |
| 91   | 识别到红色                  | Befehl | 识别到红色                  | Passiv | FE EF FF 66 EE | FE EF FF 66 EE |
| 92   | 初始化完成                  | Befehl | 初始化完成                  | Passiv | FE EF FF 67 EE | FE EF FF 67 EE |
| 93   | 第一个要排序的颜色是        | Befehl | 第一个要排序的颜色是        | Passiv | FE EF FF 68 EE | FE EF FF 68 EE |
| 94   | 第二个要排序的颜色是        | Befehl | 第二个要排序的颜色是        | Passiv | FE EF FF 69 EE | FE EF FF 69 EE |
| 95   | 第三个要排序的颜色是        | Befehl | 第三个要排序的颜色是        | Passiv | FE EF FF 6A EE | FE EF FF 6A EE |
| 96   | 第四个要排序的颜色是        | Befehl | 第四个要排序的颜色是        | Passiv | FE EF FF 6B EE | FE EF FF 6B EE |
| 97   | 这是易拉罐,属于可回收垃圾   | Befehl | 这是易拉罐,属于可回收垃圾   | Passiv | FE EF FF 6C EE | FE EF FF 6C EE |
| 98   | 这是旧书包,属于可回收垃圾   | Befehl | 这是旧书包,属于可回收垃圾   | Passiv | FE EF FF 6D EE | FE EF FF 6D EE |
| 99   | 这是报纸,属于可回收垃圾     | Befehl | 这是报纸,属于可回收垃圾     | Passiv | FE EF FF 6E EE | FE EF FF 6E EE |
| 100  | 这是书本,属于可回收垃圾     | Befehl | 这是书本,属于可回收垃圾     | Passiv | FE EF FF 6F EE | FE EF FF 6F EE |
| 101  | 这是注射器,属于有毒垃圾     | Befehl | 这是注射器,属于有毒垃圾     | Passiv | FE EF FF 70 EE | FE EF FF 70 EE |
| 102  | 这是废旧电池,属于有毒垃圾   | Befehl | 这是废旧电池,属于有毒垃圾   | Passiv | FE EF FF 71 EE | FE EF FF 71 EE |
| 103  | 这是过期化妆品,属于有毒垃圾 | Befehl | 这是过期化妆品,属于有毒垃圾 | Passiv | FE EF FF 72 EE | FE EF FF 72 EE |
| 104  | 这是过期药品,属于有毒垃圾   | Befehl | 这是过期药品,属于有毒垃圾   | Passiv | FE EF FF 73 EE | FE EF FF 73 EE |
| 105  | 这是鱼骨,属于湿垃圾         | Befehl | 这是鱼骨,属于湿垃圾         | Passiv | FE EF FF 74 EE | FE EF FF 74 EE |
| 106  | 这是西瓜皮,属于湿垃圾       | Befehl | 这是西瓜皮,属于湿垃圾       | Passiv | FE EF FF 75 EE | FE EF FF 75 EE |
| 107  | 这是苹果核,属于湿垃圾       | Befehl | 这是苹果核,属于湿垃圾       | Passiv | FE EF FF 76 EE | FE EF FF 76 EE |
| 108  | 这是鸡蛋壳,属于湿垃圾       | Befehl | 这是鸡蛋壳,属于湿垃圾       | Passiv | FE EF FF 77 EE | FE EF FF 77 EE |
| 109  | 这是一次性筷子,属于干垃圾   | Befehl | 这是一次性筷子,属于干垃圾   | Passiv | FE EF FF 78 EE | FE EF FF 78 EE |
| 110  | 这是烟蒂,属于干垃圾         | Befehl | 这是烟蒂,属于干垃圾         | Passiv | FE EF FF 79 EE | FE EF FF 79 EE |
| 111  | 这是桃核,属于干垃圾         | Befehl | 这是桃核,属于干垃圾         | Passiv | FE EF FF 80 EE | FE EF FF 80 EE |
| 112  | 这是卫生纸,属于干垃圾       | Befehl | 这是卫生纸,属于干垃圾       | Passiv | FE EF FF 8A EE | FE EF FF 8A EE |

Es gibt zwei Wiedergabemodi: aktiv und passiv.

Aktive Wiedergabe: Wenn wir das Befehlswort gemäß der Tabelle aussprechen, spielt das Modul den entsprechenden Satz aktiv ab. Wenn wir nach dem Aufwecken „小车前进“ (Auto vorwärts) sagen, gibt das Modul aktiv „好的，正在前进“ (OK, fahre vorwärts) aus.

Passive Wiedergabe: Der Befehl aus der Protokolltabelle muss über die serielle Schnittstelle an das Sprachmodul gesendet werden, damit das Modul den entsprechenden Satz abspielt. Sie kann auch ausgelöst werden, indem die entsprechenden Wiedergabedaten über das IIC-Protokoll in das Register für passive Wiedergabe geschrieben werden. Weitere Einzelheiten finden Sie unter „3. Multi-Host-Kommunikation“.
