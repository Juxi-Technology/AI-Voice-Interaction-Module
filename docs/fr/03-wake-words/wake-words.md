[English](../../en/03-wake-words/wake-words.md) | [Deutsch](../../de/03-wake-words/wake-words.md) | [Español](../../es/03-wake-words/wake-words.md) | Français | [Italiano](../../it/03-wake-words/wake-words.md) | [日本語](../../ja/03-wake-words/wake-words.md) | [한국어](../../ko/03-wake-words/wake-words.md) | [Português (BR)](../../pt-br/03-wake-words/wake-words.md) | [Português (PT)](../../pt-pt/03-wake-words/wake-words.md) | [简体中文](../../zh-hans/03-wake-words/wake-words.md) | [繁體中文](../../zh-hant/03-wake-words/wake-words.md)

# Modification des mots de réveil et des mots de commande

# 1. Précautions

Veuillez modifier les mots de réveil dans un environnement calme ; un environnement bruyant affectera la précision de reconnaissance du module d'interaction vocale.
Lorsque vous prononcez les entrées, votre voix doit être forte et pas trop rapide. Il est recommandé de rester à moins de 5 mètres du module.

# 2. Connexion de l'appareil

![1](../../en/03-wake-words/images/1.png)

# 3. Modification des mots de réveil

Dites « 你好，小犀 » (Bonjour, Xiao Xi) au module d'interaction vocale pour le réveiller. Lorsque le module répond « 我在 » (Je suis là), cela indique qu'il se trouve actuellement en mode reconnaissance.
Dites ensuite « 学习唤醒词 » (Apprendre le mot de réveil) au module d'interaction vocale. Le module répond « 说出唤醒词 » (Prononcez le mot de réveil), entrant dans l'état de la fonction d'apprentissage du mot de réveil.
Prononcez ensuite le mot de réveil souhaité au module d'interaction vocale. Gardez le mot de réveil aussi court que possible. Ici, nous utilisons « 你好，小犀 » comme exemple.
Lorsque le module d'interaction vocale le reconnaît avec succès, il annonce « 学习成功 » (Apprentissage réussi), ce qui indique que la modification du mot de réveil a réussi. À ce stade, vous pouvez utiliser l'entrée « 你好小犀 » pour réveiller le module.

Remarque : le mot de réveil « 你好，小犀 » du firmware d'usine est le mot de réveil de base et ne peut pas être modifié ni supprimé par la voix. Un seul mot de réveil modifié par l'utilisateur peut exister à la fois, et il coexiste avec le mot de réveil de base.

# 4. Modification des mots de commande

Le firmware d'usine du module d'interaction vocale est préchargé avec 8 mots de commande pouvant être modifiés par la voix, comme indiqué ci-dessous :

| Étiquette sémantique | Commande d'apprentissage               | Invite d'apprentissage                                                      | Commande de suppression             |
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

Exemple d'utilisation :

Dites « 你好，小犀 » (Bonjour, Xiao Xi) au module d'interaction vocale pour le réveiller. Lorsque le module répond « 我在 » (Je suis là), cela indique qu'il se trouve actuellement en mode reconnaissance.
Dites ensuite « 学习停车指令 » (Apprendre la commande de stationnement) au module d'interaction vocale. Le module répond « 请说指令 » (Veuillez prononcer la commande), entrant dans l'état de la fonction d'apprentissage du mot de commande.
Prononcez ensuite le mot de commande souhaité au module d'interaction vocale. Gardez le mot de commande aussi court que possible. Ici, nous utilisons « 前方停车 » (Stationner devant) comme exemple.
Lorsque le module d'interaction vocale le reconnaît avec succès, il annonce « 学习成功 » (Apprentissage réussi), ce qui indique que la modification du mot de commande a réussi. À ce stade, utiliser « 前方停车 » produira le même effet que le mot de commande « 停车 » (Stationner).
Si vous devez supprimer l'entrée « 前方停车 », dites simplement « 删除停车指令 » (Supprimer la commande de stationnement). Lorsque le module répond « 删除成功 » (Suppression réussie), l'entrée est supprimée (cela supprime uniquement « 前方停车 », pas « 停车 »).

Remarque : les mots de commande du firmware d'usine sont des mots de commande de base et ne peuvent pas être modifiés ni supprimés par la voix. Un seul mot de commande modifié par l'utilisateur peut exister à la fois, et il coexiste avec le mot de commande de base.
