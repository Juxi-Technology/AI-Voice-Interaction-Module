[English](../../en/01-quick-start/quick-start.md) | [Deutsch](../../de/01-quick-start/quick-start.md) | Español | [Français](../../fr/01-quick-start/quick-start.md) | [Italiano](../../it/01-quick-start/quick-start.md) | [日本語](../../ja/01-quick-start/quick-start.md) | [한국어](../../ko/01-quick-start/quick-start.md) | [Português (BR)](../../pt-br/01-quick-start/quick-start.md) | [Português (PT)](../../pt-pt/01-quick-start/quick-start.md) | [简体中文](../../zh-hans/01-quick-start/quick-start.md) | [繁體中文](../../zh-hant/01-quick-start/quick-start.md)

# Inicio rápido

El firmware de fábrica ya incluye la funcionalidad de reconocimiento de voz, por lo que los usuarios pueden experimentarla rápidamente sin necesidad de flashearlo. Si necesitas añadir entradas de reconocimiento adicionales, flashear otro firmware o personalizar entradas, consulta el tutorial "3. Creación de entradas de protocolo personalizado" para obtener instrucciones sobre cómo personalizar entradas.

# 1. Preparación

1. Un cable de datos Type-C
2. Módulo de interacción por voz

# 2. Conexión del dispositivo

![1](../../en/01-quick-start/images/1.png)

# 3. Reconocimiento de voz y reproducción

Después de alimentar el módulo de interacción por voz a través de Type-C, despierta el módulo diciendo "你好，小犀" (Hola, Xiao Xi). Si el despertado se realiza correctamente, el módulo responderá "我在" (Estoy aquí), lo que indica que se encuentra actualmente en el estado de reconocimiento de voz. Si no se reconoce ninguna entrada de comando en 15 segundos, el módulo entrará en modo de reposo y anunciará "我去休息了" (Me voy a descansar). Para volver a despertar el módulo, basta con decir de nuevo la palabra de activación.

El firmware de fábrica incluye palabras de comando y palabras de reproducción integradas. Puedes consultar la lista de protocolo en los archivos adjuntos de la documentación. La siguiente tabla muestra un extracto parcial de la lista de protocolo de palabras de comando y palabras de reproducción. Puedes consultar el tipo de función para ver qué representa cada palabra de comando. Las palabras de reproducción marcadas como "pasivo" deben activarse enviando el comando correspondiente al módulo de interacción por voz mediante un puerto serie de PC, un microcontrolador u otro dispositivo host. Consulta los detalles a continuación.

Palabras de función:

| Etiqueta semántica | Palabra de comando | Tipo de función | Frase de reproducción | Modo de reproducción | Protocolo de envío | Protocolo de recepción |
| -------------- | ------------ | ------------- | --------------- | ------------- | --------------- | ---------------- |
| 1              | 欢迎语       | Bienvenida    | 欢迎使用小犀    | Pasivo        | FE EF 01 00 EE  | FE EF 01 00 EE   |
| 2              | 休息语       | Reposo        | 我去休息啦      | Activo        | FE EF 02 00 EE  | FE EF 02 00 EE   |
| 3              | 你好小犀     | Palabra de activación | 我在    | Activo        | FE EF 03 00 EE  | FE EF 03 00 EE   |
| 4              | 增大音量     | Subir volumen | 增大音量        | Activo        | FE EF 04 00 EE  | FE EF 04 00 EE   |
| 5              | 减小音量     | Bajar volumen | 减小音量        | Activo        | FE EF 05 00 EE  | FE EF 05 00 EE   |
| 6              | 最大音量     | Volumen máximo | 最大音量       | Activo        | FE EF 06 00 EE  | FE EF 06 00 EE   |
| 7              | 中等音量     | Volumen medio | 中等音量        | Activo        | FE EF 07 00 EE  | FE EF 07 00 EE   |
| 8              | 最小音量     | Volumen mínimo | 最小音量       | Activo        | FE EF 08 00 EE  | FE EF 08 00 EE   |
| 9              | 开启播报     | Activar reproducción | 开启播报 | Activo       | FE EF 09 00 EE  | FE EF 09 00 EE   |
| 10             | 关闭播报     | Desactivar reproducción | 关闭播报 | Activo   | FE EF 0A 00 EE  | FE EF 0A 00 EE   |

