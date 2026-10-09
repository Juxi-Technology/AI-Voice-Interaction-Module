[English](../../en/04-custom-protocol/custom-protocol.md) | Deutsch | [Español](../../es/04-custom-protocol/custom-protocol.md) | [Français](../../fr/04-custom-protocol/custom-protocol.md) | [Italiano](../../it/04-custom-protocol/custom-protocol.md) | [日本語](../../ja/04-custom-protocol/custom-protocol.md) | [한국어](../../ko/04-custom-protocol/custom-protocol.md) | [Português (BR)](../../pt-br/04-custom-protocol/custom-protocol.md) | [Português (PT)](../../pt-pt/04-custom-protocol/custom-protocol.md) | [简体中文](../../zh-hans/04-custom-protocol/custom-protocol.md) | [繁體中文](../../zh-hant/04-custom-protocol/custom-protocol.md)

# Benutzerdefinierte Protokolleinträge erstellen

# 1. Erstellen der Voice-Chip-Firmware

# 1.1 Vorsichtsmaßnahmen

Das Modul wird ab Werk bereits mit Spracherkennungs-Firmware geflasht ausgeliefert. In den Dokumentationsanhängen ist zusätzlich die Werks-Firmware enthalten. Wenn Sie die Firmware neu erstellen möchten, können Sie den folgenden Schritten zur Firmware-Erstellung folgen.

# 1.2 Firmware-Erstellung

Öffnen Sie zunächst den Link „启英泰伦语音AI平台“ (ChipIntelli Voice-KI-Plattform), um die Website zur Firmware-Erstellung aufzurufen.
Klicken Sie in der Menüleiste auf „功能开发“ (Funktionsentwicklung) und dann im Bereich Produktentwicklung auf „离线语音识别大模型应用“ (Offline-Spracherkennung mit großem Modell).

![1](../../en/04-custom-protocol/images/1.png)

Nun werden Sie zur Anmeldung aufgefordert. Sie müssen ein Plattformkonto mit Ihren eigenen Angaben registrieren. Für dieses Tutorial haben wir uns bereits vorab registriert. Klicken Sie nach der Anmeldung erneut auf „语音识别固件及SDK开发“ (Entwicklung von Spracherkennungs-Firmware und SDK).

![2](../../en/04-custom-protocol/images/2.png)

Nachdem die Seite weitergeleitet wurde, klicken Sie links auf „新建项目“ (Neues Projekt). Erstellen Sie ein neues Produkt wie unten dargestellt, wobei Produktname und Beschreibung individuell angepasst werden können. Die übrigen Angaben müssen gemäß dem rot umrahmten Inhalt ausgewählt werden. Der Produkttyp sollte „通用->智能中控“ (Allgemein -> Intelligente zentrale Steuerung) sein. Klicken Sie anschließend auf „创建“ (Erstellen).

![3](../../en/04-custom-protocol/images/3.png)

Füllen Sie als Nächstes die grundlegenden Informationen des Projekts aus. Da wir die chinesische Erkennung benötigen, wählen Sie „中文“ (Chinesisch) als Sprachtyp. Wenn eine englische Erkennung erforderlich ist, können Sie die entsprechende Änderung vornehmen. Wählen Sie die übrigen Angaben wie unten dargestellt und klicken Sie dann auf „继续“ (Weiter).

![4](../../en/04-custom-protocol/images/4.png)

Konfigurieren Sie anschließend die Firmware. Hier erläutern wir nur die Teile, die geändert werden müssen. Aktivieren Sie die Option zur Echounterdrückung unter den Algorithmusparametern.

![5](../../en/04-custom-protocol/images/5.png)

Stellen Sie in den Hardwareparametern die Quarzoszillatorquelle auf „内部 RC“ (Interner RC) ein.

![6](../../en/04-custom-protocol/images/6.png)

Stellen Sie in der Konfiguration der Druckausgabe-Schnittstelle (Print-UART) den UART0-Pegel auf die Open-Drain-Funktion ein, die einen externen Pull-up auf 5 V unterstützt.

![7](../../en/04-custom-protocol/images/7.png)

Ändern Sie die Konfiguration der Kommunikations-Schnittstelle: Setzen Sie die Baudrate auf 115200 und konfigurieren Sie den UART1-Pegel auf die Open-Drain-Funktion, die einen externen Pull-up auf 5 V unterstützt. Klicken Sie nach der Konfiguration auf „继续“ (Weiter), um zum nächsten Schritt zu gelangen.

