[English](../../en/01-quick-start/quick-start.md) | [Deutsch](../../de/01-quick-start/quick-start.md) | [Español](../../es/01-quick-start/quick-start.md) | [Français](../../fr/01-quick-start/quick-start.md) | [Italiano](../../it/01-quick-start/quick-start.md) | [日本語](../../ja/01-quick-start/quick-start.md) | [한국어](../../ko/01-quick-start/quick-start.md) | [Português (BR)](../../pt-br/01-quick-start/quick-start.md) | Português (PT) | [简体中文](../../zh-hans/01-quick-start/quick-start.md) | [繁體中文](../../zh-hant/01-quick-start/quick-start.md)

# Início Rápido

O firmware de fábrica já inclui a funcionalidade de reconhecimento de voz, pelo que os utilizadores podem experimentá-la rapidamente sem gravar qualquer firmware. Se precisar de adicionar entradas de reconhecimento adicionais, gravar outro firmware ou personalizar entradas, consulte o tutorial "3. Criação de Entradas de Protocolo Personalizado" para obter instruções sobre como personalizar entradas.

# 1. Preparação

1. Um cabo de dados Type-C
2. Módulo de interação por voz

# 2. Ligação do Dispositivo

![1](../../en/01-quick-start/images/1.png)

# 3. Reconhecimento de Voz e Reprodução

Depois de alimentar o módulo de interação por voz através de Type-C, acorde o módulo dizendo "你好，小犀" (Olá, Xiao Xi). Após o despertar bem-sucedido, o módulo responderá "我在" (Estou aqui), indicando que se encontra atualmente no estado de reconhecimento de voz. Se nenhuma entrada de comando for reconhecida dentro de 15 segundos, o módulo entra em modo de suspensão e anuncia "我去休息了" (Vou descansar). Para voltar a acordar o módulo, basta dizer novamente a palavra de despertar.

O firmware de fábrica vem com palavras de comando e palavras de reprodução incorporadas. Pode consultar a lista de protocolos nos anexos da documentação fornecidos. A tabela abaixo apresenta um excerto parcial da lista de protocolos de palavras de comando e palavras de reprodução. Pode verificar o tipo de função para ver o que representa cada palavra de comando. As palavras de reprodução marcadas como "passivas" têm de ser acionadas enviando o comando correspondente ao módulo de interação por voz através de uma porta série de PC, de um microcontrolador ou de outro dispositivo anfitrião. Consulte os detalhes abaixo.

Palavras de Função:

| Rótulo Semântico | Palavra de Comando | Tipo de Função | Frase de Reprodução | Modo de Reprodução | Protocolo de Envio | Protocolo de Receção |
| -------------- | ------------ | ------------- | --------------- | ------------- | --------------- | ---------------- |
| 1              | 欢迎语       | Boas-vindas   | 欢迎使用小犀    | Passivo       | FE EF 01 00 EE  | FE EF 01 00 EE   |
| 2              | 休息语       | Suspensão     | 我去休息啦      | Ativo         | FE EF 02 00 EE  | FE EF 02 00 EE   |
| 3              | 你好小犀     | Palavra de Despertar | 我在     | Ativo         | FE EF 03 00 EE  | FE EF 03 00 EE   |
| 4              | 增大音量     | Aumentar Volume | 增大音量      | Ativo         | FE EF 04 00 EE  | FE EF 04 00 EE   |
| 5              | 减小音量     | Diminuir Volume | 减小音量      | Ativo         | FE EF 05 00 EE  | FE EF 05 00 EE   |
| 6              | 最大音量     | Volume Máximo | 最大音量        | Ativo         | FE EF 06 00 EE  | FE EF 06 00 EE   |
| 7              | 中等音量     | Volume Médio  | 中等音量        | Ativo         | FE EF 07 00 EE  | FE EF 07 00 EE   |
| 8              | 最小音量     | Volume Mínimo | 最小音量        | Ativo         | FE EF 08 00 EE  | FE EF 08 00 EE   |
| 9              | 开启播报     | Ativar Reprodução | 开启播报    | Ativo         | FE EF 09 00 EE  | FE EF 09 00 EE   |
| 10             | 关闭播报     | Desativar Reprodução | 关闭播报 | Ativo         | FE EF 0A 00 EE  | FE EF 0A 00 EE   |

