[English](../../en/05-firmware-flashing/firmware-flashing.md) | [Deutsch](../../de/05-firmware-flashing/firmware-flashing.md) | [Español](../../es/05-firmware-flashing/firmware-flashing.md) | [Français](../../fr/05-firmware-flashing/firmware-flashing.md) | [Italiano](../../it/05-firmware-flashing/firmware-flashing.md) | [日本語](../../ja/05-firmware-flashing/firmware-flashing.md) | [한국어](../../ko/05-firmware-flashing/firmware-flashing.md) | Português (BR) | [Português (PT)](../../pt-pt/05-firmware-flashing/firmware-flashing.md) | [简体中文](../../zh-hans/05-firmware-flashing/firmware-flashing.md) | [繁體中文](../../zh-hant/05-firmware-flashing/firmware-flashing.md)

# Método de Gravação do Firmware do Módulo

# 1. Passos de Gravação do Chip de Voz

# 1.1 Conexão do Dispositivo

![1](../../en/05-firmware-flashing/images/1.png)

# 1.2 Abrir o Software de Gravação

Abra a pasta da ferramenta de gravação do firmware do chip de voz nos anexos e clique em "PACK\_UPDATE\_TOOL.exe"

![2](../../en/05-firmware-flashing/images/2.png)

Selecione o chip CI1302, depois clique em "固件升级" (Atualização de Firmware)

![3](../../en/05-firmware-flashing/images/3.png)

Entre na interface de atualização de firmware. Pressione "F1" para ver a ajuda.

Clique para selecionar o firmware que você acabou de criar. Encontre o firmware de fábrica "CI1302中文单麦\_V00681\_UART1\_115200\_2M" nos anexos.

![4](../../en/05-firmware-flashing/images/4.png)

Selecione o firmware, encontre o número da porta serial correspondente e marque a caixa de seleção.

![5](../../en/05-firmware-flashing/images/5.png)

Mova a chave deslizante para a posição "Download". "Download" indica a gravação do firmware para o chip de voz (ou seja, o lado direito).

![6](../../en/05-firmware-flashing/images/6.png)

Depois de mover a chave para a posição correspondente, pressione o botão RST no módulo de interação de voz para entrar no processo de gravação. Aguarde a gravação ser concluída com sucesso e clique em "退出" (Sair).

![7](../../en/05-firmware-flashing/images/7.png)

![8](../../en/05-firmware-flashing/images/8.png)

![9](../../en/05-firmware-flashing/images/9.png)