![8](../../en/04-custom-protocol/images/8.png)

Nun gelangen Sie zur Funktion zur Bearbeitung der Befehlswörter. Wählen Sie zunächst die Wiedergabestimme. Hier wählen wir „小蝶-清新女声 Ver.3“ (Xiaodie – Frische Frauenstimme Ver.3).

![9](../../en/04-custom-protocol/images/9.png)

Laden Sie als Nächstes den Anhang mit den Befehlswörtern hoch. Suchen Sie die Tabellendatei „命令词播报词协议列表V1\_中文“ (Protokollliste für Befehlswörter und Wiedergabewörter V1\_Chinesisch) im selben Verzeichnis wie dieses Dokument und ziehen Sie sie direkt in die Webseite, um sie hochzuladen.

![10](../../en/04-custom-protocol/images/10.png)

Nach dem Hochladen der Datei sehen Sie unsere Befehlswortdaten in der Tabelle unten.

![11](../../en/04-custom-protocol/images/11.png)

Aktivieren Sie die Selbstlernfunktion und wählen Sie „指定学习“ (Gezieltes Lernen). Das System erzeugt automatisch 4 Selbstlernbefehle. Wir nehmen hier keine Änderungen vor.

![12](../../en/04-custom-protocol/images/12.png)

Warten Sie nach dem Absenden einige Minuten, bis die Firmware-Erstellung abgeschlossen ist. Klicken Sie anschließend auf „下载固件“ (Firmware herunterladen), um die erstellte Firmware zu erhalten.

![13](../../en/04-custom-protocol/images/13.png)

Die Schritte zum Flashen der Firmware finden Sie unter „4. Methode zum Flashen der Modul-Firmware“.

# 2. Funktionale Einträge ändern

Öffnen Sie die Datei „命令词播报词协议列表V1\_中文“ (Protokollliste für Befehlswörter und Wiedergabewörter V1\_Chinesisch) aus den Anhängen.

![14](../../en/04-custom-protocol/images/14.png)

Suchen Sie die funktionalen Einträge in der Tabelle, das sind die ersten 10 Einträge. Beachten Sie, dass diese 10 funktionalen Einträge feste Einträge sind, die nicht hinzugefügt, sondern nur geändert werden können.

![15](../../en/04-custom-protocol/images/15.png)

Hier nehmen wir das Ändern des Wiedergabesatzes des Weckworts als Beispiel: Ändern Sie die Wiedergabe von „在的“ (Ich bin hier) nach Erkennung von „你好，小犀“ auf „我在“ (Ich bin hier).

![16](../../en/04-custom-protocol/images/16.png)

Speichern Sie nach der Änderung und folgen Sie dann den Schritten in „1.2 Firmware-Erstellung“, um die Tabelle in die Website zu importieren. Wenn Sie bereits einmal Firmware erstellt haben, können Sie im vorherigen Projekt auf die Schaltfläche „继承“ (Übernehmen) klicken, wodurch die Schritte zur Parameterkonfiguration eingespart werden.

![13](../../en/04-custom-protocol/images/13.png)

Nach dem erneuten Erstellen der Firmware müssen Sie die Firmware außerdem auf das Sprachinteraktionsmodul flashen. Dadurch werden die geänderten funktionalen Einträge wirksam.

# 3. Neue Befehlseinträge hinzufügen

Öffnen Sie die Datei „命令词播报词协议列表V1\_中文“ (Protokollliste für Befehlswörter und Wiedergabewörter V1\_Chinesisch) aus den Anhängen.

![14](../../en/04-custom-protocol/images/14.png)

Fügen Sie unten in der Tabelle einen neuen Befehlseintrag hinzu. Hier nehmen wir das Hinzufügen des Befehlsworts „打扫房间“ (Zimmer reinigen) als Beispiel.

![17](../../en/04-custom-protocol/images/17.png)

Hier müssen Sie „命令词“ (Befehlswort) als Funktionstyp auswählen und den Wiedergabemodus auf „主“ (Aktiv) einstellen. So wird nach Erkennung von „打扫房间“ aktiv „好的“ (OK) abgespielt.

![18](../../en/04-custom-protocol/images/18.png)

