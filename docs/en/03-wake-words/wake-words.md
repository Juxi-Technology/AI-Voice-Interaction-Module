English | [Deutsch](../../de/03-wake-words/wake-words.md) | [Español](../../es/03-wake-words/wake-words.md) | [Français](../../fr/03-wake-words/wake-words.md) | [Italiano](../../it/03-wake-words/wake-words.md) | [日本語](../../ja/03-wake-words/wake-words.md) | [한국어](../../ko/03-wake-words/wake-words.md) | [Português (BR)](../../pt-br/03-wake-words/wake-words.md) | [Português (PT)](../../pt-pt/03-wake-words/wake-words.md) | [简体中文](../../zh-hans/03-wake-words/wake-words.md) | [繁體中文](../../zh-hant/03-wake-words/wake-words.md)

# Modifying Wake Words and Command Words

# 1. Precautions

Please modify wake words in a quiet environment; noisy surroundings will affect the voice interaction module's recognition accuracy.
When speaking entries, your voice should be loud and not too fast. It is recommended to stay within 5 meters of the module.

# 2. Device Connection

![1](images/1.png)

# 3. Modifying Wake Words

Say "你好，小犀" (Hello, Xiao Xi) to the voice interaction module to wake it up. When the module replies "我在" (I'm here), it indicates that it is currently in recognition mode.
Then say "学习唤醒词" (Learn Wake Word) to the voice interaction module. The module will respond "说出唤醒词" (Speak the wake word), entering the wake word learning function state.
Next, speak the desired wake word to the voice interaction module. Keep the wake word as short as possible. Here we use "你好，小犀" as an example.
When the voice interaction module successfully recognizes it, it will announce "学习成功" (Learning successful), indicating that the wake word modification was successful. At this point, you can use the "你好小犀" entry to wake up the module.

Note: The wake word "你好，小犀" in the factory firmware is the base wake word and cannot be modified or deleted via voice. Only one user-modified wake word can exist at a time and it coexists with the base wake word.

# 4. Modifying Command Words

The voice interaction module's factory firmware comes preloaded with 8 command words that can be modified via voice, as shown below:

| Semantic Label | Learning Command               | Learning Prompt                                                      | Delete Command             |
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

Usage example:

Say "你好，小犀" (Hello, Xiao Xi) to the voice interaction module to wake it up. When the module replies "我在" (I'm here), it indicates that it is currently in recognition mode.
Then say "学习停车指令" (Learn Parking Command) to the voice interaction module. The module will respond "请说指令" (Please speak the command), entering the command word learning function state.
Next, speak the desired command word to the voice interaction module. Keep the command word as short as possible. Here we use "前方停车" (Park Ahead) as an example.
When the voice interaction module successfully recognizes it, it will announce "学习成功" (Learning successful), indicating that the command word modification was successful. At this point, using "前方停车" will achieve the same effect as the "停车" (Park) command word.
If you need to delete the "前方停车" entry, simply say "删除停车指令" (Delete Parking Command). When the module replies "删除成功" (Deletion successful), the entry will be deleted (this only deletes "前方停车", not "停车").

Note: The command words in the factory firmware are base command words and cannot be modified or deleted via voice. Only one user-modified command word can exist at a time and it coexists with the base command word.