Palavras de Comando:

| 11   | 小车停止     | Comando | 好的,已停止           | Ativo | FE EF 00 01 EE | FE EF 00 01 EE |
| ---- | ------------ | ------- | --------------------- | ------ | -------------- | -------------- |
| 12   | 停车         | Comando | 好的,已停止           | Ativo | FE EF 00 02 EE | FE EF 00 02 EE |
| 13   | 小车休眠     | Comando | 好的,已休眠           | Ativo | FE EF 00 03 EE | FE EF 00 03 EE |
| 14   | 小车前进     | Comando | 好的,正在前进         | Ativo | FE EF 00 04 EE | FE EF 00 04 EE |
| 15   | 小车后退     | Comando | 好的,正在后退         | Ativo | FE EF 00 05 EE | FE EF 00 05 EE |
| 16   | 小车左转     | Comando | 好的,正在向左转       | Ativo | FE EF 00 06 EE | FE EF 00 06 EE |
| 17   | 小车右转     | Comando | 好的,正在向右转       | Ativo | FE EF 00 07 EE | FE EF 00 07 EE |
| 18   | 小车左旋     | Comando | 好的,正在向左旋转     | Ativo | FE EF 00 08 EE | FE EF 00 08 EE |
| 19   | 小车右旋     | Comando | 好的,正在向右旋转     | Ativo | FE EF 00 09 EE | FE EF 00 09 EE |
| 20   | 关灯         | Comando | 好的,已关灯           | Ativo | FE EF 00 0A EE | FE EF 00 0A EE |
| 21   | 亮红灯       | Comando | 好的,已亮红灯         | Ativo | FE EF 00 0B EE | FE EF 00 0B EE |
| 22   | 亮绿灯       | Comando | 好的,已亮绿灯         | Ativo | FE EF 00 0C EE | FE EF 00 0C EE |
| 23   | 亮蓝灯       | Comando | 好的,已亮蓝灯         | Ativo | FE EF 00 0D EE | FE EF 00 0D EE |
| 24   | 亮黄灯       | Comando | 好的,已亮黄灯         | Ativo | FE EF 00 0E EE | FE EF 00 0E EE |
| 25   | 打开流水灯   | Comando | 好的,已打开流水灯     | Ativo | FE EF 00 0F EE | FE EF 00 0F EE |
| 26   | 打开渐变灯   | Comando | 好的,已打开渐变灯     | Ativo | FE EF 00 10 EE | FE EF 00 10 EE |
| 27   | 打开呼吸灯   | Comando | 好的,已打开呼吸灯     | Ativo | FE EF 00 11 EE | FE EF 00 11 EE |
| 28   | 显示电量     | Comando | 好的,已显示电量       | Ativo | FE EF 00 12 EE | FE EF 00 12 EE |
| 29   | 导航去一号位 | Comando | 好的,正在去一号位     | Ativo | FE EF 00 13 EE | FE EF 00 13 EE |
| 30   | 导航去二号位 | Comando | 好的,正在去二号位     | Ativo | FE EF 00 14 EE | FE EF 00 14 EE |
| 31   | 导航去三号位 | Comando | 好的,正在去三号位     | Ativo | FE EF 00 15 EE | FE EF 00 15 EE |
| 32   | 导航去四号位 | Comando | 好的,正在去四号位     | Ativo | FE EF 00 20 EE | FE EF 00 20 EE |
| 33   | 回到原点     | Comando | 好的,正在回到原点     | Ativo | FE EF 00 21 EE | FE EF 00 21 EE |
| 34   | 关闭巡线     | Comando | 好的,已关闭巡线功能   | Ativo | FE EF 00 16 EE | FE EF 00 16 EE |
| 35   | 巡红线       | Comando | 好的,已开启巡红线功能 | Ativo | FE EF 00 17 EE | FE EF 00 17 EE |
| 36   | 巡绿线       | Comando | 好的,已开启巡绿线功能 | Ativo | FE EF 00 18 EE | FE EF 00 18 EE |
| 37   | 巡蓝线       | Comando | 好的,已开启巡蓝线功能 | Ativo | FE EF 00 19 EE | FE EF 00 19 EE |
| 38   | 巡黄线       | Comando | 好的,已开启巡黄线功能 | Ativo | FE EF 00 1A EE | FE EF 00 1A EE |
| 39   | 开启跟随     | Comando | 好的,已开启跟随功能   | Ativo | FE EF 00 1B EE | FE EF 00 1B EE |
| 40   | 关闭跟随     | Comando | 好的,已关闭跟随功能   | Ativo | FE EF 00 1C EE | FE EF 00 1C EE |
| 41   | 报警         | Comando | 好的,已开启报警       | Ativo | FE EF 00 26 EE | FE EF 00 26 EE |
| 42   | 向上         | Comando | 好的,已控制向上       | Ativo | FE EF 00 27 EE | FE EF 00 27 EE |
| 43   | 向下         | Comando | 好的,已控制向下       | Ativo | FE EF 00 28 EE | FE EF 00 28 EE |
| 44   | 向左         | Comando | 好的,已控制向左       | Ativo | FE EF 00 29 EE | FE EF 00 29 EE |
| 45   | 向右         | Comando | 好的,已控制向右       | Ativo | FE EF 00 2A EE | FE EF 00 2A EE |
| 46   | 夹紧         | Comando | 好的,已控制夹紧       | Ativo | FE EF 00 2B EE | FE EF 00 2B EE |
| 47   | 松开         | Comando | 好的,已控制松开       | Ativo | FE EF 00 2C EE | FE EF 00 2C EE |