Betrachten wir nun das Sende-Protokoll. Das 1. und 2. Byte der Daten sind der Datenrahmenkopf und müssen nicht geändert werden. Wenn wir den Funktionstyp als Befehlswort auswählen, muss gemäß dem Sende-Protokoll das 3. Datenbyte „00“ sein. Damit wird unterschieden, ob der Befehl ein „Befehlswort“ oder ein „Wiedergabesatz“ ist.

![19](../../en/04-custom-protocol/images/19.png)

Das 4. Datenbyte ist die Daten-ID des Befehlsworts und ein hexadezimaler Wert. Da die ID des vorherigen Befehlsworts „8B“ war, müssen wir dieses Byte auf „8C“ setzen. In Sonderfällen können Daten-IDs identisch sein, beispielsweise wenn die von zwei Befehlswörtern zurückgegebenen Ergebnisse gleich sind.

![20](../../en/04-custom-protocol/images/20.png)

Das 5. Byte im Protokoll ist fest auf „EE“ eingestellt und muss ebenfalls nicht geändert werden. In der Tabelle sollten Sende-Protokoll und Empfangsprotokoll übereinstimmen.

![21](../../en/04-custom-protocol/images/21.png)

Speichern Sie nach der Änderung und folgen Sie dann den Schritten in „1.2 Firmware-Erstellung“, um die Tabelle in die Website zu importieren. Wenn Sie bereits einmal Firmware erstellt haben, können Sie im vorherigen Projekt auf die Schaltfläche „继承“ (Übernehmen) klicken, wodurch die Schritte zur Parameterkonfiguration eingespart werden.

![13](../../en/04-custom-protocol/images/13.png)

Nach dem erneuten Erstellen der Firmware müssen Sie die Firmware außerdem auf das Sprachinteraktionsmodul flashen. Dadurch wird die Funktion des neuen Befehlseintrags wirksam.

# 4. Neue Wiedergabesätze hinzufügen

Öffnen Sie die Datei „命令词播报词协议列表V1\_中文“ (Protokollliste für Befehlswörter und Wiedergabewörter V1\_Chinesisch) aus den Anhängen.

![14](../../en/04-custom-protocol/images/14.png)

Fügen Sie unten in der Tabelle einen neuen Eintrag hinzu. Hier nehmen wir das Hinzufügen des Wiedergabesatzes „现在是晚上“ (Es ist jetzt Abend) als Beispiel.

![22](../../en/04-custom-protocol/images/22.png)

Hier müssen Sie „播报语“ (Wiedergabesatz) als Funktionstyp auswählen und den Wiedergabemodus auf „被“ (Passiv) einstellen.

![23](../../en/04-custom-protocol/images/23.png)

Betrachten wir nun das Sende-Protokoll. Das 1. und 2. Byte der Daten sind der Datenrahmenkopf und müssen nicht geändert werden. Wenn wir den Funktionstyp als Wiedergabesatz auswählen, muss gemäß dem Sende-Protokoll das 3. Datenbyte „FF“ sein. Damit wird der Befehl als „Wiedergabesatz“ unterschieden.

![24](../../en/04-custom-protocol/images/24.png)

Das 4. Datenbyte ist die Daten-ID des Befehlsworts und ein hexadezimaler Wert. Da die ID des vorherigen Wiedergabesatzes „8B“ war, müssen wir dieses Byte auf „8C“ setzen.

Das 5. Byte im Protokoll ist fest auf „EE“ eingestellt und muss ebenfalls nicht geändert werden. In der Tabelle sollten Sende-Protokoll und Empfangsprotokoll übereinstimmen.

![25](../../en/04-custom-protocol/images/25.png)

Speichern Sie nach der Änderung und folgen Sie dann den Schritten in „1.2 Firmware-Erstellung“, um die Tabelle in die Website zu importieren. Wenn Sie bereits einmal Firmware erstellt haben, können Sie im vorherigen Projekt auf die Schaltfläche „继承“ (Übernehmen) klicken, wodurch die Schritte zur Parameterkonfiguration eingespart werden.

![13](../../en/04-custom-protocol/images/13.png)

Nach dem erneuten Erstellen der Firmware müssen Sie die Firmware außerdem auf das Sprachinteraktionsmodul flashen. Dadurch wird die Funktion des neuen Befehlseintrags wirksam.
