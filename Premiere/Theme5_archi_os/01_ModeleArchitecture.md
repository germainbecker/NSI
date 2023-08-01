# Architecture de von Neumann

Les grands principes de fonctionnement des ordinateurs actuels résultent de travaux menés au milieu des années 1940. Ces travaux ont défini un schéma d'architecture appelée **architecture de von Neumann**, en référence à <a href="https://fr.wikipedia.org/wiki/John_von_Neumann" target="_blank">John Von Neumann</a> (1903-1957), un mathématicien et physicien (et bien d'autres choses) américano-hongrois qui a participé et publié les travaux en 1945.

<img class="centre image-responsive" src="data/JvN.jpg" width="300">
<span class="image-licence" style="display: block;text-align: center;font-size: 0.9em;color: #aaa;">John von Neumann. Source :
    <a href="https://commons.wikimedia.org/wiki/File:JohnvonNeumann-LosAlamos.jpg">Wikimedia Commons</a>
</span>

Avant de détailler cette architecture, commençons par une petite activité.


### Activité 1 : Composants d'un ordinateur

Lorsqu'on ouvre un ordinateur, quelle que soit sa marque, nous retrouvons en général les mêmes éléments : le processeur ou microprocesseur, la mémoire vive (RAM), la carte mère, la carte graphique, interface de connexion des périphériques, le lecteur de disque, le disque dur, le clavier, l'écran, la souris, l'alimentation électrique.  

**Question 1** : Associez le bon élément à chaque numéro du schéma ci-dessous.

<table class="tg" style="width:100%;border-collapse:collapse;border-spacing:0;margin: auto; font-size:1em;">
    <tbody>
        <tr>
            <td rowspan="0" style="width:50%;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;text-align:center;background:white;">
                <img class="centre image-responsive" src="data/Personal_computer.svg" style="max-width=512px;">
                <span class="image-licence" style="display: block;text-align: center;font-size: 0.9em;color: #aaa;">Crédit : 
                    <a href="https://commons.wikimedia.org/wiki/File:Personal_computer,_exploded_4.svg">Gustavb</a>, <a href="http://creativecommons.org/licenses/by-sa/3.0/">CC BY-SA 3.0</a>, via Wikimedia Commons
                </span>
            </td>            
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">1 :</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">2 :</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">3 :</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">4 :</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">5 :</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">6 :</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">7 :</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">8 :</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">9 :</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">10 :</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">11 :</td>
        </tr>
    </tbody>
</table>

**Question 2** : Associez chaque élément à sa description

<table class="tg" style="width:100%;border-collapse:collapse;border-spacing:0;margin: auto;font-size:1em;">
    <tbody>
        <tr>
            <td style="width:50%;text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Cerveau de l'ordinateur, qui permet à l'ordinateur d'effectuer les opérations (calculs) demandés.</td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"></td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Stocke les informations des programmes et données en cours de fonctionnement</td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"></td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Relie tous les éléments constituant un ordinateur.
Sa principale fonction est la mise en relation de ces composants par des bus sous forme de circuits imprimés.</td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"></td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Carte d’extension d'ordinateur qui permet de produire une image affichable sur un écran.</td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"></td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Périphérique d’entrée qui permet d’écrire</td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"></td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Assure la mise sous tension de l'ensemble des composants</td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"></td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Périphérique d'entrée-sortie qui stocke les données de base de la machine.</td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"></td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Périphérique d'entrée-sortie, assure le stockage et la lecture de données sur support externe non volatile</td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"></td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Périphérique d’entrée qui permet de déplacer le curseur de pointage à l'écran</td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"></td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Permet de connecter les périphériques (disque dur, lecteur DVD, etc.) à la carte mère.</td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"></td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Périphérique de sortie qui permet de visualiser les informations venant de l'ordinateur</td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"></td>
        </tr>
    </tbody>
</table>

## Principe de l'architecture

L'idée majeure de l'architecture de von Neumann, était d'utiliser une zone de stockage _unique_, à savoir la mémoire de l'ordinateur, pour conserver à la fois les _programmes_ (instructions) et les _données_ qu'ils devaient manipuler.

