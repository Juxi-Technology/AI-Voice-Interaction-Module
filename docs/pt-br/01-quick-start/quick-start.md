[English](../../en/01-quick-start/quick-start.md) | [Deutsch](../../de/01-quick-start/quick-start.md) | [Español](../../es/01-quick-start/quick-start.md) | [Français](../../fr/01-quick-start/quick-start.md) | [Italiano](../../it/01-quick-start/quick-start.md) | [日本語](../../ja/01-quick-start/quick-start.md) | [한국어](../../ko/01-quick-start/quick-start.md) | Português (BR) | [Português (PT)](../../pt-pt/01-quick-start/quick-start.md) | [简体中文](../../zh-hans/01-quick-start/quick-start.md) | [繁體中文](../../zh-hant/01-quick-start/quick-start.md)

# Início Rápido

O firmware de fábrica já inclui a funcionalidade de reconhecimento de voz, então os usuários podem experimentá-la rapidamente sem gravar firmware. Se você precisar adicionar entradas de reconhecimento adicionais, gravar outro firmware ou personalizar entradas, consulte o tutorial "3. Criação de Entradas de Protocolo Personalizado" para instruções sobre como personalizar entradas.

# 1. Preparação

1. Um cabo de dados Type-C
2. Módulo de interação de voz

# 2. Conexão do Dispositivo

![1](../../en/01-quick-start/images/1.png)

# 3. Reconhecimento de Voz e Reprodução

Após alimentar o módulo de interação de voz via Type-C, ative o módulo dizendo "你好，小犀" (Olá, Xiao Xi). Ao ativar com sucesso, o módulo responderá "我在" (Estou aqui), indicando que ele está atualmente no estado de reconhecimento de voz. Se nenhuma entrada de comando for reconhecida dentro de 15 segundos, o módulo entrará em modo de suspensão e anunciará "我去休息了" (Vou descansar). Para ativar o módulo novamente, basta dizer a palavra de ativação outra vez.

O firmware de fábrica vem com palavras de comando e palavras de reprodução integradas. Você pode consultar a lista de protocolos nos anexos de documentação fornecidos. A tabela abaixo mostra um trecho parcial da lista de protocolos de palavras de comando e palavras de reprodução. Você pode verificar o tipo de função para saber o que cada palavra de comando representa. As palavras de reprodução marcadas como "passive" (passiva) precisam ser acionadas enviando o comando correspondente ao módulo de interação de voz por meio de uma porta serial de PC, microcontrolador ou outro dispositivo host. Veja os detalhes abaixo.

Palavras de Função:

| Rótulo Semântico | Palavra de Comando | Tipo de Função | Frase de Reprodução | Modo de Reprodução | Protocolo de Envio | Protocolo de Recebimento |
| -------------- | ------------ | ------------- | --------------- | ------------- | --------------- | ---------------- |
| 1              | 欢迎语       | Welcome       | 欢迎使用小犀    | Passive       | FE EF 01 00 EE  | FE EF 01 00 EE   |
| 2              | 休息语       | Sleep         | 我去休息啦      | Active        | FE EF 02 00 EE  | FE EF 02 00 EE   |
| 3              | 你好小犀     | Wake Word     | 我在            | Active        | FE EF 03 00 EE  | FE EF 03 00 EE   |
| 4              | 增大音量     | Volume Up     | 增大音量        | Active        | FE EF 04 00 EE  | FE EF 04 00 EE   |
| 5              | 减小音量     | Volume Down   | 减小音量        | Active        | FE EF 05 00 EE  | FE EF 05 00 EE   |
| 6              | 最大音量     | Max Volume    | 最大音量        | Active        | FE EF 06 00 EE  | FE EF 06 00 EE   |
| 7              | 中等音量     | Medium Volume | 中等音量        | Active        | FE EF 07 00 EE  | FE EF 07 00 EE   |
| 8              | 最小音量     | Min Volume    | 最小音量        | Active        | FE EF 08 00 EE  | FE EF 08 00 EE   |
| 9              | 开启播报     | Enable Audio  | 开启播报        | Active        | FE EF 09 00 EE  | FE EF 09 00 EE   |
| 10             | 关闭播报     | Disable Audio | 关闭播报        | Active        | FE EF 0A 00 EE  | FE EF 0A 00 EE   |

Palavras de Comando:

| 11   | 小车停止     | Command | 好的,已停止           | Active | FE EF 00 01 EE | FE EF 00 01 EE |
| ---- | ------------ | ------- | --------------------- | ------ | -------------- | -------------- |
| 12   | 停车         | Command | 好的,已停止           | Active | FE EF 00 02 EE | FE EF 00 02 EE |
| 13   | 小车休眠     | Command | 好的,已休眠           | Active | FE EF 00 03 EE | FE EF 00 03 EE |
| 14   | 小车前进     | Command | 好的,正在前进         | Active | FE EF 00 04 EE | FE EF 00 04 EE |
| 15   | 小车后退     | Command | 好的,正在后退         | Active | FE EF 00 05 EE | FE EF 00 05 EE |
| 16   | 小车左转     | Command | 好的,正在向左转       | Active | FE EF 00 06 EE | FE EF 00 06 EE |
| 17   | 小车右转     | Command | 好的,正在向右转       | Active | FE EF 00 07 EE | FE EF 00 07 EE |
| 18   | 小车左旋     | Command | 好的,正在向左旋转     | Active | FE EF 00 08 EE | FE EF 00 08 EE |
| 19   | 小车右旋     | Command | 好的,正在向右旋转     | Active | FE EF 00 09 EE | FE EF 00 09 EE |
| 20   | 关灯         | Command | 好的,已关灯           | Active | FE EF 00 0A EE | FE EF 00 0A EE |
| 21   | 亮红灯       | Command | 好的,已亮红灯         | Active | FE EF 00 0B EE | FE EF 00 0B EE |
| 22   | 亮绿灯       | Command | 好的,已亮绿灯         | Active | FE EF 00 0C EE | FE EF 00 0C EE |
| 23   | 亮蓝灯       | Command | 好的,已亮蓝灯         | Active | FE EF 00 0D EE | FE EF 00 0D EE |
| 24   | 亮黄灯       | Command | 好的,已亮黄灯         | Active | FE EF 00 0E EE | FE EF 00 0E EE |
| 25   | 打开流水灯   | Command | 好的,已打开流水灯     | Active | FE EF 00 0F EE | FE EF 00 0F EE |
| 26   | 打开渐变灯   | Command | 好的,已打开渐变灯     | Active | FE EF 00 10 EE | FE EF 00 10 EE |
| 27   | 打开呼吸灯   | Command | 好的,已打开呼吸灯     | Active | FE EF 00 11 EE | FE EF 00 11 EE |
| 28   | 显示电量     | Command | 好的,已显示电量       | Active | FE EF 00 12 EE | FE EF 00 12 EE |
| 29   | 导航去一号位 | Command | 好的,正在去一号位     | Active | FE EF 00 13 EE | FE EF 00 13 EE |
| 30   | 导航去二号位 | Command | 好的,正在去二号位     | Active | FE EF 00 14 EE | FE EF 00 14 EE |
| 31   | 导航去三号位 | Command | 好的,正在去三号位     | Active | FE EF 00 15 EE | FE EF 00 15 EE |
| 32   | 导航去四号位 | Command | 好的,正在去四号位     | Active | FE EF 00 20 EE | FE EF 00 20 EE |
| 33   | 回到原点     | Command | 好的,正在回到原点     | Active | FE EF 00 21 EE | FE EF 00 21 EE |
| 34   | 关闭巡线     | Command | 好的,已关闭巡线功能   | Active | FE EF 00 16 EE | FE EF 00 16 EE |
| 35   | 巡红线       | Command | 好的,已开启巡红线功能 | Active | FE EF 00 17 EE | FE EF 00 17 EE |
| 36   | 巡绿线       | Command | 好的,已开启巡绿线功能 | Active | FE EF 00 18 EE | FE EF 00 18 EE |
| 37   | 巡蓝线       | Command | 好的,已开启巡蓝线功能 | Active | FE EF 00 19 EE | FE EF 00 19 EE |
| 38   | 巡黄线       | Command | 好的,已开启巡黄线功能 | Active | FE EF 00 1A EE | FE EF 00 1A EE |
| 39   | 开启跟随     | Command | 好的,已开启跟随功能   | Active | FE EF 00 1B EE | FE EF 00 1B EE |
| 40   | 关闭跟随     | Command | 好的,已关闭跟随功能   | Active | FE EF 00 1C EE | FE EF 00 1C EE |
| 41   | 报警         | Command | 好的,已开启报警       | Active | FE EF 00 26 EE | FE EF 00 26 EE |
| 42   | 向上         | Command | 好的,已控制向上       | Active | FE EF 00 27 EE | FE EF 00 27 EE |
| 43   | 向下         | Command | 好的,已控制向下       | Active | FE EF 00 28 EE | FE EF 00 28 EE |
| 44   | 向左         | Command | 好的,已控制向左       | Active | FE EF 00 29 EE | FE EF 00 29 EE |
| 45   | 向右         | Command | 好的,已控制向右       | Active | FE EF 00 2A EE | FE EF 00 2A EE |
| 46   | 夹紧         | Command | 好的,已控制夹紧       | Active | FE EF 00 2B EE | FE EF 00 2B EE |
| 47   | 松开         | Command | 好的,已控制松开       | Active | FE EF 00 2C EE | FE EF 00 2C EE |

Palavras de Reprodução:

