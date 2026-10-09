[English](../../en/05-firmware-flashing/firmware-flashing.md) | [Deutsch](../../de/05-firmware-flashing/firmware-flashing.md) | Español | [Français](../../fr/05-firmware-flashing/firmware-flashing.md) | [Italiano](../../it/05-firmware-flashing/firmware-flashing.md) | [日本語](../../ja/05-firmware-flashing/firmware-flashing.md) | [한국어](../../ko/05-firmware-flashing/firmware-flashing.md) | [Português (BR)](../../pt-br/05-firmware-flashing/firmware-flashing.md) | [Português (PT)](../../pt-pt/05-firmware-flashing/firmware-flashing.md) | [简体中文](../../zh-hans/05-firmware-flashing/firmware-flashing.md) | [繁體中文](../../zh-hant/05-firmware-flashing/firmware-flashing.md)

# Método de flasheo del firmware del módulo

# 1. Pasos de flasheo del chip de voz

# 1.1 Conexión del dispositivo

![1](../../en/05-firmware-flashing/images/1.png)

# 1.2 Abrir el software de flasheo

Abre la carpeta de la herramienta de flasheo del firmware del chip de voz en los archivos adjuntos y haz clic en "PACK\_UPDATE\_TOOL.exe"

![2](../../en/05-firmware-flashing/images/2.png)

Selecciona el chip CI1302 y, a continuación, haz clic en "固件升级" (Actualizar firmware)

![3](../../en/05-firmware-flashing/images/3.png)

Entra en la interfaz de actualización de firmware. Pulsa "F1" para ver la ayuda.

Haz clic para seleccionar el firmware que acabas de crear. Busca el firmware de fábrica "CI1302中文单麦\_V00681\_UART1\_115200\_2M" en los archivos adjuntos.

![4](../../en/05-firmware-flashing/images/4.png)

Selecciona el firmware, busca el número de puerto serie correspondiente y marca la casilla de verificación.

![5](../../en/05-firmware-flashing/images/5.png)

Mueve el interruptor deslizante a la posición "Download". "Download" indica el flasheo del firmware para el chip de voz (es decir, el lado derecho).

![6](../../en/05-firmware-flashing/images/6.png)

Después de mover el interruptor a la posición correspondiente, pulsa el botón RST del módulo de interacción por voz para iniciar el proceso de flasheo. Espera a que el flasheo se complete correctamente y, a continuación, haz clic en "退出" (Salir).

![7](../../en/05-firmware-flashing/images/7.png)

![8](../../en/05-firmware-flashing/images/8.png)

![9](../../en/05-firmware-flashing/images/9.png)
