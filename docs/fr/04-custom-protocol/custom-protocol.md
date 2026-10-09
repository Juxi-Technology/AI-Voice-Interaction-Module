[English](../../en/04-custom-protocol/custom-protocol.md) | [Deutsch](../../de/04-custom-protocol/custom-protocol.md) | [Español](../../es/04-custom-protocol/custom-protocol.md) | Français | [Italiano](../../it/04-custom-protocol/custom-protocol.md) | [日本語](../../ja/04-custom-protocol/custom-protocol.md) | [한국어](../../ko/04-custom-protocol/custom-protocol.md) | [Português (BR)](../../pt-br/04-custom-protocol/custom-protocol.md) | [Português (PT)](../../pt-pt/04-custom-protocol/custom-protocol.md) | [简体中文](../../zh-hans/04-custom-protocol/custom-protocol.md) | [繁體中文](../../zh-hant/04-custom-protocol/custom-protocol.md)

# Création d'entrées de protocole personnalisées

# 1. Création du firmware de la puce vocale

# 1.1 Précautions

Le module est livré avec le firmware de reconnaissance vocale préflashé en usine. Les pièces jointes de la documentation fournissent également le firmware d'usine. Si vous devez recréer un firmware, vous pouvez suivre les étapes ci-dessous pour la création du firmware.

# 1.2 Création du firmware

Ouvrez d'abord le lien « 启英泰伦语音AI平台 » (Plateforme d'IA vocale ChipIntelli) pour accéder au site web de création de firmware.
Cliquez sur « 功能开发 » (Développement de fonctionnalités) dans la barre de menus, puis cliquez sur « 离线语音识别大模型应用 » (Application de grand modèle de reconnaissance vocale hors ligne) dans la section Développement de produit.

![1](../../en/04-custom-protocol/images/1.png)

À ce stade, il vous sera demandé de vous connecter. Vous devez enregistrer un compte sur la plateforme avec vos propres informations. Pour ce tutoriel, nous nous sommes déjà inscrits à l'avance. Après vous être connecté, cliquez à nouveau sur « 语音识别固件及SDK开发 » (Développement de firmware et de SDK de reconnaissance vocale).

![2](../../en/04-custom-protocol/images/2.png)

Une fois la page redirigée, cliquez sur « 新建项目 » (Nouveau projet) sur le côté gauche. Créez un nouveau produit comme indiqué ci-dessous, où le nom et la description du produit peuvent être personnalisés. Les informations restantes doivent être sélectionnées conformément au contenu encadré en rouge. Le type de produit doit être « 通用->智能中控 » (Général -> Contrôle central intelligent). Cliquez sur « 创建 » (Créer) lorsque c'est terminé.

![3](../../en/04-custom-protocol/images/3.png)

Ensuite, renseignez les informations de base du projet. Comme nous avons besoin de la reconnaissance du chinois, sélectionnez « 中文 » (Chinois) pour le type de langue. Si la reconnaissance de l'anglais est nécessaire, vous pouvez apporter la modification correspondante. Sélectionnez les autres informations comme indiqué ci-dessous, puis cliquez sur « 继续 » (Continuer).

![4](../../en/04-custom-protocol/images/4.png)

Ensuite, configurez le firmware. Ici, nous n'expliquerons que les parties à modifier. Activez l'option d'annulation d'écho dans les paramètres d'algorithme.

![5](../../en/04-custom-protocol/images/5.png)

Dans les paramètres matériels, réglez la source de l'oscillateur à quartz sur « 内部 RC » (RC interne).

![6](../../en/04-custom-protocol/images/6.png)

Dans la configuration du port série d'impression, réglez le niveau de l'UART0 en fonction drain ouvert, avec prise en charge d'une résistance de tirage externe vers 5V.

![7](../../en/04-custom-protocol/images/7.png)

