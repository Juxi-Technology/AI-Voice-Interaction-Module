[English](../../en/03-wake-words/wake-words.md) | [Deutsch](../../de/03-wake-words/wake-words.md) | Español | [Français](../../fr/03-wake-words/wake-words.md) | [Italiano](../../it/03-wake-words/wake-words.md) | [日本語](../../ja/03-wake-words/wake-words.md) | [한국어](../../ko/03-wake-words/wake-words.md) | [Português (BR)](../../pt-br/03-wake-words/wake-words.md) | [Português (PT)](../../pt-pt/03-wake-words/wake-words.md) | [简体中文](../../zh-hans/03-wake-words/wake-words.md) | [繁體中文](../../zh-hant/03-wake-words/wake-words.md)

# Modificación de palabras de activación y palabras de comando

# 1. Precauciones

Modifica las palabras de activación en un entorno silencioso; un entorno ruidoso afectará la precisión de reconocimiento del módulo de interacción por voz.
Al pronunciar las entradas, la voz debe ser fuerte y no demasiado rápida. Se recomienda permanecer a menos de 5 metros del módulo.

# 2. Conexión del dispositivo

![1](../../en/03-wake-words/images/1.png)

# 3. Modificación de las palabras de activación

Di "你好，小犀" (Hola, Xiao Xi) al módulo de interacción por voz para despertarlo. Cuando el módulo responda "我在" (Estoy aquí), indicará que se encuentra actualmente en modo de reconocimiento.
A continuación, di "学习唤醒词" (Aprender palabra de activación) al módulo de interacción por voz. El módulo responderá "说出唤醒词" (Di la palabra de activación), entrando en el estado de la función de aprendizaje de la palabra de activación.
Después, pronuncia al módulo de interacción por voz la palabra de activación deseada. Mantén la palabra de activación lo más corta posible. Aquí usamos "你好，小犀" como ejemplo.
Cuando el módulo de interacción por voz la reconozca correctamente, anunciará "学习成功" (Aprendizaje correcto), lo que indica que la modificación de la palabra de activación se realizó correctamente. En este momento, puedes usar la entrada "你好小犀" para despertar el módulo.

Nota: La palabra de activación "你好，小犀" del firmware de fábrica es la palabra de activación base y no se puede modificar ni eliminar por voz. Solo puede existir una palabra de activación modificada por el usuario a la vez, y coexiste con la palabra de activación base.

# 4. Modificación de las palabras de comando

El firmware de fábrica del módulo de interacción por voz viene precargado con 8 palabras de comando que pueden modificarse por voz, como se muestra a continuación:

| Etiqueta semántica | Comando de aprendizaje               | Indicación de aprendizaje                                                      | Comando de eliminación             |
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

Ejemplo de uso:

Di "你好，小犀" (Hola, Xiao Xi) al módulo de interacción por voz para despertarlo. Cuando el módulo responda "我在" (Estoy aquí), indicará que se encuentra actualmente en modo de reconocimiento.
A continuación, di "学习停车指令" (Aprender comando de aparcar) al módulo de interacción por voz. El módulo responderá "请说指令" (Di el comando), entrando en el estado de la función de aprendizaje de palabras de comando.
Después, pronuncia al módulo de interacción por voz la palabra de comando deseada. Mantén la palabra de comando lo más corta posible. Aquí usamos "前方停车" (Aparcar delante) como ejemplo.
Cuando el módulo de interacción por voz la reconozca correctamente, anunciará "学习成功" (Aprendizaje correcto), lo que indica que la modificación de la palabra de comando se realizó correctamente. En este momento, usar "前方停车" logrará el mismo efecto que la palabra de comando "停车" (Aparcar).
Si necesitas eliminar la entrada "前方停车", basta con decir "删除停车指令" (Eliminar comando de aparcar). Cuando el módulo responda "删除成功" (Eliminación correcta), la entrada se eliminará (esto solo elimina "前方停车", no "停车").

Nota: Las palabras de comando del firmware de fábrica son palabras de comando base y no se pueden modificar ni eliminar por voz. Solo puede existir una palabra de comando modificada por el usuario a la vez, y coexiste con la palabra de comando base.
