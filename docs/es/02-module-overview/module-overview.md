[English](../../en/02-module-overview/module-overview.md) | [Deutsch](../../de/02-module-overview/module-overview.md) | Español | [Français](../../fr/02-module-overview/module-overview.md) | [Italiano](../../it/02-module-overview/module-overview.md) | [日本語](../../ja/02-module-overview/module-overview.md) | [한국어](../../ko/02-module-overview/module-overview.md) | [Português (BR)](../../pt-br/02-module-overview/module-overview.md) | [Português (PT)](../../pt-pt/02-module-overview/module-overview.md) | [简体中文](../../zh-hans/02-module-overview/module-overview.md) | [繁體中文](../../zh-hant/02-module-overview/module-overview.md)

# Información del producto

## 1. Introducción al módulo de interacción por voz

El CI1302 es un chip de voz inteligente con red neuronal de nueva generación y alto rendimiento, desarrollado por ChipIntelli. Integra el procesador de red neuronal Brain Neural Network Processor BNPU V3, de desarrollo propio de ChipIntelli, y un núcleo de CPU, con una frecuencia de reloj del sistema de hasta 220 MHz, hasta 640 KB de SRAM integrada, una unidad de gestión de energía PMU y un oscilador RC integrados, así como un códec de audio de doble canal de alto rendimiento y bajo consumo y múltiples interfaces de control de periféricos como UART, IIC, IIS, PWM, GPIO y PDM. El chip solo requiere unos pocos componentes externos, como resistencias y condensadores, para implementar diversas soluciones de hardware de productos de voz inteligente, ofreciendo una relación calidad-precio excepcional.

Gracias a la tecnología de hardware BNPU de tercera generación, admite redes neuronales DNN, TDNN, RNN, CNN y otras, así como operaciones vectoriales en paralelo, lo que habilita funciones como el reconocimiento de voz, el reconocimiento de huella de voz, el autoaprendizaje de palabras de comando, la detección de voz y la reducción de ruido mediante aprendizaje profundo. La solución del chip también admite varios idiomas globales, como chino, inglés y japonés, lo que la hace ampliamente aplicable en electrodomésticos, iluminación, juguetes, dispositivos portátiles, industria, automoción y otros campos de productos para la interacción por voz, el control y diversas aplicaciones de soluciones de voz inteligente.

El chip CI1302 incorpora un núcleo Brain Neural Network Processor (BNPU), que admite el cálculo acelerado de redes neuronales offline y la aceleración por hardware del procesamiento de señales de voz. La velocidad de reloj de la CPU alcanza hasta 220 MHz, lo que permite el reconocimiento de voz de campo lejano offline, con un almacenamiento FLASH integrado de 2 MB que admite hasta 300 palabras de comando.

## 2. Características del producto

- Viene precargado con más de 110 comandos de voz y admite palabras de comando personalizables en chino e inglés.

Los usuarios pueden modificar las palabras de comando a través de la interfaz web que proporcionamos, generar nuevos archivos de firmware y escribir el firmware en el módulo mediante software de PC, tras lo cual el módulo reconocerá los nuevos comandos. El espacio de almacenamiento integrado de 2 MB admite la escritura de hasta aproximadamente 120 palabras de comando.

- Altavoz de alta fidelidad y micrófono de alto rendimiento integrados.

Integra algoritmos avanzados y tecnología de reducción de ruido de circuito para filtrar eficazmente el ruido de fondo del entorno, alcanzando una tasa de reconocimiento del 99 % en un rango de 5 metros, lo que permite una conversación natural y la cancelación de eco. Ofrece una salida de audio nítida y reproduce con precisión los detalles de la voz.

- Coprocesador integrado e interfaces IIC/Serie/UART/Type-C.

Integra el chip STC8H, que puede convertir automáticamente los datos de voz en formatos de datos serie o IIC, simplificando el proceso de comunicación con dispositivos host externos. Se proporcionan gratuitamente diversos cables de conexión, lo que permite a los usuarios conectar placas de desarrollo MCU y dispositivos host embebidos para habilitar la comunicación y crear sus propios proyectos DIY.

- Proporciona tutoriales de uso basados en diversas placas de desarrollo.

Proporciona información sobre placas de desarrollo como STM32, ESP32, MSPM0, Raspberry Pi, la serie de placas de desarrollo Jetson, RDK, etc. También proporciona archivos SDK para los sistemas ROS1 y ROS2.

## 3. Principio de funcionamiento

El módulo adopta un modo de activación por palabra clave. El usuario debe pronunciar la palabra de activación predefinida para activar primero el módulo de interacción por voz. Tras la activación, se puede realizar el reconocimiento de voz. La palabra clave de activación predeterminada del firmware de fábrica es "你好，小犀" (Hola, Xiao Xi). Si no se detecta voz en 15 segundos, el módulo entrará en modo de reposo y deberá despertarse de nuevo para su uso posterior.

Cuando el chip CI1302 reconoce la entrada de voz correspondiente, la envía a través del puerto serie y la interfaz IIC, junto con la reproducción de respuesta. El chip IIC almacena los comandos de voz recibidos y los envía mediante el protocolo de esclavo IIC.

El módulo admite la modificación de la palabra de activación, la modificación de la palabra de comando y entradas personalizadas. Puedes aprender a realizar estas operaciones en los tutoriales "Modificación de palabras de activación y palabras de comando" y "Creación de entradas de protocolo personalizado".

## 4. Precauciones

1. Utiliza una tensión de alimentación de 5 V; superar los 5 V dañará el módulo.
2. El entorno de uso debe ser silencioso; los entornos ruidosos afectarán el rendimiento del reconocimiento.
3. Al pronunciar las entradas, la voz debe ser fuerte y no demasiado rápida. Se recomienda permanecer a menos de 5 metros del módulo.

## 5. Descripción de las interfaces de hardware

![2](../../en/02-module-overview/images/2.png)

| N.º | Nombre del componente         | Descripción                                                                 |
| --- | --------------------- | --------------------------------------------------------------------------- |
| 1   | Altavoz               | Convierte señales analógicas en sonido                                      |
| 2   | Interruptor deslizante | Cambia el modo del puerto serie para el flasheo del firmware               |
| 3   | Micrófono             | Convierte el sonido en señales analógicas                                   |
| 4   | Botón RST             | Botón de reinicio                                                           |
| 5   | Indicador de encendido (azul) | Permanece encendido cuando la alimentación es normal                |
| 6   | Puerto Type-C         | Se utiliza para la alimentación y la actualización y descarga del firmware del CI1302/STC8 |
| 7   | Chip amplificador de audio | Convierte señales digitales en señales analógicas para excitar el altavoz |
| 8   | Chip CI1302           | Chip de reconocimiento de voz de alto rendimiento; reconoce la voz y emite señales |
| 9   | Protección contra polaridad inversa | Protección contra conexión inversa de 5V/GND                   |
| 10  | Interfaz IIC          | Actúa como esclavo para la alimentación y la comunicación con el dispositivo host |
| 11  | Interfaz serie        | Puerto serie externo proporcionado; permite controlar la reproducción mediante protocolo |
| 12  | Chip STC8H            | Convierte los comandos del chip de voz en comandos de protocolo IIC y comandos serie |