Modifiez la configuration du port série de communication : réglez le débit en bauds sur 115200 et configurez le niveau de l'UART1 en fonction drain ouvert, avec prise en charge d'une résistance de tirage externe vers 5V. Après la configuration, cliquez sur « 继续 » (Continuer) pour passer à l'étape suivante.

![8](../../en/04-custom-protocol/images/8.png)

Vous entrez maintenant dans la fonction d'édition des mots de commande. Sélectionnez d'abord la voix de lecture. Ici, nous choisissons « 小蝶-清新女声 Ver.3 » (Xiaodie - Voix féminine fraîche Ver.3).

![9](../../en/04-custom-protocol/images/9.png)

Ensuite, importez la pièce jointe des mots de commande. Trouvez le fichier tableur « 命令词播报词协议列表V1\_中文 » (Liste de protocole des mots de commande et des phrases de lecture V1\_Chinois) dans le même répertoire que ce document et faites-le glisser directement dans la page web pour l'importer.

![10](../../en/04-custom-protocol/images/10.png)

Après l'importation du fichier, vous pouvez voir nos données de mots de commande dans le tableau ci-dessous.

![11](../../en/04-custom-protocol/images/11.png)

Activez la fonction d'auto-apprentissage et sélectionnez « 指定学习 » (Apprentissage spécifié). Le système générera automatiquement 4 commandes d'auto-apprentissage. Nous n'apporterons aucune modification ici.

![12](../../en/04-custom-protocol/images/12.png)

Après avoir soumis, attendez quelques minutes que la création du firmware soit terminée. Une fois terminé, cliquez sur « 下载固件 » (Télécharger le firmware) pour obtenir le firmware créé.

![13](../../en/04-custom-protocol/images/13.png)

Pour les étapes de flashage du firmware, veuillez vous référer à « 4. Méthode de flashage du firmware du module ».

# 2. Modification des entrées fonctionnelles

Ouvrez le fichier « 命令词播报词协议列表V1\_中文 » (Liste de protocole des mots de commande et des phrases de lecture V1\_Chinois) depuis les pièces jointes.

![14](../../en/04-custom-protocol/images/14.png)

Trouvez les entrées fonctionnelles dans le tableur, qui sont les 10 premières entrées. Notez que ces 10 entrées fonctionnelles sont des entrées fixes qui ne peuvent pas être ajoutées, seulement modifiées.

![15](../../en/04-custom-protocol/images/15.png)

Ici, nous prenons l'exemple de la modification de la phrase de lecture du mot de réveil : changez la lecture de « 在的 » (Je suis là) après reconnaissance de « 你好，小犀 » en « 我在 » (Je suis là).

![16](../../en/04-custom-protocol/images/16.png)

Enregistrez après modification, puis suivez les étapes de « 1.2 Création du firmware » pour importer le tableur dans le site web. Si vous avez déjà créé un firmware une fois, vous pouvez cliquer sur le bouton « 继承 » (Hériter) dans le projet précédent, ce qui permet d'économiser les étapes de configuration des paramètres.

![13](../../en/04-custom-protocol/images/13.png)

Après avoir recréé le firmware, vous devez également flasher le firmware sur le module d'interaction vocale. Cela activera les entrées fonctionnelles modifiées.

# 3. Ajout de nouvelles entrées de commande

Ouvrez le fichier « 命令词播报词协议列表V1\_中文 » (Liste de protocole des mots de commande et des phrases de lecture V1\_Chinois) depuis les pièces jointes.

![14](../../en/04-custom-protocol/images/14.png)

En bas du tableur, ajoutez une nouvelle entrée de commande. Ici, nous prenons l'exemple de l'ajout d'un mot de commande « 打扫房间 » (Nettoyer la pièce).

![17](../../en/04-custom-protocol/images/17.png)

Ici, vous devez sélectionner « 命令词 » (Mot de commande) pour le type de fonction et régler le mode de lecture sur « 主 » (Active). Ainsi, après reconnaissance de « 打扫房间 », il lira activement « 好的 » (OK).

