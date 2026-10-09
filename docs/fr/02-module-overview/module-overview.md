[English](../../en/02-module-overview/module-overview.md) | [Deutsch](../../de/02-module-overview/module-overview.md) | [Español](../../es/02-module-overview/module-overview.md) | Français | [Italiano](../../it/02-module-overview/module-overview.md) | [日本語](../../ja/02-module-overview/module-overview.md) | [한국어](../../ko/02-module-overview/module-overview.md) | [Português (BR)](../../pt-br/02-module-overview/module-overview.md) | [Português (PT)](../../pt-pt/02-module-overview/module-overview.md) | [简体中文](../../zh-hans/02-module-overview/module-overview.md) | [繁體中文](../../zh-hant/02-module-overview/module-overview.md)

# Informations produit

## 1. Présentation du module d'interaction vocale

Le CI1302 est une nouvelle génération de puce vocale intelligente à réseau de neurones hautes performances développée par ChipIntelli. Elle intègre le processeur de réseau de neurones cérébral Brain Neural Network Processor BNPU V3 de ChipIntelli et un cœur CPU, avec une fréquence d'horloge système pouvant atteindre 220MHz, jusqu'à 640KB de SRAM intégrée, une unité de gestion d'alimentation PMU et un oscillateur RC intégrés, ainsi qu'un codec audio double canal hautes performances à faible consommation et de multiples interfaces de contrôle périphériques telles que UART, IIC, IIS, PWM, GPIO et PDM. La puce ne nécessite que quelques composants externes tels que des résistances et des condensateurs pour mettre en œuvre diverses solutions matérielles de produits vocaux intelligents, offrant un rapport coût-efficacité exceptionnel.

En s'appuyant sur la technologie matérielle BNPU de 3e génération, elle prend en charge les réseaux de neurones DNN, TDNN, RNN, CNN et autres, ainsi que les opérations vectorielles parallèles, ce qui permet des fonctions telles que la reconnaissance vocale, la reconnaissance d'empreinte vocale, l'auto-apprentissage de mots de commande, la détection de voix et la réduction de bruit par apprentissage profond. La solution de puce prend également en charge plusieurs langues mondiales, dont le chinois, l'anglais et le japonais, ce qui la rend largement applicable dans les domaines des appareils électroménagers, de l'éclairage, des jouets, des objets connectés portables, de l'industrie et de l'automobile, pour l'interaction vocale, le contrôle et diverses applications de solutions vocales intelligentes.

La puce CI1302 dispose d'un cœur de processeur de réseau de neurones cérébral (BNPU), prenant en charge le calcul accéléré de réseaux de neurones hors ligne et l'accélération matérielle du traitement des signaux vocaux. La fréquence du CPU atteint jusqu'à 220MHz, permettant la reconnaissance vocale hors ligne en champ lointain, avec une mémoire FLASH intégrée de 2MB prenant en charge jusqu'à 300 mots de commande.

## 2. Caractéristiques du produit

- Préchargé avec plus de 110 commandes vocales, prenant en charge des mots de commande personnalisables en chinois et en anglais.

Les utilisateurs peuvent modifier les mots de commande via notre interface web fournie, générer de nouveaux fichiers de firmware et écrire le firmware sur le module à l'aide d'un logiciel PC, après quoi le module reconnaîtra les nouvelles commandes. L'espace de stockage intégré de 2MB prend en charge l'écriture de 120 mots de commande environ.

- Haut-parleur haute fidélité et microphone hautes performances intégrés.

Il intègre des algorithmes avancés et une technologie de réduction du bruit des circuits pour filtrer efficacement le bruit de fond ambiant, atteignant un taux de reconnaissance de 99% dans un rayon de 5 mètres, permettant une conversation naturelle et l'annulation d'écho. Il offre une sortie audio claire et reproduit fidèlement les détails de la voix.

- Coprocesseur embarqué et interfaces IIC/Série/UART/Type-C.

Il intègre la puce STC8H, qui peut convertir automatiquement les données vocales aux formats série ou IIC, ce qui simplifie le processus de communication avec les appareils hôtes externes. Divers câbles de connexion sont fournis gratuitement, permettant aux utilisateurs de se connecter à des cartes de développement MCU et à des appareils hôtes embarqués afin d'établir une communication et de créer leurs propres projets DIY.

- Fournit des tutoriels d'utilisation basés sur diverses cartes de développement.

Fournit des informations sur des cartes de développement telles que STM32, ESP32, MSPM0, Raspberry Pi, les cartes de développement de la série Jetson, RDK, etc. Fournit également des fichiers SDK pour les systèmes ROS1 et ROS2.

## 3. Principe de fonctionnement

Le module adopte un mode de réveil par mot-clé. L'utilisateur doit d'abord prononcer le mot de réveil prédéfini pour activer le module d'interaction vocale. Après l'activation, la reconnaissance vocale peut être effectuée. Le mot-clé de réveil par défaut du firmware d'usine est « 你好，小犀 » (Bonjour, Xiao Xi). Si aucune voix n'est détectée dans les 15 secondes, le module passe en mode veille et doit être réveillé à nouveau pour toute utilisation ultérieure.

Lorsque la puce CI1302 reconnaît l'entrée vocale correspondante, elle l'émet via le port série et l'interface IIC, accompagnée d'une lecture de retour. La puce IIC stocke les commandes vocales reçues et les émet via le protocole esclave IIC.

Le module prend en charge la modification du mot de réveil, la modification des mots de commande et les entrées personnalisées. Vous pouvez apprendre à réaliser ces opérations dans les tutoriels « Modification des mots de réveil et des mots de commande » et « Création d'entrées de protocole personnalisées ».

## 4. Précautions

1. Utilisez une tension de 5V pour l'alimentation ; dépasser 5V endommagera le module.
2. L'environnement d'utilisation doit être calme ; les environnements bruyants affecteront les performances de reconnaissance.
3. Lorsque vous prononcez les entrées, la voix doit être forte et pas trop rapide. Il est recommandé de rester à moins de 5 mètres du module.

## 5. Description de l'interface matérielle

![2](../../en/02-module-overview/images/2.png)

| N° | Nom du matériel         | Description                                                                 |
| --- | --------------------- | --------------------------------------------------------------------------- |
| 1   | Haut-parleur               | Convertit les signaux analogiques en son                                         |
| 2   | Commutateur à glissière          | Change le mode du port série pour le flashage du firmware                            |
| 3   | Microphone            | Convertit le son en signaux analogiques                                         |
| 4   | Bouton RST            | Bouton de réinitialisation                                                                |
| 5   | Indicateur d'alimentation (bleu)| Reste allumé lorsque l'alimentation est normale                                               |
| 6   | Port Type-C           | Utilisé pour l'alimentation et la mise à jour et le téléchargement du firmware CI1302/STC8          |
| 7   | Puce d'amplificateur audio  | Convertit les signaux numériques en signaux analogiques pour piloter le haut-parleur           |
| 8   | Puce CI1302           | Puce de reconnaissance vocale hautes performances ; reconnaît la voix et émet des signaux |
| 9   | Protection contre l'inversion de polarité | Protection contre l'inversion de connexion 5V/GND                                 |
| 10  | Interface IIC         | Sert d'esclave pour l'alimentation et la communication avec l'appareil hôte           |
| 11  | Interface série      | Port série externe fourni ; permet de contrôler la lecture via le protocole            |
| 12  | Puce STC8H            | Convertit les commandes de la puce vocale en commandes de protocole IIC et en commandes série |
