[English](../../en/07-pc-serial/pc-serial.md) | [Deutsch](../../de/07-pc-serial/pc-serial.md) | [Español](../../es/07-pc-serial/pc-serial.md) | [Français](../../fr/07-pc-serial/pc-serial.md) | [Italiano](../../it/07-pc-serial/pc-serial.md) | 日本語 | [한국어](../../ko/07-pc-serial/pc-serial.md) | [Português (BR)](../../pt-br/07-pc-serial/pc-serial.md) | [Português (PT)](../../pt-pt/07-pc-serial/pc-serial.md) | [简体中文](../../zh-hans/07-pc-serial/pc-serial.md) | [繁體中文](../../zh-hant/07-pc-serial/pc-serial.md)

# 1. デバイスの接続

スライドスイッチを STC8 シリアルポートモードに移動します。

![1](../../en/07-pc-serial/images/1.png)

# 2. シリアルデバッグアシスタントを開く

- Uart Assistant を開き、対応するシリアルポート番号を選択し、ボーレートを 115200 に設定します。

![2](../../en/07-pc-serial/images/2.png)

- アーカイブ内の「命令词播报词协议列表V1\_中文」（コマンドワード・読み上げワードプロトコル一覧 V1\_中文）ファイルを参照します。

![3](../../en/07-pc-serial/images/3.png)

- 「小车前进」（車が前進）と言うと、シリアルデバッグアシスタントが対応するプロトコルを出力します。

![4](../../en/07-pc-serial/images/4.png)

| 11   | 小车停止 | コマンド | 好的,已停止       | 能動 | FE EF 00 01 EE | FE EF 00 01 EE |
| ---- | -------- | ------- | ----------------- | ------ | -------------- | -------------- |
| 12   | 停车     | コマンド | 好的,已停止       | 能動 | FE EF 00 02 EE | FE EF 00 02 EE |
| 13   | 小车休眠 | コマンド | 好的,已休眠       | 能動 | FE EF 00 03 EE | FE EF 00 03 EE |
| 14   | 小车前进 | コマンド | 好的,正在前进     | 能動 | FE EF 00 04 EE | FE EF 00 04 EE |
| 15   | 小车后退 | コマンド | 好的,正在后退     | 能動 | FE EF 00 05 EE | FE EF 00 05 EE |
| 16   | 小车左转 | コマンド | 好的,正在向左转   | 能動 | FE EF 00 06 EE | FE EF 00 06 EE |
| 17   | 小车右转 | コマンド | 好的,正在向右转   | 能動 | FE EF 00 07 EE | FE EF 00 07 EE |
| 18   | 小车左旋 | コマンド | 好的,正在向左旋转 | 能動 | FE EF 00 08 EE | FE EF 00 08 EE |
| 19   | 小车右旋 | コマンド | 好的,正在向右旋转 | 能動 | FE EF 00 09 EE | FE EF 00 09 EE |

- 「命令词播报词协议列表V1\_中文」ファイルに従って対応するコマンドを入力すると、音声モジュールは対応するプロトコルのテキストを読み上げます。

| 84   | 这是红色                  | コマンド | 这是红色                  | 受動 | FE EF FF 5F EE | FE EF FF 5F EE |
| ---- | ------------------------- | ------- | ------------------------- | ------- | -------------- | -------------- |
| 85   | 这是蓝色                  | コマンド | 这是蓝色                  | 受動 | FE EF FF 60 EE | FE EF FF 60 EE |
| 86   | 这是绿色                  | コマンド | 这是绿色                  | 受動 | FE EF FF 61 EE | FE EF FF 61 EE |
| 87   | 这是黄色                  | コマンド | 这是黄色                  | 受動 | FE EF FF 62 EE | FE EF FF 62 EE |
| 88   | 识别到黄色                | コマンド | 识别到黄色                | 受動 | FE EF FF 63 EE | FE EF FF 63 EE |
| 89   | 识别到绿色                | コマンド | 识别到绿色                | 受動 | FE EF FF 64 EE | FE EF FF 64 EE |
| 90   | 识别到蓝色                | コマンド | 识别到蓝色                | 受動 | FE EF FF 65 EE | FE EF FF 65 EE |
| 91   | 识别到红色                | コマンド | 识别到红色                | 受動 | FE EF FF 66 EE | FE EF FF 66 EE |
| 92   | 初始化完成                | コマンド | 初始化完成                | 受動 | FE EF FF 67 EE | FE EF FF 67 EE |
| 93   | 第一个要排序的颜色是      | コマンド | 第一个要排序的颜色是      | 受動 | FE EF FF 68 EE | FE EF FF 68 EE |
| 94   | 第二个要排序的颜色是      | コマンド | 第二个要排序的颜色是      | 受動 | FE EF FF 69 EE | FE EF FF 69 EE |
| 95   | 第三个要排序的颜色是      | コマンド | 第三个要排序的颜色是      | 受動 | FE EF FF 6A EE | FE EF FF 6A EE |
| 96   | 第四个要排序的颜色是      | コマンド | 第四个要排序的颜色是      | 受動 | FE EF FF 6B EE | FE EF FF 6B EE |
| 97   | 这是易拉罐,属于可回收垃圾 | コマンド | 这是易拉罐,属于可回收垃圾 | 受動 | FE EF FF 6C EE | FE EF FF 6C EE |

![5](../../en/07-pc-serial/images/5.png)

音声モジュールが正常に読み上げるのを聞くことができます。
