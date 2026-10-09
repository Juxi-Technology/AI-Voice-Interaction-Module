[English](../../en/04-custom-protocol/custom-protocol.md) | [Deutsch](../../de/04-custom-protocol/custom-protocol.md) | [Español](../../es/04-custom-protocol/custom-protocol.md) | [Français](../../fr/04-custom-protocol/custom-protocol.md) | Italiano | [日本語](../../ja/04-custom-protocol/custom-protocol.md) | [한국어](../../ko/04-custom-protocol/custom-protocol.md) | [Português (BR)](../../pt-br/04-custom-protocol/custom-protocol.md) | [Português (PT)](../../pt-pt/04-custom-protocol/custom-protocol.md) | [简体中文](../../zh-hans/04-custom-protocol/custom-protocol.md) | [繁體中文](../../zh-hant/04-custom-protocol/custom-protocol.md)

# Creazione di voci con protocollo personalizzato

# 1. Creazione del firmware del chip vocale

# 1.1 Precauzioni

Il modulo viene fornito dalla fabbrica con il firmware di riconoscimento vocale già flashato. Gli allegati della documentazione forniscono anche il firmware di fabbrica. Se hai bisogno di ricreare il firmware, puoi seguire i passaggi riportati di seguito per la creazione del firmware.

# 1.2 Creazione del firmware

Per prima cosa, apri il link "启英泰伦语音AI平台" (ChipIntelli Voice AI Platform) per accedere al sito web di creazione del firmware.
Clicca su "功能开发" (Sviluppo funzionalità) nella barra dei menu, poi clicca su "离线语音识别大模型应用" (Applicazione con modello di grandi dimensioni per il riconoscimento vocale offline) nella sezione Sviluppo prodotto.

![1](../../en/04-custom-protocol/images/1.png)

A questo punto ti verrà chiesto di effettuare l'accesso. Devi registrare un account sulla piattaforma con i tuoi dati. Per questo tutorial ci siamo già registrati in anticipo. Dopo l'accesso, clicca di nuovo su "语音识别固件及SDK开发" (Sviluppo di firmware e SDK per il riconoscimento vocale).

![2](../../en/04-custom-protocol/images/2.png)

Dopo il reindirizzamento della pagina, clicca su "新建项目" (Nuovo progetto) sul lato sinistro. Crea un nuovo prodotto come mostrato di seguito, dove il nome e la descrizione del prodotto possono essere personalizzati. Le informazioni restanti devono essere selezionate in base al contenuto evidenziato in rosso. Il tipo di prodotto deve essere "通用->智能中控" (Generale -> Controllo centrale intelligente). Al termine clicca su "创建" (Crea).

![3](../../en/04-custom-protocol/images/3.png)

Successivamente, inserisci le informazioni di base del progetto. Poiché abbiamo bisogno del riconoscimento in cinese, seleziona "中文" (Cinese) come tipo di lingua. Se è necessario il riconoscimento in inglese, puoi apportare la modifica corrispondente. Seleziona le altre informazioni come mostrato di seguito, poi clicca su "继续" (Continua).

![4](../../en/04-custom-protocol/images/4.png)

Poi configura il firmware. Qui spiegheremo solo le parti che devono essere modificate. Abilita l'opzione di cancellazione dell'eco sotto i parametri dell'algoritmo.

![5](../../en/04-custom-protocol/images/5.png)

Nei parametri hardware, imposta la sorgente dell'oscillatore a cristallo su "内部 RC" (RC interno).

![6](../../en/04-custom-protocol/images/6.png)

Nella configurazione della porta seriale di stampa, imposta il livello di UART0 sulla funzione open-drain, con supporto per il pull-up esterno a 5V.

![7](../../en/04-custom-protocol/images/7.png)

Modifica la configurazione della porta seriale di comunicazione: imposta il baud rate a 115200 e configura il livello di UART1 sulla funzione open-drain, con supporto per il pull-up esterno a 5V. Dopo la configurazione, clicca su "继续" (Continua) per passare al passaggio successivo.

![8](../../en/04-custom-protocol/images/8.png)

Ora entra nella funzione di modifica delle parole di comando. Per prima cosa, seleziona la voce di riproduzione. Qui scegliamo "小蝶-清新女声 Ver.3" (Xiaodie - Voce femminile fresca Ver.3).

![9](../../en/04-custom-protocol/images/9.png)

Successivamente, carica l'allegato delle parole di comando. Trova il foglio di calcolo "命令词播报词协议列表V1\_中文" (Elenco dei protocolli delle parole di comando e delle parole di riproduzione V1\_Cinese) nella stessa directory di questo documento e trascinalo direttamente nella pagina web per caricarlo.

![10](../../en/04-custom-protocol/images/10.png)

Dopo aver caricato il file, potrai vedere i dati delle nostre parole di comando nella tabella sottostante.

![11](../../en/04-custom-protocol/images/11.png)

Abilita la funzione di autoapprendimento e seleziona "指定学习" (Apprendimento specificato). Il sistema genererà automaticamente 4 comandi di autoapprendimento. Qui non apporteremo alcuna modifica.

![12](../../en/04-custom-protocol/images/12.png)

Dopo l'invio, attendi qualche minuto per il completamento della creazione del firmware. Al termine, clicca su "下载固件" (Scarica firmware) per ottenere il firmware creato.

![13](../../en/04-custom-protocol/images/13.png)

Per i passaggi del flashing del firmware, consulta "4. Metodo di flashing del firmware del modulo".

# 2. Modifica delle voci funzionali

Apri il file "命令词播报词协议列表V1\_中文" (Elenco dei protocolli delle parole di comando e delle parole di riproduzione V1\_Cinese) dagli allegati.

