[English](../../en/05-firmware-flashing/firmware-flashing.md) | [Deutsch](../../de/05-firmware-flashing/firmware-flashing.md) | [Español](../../es/05-firmware-flashing/firmware-flashing.md) | Français | [Italiano](../../it/05-firmware-flashing/firmware-flashing.md) | [日本語](../../ja/05-firmware-flashing/firmware-flashing.md) | [한국어](../../ko/05-firmware-flashing/firmware-flashing.md) | [Português (BR)](../../pt-br/05-firmware-flashing/firmware-flashing.md) | [Português (PT)](../../pt-pt/05-firmware-flashing/firmware-flashing.md) | [简体中文](../../zh-hans/05-firmware-flashing/firmware-flashing.md) | [繁體中文](../../zh-hant/05-firmware-flashing/firmware-flashing.md)

# Méthode de flashage du firmware du module

# 1. Étapes de flashage de la puce vocale

# 1.1 Connexion de l'appareil

![1](../../en/05-firmware-flashing/images/1.png)

# 1.2 Ouvrir le logiciel de flashage

Ouvrez le dossier de l'outil de flashage du firmware de la puce vocale dans les pièces jointes et cliquez sur « PACK\_UPDATE\_TOOL.exe »

![2](../../en/05-firmware-flashing/images/2.png)

Sélectionnez la puce CI1302, puis cliquez sur « 固件升级 » (Mise à niveau du firmware)

![3](../../en/05-firmware-flashing/images/3.png)

Vous entrez dans l'interface de mise à niveau du firmware. Appuyez sur « F1 » pour afficher l'aide.

Cliquez pour sélectionner le firmware que vous venez de créer. Trouvez le firmware d'usine « CI1302中文单麦\_V00681\_UART1\_115200\_2M » dans les pièces jointes.

![4](../../en/05-firmware-flashing/images/4.png)

Sélectionnez le firmware, trouvez le numéro de port série correspondant et cochez la case.

![5](../../en/05-firmware-flashing/images/5.png)

Déplacez le commutateur à glissière sur la position « Download ». « Download » indique le flashage du firmware de la puce vocale (c'est-à-dire le côté droit).

![6](../../en/05-firmware-flashing/images/6.png)

Après avoir déplacé le commutateur sur la position correspondante, appuyez sur le bouton RST du module d'interaction vocale pour lancer le processus de flashage. Attendez que le flashage se termine avec succès, puis cliquez sur « 退出 » (Quitter).

![7](../../en/05-firmware-flashing/images/7.png)

![8](../../en/05-firmware-flashing/images/8.png)

![9](../../en/05-firmware-flashing/images/9.png)
