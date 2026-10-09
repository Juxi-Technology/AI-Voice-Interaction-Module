[English](../../en/07-pc-serial/pc-serial.md) | [Deutsch](../../de/07-pc-serial/pc-serial.md) | Español | [Français](../../fr/07-pc-serial/pc-serial.md) | [Italiano](../../it/07-pc-serial/pc-serial.md) | [日本語](../../ja/07-pc-serial/pc-serial.md) | [한국어](../../ko/07-pc-serial/pc-serial.md) | [Português (BR)](../../pt-br/07-pc-serial/pc-serial.md) | [Português (PT)](../../pt-pt/07-pc-serial/pc-serial.md) | [简体中文](../../zh-hans/07-pc-serial/pc-serial.md) | [繁體中文](../../zh-hant/07-pc-serial/pc-serial.md)

# 1. Conexión del dispositivo

Mueve el interruptor deslizante al modo de puerto serie STC8.

![1](../../en/07-pc-serial/images/1.png)

# 2. Abrir el asistente de depuración de puerto serie

- Abre Uart Assistant, selecciona el número de puerto serie correspondiente y establece la velocidad en baudios en 115200.

![2](../../en/07-pc-serial/images/2.png)

- Consulta el archivo "命令词播报词协议列表V1\_中文" (Lista de protocolo de palabras de comando y palabras de reproducción V1\_Chino) del paquete comprimido.

![3](../../en/07-pc-serial/images/3.png)

- Cuando decimos "小车前进" (Avanzar coche), el asistente de depuración de puerto serie imprimirá el protocolo correspondiente.

![4](../../en/07-pc-serial/images/4.png)

| 11   | 小车停止 | Comando | 好的,已停止       | Activo | FE EF 00 01 EE | FE EF 00 01 EE |
| ---- | -------- | ------- | ----------------- | ------ | -------------- | -------------- |
| 12   | 停车     | Comando | 好的,已停止       | Activo | FE EF 00 02 EE | FE EF 00 02 EE |
| 13   | 小车休眠 | Comando | 好的,已休眠       | Activo | FE EF 00 03 EE | FE EF 00 03 EE |
| 14   | 小车前进 | Comando | 好的,正在前进     | Activo | FE EF 00 04 EE | FE EF 00 04 EE |
| 15   | 小车后退 | Comando | 好的,正在后退     | Activo | FE EF 00 05 EE | FE EF 00 05 EE |
| 16   | 小车左转 | Comando | 好的,正在向左转   | Activo | FE EF 00 06 EE | FE EF 00 06 EE |
| 17   | 小车右转 | Comando | 好的,正在向右转   | Activo | FE EF 00 07 EE | FE EF 00 07 EE |
| 18   | 小车左旋 | Comando | 好的,正在向左旋转 | Activo | FE EF 00 08 EE | FE EF 00 08 EE |
| 19   | 小车右旋 | Comando | 好的,正在向右旋转 | Activo | FE EF 00 09 EE | FE EF 00 09 EE |

- Según el archivo "命令词播报词协议列表V1\_中文", introduce el comando correspondiente y el módulo de voz reproducirá el texto del protocolo correspondiente.

| 84   | 这是红色                  | Comando | 这是红色                  | Pasivo | FE EF FF 5F EE | FE EF FF 5F EE |
| ---- | ------------------------- | ------- | ------------------------- | ------- | -------------- | -------------- |
| 85   | 这是蓝色                  | Comando | 这是蓝色                  | Pasivo | FE EF FF 60 EE | FE EF FF 60 EE |
| 86   | 这是绿色                  | Comando | 这是绿色                  | Pasivo | FE EF FF 61 EE | FE EF FF 61 EE |
| 87   | 这是黄色                  | Comando | 这是黄色                  | Pasivo | FE EF FF 62 EE | FE EF FF 62 EE |
| 88   | 识别到黄色                | Comando | 识别到黄色                | Pasivo | FE EF FF 63 EE | FE EF FF 63 EE |
| 89   | 识别到绿色                | Comando | 识别到绿色                | Pasivo | FE EF FF 64 EE | FE EF FF 64 EE |
| 90   | 识别到蓝色                | Comando | 识别到蓝色                | Pasivo | FE EF FF 65 EE | FE EF FF 65 EE |
| 91   | 识别到红色                | Comando | 识别到红色                | Pasivo | FE EF FF 66 EE | FE EF FF 66 EE |
| 92   | 初始化完成                | Comando | 初始化完成                | Pasivo | FE EF FF 67 EE | FE EF FF 67 EE |
| 93   | 第一个要排序的颜色是      | Comando | 第一个要排序的颜色是      | Pasivo | FE EF FF 68 EE | FE EF FF 68 EE |
| 94   | 第二个要排序的颜色是      | Comando | 第二个要排序的颜色是      | Pasivo | FE EF FF 69 EE | FE EF FF 69 EE |
| 95   | 第三个要排序的颜色是      | Comando | 第三个要排序的颜色是      | Pasivo | FE EF FF 6A EE | FE EF FF 6A EE |
| 96   | 第四个要排序的颜色是      | Comando | 第四个要排序的颜色是      | Pasivo | FE EF FF 6B EE | FE EF FF 6B EE |
| 97   | 这是易拉罐,属于可回收垃圾 | Comando | 这是易拉罐,属于可回收垃圾 | Pasivo | FE EF FF 6C EE | FE EF FF 6C EE |

![5](../../en/07-pc-serial/images/5.png)

Puedes oír que el módulo de voz reproduce con normalidad.