<blockquote class="information">
    <p>Les travaux de von Neumann publiés en 1945 concernaient la conception de l'<a href="https://fr.wikipedia.org/wiki/Electronic_Discrete_Variable_Automatic_Computer" target="_blank">EDVAC</a>, un ordinateur basé sur cette architecture. Cet ordinateur était capable d'additionner, soustraire, multiplier et diviser en binaire. Sa capacité mémoire est l'équivalent actuel de 5,5 ko, alors qu'il occupait une surface de 45 m² et pesait presque 8 tonnes. Pour le faire fonctionner, trois équipes de trente personnes se succédaient en continu.</p>
</blockquote>

Dans l'architecture de von Neumann, un ordinateur est composé de 4 parties :

* L'**unité artithmétique et logique** (UAL ou _ALU_ en anglais) ou unité de traitement : son rôle est d'effectuer les opérations (calculs) de base ;
* L'**unité de contrôle** (UC ou _CU_ en anglais pour Control Unit) : c'est le chef d'orchestre de l'ordinateur, elle récupère les instructions du programme en mémoire et les données sur lesquelles doivent s'opérer les instructions (via des bus de communication), puis les envoie à l'unité arithmétique et logique ;
* La **mémoire** qui contient les programmes ET les données, et qui indiquera à l'unité de contrôle quels sont les calculs à faire sur ces données ;
* Les dispositifs d'**entrée-sortie** pour communiquer avec l'extérieur

Le **CPU** (_Central Processing Unit_ ou Unité Centrale de Traitement), aussi appelé **processeur**, regroupe à la fois l'unité artithmétique et logique et l'unité de contrôle.

<blockquote class="information">
    <p>Lorsque le processeur rassemble ce deux unités dans un seul et même circuit électronique, on parle de <em>microprocesseur</em>.</p>
</blockquote>

<img class="centre image-responsive" src="data/archiVN.svg" width="500">

<span class="image-licence" style="display: block;text-align: center;font-size: 0.9em;color: #aaa;">Crédit : image originale <a href="https://commons.wikimedia.org/wiki/File:Von_Neumann_architecture_fr.svg">Schega</a>, <a href="http://creativecommons.org/licenses/by-sa/3.0/">CC BY-SA 3.0</a>, via Wikimedia Commons
</span>

## Fonctionnement (un peu) plus détaillé des composants

Nous décrivons dans ce paragraphe le fonctionnement des 4 parties de l'architecture de von Neumann. Ces informations prendront encore davantage de sens lorsque nous aborderons le _langage machine_ à la fin de ce cours.

**Unité de contrôle**

Elle possède notamment deux _registres_ (= mémoires internes très rapides) :
* le _registre d'instruction_, nommé <span style="font-weight:bold;font-family:consolas;font-size:1.1em;">IR</span> (_Instruction Register_ en anglais), qui contient l'instruction courante à exécuter ;
* le _compteur de programme_, nommé <span style="font-weight:bold;font-family:consolas;font-size:1.1em;">PC</span> (_Program Counter_ en anglais), qui indique l'emplacement mémoire de la prochaine instruction à exécuter.

**Unité arithmétique et logique**

Elle est composée notamment de :
* plusieurs registres, appelés _registres de données_, dans lesquels sont chargés les données sur lesquelles les instructions portent
* d'un registre particulier appelé _accumulateur_ dans lequel vont s'effectuer tous les calculs
* plein de circuits électroniques pour réaliser des opérations arithmétiques (addition, soustraction, etc.), des opérations logiques (et, ou, complément à un, etc.), des comparaisons (égalité, inférieur, supérieur, etc.), des opérations sur les bits (décalages, rotations) ou des opérations de déplacement mémoire (copie de ou vers la mémoire).

<blockquote class="information">
    <p>Nous parlerons davantage de ces circuits électroniques dans un prochain chapitre, à suivre donc...</p>
</blockquote>


Les registres contiennent les valeurs de la mémoire de l'ordinateur nécessaires à l'exécution des instructions. Le résultat d'un calcul (arithmétique ou logique) est stocké dans l'accumulateur et peut être utilisé pour les instructions ultérieures de manière très rapide car cela évite les allers-retours en mémoire (l'accès aux registres est très rapide comparé à l'accès aux données en mémoire).

