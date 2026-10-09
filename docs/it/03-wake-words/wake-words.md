[English](../../en/03-wake-words/wake-words.md) | [Deutsch](../../de/03-wake-words/wake-words.md) | [Español](../../es/03-wake-words/wake-words.md) | [Français](../../fr/03-wake-words/wake-words.md) | Italiano | [日本語](../../ja/03-wake-words/wake-words.md) | [한국어](../../ko/03-wake-words/wake-words.md) | [Português (BR)](../../pt-br/03-wake-words/wake-words.md) | [Português (PT)](../../pt-pt/03-wake-words/wake-words.md) | [简体中文](../../zh-hans/03-wake-words/wake-words.md) | [繁體中文](../../zh-hant/03-wake-words/wake-words.md)

# Modifica delle parole di risveglio e delle parole di comando

# 1. Precauzioni

Ti preghiamo di modificare le parole di risveglio in un ambiente silenzioso; un ambiente rumoroso influisce sulla precisione di riconoscimento del modulo di interazione vocale.
Quando si pronunciano le voci, la voce deve essere forte e non troppo veloce. Si consiglia di rimanere entro 5 metri dal modulo.

# 2. Collegamento del dispositivo

![1](../../en/03-wake-words/images/1.png)

# 3. Modifica delle parole di risveglio

Di' "你好，小犀" (Ciao, Xiao Xi) al modulo di interazione vocale per risvegliarlo. Quando il modulo risponde "我在" (Sono qui), significa che si trova attualmente in modalità di riconoscimento.
Poi di' "学习唤醒词" (Impara la parola di risveglio) al modulo di interazione vocale. Il modulo risponderà "说出唤醒词" (Pronuncia la parola di risveglio), entrando nello stato della funzione di apprendimento della parola di risveglio.
Successivamente, pronuncia la parola di risveglio desiderata al modulo di interazione vocale. Mantieni la parola di risveglio il più breve possibile. Qui usiamo "你好，小犀" come esempio.
Quando il modulo di interazione vocale la riconosce correttamente, annuncerà "学习成功" (Apprendimento riuscito), indicando che la modifica della parola di risveglio è andata a buon fine. A questo punto, puoi usare la voce "你好小犀" per risvegliare il modulo.

Nota: la parola di risveglio "你好，小犀" nel firmware di fabbrica è la parola di risveglio di base e non può essere modificata né eliminata tramite voce. Può esistere una sola parola di risveglio modificata dall'utente alla volta e coesiste con la parola di risveglio di base.

# 4. Modifica delle parole di comando

Il firmware di fabbrica del modulo di interazione vocale è precaricato con 8 parole di comando modificabili tramite voce, come mostrato di seguito:

| Etichetta semantica | Comando di apprendimento       | Messaggio di apprendimento                                          | Comando di eliminazione    |
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

Esempio d'uso:

Di' "你好，小犀" (Ciao, Xiao Xi) al modulo di interazione vocale per risvegliarlo. Quando il modulo risponde "我在" (Sono qui), significa che si trova attualmente in modalità di riconoscimento.
Poi di' "学习停车指令" (Impara il comando di parcheggio) al modulo di interazione vocale. Il modulo risponderà "请说指令" (Pronuncia il comando), entrando nello stato della funzione di apprendimento delle parole di comando.
Successivamente, pronuncia la parola di comando desiderata al modulo di interazione vocale. Mantieni la parola di comando il più breve possibile. Qui usiamo "前方停车" (Parcheggio davanti) come esempio.
Quando il modulo di interazione vocale la riconosce correttamente, annuncerà "学习成功" (Apprendimento riuscito), indicando che la modifica della parola di comando è andata a buon fine. A questo punto, usare "前方停车" produrrà lo stesso effetto della parola di comando "停车" (Parcheggio).
Se hai bisogno di eliminare la voce "前方停车", di' semplicemente "删除停车指令" (Elimina il comando di parcheggio). Quando il modulo risponde "删除成功" (Eliminazione riuscita), la voce verrà eliminata (questo elimina solo "前方停车", non "停车").

Nota: le parole di comando nel firmware di fabbrica sono parole di comando di base e non possono essere modificate né eliminate tramite voce. Può esistere una sola parola di comando modificata dall'utente alla volta e coesiste con la parola di comando di base.
