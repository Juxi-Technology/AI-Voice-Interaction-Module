[English](../../en/07-pc-serial/pc-serial.md) | Deutsch | [Español](../../es/07-pc-serial/pc-serial.md) | [Français](../../fr/07-pc-serial/pc-serial.md) | [Italiano](../../it/07-pc-serial/pc-serial.md) | [日本語](../../ja/07-pc-serial/pc-serial.md) | [한국어](../../ko/07-pc-serial/pc-serial.md) | [Português (BR)](../../pt-br/07-pc-serial/pc-serial.md) | [Português (PT)](../../pt-pt/07-pc-serial/pc-serial.md) | [简体中文](../../zh-hans/07-pc-serial/pc-serial.md) | [繁體中文](../../zh-hant/07-pc-serial/pc-serial.md)

# 1. Geräteanschluss

Bringen Sie den Schiebeschalter in den STC8-Modus für die serielle Schnittstelle.

![1](../../en/07-pc-serial/images/1.png)

# 2. Seriellen Debug-Assistenten öffnen

- Öffnen Sie den Uart Assistant, wählen Sie die entsprechende Nummer der seriellen Schnittstelle und stellen Sie die Baudrate auf 115200 ein.

![2](../../en/07-pc-serial/images/2.png)

- Siehe die Datei „命令词播报词协议列表V1\_中文“ (Protokollliste für Befehlswörter und Wiedergabewörter V1\_Chinesisch) im Archiv.

![3](../../en/07-pc-serial/images/3.png)

- Wenn wir „小车前进“ (Auto vorwärts) sagen, gibt der serielle Debug-Assistent das entsprechende Protokoll aus.

![4](../../en/07-pc-serial/images/4.png)

| 11   | 小车停止 | Befehl | 好的,已停止       | Aktiv | FE EF 00 01 EE | FE EF 00 01 EE |
| ---- | -------- | ------- | ----------------- | ------ | -------------- | -------------- |
| 12   | 停车     | Befehl | 好的,已停止       | Aktiv | FE EF 00 02 EE | FE EF 00 02 EE |
| 13   | 小车休眠 | Befehl | 好的,已休眠       | Aktiv | FE EF 00 03 EE | FE EF 00 03 EE |
| 14   | 小车前进 | Befehl | 好的,正在前进     | Aktiv | FE EF 00 04 EE | FE EF 00 04 EE |
| 15   | 小车后退 | Befehl | 好的,正在后退     | Aktiv | FE EF 00 05 EE | FE EF 00 05 EE |
| 16   | 小车左转 | Befehl | 好的,正在向左转   | Aktiv | FE EF 00 06 EE | FE EF 00 06 EE |
| 17   | 小车右转 | Befehl | 好的,正在向右转   | Aktiv | FE EF 00 07 EE | FE EF 00 07 EE |
| 18   | 小车左旋 | Befehl | 好的,正在向左旋转 | Aktiv | FE EF 00 08 EE | FE EF 00 08 EE |
| 19   | 小车右旋 | Befehl | 好的,正在向右旋转 | Aktiv | FE EF 00 09 EE | FE EF 00 09 EE |

- Geben Sie gemäß der Datei „命令词播报词协议列表V1\_中文“ den entsprechenden Befehl ein, und das Sprachmodul spielt den Text des entsprechenden Protokolls ab.

| 84   | 这是红色                  | Befehl | 这是红色                  | Passiv | FE EF FF 5F EE | FE EF FF 5F EE |
| ---- | ------------------------- | ------- | ------------------------- | ------- | -------------- | -------------- |
| 85   | 这是蓝色                  | Befehl | 这是蓝色                  | Passiv | FE EF FF 60 EE | FE EF FF 60 EE |
| 86   | 这是绿色                  | Befehl | 这是绿色                  | Passiv | FE EF FF 61 EE | FE EF FF 61 EE |
| 87   | 这是黄色                  | Befehl | 这是黄色                  | Passiv | FE EF FF 62 EE | FE EF FF 62 EE |
| 88   | 识别到黄色                | Befehl | 识别到黄色                | Passiv | FE EF FF 63 EE | FE EF FF 63 EE |
| 89   | 识别到绿色                | Befehl | 识别到绿色                | Passiv | FE EF FF 64 EE | FE EF FF 64 EE |
| 90   | 识别到蓝色                | Befehl | 识别到蓝色                | Passiv | FE EF FF 65 EE | FE EF FF 65 EE |
| 91   | 识别到红色                | Befehl | 识别到红色                | Passiv | FE EF FF 66 EE | FE EF FF 66 EE |
| 92   | 初始化完成                | Befehl | 初始化完成                | Passiv | FE EF FF 67 EE | FE EF FF 67 EE |
| 93   | 第一个要排序的颜色是      | Befehl | 第一个要排序的颜色是      | Passiv | FE EF FF 68 EE | FE EF FF 68 EE |
| 94   | 第二个要排序的颜色是      | Befehl | 第二个要排序的颜色是      | Passiv | FE EF FF 69 EE | FE EF FF 69 EE |
| 95   | 第三个要排序的颜色是      | Befehl | 第三个要排序的颜色是      | Passiv | FE EF FF 6A EE | FE EF FF 6A EE |
| 96   | 第四个要排序的颜色是      | Befehl | 第四个要排序的颜色是      | Passiv | FE EF FF 6B EE | FE EF FF 6B EE |
| 97   | 这是易拉罐,属于可回收垃圾 | Befehl | 这是易拉罐,属于可回收垃圾 | Passiv | FE EF FF 6C EE | FE EF FF 6C EE |

![5](../../en/07-pc-serial/images/5.png)

Sie können hören, wie das Sprachmodul normal abspielt.