**La mémoire**

Les échanges de données entre le processeur et la mémoire se font par l'intermédiaire de _bus de communication_.

La mémoire de l'ordinateur (à ne pas confondre avec le disque dur) est composée de plusieurs milliards de circuits mémoires qui sont organisés en agrégats de 8, 16, 32, 64 bits (voire plus) appelés **cases mémoires**. Leur nombre définit la taille mémoire de l'ordinateur et chaque case possède une _adresse_ pour les distinguer. Comme dit précédemment, ces cases mémoires contiennent à la fois les programmes _et_ les données sur lesquelles portent les programmes.

<blockquote class="information">
    <p>Les registres du processeur sont également des cases mémoires, dont l'accès (lecture/écriture) est très rapide. Lorsque l'on parle de processeurs 32 bits, 64 bits, on fait en faire référence à la taille de ces registres.</p>
</blockquote>

**Les dispositifs d'entrée-sortie**

Il en existe un très grand nombre que l'on peut classer en deux catégories : les _périphériques d'entrée_ et les _périphériques de sortie_. Certains appartiennent à ces deux familles.

<blockquote class="question">
    <p>Pouvez-vous citer quelques périphériques de chaque famille ? Et appartenant aux deux ?</p>
</blockquote>

# Le langage machine

Dans cette partie, nous allons voir comment un ordinateur exécute un _programme_.

Un programme est une suite de nombres binaires placés en mémoire représentant des instructions exprimées en **langage machine**. C'est le seul langage que peut comprendre le processeur chargé d'exécuter ces différentes instructions.

Ainsi, un programme écrit dans un langage de programmation évolué (on dit de _haut niveau_) comme Python, Java, C, etc. ne peut pas être compris par le processeur. On doit donc utiliser un _compilateur_ (pour le C, par exemple) ou un _interpréteur_ (pour Python, par exemple) pour transformer le programme en langage machine.

## Instruction machine

Une instruction machine est un mot binaire composé de deux parties :