Palabras de comando:

| 11   | 小车停止     | Comando | 好的,已停止           | Activo | FE EF 00 01 EE | FE EF 00 01 EE |
| ---- | ------------ | ------- | --------------------- | ------ | -------------- | -------------- |
| 12   | 停车         | Comando | 好的,已停止           | Activo | FE EF 00 02 EE | FE EF 00 02 EE |
| 13   | 小车休眠     | Comando | 好的,已休眠           | Activo | FE EF 00 03 EE | FE EF 00 03 EE |
| 14   | 小车前进     | Comando | 好的,正在前进         | Activo | FE EF 00 04 EE | FE EF 00 04 EE |
| 15   | 小车后退     | Comando | 好的,正在后退         | Activo | FE EF 00 05 EE | FE EF 00 05 EE |
| 16   | 小车左转     | Comando | 好的,正在向左转       | Activo | FE EF 00 06 EE | FE EF 00 06 EE |
| 17   | 小车右转     | Comando | 好的,正在向右转       | Activo | FE EF 00 07 EE | FE EF 00 07 EE |
| 18   | 小车左旋     | Comando | 好的,正在向左旋转     | Activo | FE EF 00 08 EE | FE EF 00 08 EE |
| 19   | 小车右旋     | Comando | 好的,正在向右旋转     | Activo | FE EF 00 09 EE | FE EF 00 09 EE |
| 20   | 关灯         | Comando | 好的,已关灯           | Activo | FE EF 00 0A EE | FE EF 00 0A EE |
| 21   | 亮红灯       | Comando | 好的,已亮红灯         | Activo | FE EF 00 0B EE | FE EF 00 0B EE |
| 22   | 亮绿灯       | Comando | 好的,已亮绿灯         | Activo | FE EF 00 0C EE | FE EF 00 0C EE |
| 23   | 亮蓝灯       | Comando | 好的,已亮蓝灯         | Activo | FE EF 00 0D EE | FE EF 00 0D EE |
| 24   | 亮黄灯       | Comando | 好的,已亮黄灯         | Activo | FE EF 00 0E EE | FE EF 00 0E EE |
| 25   | 打开流水灯   | Comando | 好的,已打开流水灯     | Activo | FE EF 00 0F EE | FE EF 00 0F EE |
| 26   | 打开渐变灯   | Comando | 好的,已打开渐变灯     | Activo | FE EF 00 10 EE | FE EF 00 10 EE |
| 27   | 打开呼吸灯   | Comando | 好的,已打开呼吸灯     | Activo | FE EF 00 11 EE | FE EF 00 11 EE |
| 28   | 显示电量     | Comando | 好的,已显示电量       | Activo | FE EF 00 12 EE | FE EF 00 12 EE |
| 29   | 导航去一号位 | Comando | 好的,正在去一号位     | Activo | FE EF 00 13 EE | FE EF 00 13 EE |
| 30   | 导航去二号位 | Comando | 好的,正在去二号位     | Activo | FE EF 00 14 EE | FE EF 00 14 EE |
| 31   | 导航去三号位 | Comando | 好的,正在去三号位     | Activo | FE EF 00 15 EE | FE EF 00 15 EE |
| 32   | 导航去四号位 | Comando | 好的,正在去四号位     | Activo | FE EF 00 20 EE | FE EF 00 20 EE |
| 33   | 回到原点     | Comando | 好的,正在回到原点     | Activo | FE EF 00 21 EE | FE EF 00 21 EE |
| 34   | 关闭巡线     | Comando | 好的,已关闭巡线功能   | Activo | FE EF 00 16 EE | FE EF 00 16 EE |
| 35   | 巡红线       | Comando | 好的,已开启巡红线功能 | Activo | FE EF 00 17 EE | FE EF 00 17 EE |
| 36   | 巡绿线       | Comando | 好的,已开启巡绿线功能 | Activo | FE EF 00 18 EE | FE EF 00 18 EE |
| 37   | 巡蓝线       | Comando | 好的,已开启巡蓝线功能 | Activo | FE EF 00 19 EE | FE EF 00 19 EE |
| 38   | 巡黄线       | Comando | 好的,已开启巡黄线功能 | Activo | FE EF 00 1A EE | FE EF 00 1A EE |
| 39   | 开启跟随     | Comando | 好的,已开启跟随功能   | Activo | FE EF 00 1B EE | FE EF 00 1B EE |
| 40   | 关闭跟随     | Comando | 好的,已关闭跟随功能   | Activo | FE EF 00 1C EE | FE EF 00 1C EE |
| 41   | 报警         | Comando | 好的,已开启报警       | Activo | FE EF 00 26 EE | FE EF 00 26 EE |
| 42   | 向上         | Comando | 好的,已控制向上       | Activo | FE EF 00 27 EE | FE EF 00 27 EE |
| 43   | 向下         | Comando | 好的,已控制向下       | Activo | FE EF 00 28 EE | FE EF 00 28 EE |
| 44   | 向左         | Comando | 好的,已控制向左       | Activo | FE EF 00 29 EE | FE EF 00 29 EE |
| 45   | 向右         | Comando | 好的,已控制向右       | Activo | FE EF 00 2A EE | FE EF 00 2A EE |
| 46   | 夹紧         | Comando | 好的,已控制夹紧       | Activo | FE EF 00 2B EE | FE EF 00 2B EE |
| 47   | 松开         | Comando | 好的,已控制松开       | Activo | FE EF 00 2C EE | FE EF 00 2C EE |

