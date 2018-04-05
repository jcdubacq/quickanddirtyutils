Cet utilitaire permet de découper les fichiers d'impression de Parcoursup'
(anciennement APB) étudiants par étudiants.

Il nécessite l'installation de pdftk et pdftotext.

L'utilitaire **apb_decoupe.py** permet de saucissonner un fichier issu
de l'impression.

L'utilitaire **process.sh** permet de ranger facilement les résultas et de
générer des fichiers textes comprenant les parcours de formation motivés
(anciennement lettres de motivation). C'est le programme qu'il faut appeller.
Il faut le paramétrer en créant un fichier CONFIG qui contient par exemple:

    FORMATION_INITIALE_INFO:dossiers_12345678_Informatique.pdf
    FORMATION_INITIALE_MECA:dossiers_12345678_Mecanique.pdf

Ensuite on le lance par :

    ./process.sh

Ou pour mettre à jour seulement un des fichiers :

    ./process.sh FORMATION_INTIALE_INFO

