[English](../../en/03-wake-words/wake-words.md) | Deutsch | [Español](../../es/03-wake-words/wake-words.md) | [Français](../../fr/03-wake-words/wake-words.md) | [Italiano](../../it/03-wake-words/wake-words.md) | [日本語](../../ja/03-wake-words/wake-words.md) | [한국어](../../ko/03-wake-words/wake-words.md) | [Português (BR)](../../pt-br/03-wake-words/wake-words.md) | [Português (PT)](../../pt-pt/03-wake-words/wake-words.md) | [简体中文](../../zh-hans/03-wake-words/wake-words.md) | [繁體中文](../../zh-hant/03-wake-words/wake-words.md)

# Weckwörter und Befehlswörter ändern

# 1. Vorsichtsmaßnahmen

Bitte ändern Sie Weckwörter in einer ruhigen Umgebung; eine laute Umgebung beeinträchtigt die Erkennungsgenauigkeit des Sprachinteraktionsmoduls.
Beim Aussprechen von Einträgen sollte Ihre Stimme laut und nicht zu schnell sein. Es wird empfohlen, sich innerhalb von 5 Metern zum Modul aufzuhalten.

# 2. Geräteanschluss

![1](../../en/03-wake-words/images/1.png)

# 3. Weckwörter ändern

Sagen Sie „你好，小犀“ (Hallo, Xiao Xi) zum Sprachinteraktionsmodul, um es aufzuwecken. Wenn das Modul mit „我在“ (Ich bin hier) antwortet, zeigt dies an, dass es sich derzeit im Erkennungsmodus befindet.
Sagen Sie dann „学习唤醒词“ (Weckwort lernen) zum Sprachinteraktionsmodul. Das Modul antwortet mit „说出唤醒词“ (Sprechen Sie das Weckwort aus) und wechselt in den Zustand der Weckwort-Lernfunktion.
Sprechen Sie als Nächstes das gewünschte Weckwort zum Sprachinteraktionsmodul. Halten Sie das Weckwort so kurz wie möglich. Hier verwenden wir „你好，小犀“ als Beispiel.
Wenn das Sprachinteraktionsmodul es erfolgreich erkennt, sagt es „学习成功“ (Lernen erfolgreich) und zeigt damit an, dass die Änderung des Weckworts erfolgreich war. Anschließend können Sie das Modul mit dem Eintrag „你好小犀“ aufwecken.

Hinweis: Das Weckwort „你好，小犀“ in der Werks-Firmware ist das Basis-Weckwort und kann nicht per Sprache geändert oder gelöscht werden. Es kann jeweils nur ein vom Anwender geändertes Weckwort existieren, und es besteht parallel zum Basis-Weckwort.

# 4. Befehlswörter ändern

Die Werks-Firmware des Sprachinteraktionsmoduls ist mit 8 Befehlswörtern vorbestückt, die per Sprache geändert werden können, wie unten dargestellt:

| Semantisches Label | Lernbefehl               | Lernaufforderung                                                      | Löschbefehl                |
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

Anwendungsbeispiel:

Sagen Sie „你好，小犀“ (Hallo, Xiao Xi) zum Sprachinteraktionsmodul, um es aufzuwecken. Wenn das Modul mit „我在“ (Ich bin hier) antwortet, zeigt dies an, dass es sich derzeit im Erkennungsmodus befindet.
Sagen Sie dann „学习停车指令“ (Parkbefehl lernen) zum Sprachinteraktionsmodul. Das Modul antwortet mit „请说指令“ (Sprechen Sie den Befehl aus) und wechselt in den Zustand der Befehlswort-Lernfunktion.
Sprechen Sie als Nächstes das gewünschte Befehlswort zum Sprachinteraktionsmodul. Halten Sie das Befehlswort so kurz wie möglich. Hier verwenden wir „前方停车“ (Vorne anhalten) als Beispiel.
Wenn das Sprachinteraktionsmodul es erfolgreich erkennt, sagt es „学习成功“ (Lernen erfolgreich) und zeigt damit an, dass die Änderung des Befehlsworts erfolgreich war. Anschließend erzielt die Verwendung von „前方停车“ denselben Effekt wie das Befehlswort „停车“ (Anhalten).
Wenn Sie den Eintrag „前方停车“ löschen möchten, sagen Sie einfach „删除停车指令“ (Parkbefehl löschen). Wenn das Modul mit „删除成功“ (Löschen erfolgreich) antwortet, wird der Eintrag gelöscht (dies löscht nur „前方停车“, nicht „停车“).

Hinweis: Die Befehlswörter in der Werks-Firmware sind Basis-Befehlswörter und können nicht per Sprache geändert oder gelöscht werden. Es kann jeweils nur ein vom Anwender geändertes Befehlswort existieren, und es besteht parallel zum Basis-Befehlswort.
