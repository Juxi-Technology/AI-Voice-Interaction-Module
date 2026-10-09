[English](../../en/02-module-overview/module-overview.md) | Deutsch | [Español](../../es/02-module-overview/module-overview.md) | [Français](../../fr/02-module-overview/module-overview.md) | [Italiano](../../it/02-module-overview/module-overview.md) | [日本語](../../ja/02-module-overview/module-overview.md) | [한국어](../../ko/02-module-overview/module-overview.md) | [Português (BR)](../../pt-br/02-module-overview/module-overview.md) | [Português (PT)](../../pt-pt/02-module-overview/module-overview.md) | [简体中文](../../zh-hans/02-module-overview/module-overview.md) | [繁體中文](../../zh-hant/02-module-overview/module-overview.md)

# Produktinformationen

## 1. Einführung in das Sprachinteraktionsmodul

CI1302 ist ein neuartiger, hochleistungsfähiger intelligenter Sprachchip der nächsten Generation mit neuronalem Netzwerk, der von ChipIntelli entwickelt wurde. Er integriert den von ChipIntelli selbst entwickelten Brain Neural Network Processor BNPU V3 sowie einen CPU-Kern, verfügt über eine Systemtaktfrequenz von bis zu 220 MHz und einen integrierten SRAM-Speicher von bis zu 640 KB, enthält eine integrierte PMU-Leistungsverwaltungseinheit und einen RC-Oszillator und bietet einen integrierten Dual-Kanal-Audio-Codec mit hoher Leistung und niedrigem Verbrauch sowie mehrere periphere Steuerschnittstellen wie UART, IIC, IIS, PWM, GPIO und PDM. Der Chip benötigt nur wenige externe Bauteile wie Widerstände und Kondensatoren, um verschiedene Hardwarelösungen für intelligente Sprachprodukte umzusetzen, und bietet damit ein außergewöhnliches Preis-Leistungs-Verhältnis.

Mithilfe der Hardware-BNPU-Technologie der 3. Generation unterstützt er neuronale Netzwerke wie DNN, TDNN, RNN und CNN sowie parallele Vektoroperationen und ermöglicht Funktionen wie Spracherkennung, Stimmerkennung (Voiceprint), Selbstlernen von Befehlswörtern, Spracherkennung (Voice Detection) und Rauschunterdrückung durch Deep Learning. Die Chiplösung unterstützt zudem mehrere Weltsprachen, darunter Chinesisch, Englisch und Japanisch, und ist damit breit einsetzbar in den Bereichen Haushaltsgeräte, Beleuchtung, Spielzeug, tragbare Geräte, Industrie, Automobil und anderen Produktfeldern für Sprachinteraktion, Steuerung und vielfältige intelligente Sprachlösungen.

Der CI1302-Chip verfügt über einen Brain Neural Network Processor-Kern (BNPU), der die Offline-Beschleunigungsberechnung neuronaler Netze und die Hardwarebeschleunigung der Sprachsignalverarbeitung unterstützt. Die CPU-Taktfrequenz erreicht bis zu 220 MHz und ermöglicht die Offline-Fernfeld-Spracherkennung, mit integriertem 2 MB FLASH-Speicher, der bis zu 300 Befehlswörter unterstützt.

## 2. Produktmerkmale

- Vorbestückt mit über 110 Sprachbefehlen, unterstützt anpassbare chinesische und englische Befehlswörter.

Anwender können Befehlswörter über unsere bereitgestellte Weboberfläche ändern, neue Firmware-Dateien erzeugen und die Firmware über eine PC-Software auf das Modul schreiben, wonach das Modul die neuen Befehle erkennt. Der integrierte 2 MB Speicherplatz unterstützt das Schreiben von bis zu etwa 120 Befehlswörtern.

- Integrierter hochwertiger Lautsprecher und leistungsstarkes Mikrofon.

Es integriert fortschrittliche Algorithmen und Schaltungsrauschunterdrückungstechnologie, um Umgebungsgeräusche effektiv herauszufiltern, und erreicht eine Erkennungsrate von 99 % innerhalb einer Reichweite von 5 Metern, was natürliche Konversation und Echounterdrückung ermöglicht. Es liefert eine klare Audioausgabe und gibt Sprachdetails präzise wieder.

- Integrierter Co-Prozessor und Schnittstellen IIC/Seriell/UART/Type-C.

