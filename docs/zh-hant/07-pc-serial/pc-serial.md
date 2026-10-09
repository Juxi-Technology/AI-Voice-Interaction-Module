[English](../../en/07-pc-serial/pc-serial.md) | [Deutsch](../../de/07-pc-serial/pc-serial.md) | [Español](../../es/07-pc-serial/pc-serial.md) | [Français](../../fr/07-pc-serial/pc-serial.md) | [Italiano](../../it/07-pc-serial/pc-serial.md) | [日本語](../../ja/07-pc-serial/pc-serial.md) | [한국어](../../ko/07-pc-serial/pc-serial.md) | [Português (BR)](../../pt-br/07-pc-serial/pc-serial.md) | [Português (PT)](../../pt-pt/07-pc-serial/pc-serial.md) | [简体中文](../../zh-hans/07-pc-serial/pc-serial.md) | 繁體中文

# 1. 裝置連接

滑動開關移動到STC8序列埠模式

![1](../../en/07-pc-serial/images/1.png)

# 2. 打開序列埠除錯助手

\- 打開Uart Assistant，選擇對應的序列埠號，以及鮑率為115200，

![2](../../en/07-pc-serial/images/2.png)

\- 參考壓縮包中的命令词播报词协议列表V1\_中文檔案

![3](../../en/07-pc-serial/images/3.png)

\- 當我們說出“小车前进”的時候，序列埠除錯助手會列印出對應的協定

![4](../../en/07-pc-serial/images/4.png)

| 11   | 小车停止 | 命令詞 | 好的,已停止       | 主   | FE EF 00 01 EE | FE EF 00 01 EE |
| ---- | -------- | ------ | ----------------- | ---- | -------------- | -------------- |
| 12   | 停车     | 命令詞 | 好的,已停止       | 主   | FE EF 00 02 EE | FE EF 00 02 EE |
| 13   | 小车休眠 | 命令詞 | 好的,已休眠       | 主   | FE EF 00 03 EE | FE EF 00 03 EE |
| 14   | 小车前进 | 命令詞 | 好的,正在前进     | 主   | FE EF 00 04 EE | FE EF 00 04 EE |
| 15   | 小车后退 | 命令詞 | 好的,正在后退     | 主   | FE EF 00 05 EE | FE EF 00 05 EE |
| 16   | 小车左转 | 命令詞 | 好的,正在向左转   | 主   | FE EF 00 06 EE | FE EF 00 06 EE |
| 17   | 小车右转 | 命令詞 | 好的,正在向右转   | 主   | FE EF 00 07 EE | FE EF 00 07 EE |
| 18   | 小车左旋 | 命令詞 | 好的,正在向左旋转 | 主   | FE EF 00 08 EE | FE EF 00 08 EE |
| 19   | 小车右旋 | 命令詞 | 好的,正在向右旋转 | 主   | FE EF 00 09 EE | FE EF 00 09 EE |

\- 根據命令词播报词协议列表V1\_中文檔案輸入對應指令，語音模組播報對應協定的文字

| 84   | 这是红色                  | 命令詞 | 这是红色                  | 被   | FE EF FF 5F EE | FE EF FF 5F EE |
| ---- | ------------------------- | ------ | ------------------------- | ---- | -------------- | -------------- |
| 85   | 这是蓝色                  | 命令詞 | 这是蓝色                  | 被   | FE EF FF 60 EE | FE EF FF 60 EE |
| 86   | 这是绿色                  | 命令詞 | 这是绿色                  | 被   | FE EF FF 61 EE | FE EF FF 61 EE |
| 87   | 这是黄色                  | 命令詞 | 这是黄色                  | 被   | FE EF FF 62 EE | FE EF FF 62 EE |
| 88   | 识别到黄色                | 命令詞 | 识别到黄色                | 被   | FE EF FF 63 EE | FE EF FF 63 EE |
| 89   | 识别到绿色                | 命令詞 | 识别到绿色                | 被   | FE EF FF 64 EE | FE EF FF 64 EE |
| 90   | 识别到蓝色                | 命令詞 | 识别到蓝色                | 被   | FE EF FF 65 EE | FE EF FF 65 EE |
| 91   | 识别到红色                | 命令詞 | 识别到红色                | 被   | FE EF FF 66 EE | FE EF FF 66 EE |
| 92   | 初始化完成                | 命令詞 | 初始化完成                | 被   | FE EF FF 67 EE | FE EF FF 67 EE |
| 93   | 第一个要排序的颜色是      | 命令詞 | 第一个要排序的颜色是      | 被   | FE EF FF 68 EE | FE EF FF 68 EE |
| 94   | 第二个要排序的颜色是      | 命令詞 | 第二个要排序的颜色是      | 被   | FE EF FF 69 EE | FE EF FF 69 EE |
| 95   | 第三个要排序的颜色是      | 命令詞 | 第三个要排序的颜色是      | 被   | FE EF FF 6A EE | FE EF FF 6A EE |
| 96   | 第四个要排序的颜色是      | 命令詞 | 第四个要排序的颜色是      | 被   | FE EF FF 6B EE | FE EF FF 6B EE |
| 97   | 这是易拉罐,属于可回收垃圾 | 命令詞 | 这是易拉罐,属于可回收垃圾 | 被   | FE EF FF 6C EE | FE EF FF 6C EE |

![5](../../en/07-pc-serial/images/5.png)

可以聽到語音模組正常播報。
