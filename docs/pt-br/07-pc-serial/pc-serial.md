[English](../../en/07-pc-serial/pc-serial.md) | [Deutsch](../../de/07-pc-serial/pc-serial.md) | [Español](../../es/07-pc-serial/pc-serial.md) | [Français](../../fr/07-pc-serial/pc-serial.md) | [Italiano](../../it/07-pc-serial/pc-serial.md) | [日本語](../../ja/07-pc-serial/pc-serial.md) | [한국어](../../ko/07-pc-serial/pc-serial.md) | Português (BR) | [Português (PT)](../../pt-pt/07-pc-serial/pc-serial.md) | [简体中文](../../zh-hans/07-pc-serial/pc-serial.md) | [繁體中文](../../zh-hant/07-pc-serial/pc-serial.md)

# 1. Conexão do Dispositivo

Mova a chave deslizante para o modo de porta serial STC8.

![1](../../en/07-pc-serial/images/1.png)

# 2. Abrir o Assistente de Depuração Serial

- Abra o Uart Assistant, selecione o número da porta serial correspondente e defina a taxa de transmissão (baud rate) como 115200.

![2](../../en/07-pc-serial/images/2.png)

- Consulte o arquivo "命令词播报词协议列表V1\_中文" (Lista de Protocolos de Palavras de Comando e Palavras de Reprodução V1\_Chinês) no pacote.

![3](../../en/07-pc-serial/images/3.png)

- Quando dissermos "小车前进" (Avançar), o assistente de depuração serial imprimirá o protocolo correspondente.

![4](../../en/07-pc-serial/images/4.png)

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

- De acordo com o arquivo "命令词播报词协议列表V1\_中文", insira o comando correspondente e o módulo de voz reproduzirá o texto do protocolo correspondente.

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

![5](../../en/07-pc-serial/images/5.png)

Você poderá ouvir o módulo de voz reproduzindo normalmente.
