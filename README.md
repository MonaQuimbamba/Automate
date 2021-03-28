# Projet d’analyse lexicale
## Introduction
### Description du projet

Ce projet est organis´e en trois s´eances de TEA.
Au cours de ces s´eances, vous allez mettre en oeuvre, en Python, une application relative aux
AEF qui sera `a mˆeme d’effectuer l’essentiel du travail d’un analyseur lexical.
Vous travaillerez en trinˆome, r´epartissez vous donc les tˆaches de mani`ere efficace.
Votre projet sera ´evalu´e via une d´emonstration faites aux enseignants lors de la derni`ere s´eance.

Le projet est organis´e en deux parties, d´ependantes l’une de l’autre :
- Le moteur d’automate
- La d´eterminisation

## Moteur d’AEF
### Objectifs

Le but de cette premi`ere partie est de construire un moteur d’ex´ecution d’automates `a ´etats
finis, d´eterministes et sans λ-transitions.
Le moteur commence par consulter la description (fichier .descr, expliqu´e `a la fin du document
de cours ou sur Moodle) de l’automate A qu’il incarne et afficher cette description, `a fins de
v´erification.
Vous impl´ementerez ´egalement une m´ethode permettant d’exporter vos automates au format
.dot utilis´e par Graphviz. En utilisant Graphviz, vous pourrez alors g´en´erer des images .png
de vos automates. La grammaire des fichiers .dot est expliqu´ee dans le mode d’emploi d´epos´e
sur Moodle (dotguide).
Le moteur d’automage est capable de traiter les entr´ees qu’on lui fournit. Les diff´erents mots
fournis seront s´epar´es par des espaces ou des retours `a la ligne. Pour signifier la fin de la saisie
des entr´ees vous utiliserez ###. Il est ´egalement rappel´e que la phrase vide est pertinente.

Pour chacune des entr´ees qu’il analyse, le moteur produit :
- la liste des configurations successives de l’automate,
- la sortie ´eventuellement produite,
- le diagnostic d’acceptation de l’entr´ee ou l’explication d’un ´eventuel blocage.

Lors de la d´emonstration `a un enseignant, votre moteur doit indiquer clairement l’´etat dans
lequel l’automate s’est arrˆet´e : l’automate est bloqu´e au milieu d’un mot et le moteur justifie
pourquoi, l’automate a tout lu et le moteur explique si le mot est accept´e ou pas, etc.
Rappels :

- Un automate d´eterministe poss`ede un seul ´etat initial, mais peut avoir plusieurs ´etats
acceptants.
- Un automate qui a plusieurs ´etats initiaux est n´ecessairement non d´eterministe.
- Un automate peut g´en´erer des sorties. Nous ne consid`ererons pas d’automates non-d´eterministes g´en´erant des sorties, par contre vous devez dans cette premi`ere partie prendre en compte les ´eventuelles sorties.
- Un automate non-complet peut bloquer au milieu d’un mot, faute de trouver une transition.


### Description de l’automate

Elle est contenue dans un fichier .descr et respecte la syntaxe d´efinie en annexe.
Pour tester votre moteur d’automate, vous devez cr´eer vous-mˆeme des automates de test.
Les enseignants valideront votre travail `a l’aide de leurs propres jeux d’essais, conformes `a cette syntaxe.
Dans un premier temps, vous ne travaillez qu’avec des automates d´eterministes mais votre moteur devra ensuite ˆetre capable de travailler avec tous les automates d´efinis par un fichier .descr. En particulier, un automate ayant plusieurs ´etat initiaux, ayant des λ-transitions, etc.

### Remarque

Le sujet vous laisse une grande latitude dans vos choix d’impl´ementation. Prenez le temps de bien analyser le probl`eme avant de vous lancer dans le codage. Les d´efinitions donn´ees dans le document de cours peuvent ˆetre un guide utile . . .
Prenez ´egalement soin de maintenir un code propre et comment´e ; validez vous-mˆeme votre code `a l’aide de tests unitaires.

# D´eterminisation d’un AEFND

## Objectif

Le but de cette partie est d’´etendre le travail pr´ec´edent avec la d´eterminisation d’un automate N non-d´eterministe avec λ−transitions.
Votre application construira l’automate d´eterministe D ´equivalent `a N et en produira une repr´esentation compatible avec le moteur que vous avez mis au point dans la premi`ere partie.

Vous devez donc pouvoir faire fonctionner N en deux ´etapes :

- 1. D´eterminisation de N avec cette seconde partie (donne D)
- 2. Emulation de ´ D par le moteur de la premi`ere partie.

##  Sp´ecifications de l’application
##  Description de l’AEF non d´eterministe

C’est la mˆeme que celle de la partie pr´ec´edente (fichier .descr). Vous aurez probablement `a
modifier les m´ethodes de lecture d’un automate `a partir d’un fichier .descr pour tenir compte
des ´etats initiaux multiples, des λ−transitions et des configurations `a ´etats successeurs multiples.

## Description de l’AEF d´eterministe produit

Elle sera contenue dans un fichier texte et respectera les contraintes de la premi`ere partie. Vous
impl´ementerez donc une m´ethode permettant d’exporter au format .descr.
Elle devra pouvoir ˆetre fournie au moteur de la premi`ere partie, sans modification.

### Algorithme mis en œuvre

C’est celui vu en cours. Vous n’avez pas, ici, `a minimiser l’automate obtenu.
Pour illustrer votre compr´ehension de cet algorithme et favoriser la mise au point de votre
application, il serait souhaitable que les m´ethodes calculant λ-fermeture(T) et transiter(T, a)
soient explicit´ees dans votre code.
Ce n’est donc peut-ˆetre pas une perte de temps, que de formuler la structure de votre code, en
utilisant au plus pr`es le formalisme du document de cours . . .
### Bilan
Une fois cette deuxi`eme ´etape termin´ee, votre projet doit ˆetre capable de :
- Lire un fichier .descr d’automate quelconque (d´eterministe ou non, avec lambda-transitions, plusieurs ´etats initiaux, etc.).-
- Produire un fichier .descr ou .dot.
- Une fois l’automate charg´e en m´emoire, lire des phrases et les analyser.
- D´eterminiser un automate.

