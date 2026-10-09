[English](../../en/02-module-overview/module-overview.md) | [Deutsch](../../de/02-module-overview/module-overview.md) | [Español](../../es/02-module-overview/module-overview.md) | [Français](../../fr/02-module-overview/module-overview.md) | Italiano | [日本語](../../ja/02-module-overview/module-overview.md) | [한국어](../../ko/02-module-overview/module-overview.md) | [Português (BR)](../../pt-br/02-module-overview/module-overview.md) | [Português (PT)](../../pt-pt/02-module-overview/module-overview.md) | [简体中文](../../zh-hans/02-module-overview/module-overview.md) | [繁體中文](../../zh-hant/02-module-overview/module-overview.md)

# Informazioni sul prodotto

## 1. Introduzione al modulo di interazione vocale

CI1302 è un chip vocale intelligente di nuova generazione ad alte prestazioni con rete neurale, sviluppato da ChipIntelli. Integra il Brain Neural Network Processor BNPU V3 e il core CPU sviluppati internamente da ChipIntelli, con una frequenza di clock di sistema fino a 220MHz, fino a 640KB di SRAM integrata, unità di gestione dell'alimentazione PMU e oscillatore RC integrati, oltre a un codec audio dual-channel ad alte prestazioni e basso consumo e a numerose interfacce di controllo periferiche come UART, IIC, IIS, PWM, GPIO e PDM. Il chip richiede solo pochi componenti esterni, come resistori e condensatori, per realizzare diverse soluzioni hardware per prodotti vocali intelligenti, offrendo un rapporto qualità-prezzo eccezionale.

Sfruttando la tecnologia hardware BNPU di terza generazione, supporta reti neurali come DNN, TDNN, RNN e CNN, nonché operazioni vettoriali parallele, abilitando funzioni come il riconoscimento vocale, il riconoscimento dell'impronta vocale, l'autoapprendimento delle parole di comando, il rilevamento vocale e la riduzione del rumore tramite deep learning. La soluzione basata su questo chip supporta inoltre numerose lingue globali, tra cui cinese, inglese e giapponese, risultando ampiamente applicabile in elettrodomestici, illuminazione, giocattoli, dispositivi indossabili, ambito industriale, automotive e altri settori per l'interazione vocale, il controllo e varie applicazioni di soluzioni vocali intelligenti.

Il chip CI1302 è dotato di un core Brain Neural Network Processor (BNPU), che supporta il calcolo accelerato di reti neurali offline e l'accelerazione hardware dell'elaborazione dei segnali vocali. La frequenza di clock della CPU raggiunge fino a 220MHz, abilitando il riconoscimento vocale offline a distanza, con 2MB di memoria FLASH integrata che supporta fino a 300 parole di comando.

## 2. Caratteristiche del prodotto

- Precaricato con oltre 110 comandi vocali, con supporto per parole di comando personalizzabili in cinese e inglese.

Gli utenti possono modificare le parole di comando tramite l'interfaccia web che forniamo, generare nuovi file firmware e scrivere il firmware sul modulo tramite il software per PC; successivamente il modulo riconoscerà i nuovi comandi. Lo spazio di memoria integrato da 2MB supporta la scrittura di circa 120 parole di comando.

- Altoparlante ad alta fedeltà e microfono ad alte prestazioni integrati.

Integra algoritmi avanzati e tecnologia di riduzione del rumore dei circuiti per filtrare efficacemente il rumore di fondo ambientale, raggiungendo un tasso di riconoscimento del 99% entro una distanza di 5 metri, consentendo una conversazione naturale e la cancellazione dell'eco. Offre un'uscita audio chiara e riproduce accuratamente i dettagli della voce.

- Coprocessore integrato e interfacce IIC/seriale/UART/Type-C.

Integra il chip STC8H, in grado di convertire automaticamente i dati vocali nei formati seriale o IIC, semplificando il processo di comunicazione con i dispositivi host esterni. Vengono forniti gratuitamente diversi cavi di collegamento, che consentono agli utenti di collegarsi a schede di sviluppo MCU e dispositivi host embedded per abilitare la comunicazione e creare i propri progetti DIY.

- Fornisce tutorial di utilizzo basati su diverse schede di sviluppo.

Fornisce informazioni sulle schede di sviluppo come STM32, ESP32, MSPM0, Raspberry Pi, schede della serie Jetson, RDK e altre. Fornisce inoltre file SDK per i sistemi ROS1 e ROS2.

## 3. Principio di funzionamento

Il modulo adotta una modalità di attivazione tramite parola chiave. L'utente deve pronunciare la parola di risveglio preimpostata per attivare prima il modulo di interazione vocale. Dopo l'attivazione è possibile eseguire il riconoscimento vocale. La parola di risveglio predefinita del firmware di fabbrica è "你好，小犀" (Ciao, Xiao Xi). Se non viene rilevata alcuna voce entro 15 secondi, il modulo entra in modalità riposo e deve essere risvegliato nuovamente per l'uso successivo.

Quando il chip CI1302 riconosce la voce corrispondente, la invia attraverso la porta seriale e l'interfaccia IIC, insieme alla riproduzione di risposta. Il chip IIC memorizza i comandi vocali ricevuti e li invia tramite il protocollo slave IIC.

Il modulo supporta la modifica della parola di risveglio, la modifica delle parole di comando e le voci personalizzate. Puoi imparare come eseguire queste operazioni nei tutorial "Modifica delle parole di risveglio e delle parole di comando" e "Creazione di voci con protocollo personalizzato".

## 4. Precauzioni

1. Utilizzare una tensione di alimentazione di 5V; superare i 5V danneggerà il modulo.
2. L'ambiente d'uso deve essere silenzioso; gli ambienti rumorosi influiscono sulle prestazioni di riconoscimento.
3. Quando si pronunciano le voci, la voce deve essere forte e non troppo veloce. Si consiglia di rimanere entro 5 metri dal modulo.

## 5. Descrizione dell'interfaccia hardware

![2](../../en/02-module-overview/images/2.png)

| N. | Nome hardware         | Descrizione                                                                 |
| --- | --------------------- | --------------------------------------------------------------------------- |
| 1   | Altoparlante          | Converte i segnali analogici in suono                                      |
| 2   | Interruttore a slitta | Commuta la modalità della porta seriale per il flashing del firmware       |
| 3   | Microfono             | Converte il suono in segnali analogici                                     |
| 4   | Pulsante RST          | Pulsante di reset                                                          |
| 5   | Indicatore di alimentazione (blu)| Rimane acceso quando l'alimentazione è regolare                 |
| 6   | Porta Type-C          | Utilizzata per l'alimentazione e per l'aggiornamento e il download del firmware CI1302/STC8 |
| 7   | Chip amplificatore audio | Converte i segnali digitali in segnali analogici per pilotare l'altoparlante |
| 8   | Chip CI1302           | Chip di riconoscimento vocale ad alte prestazioni; riconosce la voce ed emette segnali |
| 9   | Protezione contro l'inversione di polarità | Protezione contro il collegamento inverso di 5V/GND           |
| 10  | Interfaccia IIC       | Funziona come slave per l'alimentazione e la comunicazione con il dispositivo host |
| 11  | Interfaccia seriale   | Porta seriale esterna fornita; consente di controllare la riproduzione tramite protocollo |
| 12  | Chip STC8H            | Converte i comandi del chip vocale in comandi del protocollo IIC e comandi seriali |