![18](../../en/04-custom-protocol/images/18.png)

Comprenons maintenant le protocole d'envoi. Les 1er et 2e octets des données sont l'en-tête de trame de données et n'ont pas besoin d'être modifiés. Lorsque nous sélectionnons le type de fonction comme mot de commande, conformément au protocole d'envoi, le 3e octet de données doit être « 00 ». Cela permet de distinguer si la commande est un « mot de commande » ou une « phrase de lecture ».

![19](../../en/04-custom-protocol/images/19.png)

Le 4e octet de données est l'ID de données du mot de commande, qui est une valeur hexadécimale. Comme l'ID du mot de commande précédent était « 8B », nous devons régler cet octet sur « 8C ». Dans des cas particuliers, les ID de données peuvent être identiques, par exemple lorsque les résultats renvoyés par deux mots de commande sont identiques.

![20](../../en/04-custom-protocol/images/20.png)

Le 5e octet du protocole est fixé à « EE » et n'a pas non plus besoin d'être modifié. Dans le tableur, le protocole d'envoi et le protocole de réception doivent être cohérents.

![21](../../en/04-custom-protocol/images/21.png)

Enregistrez après modification, puis suivez les étapes de « 1.2 Création du firmware » pour importer le tableur dans le site web. Si vous avez déjà créé un firmware une fois, vous pouvez cliquer sur le bouton « 继承 » (Hériter) dans le projet précédent, ce qui permet d'économiser les étapes de configuration des paramètres.

![13](../../en/04-custom-protocol/images/13.png)

Après avoir recréé le firmware, vous devez également flasher le firmware sur le module d'interaction vocale. Cela activera la nouvelle fonction d'entrée de commande.

# 4. Ajout de nouvelles phrases de lecture

Ouvrez le fichier « 命令词播报词协议列表V1\_中文 » (Liste de protocole des mots de commande et des phrases de lecture V1\_Chinois) depuis les pièces jointes.

![14](../../en/04-custom-protocol/images/14.png)

En bas du tableur, ajoutez une nouvelle entrée. Ici, nous prenons l'exemple de l'ajout d'une phrase de lecture « 现在是晚上 » (Il fait nuit maintenant).

![22](../../en/04-custom-protocol/images/22.png)

Ici, vous devez sélectionner « 播报语 » (Phrase de lecture) pour le type de fonction et régler le mode de lecture sur « 被 » (Passive).

![23](../../en/04-custom-protocol/images/23.png)

Comprenons maintenant le protocole d'envoi. Les 1er et 2e octets des données sont l'en-tête de trame de données et n'ont pas besoin d'être modifiés. Lorsque nous sélectionnons le type de fonction comme phrase de lecture, conformément au protocole d'envoi, le 3e octet de données doit être « FF ». Cela permet de distinguer la commande comme une « phrase de lecture ».

![24](../../en/04-custom-protocol/images/24.png)

Le 4e octet de données est l'ID de données du mot de commande, qui est une valeur hexadécimale. Comme l'ID de la phrase de lecture précédente était « 8B », nous devons régler cet octet sur « 8C ».

Le 5e octet du protocole est fixé à « EE » et n'a pas non plus besoin d'être modifié. Dans le tableur, le protocole d'envoi et le protocole de réception doivent être cohérents.

![25](../../en/04-custom-protocol/images/25.png)

Enregistrez après modification, puis suivez les étapes de « 1.2 Création du firmware » pour importer le tableur dans le site web. Si vous avez déjà créé un firmware une fois, vous pouvez cliquer sur le bouton « 继承 » (Hériter) dans le projet précédent, ce qui permet d'économiser les étapes de configuration des paramètres.

![13](../../en/04-custom-protocol/images/13.png)

Après avoir recréé le firmware, vous devez également flasher le firmware sur le module d'interaction vocale. Cela activera la nouvelle fonction d'entrée de commande.
