[English](../../en/04-custom-protocol/custom-protocol.md) | [Deutsch](../../de/04-custom-protocol/custom-protocol.md) | [Español](../../es/04-custom-protocol/custom-protocol.md) | [Français](../../fr/04-custom-protocol/custom-protocol.md) | [Italiano](../../it/04-custom-protocol/custom-protocol.md) | [日本語](../../ja/04-custom-protocol/custom-protocol.md) | [한국어](../../ko/04-custom-protocol/custom-protocol.md) | [Português (BR)](../../pt-br/04-custom-protocol/custom-protocol.md) | Português (PT) | [简体中文](../../zh-hans/04-custom-protocol/custom-protocol.md) | [繁體中文](../../zh-hant/04-custom-protocol/custom-protocol.md)

# Criação de Entradas de Protocolo Personalizado

# 1. Criação do Firmware do Chip de Voz

# 1.1 Precauções

O módulo vem com o firmware de reconhecimento de voz gravado de fábrica. Os anexos da documentação também fornecem o firmware de fábrica. Se precisar de recriar o firmware, pode seguir os passos abaixo para a criação do firmware.

# 1.2 Criação do Firmware

Primeiro, abra a ligação "启英泰伦语音AI平台" (Plataforma de IA de Voz ChipIntelli) para aceder ao sítio web de criação de firmware.
Clique em "功能开发" (Desenvolvimento de Funcionalidades) na barra de menu e, em seguida, clique em "离线语音识别大模型应用" (Aplicação de Grande Modelo de Reconhecimento de Voz Offline) na secção Desenvolvimento de Produto.

![1](../../en/04-custom-protocol/images/1.png)

Neste momento, será solicitado que inicie sessão. Precisa de registar uma conta na plataforma com os seus próprios dados. Para este tutorial, já nos registámos previamente. Após iniciar sessão, clique novamente em "语音识别固件及SDK开发" (Desenvolvimento de Firmware e SDK de Reconhecimento de Voz).

![2](../../en/04-custom-protocol/images/2.png)

Após o redirecionamento da página, clique em "新建项目" (Novo Projeto) no lado esquerdo. Crie um novo produto como se mostra abaixo, em que o nome e a descrição do produto podem ser personalizados. As restantes informações têm de ser selecionadas de acordo com o conteúdo realçado a vermelho. O tipo de produto deve ser "通用->智能中控" (Geral -> Controlo Central Inteligente). Clique em "创建" (Criar) quando terminar.

![3](../../en/04-custom-protocol/images/3.png)

De seguida, preencha as informações básicas do projeto. Como precisamos de reconhecimento de chinês, selecione "中文" (Chinês) para o tipo de idioma. Se for necessário reconhecimento de inglês, pode fazer a modificação correspondente. Selecione as restantes informações como se mostra abaixo e clique em "继续" (Continuar).

![4](../../en/04-custom-protocol/images/4.png)

Depois, configure o firmware. Aqui explicaremos apenas as partes que necessitam de modificação. Ative a opção de cancelamento de eco nos parâmetros do algoritmo.

![5](../../en/04-custom-protocol/images/5.png)

Nos parâmetros de hardware, defina a fonte do oscilador de cristal como "内部 RC" (RC Interno).

![6](../../en/04-custom-protocol/images/6.png)

Na configuração da porta série de impressão, defina o nível do UART0 para a função de dreno aberto (open-drain), suportando pull-up externo para 5 V.

![7](../../en/04-custom-protocol/images/7.png)

Modifique a configuração da porta série de comunicação: defina a taxa de transferência (baud rate) para 115200 e configure o nível do UART1 para a função de dreno aberto, suportando pull-up externo para 5 V. Após a configuração, clique em "继续" (Continuar) para avançar para o passo seguinte.

![8](../../en/04-custom-protocol/images/8.png)

Agora entre na função de edição de palavras de comando. Primeiro, selecione a voz de reprodução. Aqui escolhemos "小蝶-清新女声 Ver.3" (Xiaodie - Voz Feminina Fresca Ver.3).

![9](../../en/04-custom-protocol/images/9.png)

De seguida, carregue o anexo das palavras de comando. Encontre a folha de cálculo "命令词播报词协议列表V1\_中文" (Lista de Protocolo de Palavras de Comando e Palavras de Reprodução V1\_Chinês) no mesmo diretório que este documento e arraste-a diretamente para a página web para a carregar.

![10](../../en/04-custom-protocol/images/10.png)

Após carregar o ficheiro, pode ver os dados das nossas palavras de comando na tabela abaixo.

![11](../../en/04-custom-protocol/images/11.png)

Ative a função de autoaprendizagem e selecione "指定学习" (Aprendizagem Especificada). O sistema gerará automaticamente 4 comandos de autoaprendizagem. Não faremos aqui qualquer alteração.

![12](../../en/04-custom-protocol/images/12.png)

Após a submissão, aguarde alguns minutos para a criação do firmware terminar. Quando terminar, clique em "下载固件" (Descarregar Firmware) para obter o firmware criado.

![13](../../en/04-custom-protocol/images/13.png)

Para os passos de gravação do firmware, consulte "4. Método de Gravação do Firmware do Módulo".

# 2. Modificação de Entradas Funcionais

Abra o ficheiro "命令词播报词协议列表V1\_中文" (Lista de Protocolo de Palavras de Comando e Palavras de Reprodução V1\_Chinês) dos anexos.

