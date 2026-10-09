[English](../../en/05-firmware-flashing/firmware-flashing.md) | [Deutsch](../../de/05-firmware-flashing/firmware-flashing.md) | [Español](../../es/05-firmware-flashing/firmware-flashing.md) | [Français](../../fr/05-firmware-flashing/firmware-flashing.md) | [Italiano](../../it/05-firmware-flashing/firmware-flashing.md) | 日本語 | [한국어](../../ko/05-firmware-flashing/firmware-flashing.md) | [Português (BR)](../../pt-br/05-firmware-flashing/firmware-flashing.md) | [Português (PT)](../../pt-pt/05-firmware-flashing/firmware-flashing.md) | [简体中文](../../zh-hans/05-firmware-flashing/firmware-flashing.md) | [繁體中文](../../zh-hant/05-firmware-flashing/firmware-flashing.md)

# モジュールファームウェアの書き込み方法

# 1. 音声チップの書き込み手順

# 1.1 デバイスの接続

![1](../../en/05-firmware-flashing/images/1.png)

# 1.2 書き込みソフトウェアを開く

添付ファイルの音声チップファームウェア書き込みツールフォルダを開き、「PACK\_UPDATE\_TOOL.exe」をクリックします

![2](../../en/05-firmware-flashing/images/2.png)

CI1302 チップを選択し、「固件升级」（ファームウェアアップグレード）をクリックします

![3](../../en/05-firmware-flashing/images/3.png)

ファームウェアアップグレード画面に入ります。"F1" を押すとヘルプを表示します。

クリックして、作成したファームウェアを選択します。添付ファイル内の出荷時ファームウェア「CI1302中文单麦\_V00681\_UART1\_115200\_2M」を見つけます。

![4](../../en/05-firmware-flashing/images/4.png)

ファームウェアを選択し、対応するシリアルポート番号を見つけて、チェックボックスにチェックを入れます。

![5](../../en/05-firmware-flashing/images/5.png)

スライドスイッチを "Download" の位置に移動します。"Download" は音声チップにファームウェアを書き込むこと（つまり右側）を表します。

![6](../../en/05-firmware-flashing/images/6.png)

スイッチを対応する位置に移動した後、音声対話モジュールの RST ボタンを押して書き込みプロセスに入ります。書き込みが正常に完了するのを待ち、その後「退出」（終了）をクリックします。

![7](../../en/05-firmware-flashing/images/7.png)

![8](../../en/05-firmware-flashing/images/8.png)

![9](../../en/05-firmware-flashing/images/9.png)
