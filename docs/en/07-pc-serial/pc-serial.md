English | [Deutsch](../../de/07-pc-serial/pc-serial.md) | [Español](../../es/07-pc-serial/pc-serial.md) | [Français](../../fr/07-pc-serial/pc-serial.md) | [Italiano](../../it/07-pc-serial/pc-serial.md) | [日本語](../../ja/07-pc-serial/pc-serial.md) | [한국어](../../ko/07-pc-serial/pc-serial.md) | [Português (BR)](../../pt-br/07-pc-serial/pc-serial.md) | [Português (PT)](../../pt-pt/07-pc-serial/pc-serial.md) | [简体中文](../../zh-hans/07-pc-serial/pc-serial.md) | [繁體中文](../../zh-hant/07-pc-serial/pc-serial.md)

# 1. Device Connection

Move the slide switch to STC8 serial port mode.

![1](images/1.png)

# 2. Open Serial Debug Assistant

- Open Uart Assistant, select the corresponding serial port number, and set the baud rate to 115200.

![2](images/2.png)

- Refer to the "命令词播报词协议列表V1\_中文" (Command Word Playback Word Protocol List V1\_Chinese) file in the archive.

![3](images/3.png)

- When we say "小车前进" (Car Forward), the serial debug assistant will print the corresponding protocol.

![4](images/4.png)

| 11   | 小车停止 | Command | 好的,已停止       | Active | FE EF 00 01 EE | FE EF 00 01 EE |
| ---- | -------- | ------- | ----------------- | ------ | -------------- | -------------- |
| 12   | 停车     | Command | 好的,已停止       | Active | FE EF 00 02 EE | FE EF 00 02 EE |
| 13   | 小车休眠 | Command | 好的,已休眠       | Active | FE EF 00 03 EE | FE EF 00 03 EE |
| 14   | 小车前进 | Command | 好的,正在前进     | Active | FE EF 00 04 EE | FE EF 00 04 EE |
| 15   | 小车后退 | Command | 好的,正在后退     | Active | FE EF 00 05 EE | FE EF 00 05 EE |
| 16   | 小车左转 | Command | 好的,正在向左转   | Active | FE EF 00 06 EE | FE EF 00 06 EE |
| 17   | 小车右转 | Command | 好的,正在向右转   | Active | FE EF 00 07 EE | FE EF 00 07 EE |
| 18   | 小车左旋 | Command | 好的,正在向左旋转 | Active | FE EF 00 08 EE | FE EF 00 08 EE |
| 19   | 小车右旋 | Command | 好的,正在向右旋转 | Active | FE EF 00 09 EE | FE EF 00 09 EE |

- According to the "命令词播报词协议列表V1\_中文" file, input the corresponding command, and the voice module will play the text of the corresponding protocol.

| 84   | 这是红色                  | Command | 这是红色                  | Passive | FE EF FF 5F EE | FE EF FF 5F EE |
| ---- | ------------------------- | ------- | ------------------------- | ------- | -------------- | -------------- |
| 85   | 这是蓝色                  | Command | 这是蓝色                  | Passive | FE EF FF 60 EE | FE EF FF 60 EE |
| 86   | 这是绿色                  | Command | 这是绿色                  | Passive | FE EF FF 61 EE | FE EF FF 61 EE |
| 87   | 这是黄色                  | Command | 这是黄色                  | Passive | FE EF FF 62 EE | FE EF FF 62 EE |
| 88   | 识别到黄色                | Command | 识别到黄色                | Passive | FE EF FF 63 EE | FE EF FF 63 EE |
| 89   | 识别到绿色                | Command | 识别到绿色                | Passive | FE EF FF 64 EE | FE EF FF 64 EE |
| 90   | 识别到蓝色                | Command | 识别到蓝色                | Passive | FE EF FF 65 EE | FE EF FF 65 EE |
| 91   | 识别到红色                | Command | 识别到红色                | Passive | FE EF FF 66 EE | FE EF FF 66 EE |
| 92   | 初始化完成                | Command | 初始化完成                | Passive | FE EF FF 67 EE | FE EF FF 67 EE |
| 93   | 第一个要排序的颜色是      | Command | 第一个要排序的颜色是      | Passive | FE EF FF 68 EE | FE EF FF 68 EE |
| 94   | 第二个要排序的颜色是      | Command | 第二个要排序的颜色是      | Passive | FE EF FF 69 EE | FE EF FF 69 EE |
| 95   | 第三个要排序的颜色是      | Command | 第三个要排序的颜色是      | Passive | FE EF FF 6A EE | FE EF FF 6A EE |
| 96   | 第四个要排序的颜色是      | Command | 第四个要排序的颜色是      | Passive | FE EF FF 6B EE | FE EF FF 6B EE |
| 97   | 这是易拉罐,属于可回收垃圾 | Command | 这是易拉罐,属于可回收垃圾 | Passive | FE EF FF 6C EE | FE EF FF 6C EE |

![5](images/5.png)

You can hear the voice module playing normally.