![14](../../en/04-custom-protocol/images/14.png)

Encontre as entradas funcionais na folha de cálculo, que são as primeiras 10 entradas. Note que estas 10 entradas funcionais são entradas fixas que não podem ser adicionadas, apenas modificadas.

![15](../../en/04-custom-protocol/images/15.png)

Aqui tomamos como exemplo a modificação da frase de reprodução da palavra de despertar: altere a reprodução de "在的" (Estou aqui) após reconhecer "你好，小犀" para "我在" (Estou aqui).

![16](../../en/04-custom-protocol/images/16.png)

Guarde após a modificação e, em seguida, siga os passos de "1.2 Criação do Firmware" para importar a folha de cálculo para o sítio web. Se já criou um firmware uma vez, pode clicar no botão "继承" (Herdar) no projeto anterior, o que permite guardar os passos de configuração de parâmetros.

![13](../../en/04-custom-protocol/images/13.png)

Após recriar o firmware, também precisa de gravar o firmware no módulo de interação por voz. Isto ativará as entradas funcionais modificadas.

# 3. Adição de Novas Entradas de Comando

Abra o ficheiro "命令词播报词协议列表V1\_中文" (Lista de Protocolo de Palavras de Comando e Palavras de Reprodução V1\_Chinês) dos anexos.

![14](../../en/04-custom-protocol/images/14.png)

Na parte inferior da folha de cálculo, adicione uma nova entrada de comando. Aqui tomamos como exemplo a adição de uma palavra de comando "打扫房间" (Limpar o Quarto).

![17](../../en/04-custom-protocol/images/17.png)

Aqui precisa de selecionar "命令词" (Palavra de Comando) para o tipo de função e definir o modo de reprodução como "主" (Ativo). Desta forma, após reconhecer "打扫房间", reproduzirá ativamente "好的" (OK).

![18](../../en/04-custom-protocol/images/18.png)

Agora vamos compreender o protocolo de envio. O 1.º e o 2.º bytes dos dados são o cabeçalho do frame de dados e não precisam de ser modificados. Quando selecionamos o tipo de função como palavra de comando, de acordo com o protocolo de envio, o 3.º byte de dados tem de ser "00". Isto serve para distinguir se o comando é uma "palavra de comando" ou uma "frase de reprodução".

![19](../../en/04-custom-protocol/images/19.png)

O 4.º byte de dados é o ID de dados da palavra de comando, que é um valor hexadecimal. Como o ID da palavra de comando anterior era "8B", precisamos de definir este byte como "8C". Em casos especiais, os IDs de dados podem ser iguais, por exemplo quando os resultados devolvidos por duas palavras de comando são idênticos.

![20](../../en/04-custom-protocol/images/20.png)

O 5.º byte no protocolo está fixo em "EE" e também não precisa de ser modificado. Na folha de cálculo, o protocolo de envio e o protocolo de receção devem ser consistentes.

![21](../../en/04-custom-protocol/images/21.png)

Guarde após a modificação e, em seguida, siga os passos de "1.2 Criação do Firmware" para importar a folha de cálculo para o sítio web. Se já criou um firmware uma vez, pode clicar no botão "继承" (Herdar) no projeto anterior, o que permite guardar os passos de configuração de parâmetros.

![13](../../en/04-custom-protocol/images/13.png)

Após recriar o firmware, também precisa de gravar o firmware no módulo de interação por voz. Isto ativará a função da nova entrada de comando.

# 4. Adição de Novas Frases de Reprodução

Abra o ficheiro "命令词播报词协议列表V1\_中文" (Lista de Protocolo de Palavras de Comando e Palavras de Reprodução V1\_Chinês) dos anexos.

![14](../../en/04-custom-protocol/images/14.png)

Na parte inferior da folha de cálculo, adicione uma nova entrada. Aqui tomamos como exemplo a adição de uma frase de reprodução "现在是晚上" (É de Noite Agora).

![22](../../en/04-custom-protocol/images/22.png)

Aqui precisa de selecionar "播报语" (Frase de Reprodução) para o tipo de função e definir o modo de reprodução como "被" (Passivo).

![23](../../en/04-custom-protocol/images/23.png)

Agora vamos compreender o protocolo de envio. O 1.º e o 2.º bytes dos dados são o cabeçalho do frame de dados e não precisam de ser modificados. Quando selecionamos o tipo de função como frase de reprodução, de acordo com o protocolo de envio, o 3.º byte de dados tem de ser "FF". Isto serve para distinguir o comando como uma "frase de reprodução".

![24](../../en/04-custom-protocol/images/24.png)

O 4.º byte de dados é o ID de dados da palavra de comando, que é um valor hexadecimal. Como o ID da frase de reprodução anterior era "8B", precisamos de definir este byte como "8C".

O 5.º byte no protocolo está fixo em "EE" e também não precisa de ser modificado. Na folha de cálculo, o protocolo de envio e o protocolo de receção devem ser consistentes.

![25](../../en/04-custom-protocol/images/25.png)

Guarde após a modificação e, em seguida, siga os passos de "1.2 Criação do Firmware" para importar a folha de cálculo para o sítio web. Se já criou um firmware uma vez, pode clicar no botão "继承" (Herdar) no projeto anterior, o que permite guardar os passos de configuração de parâmetros.

![13](../../en/04-custom-protocol/images/13.png)

Após recriar o firmware, também precisa de gravar o firmware no módulo de interação por voz. Isto ativará a função da nova entrada de comando.