| 84   | 这是红色                    | Command | 这是红色                    | Passive | FE EF FF 5F EE | FE EF FF 5F EE |
| ---- | --------------------------- | ------- | --------------------------- | ------- | -------------- | -------------- |
| 85   | 这是蓝色                    | Command | 这是蓝色                    | Passive | FE EF FF 60 EE | FE EF FF 60 EE |
| 86   | 这是绿色                    | Command | 这是绿色                    | Passive | FE EF FF 61 EE | FE EF FF 61 EE |
| 87   | 这是黄色                    | Command | 这是黄色                    | Passive | FE EF FF 62 EE | FE EF FF 62 EE |
| 88   | 识别到黄色                  | Command | 识别到黄色                  | Passive | FE EF FF 63 EE | FE EF FF 63 EE |
| 89   | 识别到绿色                  | Command | 识别到绿色                  | Passive | FE EF FF 64 EE | FE EF FF 64 EE |
| 90   | 识别到蓝色                  | Command | 识别到蓝色                  | Passive | FE EF FF 65 EE | FE EF FF 65 EE |
| 91   | 识别到红色                  | Command | 识别到红色                  | Passive | FE EF FF 66 EE | FE EF FF 66 EE |
| 92   | 初始化完成                  | Command | 初始化完成                  | Passive | FE EF FF 67 EE | FE EF FF 67 EE |
| 93   | 第一个要排序的颜色是        | Command | 第一个要排序的颜色是        | Passive | FE EF FF 68 EE | FE EF FF 68 EE |
| 94   | 第二个要排序的颜色是        | Command | 第二个要排序的颜色是        | Passive | FE EF FF 69 EE | FE EF FF 69 EE |
| 95   | 第三个要排序的颜色是        | Command | 第三个要排序的颜色是        | Passive | FE EF FF 6A EE | FE EF FF 6A EE |
| 96   | 第四个要排序的颜色是        | Command | 第四个要排序的颜色是        | Passive | FE EF FF 6B EE | FE EF FF 6B EE |
| 97   | 这是易拉罐,属于可回收垃圾   | Command | 这是易拉罐,属于可回收垃圾   | Passive | FE EF FF 6C EE | FE EF FF 6C EE |
| 98   | 这是旧书包,属于可回收垃圾   | Command | 这是旧书包,属于可回收垃圾   | Passive | FE EF FF 6D EE | FE EF FF 6D EE |
| 99   | 这是报纸,属于可回收垃圾     | Command | 这是报纸,属于可回收垃圾     | Passive | FE EF FF 6E EE | FE EF FF 6E EE |
| 100  | 这是书本,属于可回收垃圾     | Command | 这是书本,属于可回收垃圾     | Passive | FE EF FF 6F EE | FE EF FF 6F EE |
| 101  | 这是注射器,属于有毒垃圾     | Command | 这是注射器,属于有毒垃圾     | Passive | FE EF FF 70 EE | FE EF FF 70 EE |
| 102  | 这是废旧电池,属于有毒垃圾   | Command | 这是废旧电池,属于有毒垃圾   | Passive | FE EF FF 71 EE | FE EF FF 71 EE |
| 103  | 这是过期化妆品,属于有毒垃圾 | Command | 这是过期化妆品,属于有毒垃圾 | Passive | FE EF FF 72 EE | FE EF FF 72 EE |
| 104  | 这是过期药品,属于有毒垃圾   | Command | 这是过期药品,属于有毒垃圾   | Passive | FE EF FF 73 EE | FE EF FF 73 EE |
| 105  | 这是鱼骨,属于湿垃圾         | Command | 这是鱼骨,属于湿垃圾         | Passive | FE EF FF 74 EE | FE EF FF 74 EE |
| 106  | 这是西瓜皮,属于湿垃圾       | Command | 这是西瓜皮,属于湿垃圾       | Passive | FE EF FF 75 EE | FE EF FF 75 EE |
| 107  | 这是苹果核,属于湿垃圾       | Command | 这是苹果核,属于湿垃圾       | Passive | FE EF FF 76 EE | FE EF FF 76 EE |
| 108  | 这是鸡蛋壳,属于湿垃圾       | Command | 这是鸡蛋壳,属于湿垃圾       | Passive | FE EF FF 77 EE | FE EF FF 77 EE |
| 109  | 这是一次性筷子,属于干垃圾   | Command | 这是一次性筷子,属于干垃圾   | Passive | FE EF FF 78 EE | FE EF FF 78 EE |
| 110  | 这是烟蒂,属于干垃圾         | Command | 这是烟蒂,属于干垃圾         | Passive | FE EF FF 79 EE | FE EF FF 79 EE |
| 111  | 这是桃核,属于干垃圾         | Command | 这是桃核,属于干垃圾         | Passive | FE EF FF 80 EE | FE EF FF 80 EE |
| 112  | 这是卫生纸,属于干垃圾       | Command | 这是卫生纸,属于干垃圾       | Passive | FE EF FF 8A EE | FE EF FF 8A EE |

Existem dois modos de reprodução: ativo e passivo.

Reprodução Ativa: Quando falamos a palavra de comando conforme a tabela, o módulo reproduz ativamente a frase correspondente. Após a ativação, se dissermos "小车前进" (Avançar), o módulo transmitirá ativamente "好的，正在前进" (OK, avançando).

Reprodução Passiva: O comando da tabela de protocolos deve ser enviado ao módulo de voz pela porta serial para que o módulo reproduza a frase correspondente. Também pode ser acionado escrevendo os dados de reprodução correspondentes no registrador de reprodução passiva por meio do protocolo IIC. Para mais detalhes, consulte "3. Comunicação com Múltiplos Hosts".
