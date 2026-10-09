[English](../../en/02-module-overview/module-overview.md) | [Deutsch](../../de/02-module-overview/module-overview.md) | [Español](../../es/02-module-overview/module-overview.md) | [Français](../../fr/02-module-overview/module-overview.md) | [Italiano](../../it/02-module-overview/module-overview.md) | [日本語](../../ja/02-module-overview/module-overview.md) | [한국어](../../ko/02-module-overview/module-overview.md) | Português (BR) | [Português (PT)](../../pt-pt/02-module-overview/module-overview.md) | [简体中文](../../zh-hans/02-module-overview/module-overview.md) | [繁體中文](../../zh-hant/02-module-overview/module-overview.md)

# Informações do Produto

## 1. Introdução ao Módulo de Interação de Voz

O CI1302 é um chip de voz inteligente de rede neural de alto desempenho de nova geração desenvolvido pela ChipIntelli. Ele integra o processador de rede neural Brain Neural Network Processor BNPU V3, desenvolvido pela própria ChipIntelli, e um núcleo de CPU, com frequência de clock do sistema de até 220 MHz, SRAM integrada de até 640 KB, unidade de gerenciamento de energia PMU e oscilador RC integrados, além de Codec de Áudio de baixo consumo e alto desempenho de canal duplo e múltiplas interfaces de controle de periféricos como UART, IIC, IIS, PWM, GPIO e PDM. O chip exige apenas alguns componentes externos, como resistores e capacitores, para implementar diversas soluções de hardware de produtos de voz inteligente, oferecendo um custo-benefício excepcional.

Utilizando a tecnologia de hardware BNPU de 3ª geração, ele suporta redes neurais como DNN, TDNN, RNN, CNN e outras, bem como operações vetoriais paralelas, possibilitando funções como reconhecimento de voz, reconhecimento de impressão vocal (voiceprint), autoaprendizagem de palavras de comando, detecção de voz e redução de ruído por aprendizado profundo. A solução do chip também suporta vários idiomas globais, incluindo chinês, inglês e japonês, tornando-o amplamente aplicável em eletrodomésticos, iluminação, brinquedos, dispositivos vestíveis, industrial, automotivo e outros campos de produtos para interação de voz, controle e diversas aplicações de soluções de voz inteligente.

O chip CI1302 possui um núcleo de processador de rede neural Brain Neural Network Processor (BNPU), que suporta computação de aceleração de redes neurais offline e aceleração de hardware para processamento de sinais de voz. A velocidade de clock da CPU chega a 220 MHz, possibilitando reconhecimento de voz offline de campo distante (far-field), com armazenamento FLASH integrado de 2 MB que suporta até 300 palavras de comando.

## 2. Características do Produto

- Vem pré-carregado com mais de 110 comandos de voz, com suporte a palavras de comando personalizáveis em chinês e inglês.

Os usuários podem modificar as palavras de comando pela interface web que fornecemos, gerar novos arquivos de firmware e gravá-los no módulo por meio de um software de PC; após isso, o módulo reconhecerá os novos comandos. O espaço de armazenamento integrado de 2 MB suporta a gravação de aproximadamente 120 palavras de comando.

- Alto-falante de alta fidelidade e microfone de alto desempenho integrados.

Ele integra algoritmos avançados e tecnologia de redução de ruído de circuito para filtrar efetivamente o ruído de fundo do ambiente, alcançando uma taxa de reconhecimento de 99% em um raio de 5 metros, possibilitando conversação natural e cancelamento de eco. Ele oferece saída de áudio nítida e reproduz com precisão os detalhes da voz.

- Coprocessador integrado na placa e interfaces IIC/Serial/UART/Type-C.

Ele integra o chip STC8H, que pode converter automaticamente os dados de voz em formatos de dados serial ou IIC, simplificando o processo de comunicação com dispositivos host externos. Diversos cabos de conexão são fornecidos gratuitamente, permitindo que os usuários se conectem a placas de desenvolvimento MCU e dispositivos host embarcados para viabilizar a comunicação e criar seus próprios projetos DIY.

- Fornece tutoriais de uso baseados em diversas placas de desenvolvimento.

Fornece informações sobre placas de desenvolvimento como STM32, ESP32, MSPM0, Raspberry Pi, placas da série Jetson, RDK etc. Também fornece arquivos de SDK para os sistemas ROS1 e ROS2.

## 3. Princípio de Funcionamento

O módulo adota um modo de ativação por palavra-chave. O usuário precisa falar a palavra de ativação predefinida para primeiro ativar o módulo de interação de voz. Após a ativação, o reconhecimento de voz pode ser realizado. A palavra de ativação padrão do firmware de fábrica é "你好，小犀" (Olá, Xiao Xi). Se nenhuma voz for detectada em 15 segundos, o módulo entrará em modo de suspensão e precisará ser ativado novamente para uso posterior.

Quando o chip CI1302 reconhece a entrada de voz correspondente, ele a envia pela porta serial e pela interface IIC, junto com a reprodução de resposta. O chip IIC armazena os comandos de voz recebidos e os envia pelo protocolo de escravo (slave) IIC.

O módulo suporta modificação da palavra de ativação, modificação de palavras de comando e entradas personalizadas. Você pode aprender como operar tudo isso nos tutoriais "Modificação de Palavras de Ativação e Palavras de Comando" e "Criação de Entradas de Protocolo Personalizado".

## 4. Precauções

1. Use tensão de 5V para a alimentação; ultrapassar 5V danificará o módulo.
2. O ambiente de uso deve ser silencioso; ambientes ruidosos afetam o desempenho do reconhecimento.
3. Ao falar as entradas, a voz deve ser alta e não muito rápida. Recomenda-se permanecer a até 5 metros do módulo.

## 5. Descrição da Interface de Hardware

![2](../../en/02-module-overview/images/2.png)

| Nº | Nome do Hardware         | Descrição                                                                 |
| --- | --------------------- | --------------------------------------------------------------------------- |
| 1   | Alto-falante          | Converte sinais analógicos em som                                          |
| 2   | Chave Deslizante      | Alterna o modo da porta serial para gravação de firmware                   |
| 3   | Microfone             | Converte som em sinais analógicos                                          |
| 4   | Botão RST             | Botão de reinicialização (reset)                                           |
| 5   | Indicador de Energia (Azul)| Permanece aceso quando a energia está normal                          |
| 6   | Porta Type-C          | Usada para alimentação e atualização/download do firmware CI1302/STC8       |
| 7   | Chip Amplificador de Áudio | Converte sinais digitais em sinais analógicos para acionar o alto-falante |
| 8   | Chip CI1302           | Chip de reconhecimento de voz de alto desempenho; reconhece voz e emite sinais |
| 9   | Proteção contra Polaridade Inversa | Proteção contra conexão invertida de 5V/GND                    |
| 10  | Interface IIC         | Atua como escravo (slave) para alimentação e comunicação com o dispositivo host |
| 11  | Interface Serial      | Porta serial externa fornecida; pode controlar a reprodução via protocolo   |
| 12  | Chip STC8H            | Converte os comandos do chip de voz em comandos de protocolo IIC e comandos seriais |