Palavras de Reprodução:

| 84   | 这是红色                    | Comando | 这是红色                    | Passivo | FE EF FF 5F EE | FE EF FF 5F EE |
| ---- | --------------------------- | ------- | --------------------------- | ------- | -------------- | -------------- |
| 85   | 这是蓝色                    | Comando | 这是蓝色                    | Passivo | FE EF FF 60 EE | FE EF FF 60 EE |
| 86   | 这是绿色                    | Comando | 这是绿色                    | Passivo | FE EF FF 61 EE | FE EF FF 61 EE |
| 87   | 这是黄色                    | Comando | 这是黄色                    | Passivo | FE EF FF 62 EE | FE EF FF 62 EE |
| 88   | 识别到黄色                  | Comando | 识别到黄色                  | Passivo | FE EF FF 63 EE | FE EF FF 63 EE |
| 89   | 识别到绿色                  | Comando | 识别到绿色                  | Passivo | FE EF FF 64 EE | FE EF FF 64 EE |
| 90   | 识别到蓝色                  | Comando | 识别到蓝色                  | Passivo | FE EF FF 65 EE | FE EF FF 65 EE |
| 91   | 识别到红色                  | Comando | 识别到红色                  | Passivo | FE EF FF 66 EE | FE EF FF 66 EE |
| 92   | 初始化完成                  | Comando | 初始化完成                  | Passivo | FE EF FF 67 EE | FE EF FF 67 EE |
| 93   | 第一个要排序的颜色是        | Comando | 第一个要排序的颜色是        | Passivo | FE EF FF 68 EE | FE EF FF 68 EE |
| 94   | 第二个要排序的颜色是        | Comando | 第二个要排序的颜色是        | Passivo | FE EF FF 69 EE | FE EF FF 69 EE |
| 95   | 第三个要排序的颜色是        | Comando | 第三个要排序的颜色是        | Passivo | FE EF FF 6A EE | FE EF FF 6A EE |
| 96   | 第四个要排序的颜色是        | Comando | 第四个要排序的颜色是        | Passivo | FE EF FF 6B EE | FE EF FF 6B EE |
| 97   | 这是易拉罐,属于可回收垃圾   | Comando | 这是易拉罐,属于可回收垃圾   | Passivo | FE EF FF 6C EE | FE EF FF 6C EE |
| 98   | 这是旧书包,属于可回收垃圾   | Comando | 这是旧书包,属于可回收垃圾   | Passivo | FE EF FF 6D EE | FE EF FF 6D EE |
| 99   | 这是报纸,属于可回收垃圾     | Comando | 这是报纸,属于可回收垃圾     | Passivo | FE EF FF 6E EE | FE EF FF 6E EE |
| 100  | 这是书本,属于可回收垃圾     | Comando | 这是书本,属于可回收垃圾     | Passivo | FE EF FF 6F EE | FE EF FF 6F EE |
| 101  | 这是注射器,属于有毒垃圾     | Comando | 这是注射器,属于有毒垃圾     | Passivo | FE EF FF 70 EE | FE EF FF 70 EE |
| 102  | 这是废旧电池,属于有毒垃圾   | Comando | 这是废旧电池,属于有毒垃圾   | Passivo | FE EF FF 71 EE | FE EF FF 71 EE |
| 103  | 这是过期化妆品,属于有毒垃圾 | Comando | 这是过期化妆品,属于有毒垃圾 | Passivo | FE EF FF 72 EE | FE EF FF 72 EE |
| 104  | 这是过期药品,属于有毒垃圾   | Comando | 这是过期药品,属于有毒垃圾   | Passivo | FE EF FF 73 EE | FE EF FF 73 EE |
| 105  | 这是鱼骨,属于湿垃圾         | Comando | 这是鱼骨,属于湿垃圾         | Passivo | FE EF FF 74 EE | FE EF FF 74 EE |
| 106  | 这是西瓜皮,属于湿垃圾       | Comando | 这是西瓜皮,属于湿垃圾       | Passivo | FE EF FF 75 EE | FE EF FF 75 EE |
| 107  | 这是苹果核,属于湿垃圾       | Comando | 这是苹果核,属于湿垃圾       | Passivo | FE EF FF 76 EE | FE EF FF 76 EE |
| 108  | 这是鸡蛋壳,属于湿垃圾       | Comando | 这是鸡蛋壳,属于湿垃圾       | Passivo | FE EF FF 77 EE | FE EF FF 77 EE |
| 109  | 这是一次性筷子,属于干垃圾   | Comando | 这是一次性筷子,属于干垃圾   | Passivo | FE EF FF 78 EE | FE EF FF 78 EE |
| 110  | 这是烟蒂,属于干垃圾         | Comando | 这是烟蒂,属于干垃圾         | Passivo | FE EF FF 79 EE | FE EF FF 79 EE |
| 111  | 这是桃核,属于干垃圾         | Comando | 这是桃核,属于干垃圾         | Passivo | FE EF FF 80 EE | FE EF FF 80 EE |
| 112  | 这是卫生纸,属于干垃圾       | Comando | 这是卫生纸,属于干垃圾       | Passivo | FE EF FF 8A EE | FE EF FF 8A EE |

Existem dois modos de reprodução: ativo e passivo.

Reprodução Ativa: quando dizemos a palavra de comando de acordo com a tabela, o módulo reproduz ativamente a frase correspondente. Após acordar, se dissermos "小车前进" (Avançar), o módulo transmite ativamente "好的，正在前进" (OK, a avançar).

Reprodução Passiva: o comando da tabela de protocolo tem de ser enviado ao módulo de voz através da porta série para que o módulo reproduza a frase correspondente. Também pode ser acionada escrevendo os dados de reprodução correspondentes no registo de reprodução passiva através do protocolo IIC. Para mais detalhes, consulte "3. Comunicação Multi-Host".
