[English](../../en/05-firmware-flashing/firmware-flashing.md) | Deutsch | [Español](../../es/05-firmware-flashing/firmware-flashing.md) | [Français](../../fr/05-firmware-flashing/firmware-flashing.md) | [Italiano](../../it/05-firmware-flashing/firmware-flashing.md) | [日本語](../../ja/05-firmware-flashing/firmware-flashing.md) | [한국어](../../ko/05-firmware-flashing/firmware-flashing.md) | [Português (BR)](../../pt-br/05-firmware-flashing/firmware-flashing.md) | [Português (PT)](../../pt-pt/05-firmware-flashing/firmware-flashing.md) | [简体中文](../../zh-hans/05-firmware-flashing/firmware-flashing.md) | [繁體中文](../../zh-hant/05-firmware-flashing/firmware-flashing.md)

# Methode zum Flashen der Modul-Firmware

# 1. Schritte zum Flashen des Sprachchips

# 1.1 Geräteanschluss

![1](../../en/05-firmware-flashing/images/1.png)

# 1.2 Flashing-Software öffnen

Öffnen Sie in den Anhängen den Ordner mit dem Flashing-Tool für die Sprachchip-Firmware und klicken Sie auf „PACK\_UPDATE\_TOOL.exe“

![2](../../en/05-firmware-flashing/images/2.png)

Wählen Sie den CI1302-Chip aus und klicken Sie dann auf „固件升级“ (Firmware-Upgrade)

![3](../../en/05-firmware-flashing/images/3.png)

Sie gelangen in die Oberfläche für das Firmware-Upgrade. Drücken Sie „F1“, um die Hilfe anzuzeigen.

Klicken Sie, um die soeben erstellte Firmware auszuwählen. Suchen Sie die Werks-Firmware „CI1302中文单麦\_V00681\_UART1\_115200\_2M“ in den Anhängen.

![4](../../en/05-firmware-flashing/images/4.png)

Wählen Sie die Firmware aus, suchen Sie die entsprechende Nummer der seriellen Schnittstelle und setzen Sie das Kontrollkästchen.

![5](../../en/05-firmware-flashing/images/5.png)

Bringen Sie den Schiebeschalter in die Stellung „Download“. „Download“ bedeutet das Flashen der Firmware für den Sprachchip (d. h. die rechte Seite).

![6](../../en/05-firmware-flashing/images/6.png)

Nachdem Sie den Schalter in die entsprechende Stellung gebracht haben, drücken Sie die RST-Taste am Sprachinteraktionsmodul, um den Flashvorgang zu starten. Warten Sie, bis das Flashen erfolgreich abgeschlossen ist, und klicken Sie dann auf „退出“ (Beenden).

![7](../../en/05-firmware-flashing/images/7.png)

![8](../../en/05-firmware-flashing/images/8.png)

![9](../../en/05-firmware-flashing/images/9.png)
