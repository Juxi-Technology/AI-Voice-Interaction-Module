[English](../../en/04-custom-protocol/custom-protocol.md) | [Deutsch](../../de/04-custom-protocol/custom-protocol.md) | [Español](../../es/04-custom-protocol/custom-protocol.md) | [Français](../../fr/04-custom-protocol/custom-protocol.md) | [Italiano](../../it/04-custom-protocol/custom-protocol.md) | [日本語](../../ja/04-custom-protocol/custom-protocol.md) | [한국어](../../ko/04-custom-protocol/custom-protocol.md) | Português (BR) | [Português (PT)](../../pt-pt/04-custom-protocol/custom-protocol.md) | [简体中文](../../zh-hans/04-custom-protocol/custom-protocol.md) | [繁體中文](../../zh-hant/04-custom-protocol/custom-protocol.md)

# Criação de Entradas de Protocolo Personalizado

# 1. Criação do Firmware do Chip de Voz

# 1.1 Precauções

O módulo já vem com o firmware de reconhecimento de voz gravado de fábrica. Os anexos da documentação também fornecem o firmware de fábrica. Se você precisar recriar o firmware, pode seguir os passos abaixo para a criação do firmware.

# 1.2 Criação do Firmware

Primeiro, abra o link "启英泰伦语音AI平台" (Plataforma de IA de Voz ChipIntelli) para acessar o site de criação de firmware.
Clique em "功能开发" (Desenvolvimento de Funcionalidades) na barra de menus e, em seguida, clique em "离线语音识别大模型应用" (Aplicação de Grande Modelo de Reconhecimento de Voz Offline) na seção Desenvolvimento de Produto.

![1](../../en/04-custom-protocol/images/1.png)

Nesse momento, será solicitado que você faça login. Você precisa registrar uma conta na plataforma com suas próprias informações. Para este tutorial, já registramos uma conta antecipadamente. Após o login, clique novamente em "语音识别固件及SDK开发" (Desenvolvimento de Firmware e SDK de Reconhecimento de Voz).

![2](../../en/04-custom-protocol/images/2.png)

Após o redirecionamento da página, clique em "新建项目" (Novo Projeto) no lado esquerdo. Crie um novo produto conforme mostrado abaixo, em que o nome e a descrição do produto podem ser personalizados. As demais informações devem ser selecionadas de acordo com o conteúdo destacado em vermelho. O tipo de produto deve ser "通用->智能中控" (Geral -> Controle Central Inteligente). Clique em "创建" (Criar) ao terminar.

![3](../../en/04-custom-protocol/images/3.png)

A seguir, preencha as informações básicas do projeto. Como precisamos de reconhecimento em chinês, selecione "中文" (Chinês) para o tipo de idioma. Se for necessário reconhecimento em inglês, você pode fazer a modificação correspondente. Selecione as demais informações conforme mostrado abaixo e clique em "继续" (Continuar).

![4](../../en/04-custom-protocol/images/4.png)

Em seguida, configure o firmware. Aqui explicaremos apenas as partes que precisam de modificação. Ative a opção de cancelamento de eco nos parâmetros de algoritmo.

![5](../../en/04-custom-protocol/images/5.png)

Nos parâmetros de hardware, defina a fonte do oscilador de cristal como "内部 RC" (RC Interno).

![6](../../en/04-custom-protocol/images/6.png)

Na configuração da porta serial de impressão (print), defina o nível do UART0 como função open-drain, com suporte a pull-up externo para 5V.

![7](../../en/04-custom-protocol/images/7.png)

Modifique a configuração da porta serial de comunicação: defina a taxa de transmissão (baud rate) como 115200 e configure o nível do UART1 como função open-drain, com suporte a pull-up externo para 5V. Após a configuração, clique em "继续" (Continuar) para prosseguir para a próxima etapa.

![8](../../en/04-custom-protocol/images/8.png)

Agora entre na função de edição de palavras de comando. Primeiro, selecione a voz de reprodução. Aqui escolhemos "小蝶-清新女声 Ver.3" (Xiaodie - Voz Feminina Fresca Ver.3).

![9](../../en/04-custom-protocol/images/9.png)

A seguir, envie o anexo de palavras de comando. Encontre a planilha "命令词播报词协议列表V1\_中文" (Lista de Protocolos de Palavras de Comando e Palavras de Reprodução V1\_Chinês) no mesmo diretório deste documento e arraste-a diretamente para a página web para enviá-la.

![10](../../en/04-custom-protocol/images/10.png)

Após enviar o arquivo, você poderá ver nossos dados de palavras de comando na tabela abaixo.

![11](../../en/04-custom-protocol/images/11.png)

Ative a função de autoaprendizagem e selecione "指定学习" (Aprendizagem Especificada). O sistema gerará automaticamente 4 comandos de autoaprendizagem. Não faremos nenhuma alteração aqui.

![12](../../en/04-custom-protocol/images/12.png)

Após enviar, aguarde alguns minutos para a criação do firmware ser concluída. Quando terminar, clique em "下载固件" (Baixar Firmware) para obter o firmware criado.

![13](../../en/04-custom-protocol/images/13.png)

Para os passos de gravação do firmware, consulte "4. Método de Gravação do Firmware do Módulo".

# 2. Modificação de Entradas Funcionais

Abra o arquivo "命令词播报词协议列表V1\_中文" (Lista de Protocolos de Palavras de Comando e Palavras de Reprodução V1\_Chinês) dos anexos.

