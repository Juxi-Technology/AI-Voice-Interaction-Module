[English](../../en/03-wake-words/wake-words.md) | [Deutsch](../../de/03-wake-words/wake-words.md) | [Español](../../es/03-wake-words/wake-words.md) | [Français](../../fr/03-wake-words/wake-words.md) | [Italiano](../../it/03-wake-words/wake-words.md) | [日本語](../../ja/03-wake-words/wake-words.md) | [한국어](../../ko/03-wake-words/wake-words.md) | [Português (BR)](../../pt-br/03-wake-words/wake-words.md) | Português (PT) | [简体中文](../../zh-hans/03-wake-words/wake-words.md) | [繁體中文](../../zh-hant/03-wake-words/wake-words.md)

# Modificação de Palavras de Despertar e Palavras de Comando

# 1. Precauções

Modifique as palavras de despertar num ambiente silencioso; um ambiente ruidoso afetará a precisão de reconhecimento do módulo de interação por voz.
Ao dizer as entradas, a sua voz deve ser forte e não demasiado rápida. Recomenda-se que se mantenha a menos de 5 metros do módulo.

# 2. Ligação do Dispositivo

![1](../../en/03-wake-words/images/1.png)

# 3. Modificação das Palavras de Despertar

Diga "你好，小犀" (Olá, Xiao Xi) ao módulo de interação por voz para o acordar. Quando o módulo responder "我在" (Estou aqui), isso indica que se encontra atualmente em modo de reconhecimento.
De seguida, diga "学习唤醒词" (Aprender Palavra de Despertar) ao módulo de interação por voz. O módulo responderá "说出唤醒词" (Diga a palavra de despertar), entrando no estado da função de aprendizagem da palavra de despertar.
A seguir, diga a palavra de despertar pretendida ao módulo de interação por voz. Mantenha a palavra de despertar o mais curta possível. Aqui usamos "你好，小犀" como exemplo.
Quando o módulo de interação por voz a reconhecer com sucesso, anunciará "学习成功" (Aprendizagem bem-sucedida), indicando que a modificação da palavra de despertar foi bem-sucedida. Neste momento, pode usar a entrada "你好小犀" para acordar o módulo.

Nota: A palavra de despertar "你好，小犀" no firmware de fábrica é a palavra de despertar base e não pode ser modificada nem eliminada por voz. Só pode existir uma palavra de despertar modificada pelo utilizador de cada vez, e esta coexiste com a palavra de despertar base.

# 4. Modificação das Palavras de Comando

O firmware de fábrica do módulo de interação por voz vem pré-carregado com 8 palavras de comando que podem ser modificadas por voz, como se mostra abaixo:

| Rótulo Semântico | Comando de Aprendizagem        | Aviso de Aprendizagem                                                | Comando de Eliminação      |
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

Exemplo de utilização:

Diga "你好，小犀" (Olá, Xiao Xi) ao módulo de interação por voz para o acordar. Quando o módulo responder "我在" (Estou aqui), isso indica que se encontra atualmente em modo de reconhecimento.
De seguida, diga "学习停车指令" (Aprender Comando de Estacionar) ao módulo de interação por voz. O módulo responderá "请说指令" (Diga o comando), entrando no estado da função de aprendizagem de palavras de comando.
A seguir, diga a palavra de comando pretendida ao módulo de interação por voz. Mantenha a palavra de comando o mais curta possível. Aqui usamos "前方停车" (Estacionar em Frente) como exemplo.
Quando o módulo de interação por voz a reconhecer com sucesso, anunciará "学习成功" (Aprendizagem bem-sucedida), indicando que a modificação da palavra de comando foi bem-sucedida. Neste momento, usar "前方停车" produzirá o mesmo efeito que a palavra de comando "停车" (Estacionar).
Se precisar de eliminar a entrada "前方停车", basta dizer "删除停车指令" (Eliminar Comando de Estacionar). Quando o módulo responder "删除成功" (Eliminação bem-sucedida), a entrada será eliminada (isto elimina apenas "前方停车", não "停车").

Nota: As palavras de comando no firmware de fábrica são palavras de comando base e não podem ser modificadas nem eliminadas por voz. Só pode existir uma palavra de comando modificada pelo utilizador de cada vez, e esta coexiste com a palavra de comando base.