![14](../../en/04-custom-protocol/images/14.png)

Trova le voci funzionali nel foglio di calcolo, ovvero le prime 10 voci. Tieni presente che queste 10 voci funzionali sono voci fisse che non possono essere aggiunte, ma solo modificate.

![15](../../en/04-custom-protocol/images/15.png)

Qui prendiamo come esempio la modifica della frase di riproduzione della parola di risveglio: cambia la riproduzione da "在的" (Sono qui) dopo il riconoscimento di "你好，小犀" in "我在" (Sono qui).

![16](../../en/04-custom-protocol/images/16.png)

Salva dopo la modifica, poi segui i passaggi di "1.2 Creazione del firmware" per importare il foglio di calcolo nel sito web. Se hai già creato il firmware una volta, puoi cliccare sul pulsante "继承" (Eredita) nel progetto precedente, che consente di risparmiare i passaggi di configurazione dei parametri.

![13](../../en/04-custom-protocol/images/13.png)

Dopo aver ricreato il firmware, devi anche eseguire il flashing del firmware sul modulo di interazione vocale. Questo abiliterà le voci funzionali modificate.

# 3. Aggiunta di nuove voci di comando

Apri il file "命令词播报词协议列表V1\_中文" (Elenco dei protocolli delle parole di comando e delle parole di riproduzione V1\_Cinese) dagli allegati.

![14](../../en/04-custom-protocol/images/14.png)

In fondo al foglio di calcolo, aggiungi una nuova voce di comando. Qui prendiamo come esempio l'aggiunta di una parola di comando "打扫房间" (Pulisci la stanza).

![17](../../en/04-custom-protocol/images/17.png)

Qui devi selezionare "命令词" (Parola di comando) per il tipo di funzione e impostare la modalità di riproduzione su "主" (Attiva). In questo modo, dopo il riconoscimento di "打扫房间", verrà riprodotto attivamente "好的" (Bene).

![18](../../en/04-custom-protocol/images/18.png)

Ora cerchiamo di capire il protocollo di invio. Il 1° e il 2° byte dei dati sono l'intestazione del frame dati e non devono essere modificati. Quando selezioniamo il tipo di funzione come parola di comando, secondo il protocollo di invio il 3° byte dei dati deve essere "00". Serve a distinguere se il comando è una "parola di comando" o una "frase di riproduzione".

![19](../../en/04-custom-protocol/images/19.png)

Il 4° byte dei dati è l'ID dati della parola di comando, che è un valore esadecimale. Poiché l'ID della parola di comando precedente era "8B", dobbiamo impostare questo byte su "8C". In casi speciali, gli ID dati possono essere uguali, ad esempio quando i risultati restituiti da due parole di comando sono identici.

![20](../../en/04-custom-protocol/images/20.png)

Il 5° byte del protocollo è fisso a "EE" e anch'esso non deve essere modificato. Nel foglio di calcolo, il protocollo di invio e il protocollo di ricezione devono essere coerenti.

![21](../../en/04-custom-protocol/images/21.png)

Salva dopo la modifica, poi segui i passaggi di "1.2 Creazione del firmware" per importare il foglio di calcolo nel sito web. Se hai già creato il firmware una volta, puoi cliccare sul pulsante "继承" (Eredita) nel progetto precedente, che consente di risparmiare i passaggi di configurazione dei parametri.

![13](../../en/04-custom-protocol/images/13.png)

Dopo aver ricreato il firmware, devi anche eseguire il flashing del firmware sul modulo di interazione vocale. Questo abiliterà la funzione della nuova voce di comando.

# 4. Aggiunta di nuove frasi di riproduzione

Apri il file "命令词播报词协议列表V1\_中文" (Elenco dei protocolli delle parole di comando e delle parole di riproduzione V1\_Cinese) dagli allegati.

![14](../../en/04-custom-protocol/images/14.png)

In fondo al foglio di calcolo, aggiungi una nuova voce. Qui prendiamo come esempio l'aggiunta di una frase di riproduzione "现在是晚上" (Ora è sera).

![22](../../en/04-custom-protocol/images/22.png)

Qui devi selezionare "播报语" (Frase di riproduzione) per il tipo di funzione e impostare la modalità di riproduzione su "被" (Passiva).

![23](../../en/04-custom-protocol/images/23.png)

Ora cerchiamo di capire il protocollo di invio. Il 1° e il 2° byte dei dati sono l'intestazione del frame dati e non devono essere modificati. Quando selezioniamo il tipo di funzione come frase di riproduzione, secondo il protocollo di invio il 3° byte dei dati deve essere "FF". Serve a distinguere il comando come "frase di riproduzione".

![24](../../en/04-custom-protocol/images/24.png)

Il 4° byte dei dati è l'ID dati della parola di comando, che è un valore esadecimale. Poiché l'ID della frase di riproduzione precedente era "8B", dobbiamo impostare questo byte su "8C".

Il 5° byte del protocollo è fisso a "EE" e anch'esso non deve essere modificato. Nel foglio di calcolo, il protocollo di invio e il protocollo di ricezione devono essere coerenti.

![25](../../en/04-custom-protocol/images/25.png)

Salva dopo la modifica, poi segui i passaggi di "1.2 Creazione del firmware" per importare il foglio di calcolo nel sito web. Se hai già creato il firmware una volta, puoi cliccare sul pulsante "继承" (Eredita) nel progetto precedente, che consente di risparmiare i passaggi di configurazione dei parametri.

![13](../../en/04-custom-protocol/images/13.png)

Dopo aver ricreato il firmware, devi anche eseguire il flashing del firmware sul modulo di interazione vocale. Questo abiliterà la funzione della nuova voce di comando.