![14](../../en/04-custom-protocol/images/14.png)

Encontre as entradas funcionais na planilha, que são as 10 primeiras entradas. Observe que essas 10 entradas funcionais são entradas fixas que não podem ser adicionadas, apenas modificadas.

![15](../../en/04-custom-protocol/images/15.png)

Aqui usamos como exemplo a modificação da frase de reprodução da palavra de ativação: alterar a reprodução de "在的" (Estou aqui) após reconhecer "你好，小犀" para "我在" (Estou aqui).

![16](../../en/04-custom-protocol/images/16.png)

Salve após a modificação e siga os passos de "1.2 Criação do Firmware" para importar a planilha para o site. Se você já criou um firmware uma vez, pode clicar no botão "继承" (Herdar) no projeto anterior, o que pode poupar as etapas de configuração de parâmetros.

![13](../../en/04-custom-protocol/images/13.png)

Após recriar o firmware, você também precisa gravá-lo no módulo de interação de voz. Isso habilitará as entradas funcionais modificadas.

# 3. Adição de Novas Entradas de Comando

Abra o arquivo "命令词播报词协议列表V1\_中文" (Lista de Protocolos de Palavras de Comando e Palavras de Reprodução V1\_Chinês) dos anexos.

![14](../../en/04-custom-protocol/images/14.png)

Na parte inferior da planilha, adicione uma nova entrada de comando. Aqui usamos como exemplo a adição de uma palavra de comando "打扫房间" (Limpar o Quarto).

![17](../../en/04-custom-protocol/images/17.png)

Aqui você precisa selecionar "命令词" (Palavra de Comando) para o tipo de função e definir o modo de reprodução como "主" (Ativo). Assim, após reconhecer "打扫房间", ele reproduzirá ativamente "好的" (OK).

![18](../../en/04-custom-protocol/images/18.png)

Agora vamos entender o protocolo de envio. O 1º e o 2º bytes dos dados são o cabeçalho do quadro de dados e não precisam ser modificados. Quando selecionamos o tipo de função como palavra de comando, de acordo com o protocolo de envio, o 3º byte dos dados deve ser "00". Isso serve para distinguir se o comando é uma "palavra de comando" ou uma "frase de reprodução".

![19](../../en/04-custom-protocol/images/19.png)

O 4º byte dos dados é o ID de dados da palavra de comando, que é um valor hexadecimal. Como o ID da palavra de comando anterior era "8B", precisamos definir esse byte como "8C". Em casos especiais, os IDs de dados podem ser iguais, por exemplo, quando os resultados retornados por duas palavras de comando são idênticos.

![20](../../en/04-custom-protocol/images/20.png)

O 5º byte no protocolo é fixo em "EE" e também não precisa ser modificado. Na planilha, o protocolo de envio e o protocolo de recebimento devem ser consistentes.

![21](../../en/04-custom-protocol/images/21.png)

Salve após a modificação e siga os passos de "1.2 Criação do Firmware" para importar a planilha para o site. Se você já criou um firmware uma vez, pode clicar no botão "继承" (Herdar) no projeto anterior, o que pode poupar as etapas de configuração de parâmetros.

![13](../../en/04-custom-protocol/images/13.png)

Após recriar o firmware, você também precisa gravá-lo no módulo de interação de voz. Isso habilitará a função da nova entrada de comando.

# 4. Adição de Novas Frases de Reprodução

Abra o arquivo "命令词播报词协议列表V1\_中文" (Lista de Protocolos de Palavras de Comando e Palavras de Reprodução V1\_Chinês) dos anexos.

![14](../../en/04-custom-protocol/images/14.png)

Na parte inferior da planilha, adicione uma nova entrada. Aqui usamos como exemplo a adição de uma frase de reprodução "现在是晚上" (Agora é Noite).

![22](../../en/04-custom-protocol/images/22.png)

Aqui você precisa selecionar "播报语" (Frase de Reprodução) para o tipo de função e definir o modo de reprodução como "被" (Passivo).

![23](../../en/04-custom-protocol/images/23.png)

Agora vamos entender o protocolo de envio. O 1º e o 2º bytes dos dados são o cabeçalho do quadro de dados e não precisam ser modificados. Quando selecionamos o tipo de função como frase de reprodução, de acordo com o protocolo de envio, o 3º byte dos dados deve ser "FF". Isso serve para distinguir se o comando é uma "frase de reprodução".

![24](../../en/04-custom-protocol/images/24.png)

O 4º byte dos dados é o ID de dados da palavra de comando, que é um valor hexadecimal. Como o ID da frase de reprodução anterior era "8B", precisamos definir esse byte como "8C".

O 5º byte no protocolo é fixo em "EE" e também não precisa ser modificado. Na planilha, o protocolo de envio e o protocolo de recebimento devem ser consistentes.

![25](../../en/04-custom-protocol/images/25.png)

Salve após a modificação e siga os passos de "1.2 Criação do Firmware" para importar a planilha para o site. Se você já criou um firmware uma vez, pode clicar no botão "继承" (Herdar) no projeto anterior, o que pode poupar as etapas de configuração de parâmetros.

![13](../../en/04-custom-protocol/images/13.png)

Após recriar o firmware, você também precisa gravá-lo no módulo de interação de voz. Isso habilitará a função da nova entrada de comando.