Palabras de reproducción:

| 84   | 这是红色                    | Comando | 这是红色                    | Pasivo | FE EF FF 5F EE | FE EF FF 5F EE |
| ---- | --------------------------- | ------- | --------------------------- | ------- | -------------- | -------------- |
| 85   | 这是蓝色                    | Comando | 这是蓝色                    | Pasivo | FE EF FF 60 EE | FE EF FF 60 EE |
| 86   | 这是绿色                    | Comando | 这是绿色                    | Pasivo | FE EF FF 61 EE | FE EF FF 61 EE |
| 87   | 这是黄色                    | Comando | 这是黄色                    | Pasivo | FE EF FF 62 EE | FE EF FF 62 EE |
| 88   | 识别到黄色                  | Comando | 识别到黄色                  | Pasivo | FE EF FF 63 EE | FE EF FF 63 EE |
| 89   | 识别到绿色                  | Comando | 识别到绿色                  | Pasivo | FE EF FF 64 EE | FE EF FF 64 EE |
| 90   | 识别到蓝色                  | Comando | 识别到蓝色                  | Pasivo | FE EF FF 65 EE | FE EF FF 65 EE |
| 91   | 识别到红色                  | Comando | 识别到红色                  | Pasivo | FE EF FF 66 EE | FE EF FF 66 EE |
| 92   | 初始化完成                  | Comando | 初始化完成                  | Pasivo | FE EF FF 67 EE | FE EF FF 67 EE |
| 93   | 第一个要排序的颜色是        | Comando | 第一个要排序的颜色是        | Pasivo | FE EF FF 68 EE | FE EF FF 68 EE |
| 94   | 第二个要排序的颜色是        | Comando | 第二个要排序的颜色是        | Pasivo | FE EF FF 69 EE | FE EF FF 69 EE |
| 95   | 第三个要排序的颜色是        | Comando | 第三个要排序的颜色是        | Pasivo | FE EF FF 6A EE | FE EF FF 6A EE |
| 96   | 第四个要排序的颜色是        | Comando | 第四个要排序的颜色是        | Pasivo | FE EF FF 6B EE | FE EF FF 6B EE |
| 97   | 这是易拉罐,属于可回收垃圾   | Comando | 这是易拉罐,属于可回收垃圾   | Pasivo | FE EF FF 6C EE | FE EF FF 6C EE |
| 98   | 这是旧书包,属于可回收垃圾   | Comando | 这是旧书包,属于可回收垃圾   | Pasivo | FE EF FF 6D EE | FE EF FF 6D EE |
| 99   | 这是报纸,属于可回收垃圾     | Comando | 这是报纸,属于可回收垃圾     | Pasivo | FE EF FF 6E EE | FE EF FF 6E EE |
| 100  | 这是书本,属于可回收垃圾     | Comando | 这是书本,属于可回收垃圾     | Pasivo | FE EF FF 6F EE | FE EF FF 6F EE |
| 101  | 这是注射器,属于有毒垃圾     | Comando | 这是注射器,属于有毒垃圾     | Pasivo | FE EF FF 70 EE | FE EF FF 70 EE |
| 102  | 这是废旧电池,属于有毒垃圾   | Comando | 这是废旧电池,属于有毒垃圾   | Pasivo | FE EF FF 71 EE | FE EF FF 71 EE |
| 103  | 这是过期化妆品,属于有毒垃圾 | Comando | 这是过期化妆品,属于有毒垃圾 | Pasivo | FE EF FF 72 EE | FE EF FF 72 EE |
| 104  | 这是过期药品,属于有毒垃圾   | Comando | 这是过期药品,属于有毒垃圾   | Pasivo | FE EF FF 73 EE | FE EF FF 73 EE |
| 105  | 这是鱼骨,属于湿垃圾         | Comando | 这是鱼骨,属于湿垃圾         | Pasivo | FE EF FF 74 EE | FE EF FF 74 EE |
| 106  | 这是西瓜皮,属于湿垃圾       | Comando | 这是西瓜皮,属于湿垃圾       | Pasivo | FE EF FF 75 EE | FE EF FF 75 EE |
| 107  | 这是苹果核,属于湿垃圾       | Comando | 这是苹果核,属于湿垃圾       | Pasivo | FE EF FF 76 EE | FE EF FF 76 EE |
| 108  | 这是鸡蛋壳,属于湿垃圾       | Comando | 这是鸡蛋壳,属于湿垃圾       | Pasivo | FE EF FF 77 EE | FE EF FF 77 EE |
| 109  | 这是一次性筷子,属于干垃圾   | Comando | 这是一次性筷子,属于干垃圾   | Pasivo | FE EF FF 78 EE | FE EF FF 78 EE |
| 110  | 这是烟蒂,属于干垃圾         | Comando | 这是烟蒂,属于干垃圾         | Pasivo | FE EF FF 79 EE | FE EF FF 79 EE |
| 111  | 这是桃核,属于干垃圾         | Comando | 这是桃核,属于干垃圾         | Pasivo | FE EF FF 80 EE | FE EF FF 80 EE |
| 112  | 这是卫生纸,属于干垃圾       | Comando | 这是卫生纸,属于干垃圾       | Pasivo | FE EF FF 8A EE | FE EF FF 8A EE |

Existen dos modos de reproducción: activo y pasivo.

Reproducción activa: Cuando pronunciamos la palabra de comando según la tabla, el módulo reproducirá activamente la frase correspondiente. Después de despertar, si decimos "小车前进" (Avanzar coche), el módulo emitirá activamente "好的，正在前进" (De acuerdo, avanzando).

Reproducción pasiva: El comando de la tabla de protocolo debe enviarse al módulo de voz a través del puerto serie para que el módulo reproduzca la frase correspondiente. También puede activarse escribiendo los datos de reproducción correspondientes en el registro de reproducción pasiva mediante el protocolo IIC. Para más detalles, consulta "3. Comunicación con múltiples hosts".
