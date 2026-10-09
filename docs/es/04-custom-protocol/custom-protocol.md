[English](../../en/04-custom-protocol/custom-protocol.md) | [Deutsch](../../de/04-custom-protocol/custom-protocol.md) | Español | [Français](../../fr/04-custom-protocol/custom-protocol.md) | [Italiano](../../it/04-custom-protocol/custom-protocol.md) | [日本語](../../ja/04-custom-protocol/custom-protocol.md) | [한국어](../../ko/04-custom-protocol/custom-protocol.md) | [Português (BR)](../../pt-br/04-custom-protocol/custom-protocol.md) | [Português (PT)](../../pt-pt/04-custom-protocol/custom-protocol.md) | [简体中文](../../zh-hans/04-custom-protocol/custom-protocol.md) | [繁體中文](../../zh-hant/04-custom-protocol/custom-protocol.md)

# Creación de entradas de protocolo personalizado

# 1. Creación del firmware del chip de voz

# 1.1 Precauciones

El módulo viene con el firmware de reconocimiento de voz flasheado de fábrica. Los archivos adjuntos de la documentación también incluyen el firmware de fábrica. Si necesitas volver a crear el firmware, puedes seguir los pasos a continuación para la creación del firmware.

# 1.2 Creación del firmware

En primer lugar, abre el enlace "启英泰伦语音AI平台" (Plataforma de IA de voz ChipIntelli) para acceder al sitio web de creación de firmware.
Haz clic en "功能开发" (Desarrollo de funciones) en la barra de menú y, a continuación, haz clic en "离线语音识别大模型应用" (Aplicación de modelo grande de reconocimiento de voz offline), dentro de la sección Desarrollo de productos.

![1](../../en/04-custom-protocol/images/1.png)

En este momento, se te pedirá que inicies sesión. Debes registrar una cuenta de la plataforma con tus propios datos. Para este tutorial, ya nos hemos registrado de antemano. Después de iniciar sesión, haz clic de nuevo en "语音识别固件及SDK开发" (Desarrollo de firmware y SDK de reconocimiento de voz).

![2](../../en/04-custom-protocol/images/2.png)

Una vez que la página se redirija, haz clic en "新建项目" (Nuevo proyecto) en el lado izquierdo. Crea un nuevo producto como se muestra a continuación, donde el nombre y la descripción del producto pueden personalizarse. El resto de la información debe seleccionarse según el contenido marcado en rojo. El tipo de producto debe ser "通用->智能中控" (General -> Control central inteligente). Haz clic en "创建" (Crear) cuando termines.

![3](../../en/04-custom-protocol/images/3.png)

A continuación, rellena la información básica del proyecto. Como necesitamos reconocimiento en chino, selecciona "中文" (Chino) como tipo de idioma. Si se necesita reconocimiento en inglés, puedes realizar la modificación correspondiente. Selecciona el resto de la información como se muestra a continuación y haz clic en "继续" (Continuar).

![4](../../en/04-custom-protocol/images/4.png)

Después, configura el firmware. Aquí solo explicaremos las partes que necesitan modificación. Activa la opción de cancelación de eco en los parámetros del algoritmo.

![5](../../en/04-custom-protocol/images/5.png)

En los parámetros de hardware, configura el origen del oscilador de cristal como "内部 RC" (RC interno).

![6](../../en/04-custom-protocol/images/6.png)

En la configuración del puerto serie de impresión, ajusta el nivel de UART0 a la función de drenaje abierto (open-drain), compatible con pull-up externo a 5 V.

![7](../../en/04-custom-protocol/images/7.png)

Modifica la configuración del puerto serie de comunicación: establece la velocidad en baudios en 115200 y configura el nivel de UART1 a la función de drenaje abierto, compatible con pull-up externo a 5 V. Una vez configurado, haz clic en "继续" (Continuar) para pasar al siguiente paso.

![8](../../en/04-custom-protocol/images/8.png)

Ahora entra en la función de edición de palabras de comando. Primero, selecciona la voz de reproducción. Aquí elegimos "小蝶-清新女声 Ver.3" (Xiaodie - Voz femenina fresca Ver.3).

![9](../../en/04-custom-protocol/images/9.png)

A continuación, sube el archivo adjunto de palabras de comando. Busca la hoja de cálculo "命令词播报词协议列表V1\_中文" (Lista de protocolo de palabras de comando y palabras de reproducción V1\_Chino) en el mismo directorio que este documento y arrástrala directamente a la página web para subirla.

![10](../../en/04-custom-protocol/images/10.png)

Después de subir el archivo, puedes ver nuestros datos de palabras de comando en la tabla de abajo.

![11](../../en/04-custom-protocol/images/11.png)

Activa la función de autoaprendizaje y selecciona "指定学习" (Aprendizaje especificado). El sistema generará automáticamente 4 comandos de autoaprendizaje. Aquí no haremos ningún cambio.

![12](../../en/04-custom-protocol/images/12.png)

Después de enviar, espera unos minutos a que se complete la creación del firmware. Una vez hecho, haz clic en "下载固件" (Descargar firmware) para obtener el firmware creado.

![13](../../en/04-custom-protocol/images/13.png)

Para los pasos de flasheo del firmware, consulta "4. Método de flasheo del firmware del módulo".

# 2. Modificación de entradas funcionales

Abre el archivo "命令词播报词协议列表V1\_中文" (Lista de protocolo de palabras de comando y palabras de reproducción V1\_Chino) de los archivos adjuntos.

