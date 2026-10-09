[English](../../en/03-wake-words/wake-words.md) | [Deutsch](../../de/03-wake-words/wake-words.md) | [Español](../../es/03-wake-words/wake-words.md) | [Français](../../fr/03-wake-words/wake-words.md) | [Italiano](../../it/03-wake-words/wake-words.md) | [日本語](../../ja/03-wake-words/wake-words.md) | [한국어](../../ko/03-wake-words/wake-words.md) | Português (BR) | [Português (PT)](../../pt-pt/03-wake-words/wake-words.md) | [简体中文](../../zh-hans/03-wake-words/wake-words.md) | [繁體中文](../../zh-hant/03-wake-words/wake-words.md)

# Modificação de Palavras de Ativação e Palavras de Comando

# 1. Precauções

Modifique as palavras de ativação em um ambiente silencioso; arredores ruidosos afetarão a precisão de reconhecimento do módulo de interação de voz.
Ao falar as entradas, sua voz deve ser alta e não muito rápida. Recomenda-se permanecer a até 5 metros do módulo.

# 2. Conexão do Dispositivo

![1](../../en/03-wake-words/images/1.png)

# 3. Modificação de Palavras de Ativação

Diga "你好，小犀" (Olá, Xiao Xi) ao módulo de interação de voz para ativá-lo. Quando o módulo responder "我在" (Estou aqui), isso indica que ele está atualmente em modo de reconhecimento.
Em seguida, diga "学习唤醒词" (Aprender Palavra de Ativação) ao módulo de interação de voz. O módulo responderá "说出唤醒词" (Diga a palavra de ativação), entrando no estado de função de aprendizagem da palavra de ativação.
A seguir, fale a palavra de ativação desejada ao módulo de interação de voz. Mantenha a palavra de ativação o mais curta possível. Aqui usamos "你好，小犀" como exemplo.
Quando o módulo de interação de voz a reconhecer com sucesso, ele anunciará "学习成功" (Aprendizagem bem-sucedida), indicando que a modificação da palavra de ativação foi bem-sucedida. Nesse momento, você pode usar a entrada "你好小犀" para ativar o módulo.

Observação: A palavra de ativação "你好，小犀" no firmware de fábrica é a palavra de ativação base e não pode ser modificada nem excluída por voz. Só pode existir uma palavra de ativação modificada pelo usuário por vez, e ela coexiste com a palavra de ativação base.

# 4. Modificação de Palavras de Comando

O firmware de fábrica do módulo de interação de voz vem pré-carregado com 8 palavras de comando que podem ser modificadas por voz, conforme mostrado abaixo:

| Rótulo Semântico | Comando de Aprendizagem               | Prompt de Aprendizagem                                                      | Comando de Exclusão             |
| -------------- | ------------------------------- | -------------------------------------------------------------------- | -------------------------- |
| 3              | 学习唤醒词                      | 请在安静环境下，说出你要学习的唤醒词                                  | 删除唤醒词                 |
| 11             | 学习小车停止指令                | 请说小车停止的指令                                                    | 删除小车停止指令           |
| 12             | 学习停车指令                    | 请说停车的指令                                                        | 删除停车指令               |
| 13             | 学习小车休眠指令                | 请说小车休眠的指令                                                    | 删除小车休眠指令           |
| 15             | 学习小车后退指令                | 请说小车后退的指令                                                    | 删除小车后退指令           |
| 29             | 学习导航去一号位指令            | 请说出一号位指令                                                      | 删除一号位指令             |
| 30             | 学习导航去二号位指令            | 请说出二号位指令                                                      | 删除二号位指令             |
| 31             | 学习导航去三号位指令            | 请说出三号位指令                                                      | 删除三号位指令             |
| 32             | 学习导航去四号位指令            | 请说出四号位指令                                                      | 删除四号位指令             |

Exemplo de uso:

Diga "你好，小犀" (Olá, Xiao Xi) ao módulo de interação de voz para ativá-lo. Quando o módulo responder "我在" (Estou aqui), isso indica que ele está atualmente em modo de reconhecimento.
Em seguida, diga "学习停车指令" (Aprender Comando de Estacionar) ao módulo de interação de voz. O módulo responderá "请说指令" (Diga o comando), entrando no estado de função de aprendizagem de palavras de comando.
A seguir, fale a palavra de comando desejada ao módulo de interação de voz. Mantenha a palavra de comando o mais curta possível. Aqui usamos "前方停车" (Estacionar Adiante) como exemplo.
Quando o módulo de interação de voz a reconhecer com sucesso, ele anunciará "学习成功" (Aprendizagem bem-sucedida), indicando que a modificação da palavra de comando foi bem-sucedida. Nesse momento, usar "前方停车" produzirá o mesmo efeito que a palavra de comando "停车" (Estacionar).
Se você precisar excluir a entrada "前方停车", basta dizer "删除停车指令" (Excluir Comando de Estacionar). Quando o módulo responder "删除成功" (Exclusão bem-sucedida), a entrada será excluída (isso exclui apenas "前方停车", não "停车").

Observação: As palavras de comando no firmware de fábrica são palavras de comando base e não podem ser modificadas nem excluídas por voz. Só pode existir uma palavra de comando modificada pelo usuário por vez, e ela coexiste com a palavra de comando base.