Es integriert den STC8H-Chip, der Sprachdaten automatisch in serielle oder IIC-Datenformate umwandeln kann, was den Kommunikationsprozess mit externen Hostgeräten vereinfacht. Verschiedene Anschlusskabel werden kostenlos bereitgestellt, sodass Anwender MCU-Entwicklungsboards und eingebettete Hostgeräte anschließen können, um zu kommunizieren und eigene DIY-Projekte umzusetzen.

- Bietet Nutzungstutorials für verschiedene Entwicklungsboards.

Stellt Informationen zu Entwicklungsboards wie STM32, ESP32, MSPM0, Raspberry Pi, Entwicklungsboards der Jetson-Serie, RDK usw. bereit. Außerdem werden SDK-Dateien für ROS1- und ROS2-Systeme bereitgestellt.

## 3. Funktionsprinzip

Das Modul verwendet einen Aufweckmodus per Schlüsselwort. Der Anwender muss zunächst das voreingestellte Weckwort aussprechen, um das Sprachinteraktionsmodul zu aktivieren. Nach der Aktivierung kann die Spracherkennung durchgeführt werden. Das standardmäßige Aufweck-Schlüsselwort der Werks-Firmware ist „你好，小犀“ (Hallo, Xiao Xi). Wird innerhalb von 15 Sekunden keine Stimme erkannt, wechselt das Modul in den Schlafmodus und muss für die weitere Nutzung erneut aufgeweckt werden.

Wenn der CI1302-Chip den entsprechenden Spracheintrag erkennt, sendet er ihn über die serielle Schnittstelle und die IIC-Schnittstelle zusammen mit einer Rückmeldungs-Wiedergabe aus. Der IIC-Chip speichert die empfangenen Sprachbefehle und sendet sie über das IIC-Slave-Protokoll aus.

Das Modul unterstützt die Änderung von Weckwörtern, die Änderung von Befehlswörtern und benutzerdefinierte Einträge. Wie Sie dabei vorgehen, erfahren Sie in den Tutorials „Weckwörter und Befehlswörter ändern“ und „Benutzerdefinierte Protokolleinträge erstellen“.

## 4. Vorsichtsmaßnahmen

1. Verwenden Sie zur Stromversorgung eine Spannung von 5 V; eine Überschreitung von 5 V beschädigt das Modul.
2. Die Nutzungsumgebung sollte ruhig sein; laute Umgebungen beeinträchtigen die Erkennungsleistung.
3. Beim Aussprechen von Einträgen sollte die Stimme laut und nicht zu schnell sein. Es wird empfohlen, sich innerhalb von 5 Metern zum Modul aufzuhalten.

## 5. Beschreibung der Hardware-Schnittstellen

![2](../../en/02-module-overview/images/2.png)

| Nr. | Hardware-Name         | Beschreibung                                                                 |
| --- | --------------------- | --------------------------------------------------------------------------- |
| 1   | Lautsprecher          | Wandelt analoge Signale in Schall um                                         |
| 2   | Schiebeschalter       | Schaltet den Modus der seriellen Schnittstelle zum Flashen der Firmware      |
| 3   | Mikrofon              | Wandelt Schall in analoge Signale um                                         |
| 4   | RST-Taste             | Reset-Taste                                                                  |
| 5   | Stromanzeige (Blau)   | Leuchtet dauerhaft bei normaler Stromversorgung                             |
| 6   | Type-C-Anschluss      | Dient zur Stromversorgung sowie zum Aktualisieren und Herunterladen der CI1302/STC8-Firmware |
| 7   | Audioverstärker-Chip  | Wandelt digitale Signale in analoge Signale um, um den Lautsprecher anzusteuern |
| 8   | CI1302-Chip           | Hochleistungs-Spracherkennungschip; erkennt Sprache und gibt Signale aus   |
| 9   | Verpolungsschutz      | Schutz gegen Verpolung von 5V/GND                                          |
| 10  | IIC-Schnittstelle     | Dient als Slave für die Stromversorgung und Kommunikation mit dem Hostgerät |
| 11  | Serielle Schnittstelle | Externe serielle Schnittstelle; Wiedergabe kann per Protokoll gesteuert werden |
| 12  | STC8H-Chip            | Wandelt Befehle des Sprachchips in IIC-Protokollbefehle und serielle Befehle um |