![14](../../en/04-custom-protocol/images/14.png)

Localiza las entradas funcionales en la hoja de cálculo, que son las 10 primeras entradas. Ten en cuenta que estas 10 entradas funcionales son entradas fijas que no se pueden añadir, solo modificar.

![15](../../en/04-custom-protocol/images/15.png)

Aquí tomamos como ejemplo la modificación de la frase de reproducción de la palabra de activación: cambiar la reproducción de "在的" (Estoy aquí) tras reconocer "你好，小犀" a "我在" (Estoy aquí).

![16](../../en/04-custom-protocol/images/16.png)

Guarda después de la modificación y, a continuación, sigue los pasos de "1.2 Creación del firmware" para importar la hoja de cálculo al sitio web. Si ya has creado firmware una vez, puedes hacer clic en el botón "继承" (Heredar) del proyecto anterior, lo que permite ahorrar los pasos de configuración de parámetros.

![13](../../en/04-custom-protocol/images/13.png)

Después de volver a crear el firmware, también debes flashearlo en el módulo de interacción por voz. Esto habilitará las entradas funcionales modificadas.

# 3. Añadir nuevas entradas de comando

Abre el archivo "命令词播报词协议列表V1\_中文" (Lista de protocolo de palabras de comando y palabras de reproducción V1\_Chino) de los archivos adjuntos.

![14](../../en/04-custom-protocol/images/14.png)

En la parte inferior de la hoja de cálculo, añade una nueva entrada de comando. Aquí tomamos como ejemplo añadir la palabra de comando "打扫房间" (Limpiar la habitación).

![17](../../en/04-custom-protocol/images/17.png)

Aquí debes seleccionar "命令词" (Palabra de comando) como tipo de función y establecer el modo de reproducción en "主" (Activo). De este modo, tras reconocer "打扫房间", reproducirá activamente "好的" (De acuerdo).

![18](../../en/04-custom-protocol/images/18.png)

Ahora entendamos el protocolo de envío. El 1.er y 2.º byte de los datos son la cabecera de la trama de datos y no necesitan modificarse. Cuando seleccionamos el tipo de función como palabra de comando, según el protocolo de envío, el 3.er byte de datos debe ser "00". Esto sirve para distinguir si el comando es una "palabra de comando" o una "frase de reproducción".

![19](../../en/04-custom-protocol/images/19.png)

El 4.º byte de datos es el ID de datos de la palabra de comando, que es un valor hexadecimal. Como el ID de la palabra de comando anterior era "8B", debemos establecer este byte en "8C". En casos especiales, los ID de datos pueden ser iguales, por ejemplo cuando los resultados devueltos por dos palabras de comando son idénticos.

![20](../../en/04-custom-protocol/images/20.png)

El 5.º byte del protocolo está fijado en "EE" y tampoco necesita modificarse. En la hoja de cálculo, el protocolo de envío y el protocolo de recepción deben ser coherentes.

![21](../../en/04-custom-protocol/images/21.png)

Guarda después de la modificación y, a continuación, sigue los pasos de "1.2 Creación del firmware" para importar la hoja de cálculo al sitio web. Si ya has creado firmware una vez, puedes hacer clic en el botón "继承" (Heredar) del proyecto anterior, lo que permite ahorrar los pasos de configuración de parámetros.

![13](../../en/04-custom-protocol/images/13.png)

Después de volver a crear el firmware, también debes flashearlo en el módulo de interacción por voz. Esto habilitará la función de la nueva entrada de comando.

# 4. Añadir nuevas frases de reproducción

Abre el archivo "命令词播报词协议列表V1\_中文" (Lista de protocolo de palabras de comando y palabras de reproducción V1\_Chino) de los archivos adjuntos.

![14](../../en/04-custom-protocol/images/14.png)

En la parte inferior de la hoja de cálculo, añade una nueva entrada. Aquí tomamos como ejemplo añadir la frase de reproducción "现在是晚上" (Ahora es de noche).

![22](../../en/04-custom-protocol/images/22.png)

Aquí debes seleccionar "播报语" (Frase de reproducción) como tipo de función y establecer el modo de reproducción en "被" (Pasivo).

![23](../../en/04-custom-protocol/images/23.png)

Ahora entendamos el protocolo de envío. El 1.er y 2.º byte de los datos son la cabecera de la trama de datos y no necesitan modificarse. Cuando seleccionamos el tipo de función como frase de reproducción, según el protocolo de envío, el 3.er byte de datos debe ser "FF". Esto sirve para distinguir el comando como una "frase de reproducción".

![24](../../en/04-custom-protocol/images/24.png)

El 4.º byte de datos es el ID de datos de la palabra de comando, que es un valor hexadecimal. Como el ID de la frase de reproducción anterior era "8B", debemos establecer este byte en "8C".

El 5.º byte del protocolo está fijado en "EE" y tampoco necesita modificarse. En la hoja de cálculo, el protocolo de envío y el protocolo de recepción deben ser coherentes.

![25](../../en/04-custom-protocol/images/25.png)

Guarda después de la modificación y, a continuación, sigue los pasos de "1.2 Creación del firmware" para importar la hoja de cálculo al sitio web. Si ya has creado firmware una vez, puedes hacer clic en el botón "继承" (Heredar) del proyecto anterior, lo que permite ahorrar los pasos de configuración de parámetros.

![13](../../en/04-custom-protocol/images/13.png)

Después de volver a crear el firmware, también debes flashearlo en el módulo de interacción por voz. Esto habilitará la función de la nueva entrada de comando.