* le champ _code opération_ qui indique au processeur quelle opération il doit effectuer (charger une donnée en mémoire, faire une addition, une comparaison, etc.)
* le champ _opérandes_ qui indique au processeurs la (les) donnée(s) sur laquelle (lesquelles) doit s'appliquer l'opération (l'adresse mémoire de la donnée à charger, les deux valeurs à additionner, les deux valeurs à comparer, etc.)

Une instruction machine possède le schéma suivant :

<table class="tg" style="border-collapse:collapse;border-spacing:0;margin: auto;font-size:0.9em;">
    <tbody>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">champ code opération</td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">champ opérandes</td>
        </tr>
    </tbody>
</table>

Nous allons voir des exemples tout de suite !

## Le langage _assembleur_

Il n'est pas facile (voire impossible) pour un humain d'écrire directement les mots binaires d'un programme en langage machine. On peut utiliser à la place un langage d'assemblage, appelé **assembleur**, qui est le langage de plus _bas niveau_ d'un ordinateur lisible par un humain. Nous allons détailler un langage d'assemblage pour que vous puissiez comprendre l'exécution d'une séquence d'instructions de type langage machine.

<blockquote class="information">
    <p>Il existe plusieurs sortes de langage assembleur car ce dernier dépend du processeur utilisé.</p>
</blockquote>

Chaque instruction écrite en assembleur possède les deux champs "code opération" et "opérandes".

Dans la suite on utilisera le jeu d'instructions du simulateur RISC développé par Peter Higginson et disponible à cette adresse : <a href="https://peterhigginson.co.uk/RISC/" target="_blank">https://peterhigginson.co.uk/RISC/</a>.

<blockquote class="information">
    <p>On ne donne qu'une partie des instructions possibles, la liste complète est disponible <a href="http://www.peterhigginson.co.uk/RISC/instruction_set.pdf" target="_blank">ici</a>. Vous utiliserez ce simulateur dans les activités pour bien fixer les idées.</p>
</blockquote>

**Exemples d'instructions**

Voici quelques instructions écrites en assembleur et leurs significations.

<table class="tg" style="border-collapse:collapse;border-spacing:0;margin:auto;font-size:1em;">
    <thead>
        <tr>
            <td style="font-weight:bold; text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background-color:white;">Instruction en assembleur</td>
            <td style="font-weight:bold; text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background-color:white;">Signification</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"><span style="font-family:consolas; font-size:1.1em;">LDR R1,12</span></td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Charge dans le registre <span style="font-family:consolas; font-size:1.1em;">R1</span> la valeur stockée à l'adresse mémoire <span style="font-family:consolas; font-size:1.1em;">12</span>.</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"><span style="font-family:consolas; font-size:1.1em;">STR R3,125</span></td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Stocke la valeur du registre <span style="font-family:consolas; font-size:1.1em;">R3</span> en mémoire vive à l'adresse <span style="font-family:consolas; font-size:1.1em;">125</span>.</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"><span style="font-family:consolas; font-size:1.1em;">ADD R1,#128</span></td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
                       overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Additionne le <em>nombre</em> <span style="font-family:consolas; font-size:1.1em;">128</span> (une valeur immédiate est identifiée grâce au symbole <span style="font-family:consolas; font-size:1.1em;">#</span>) et la valeur stockée dans le registre <span style="font-family:consolas; font-size:1.1em;">R1</span>, stocke le résultat dans le registre <span style="font-family:consolas; font-size:1.1em;">R1</span>.</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"><span style="font-family:consolas; font-size:1.1em;">ADD R0,R1,R2</span></td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
                       overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Additionne la valeur stockée dans le registre <span style="font-family:consolas; font-size:1.1em;">R1</span> et la valeur stockée dans le registre <span style="font-family:consolas; font-size:1.1em;">R2</span>, stocke le résultat dans le registre <span style="font-family:consolas; font-size:1.1em;">R0</span>.</td>
        </tr>        
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"><span style="font-family:consolas; font-size:1.1em;">SUB R1,#128</span></td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
                       overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Soustrait le <em>nombre</em> <span style="font-family:consolas; font-size:1.1em;">128</span> de la valeur stockée dans le registre <span style="font-family:consolas; font-size:1.1em;">R1</span>, stocke le résultat dans le registre <span style="font-family:consolas; font-size:1.1em;">R1</span>.</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"><span style="font-family:consolas; font-size:1.1em;">SUB R0,R1,R2</span></td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
                       overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Soustrait la valeur stockée dans le registre <span style="font-family:consolas; font-size:1.1em;">R2</span> de la valeur stockée dans le registre <span style="font-family:consolas; font-size:1.1em;">R1</span>, stocke le résultat dans le registre <span style="font-family:consolas; font-size:1.1em;">R0</span>.</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"><span style="font-family:consolas; font-size:1.1em;">MOV R1,#23</span></td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Place le nombre <span style="font-family:consolas; font-size:1.1em;">23</span> dans le registre <span style="font-family:consolas; font-size:1.1em;">R1</span>.</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"><span style="font-family:consolas; font-size:1.1em;">MOV R0,R3</span></td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Place la valeur stockée dans le registre <span style="font-family:consolas; font-size:1.1em;">R3</span> dans le registre <span style="font-family:consolas; font-size:1.1em;">R0</span>.</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"><span style="font-family:consolas; font-size:1.1em;">HLT</span></td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Arrête l'exécution du programme.</td>
        </tr>
    </tbody>
</table>

<blockquote class="information">
    <p>On trouve pour chacune un premier mot de 3 caractères qui correspond au "code opération" suivi d'un espace et des "opérandes".</p>
</blockquote>



Ainsi, le programme Python 

```python
a = 2
b = 7
c = a + b
```

pourrait s'écrire en assembleur de la façon suivante

```
MOV R0,#2
MOV R1,#7
ADD R1,R0,R1
STR R1,21
HLT
```

<blockquote class="question">
    <p>Dans ce cas, quels sont les états des registres à la fin du programme ? Où est stockée la valeur de la variable <code>c</code> à la fin du programme ?</p>
</blockquote>

Ce programme en assembleur peut être converti en une suite d'instructions machine pouvant être exécutées par le processeur. En l'occurrence, dans le cas du simulateur RISC cité plus haut, on obtiendrait, en utilisant la documentation, le code machine suivant (les cases mémoires sont de taille 16 bits ici) : 

<pre><code>0010100000000010 0010100100000111 0110000001000001 1110001000010101 0000000000000000</code></pre>

On peut voir les correspondances, dans le tableau ci-dessous, où on a écrit en rouge le champ _code opération_ :

<table class="tg" style="border-collapse:collapse;border-spacing:0;margin:auto;font-size:1em;">
    <thead>
        <tr>
            <td style="font-weight:bold; text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background-color:white;">
                Instructions machine
            </td>
            <td style="font-weight:bold; text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background-color:white;">
                Correspondance
            </td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background-color:white;">
                <span style="color:#EF2E4B;">00101</span><span style="color:#0C69B2;">000</span><span style="color:#1DB20C;">00000010</span>
            </td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background-color:white;">
                <span style="color:#EF2E4B;">MOV</span> <span style="color:#0C69B2;">R0</span>,<span style="color:#1DB20C;">#2</span>
            </td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background-color:white;">
                <span style="color:#EF2E4B;">00101</span><span style="color:#0C69B2;">001</span><span style="color:#1DB20C;">00000111</span>
            </td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background-color:white;">
                <span style="color:#EF2E4B;">MOV</span> <span style="color:#0C69B2;">R1</span>,<span style="color:#1DB20C;">#7</span>
            </td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background-color:white;">
                <span style="color:#EF2E4B;">0110000</span><span style="color:#0C69B2;">001</span><span style="color:#1DB20C;">000</span><span style="color:#FF8402;">001</span>
            </td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background-color:white;">
                <span style="color:#EF2E4B;">ADD</span> <span style="color:#0C69B2;">R1</span>,<span style="color:#1DB20C;">R0</span>,<span style="color:#FF8402;">R1</span>
            </td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background-color:white;">
                <span style="color:#EF2E4B;">1110</span><span style="color:#0C69B2;">001</span><span style="color:#1DB20C;">000010101</span>
            </td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background-color:white;">
                <span style="color:#EF2E4B;">STR</span> <span style="color:#0C69B2;">R1</span>,<span style="color:#1DB20C;">21</span>
            </td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background-color:white;">
                <span style="color:#EF2E4B;">00000</span><span>00000000000</span>
            </td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background-color:white;">
                <span style="color:#EF2E4B;">HLT</span>
            </td>
        </tr>
    </tbody>
</table>

En copiant le code assembleur dans la fenêtre de gauche du simulateur, on peut observer tout le déroulé de l'exécution du programme (on veillera à choisir l'option "binary" pour voir les mots en mémoire en binaire) : <a href="https://peterhigginson.co.uk/RISC/" target="_blank">https://peterhigginson.co.uk/RISC/</a>

<blockquote class="information">
    <p>Ce simulateur utilise des cases mémoires de 16 bits, les ordinateurs plus récents en ont de taille 64 bits généralement. De plus, le simulateur possède beaucoup d'autres instructions machine, certaines seront développées dans les activités 🙂</p>
</blockquote>

## Cycle et horloge

Un CPU possède une **horloge** qui définit le rythme auquel les instructions sont exécutées. Pour exécuter une instruction, le processeur va effectuer ce qu'on appelle un **cycle d'exécution** qui s'effectue en trois étapes :

1. **Chargement** (_load_ en anglais) : l'unité de contrôle récupère le mot binaire (qui contient la prochaine instruction à exécuter) situé en mémoire à l'adresse indiquée par son registre <span style="font-weight:bold;font-family:consolas;font-size:1.1em;">PC</span> et la stocke dans son registre <span style="font-weight:bold;font-family:consolas;font-size:1.1em;">IR</span> ;
2. **Décodage** : la suite de bits de l'instruction contenue dans le registre <span style="font-weight:bold;font-family:consolas;font-size:1.1em;">IR</span> est décodée pour déduire quelle instruction est à exécuter et sur quelles données. Cette étape peut alors nécessiter de lire d'autres mots binaires depuis la mémoire ou les registres, pour charger les données (les "opérandes") sur lesquelles portent l'opération à effectuer.
3. **Exécution** : l'instruction est exécutée, soit par l'ALU s'il s'agit d'une opération arithmétique ou logique, soit par l'UC s'il s'agit d'une opération de branchement qui va modifier la valeur du registre <span style="font-weight:bold;font-family:consolas;font-size:1.1em;">PC</span>.

Par exemple, un processesseur ayant une fréquence de 3,2 GHz va effectuer 3,2 milliards de cycles d'horloge par seconde. 

<blockquote class="information">
    <p>La fréquence des processeurs a augmenté de manière linéaire depuis les premiers ordinateurs mais stagne depuis une vingtaine d'année car la chaleur produite devient trop importante et pourrait perturber la lecture des informations voire détériorer physiquement les circuits 🌡️🥵</p>
</blockquote>

# Qu'en est-il aujourd'hui ?

Le modèle de von Neumann défini en 1945 est toujours celui utilisé dans les ordinateurs actuels. Évidemment, les composants se sont de plus en plus miniaturisés et sont de plus en plus performant.

Par rapport au schéma initial, deux évolutions sont à noter :

* les entrées-sorties, intialement commandées par le CPU, sont depuis les années 1960 sous le contrôle de processeurs autonomes

* les ordinateurs sont désormais **multiprocesseurs**, c'està-dire qu'ils possèdent plusieurs processeurs, qu'il s'agisse d'unités séparées ou de _coeurs_ multiples à l'intérieur d'une même puce. Cela permet d'atteindre une puissance de calculs élevée sans augmenter la vitesse des processeurs individuels, limitée par les capacités d'évacuation de la chaleur dans des circuits de plus en plus denses.

Ces deux évolutions ont pour conséquence de mettre la mémoire, plutôt que l'unité centrale de contrôle, au centre de l'ordinateur, et d’augmenter le degré de parallélisme dans le traitement et la circulation de l’information. Mais elles ne remettent pas en cause le modèle de von Neumann.

<img class="centre image-responsive" src="data/archiVN_actuelle.svg" width="500">

# Bilan

* Les ordinateurs actuels sont basés sur le modèle de von Neumann, dans lequel la mémoire stocke à la fois les données et les programmes.
* Dans l'architecture de von Neumann, un ordinateur est composé de 4 parties : d'une **unité arithmétique et logique** (ALU), d'une **unité de contrôle** (UC), d'une **mémoire** et de dispositifs d'**entrée-sortie**.
* Le processeur (CPU), composé de l'UAL et de l'UC, est chargé d'exécuter des instructions écrites en **langage machine**, c'est-à-dire des mots écrits en binaire et stockés dans la mémoire.
* Tout programme doit être "converti" en langage machine afin d'être exécuté.
* Le langage **assembleur** est le langage de plus bas niveau lisible par un humain. Il permet donc de programmer "au niveau" du langage machine.

---

**Références :**

- Equipe pédagogique DIU EIL, Université de Nantes.
- Article Wikipédia sur l'[Architecture de von Neumann](https://fr.wikipedia.org/wiki/Architecture_de_von_Neumann)
- Livre *Spécialité Numérique et sciences informatiques : 30 leçons avec exercices corrigés - Première*, éditions Ellipses, T. Balabonski, S. Conchon, J.-C. Filliâtre, K. Nguyen : [http://www.nsi-premiere.fr/](http://www.nsi-premiere.fr/).
- Livre *Informatique et Sciences du Numérique* de Gilles Dowek en téléchargement libre : [ici](https://wiki.inria.fr/wikis/sciencinfolycee/images/a/a7/Informatique_et_Sciences_du_Num%C3%A9rique_-_Sp%C3%A9cialit%C3%A9_ISN_en_Terminale_S._version_Python.pdf)
- Cours de David Roche sur le [Modèle d'architecture de von Neumann](https://pixees.fr/informatiquelycee/prem/c8c.html)
- Article [Le modèle d’architecture de von Neumann](https://interstices.info/le-modele-darchitecture-de-von-neumann/) sur le site interstices.info.
- Wikilivre sur les [composants d'un processeur](https://fr.wikibooks.org/wiki/Fonctionnement_d%27un_ordinateur/Les_composants_d%27un_processeur).
---
Germain BECKER, Lycée Mounier, ANGERS 

![Licence Creative Commons](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)
