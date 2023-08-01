# Exercice 1 : Comprendre l'exécution d'un programme

Vous trouverez ci-dessous une capture d'écran du simulateur RISC développé par Peter Higginson : [https://peterhigginson.co.uk/RISC/](https://peterhigginson.co.uk/RISC/)

<img class="centre image-responsive" src="data/risc.png" alt="capture d'écran simulateur RISC">

✍️ **Question 1** : Identifiez, en les entourant, les 4 parties de l'architecture de von Neumann sur ce simulateur. Entourez également le CPU et localisez les registres <span style="font-weight:bold;font-family:consolas;font-size:1.1em;">PC</span> et <span style="font-weight:bold;font-family:consolas;font-size:1.1em;">IR</span>.

✍️ **Question 2** : Traduisez par des phrases chacune des instructions du programme en langage d'assemblage suivant (aidez-vous du tableau donné dans le cours) :

```
MOV R0,#34
STR R0,33
HLT
```

Ouvrez le simulateur à l'adresse [https://peterhigginson.co.uk/RISC/](https://peterhigginson.co.uk/RISC/) et sélectionnez "binary" dans le menu déroulant "OPTIONS" afin d'obtenir une visualisation de la mémoire en binaire (comme c'est le cas en réalité). Vous devez obtenir un écran similaire à la capture donnée au-dessus.

💻✍️ **Question 3** : Recopiez dans la partie de gauche "Assembly Language" le programme ci-dessus et validez en cliquant sur le bouton "Submit". Le programme a été traduit en langage machine et est stocké dans la mémoire à partir de l'adresse 0. Repérez et recopiez sur votre feuille les mots binaires de ce programme en langage machine.

💻✍️ **Question 4** : Exécutez le programme pas à pas en cliquant sur le bouton STEP à chaque étape (vous pouvez diminuer ou augmenter la vitesse de l'animation) en prenant soin d'observer et comprendre ce qu'il se passe. Pour chaque instruction, rédigez de manière détaillés ce qu'il se passe en faisant le lien avec le cours.

# Exercice 2 : Comprendre l'exécution d'un programme (suite)

✍️ **Question 1** : Traduire par des phrases chacune des instructions machine du programme suivant :

```
MOV R0,#34
MOV R1,#5
SUB R0,#30
ADD R0,R0,R1
STR R0,12
HLT
```

✍️ **Question 2** : Quels sont les états des registres à la fin du programme et quelle est la valeur stockée dans la case mémoire 12 ?

💻 **Question 3** : Recopiez le programme dans le simulateur, lancez l'exécution et observez ce qu'il se passe à chaque étape en faisant le lien avec le cours.

# Exercice 3 : Cas des instructions conditionnelles

## Instructions de comparaisons et de saut

Il existe d'autres instructions que celles que l'on a vues (pour information, la liste complète est disponible à l'adresse [http://www.peterhigginson.co.uk/RISC/instruction_set.pdf](http://www.peterhigginson.co.uk/RISC/instruction_set.pdf)).

En voici quelques unes importantes concernant les _comparaisons_ et _sauts_ (ruptures de séquence) qui permettent de faire des tests (instructions conditionnelles).

<table class="tg first-column-not-bold" style="border-collapse:collapse;border-spacing:0;margin:auto;font-size:1em;">
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
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"><span style="font-family:consolas; font-size:1.1em;">BRA 42</span></td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Il s'agit d'un saut inconditionnel (<span style="font-family:consolas; font-size:1.1em;">BRA</span> pour <em>branch</em> que l'on peut traduire par "bifurcation") : indique que la prochaine instruction à exécuter se situe en mémoire à l'adresse <span style="font-family:consolas; font-size:1.1em;">42</span>.</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"><span style="font-family:consolas; font-size:1.1em;">CMP R0,#23</span></td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Compare (<span style="font-family:consolas; font-size:1.1em;">CMP</span> pour <em>compare</em>) la valeur stockée dans le registre <span style="font-family:consolas; font-size:1.1em;">R0</span> et le nombre 23. Cette instruction <span style="font-family:consolas; font-size:1.1em;">CMP</span> doit précéder une instruction de saut conditionnel <span style="font-family:consolas; font-size:1.1em;">BEQ</span>, <span style="font-family:consolas; font-size:1.1em;">BNE</span>, <span style="font-family:consolas; font-size:1.1em;">BGT</span>, <span style="font-family:consolas; font-size:1.1em;">BLT</span> (voir ci-dessous).</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;"><span style="font-family:consolas; font-size:1.1em;">CMP R0,R1</span></td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">Compare la valeur stockée dans le registre <span style="font-family:consolas; font-size:1.1em;">R0</span> et la valeur stockée dans le registre <span style="font-family:consolas; font-size:1.1em;">R1</span>.</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">
                <span style="font-family:consolas; font-size:1.1em;">CMP R0,#23</span>
                <br>
                <span style="font-family:consolas; font-size:1.1em;">BEQ 78</span>
            </td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">La prochaine instruction à exécuter se situe à l'adresse mémoire 78 si la valeur stockée dans le registre <span style="font-family:consolas; font-size:1.1em;">R0</span> est égale à <span style="font-family:consolas; font-size:1.1em;">23</span>.
                <br>
                <span style="font-family:consolas; font-size:1.1em;">BEQ</span> signifie <em>Branch if EQual</em> (birfurcation si les deux opérandes sont égales).</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">
                <span style="font-family:consolas; font-size:1.1em;">CMP R0,#23</span>
                <br>
                <span style="font-family:consolas; font-size:1.1em;">BNE 78</span>
            </td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">La prochaine instruction à exécuter se situe à l'adresse mémoire 78 si la valeur stockée dans le registre <span style="font-family:consolas; font-size:1.1em;">R0</span> n'est pas égale à <span style="font-family:consolas; font-size:1.1em;">23</span>.
                <br>
                <span style="font-family:consolas; font-size:1.1em;">BNE</span> signifie <em>Branch if Not Equal</em> (birfurcation si les deux opérandes ne sont pas égales).</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">
                <span style="font-family:consolas; font-size:1.1em;">CMP R0,#23</span>
                <br>
                <span style="font-family:consolas; font-size:1.1em;">BGT 78</span>
            </td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">La prochaine instruction à exécuter se situe à l'adresse mémoire 78 si la valeur stockée dans le registre <span style="font-family:consolas; font-size:1.1em;">R0</span> est strictement supérieure à <span style="font-family:consolas; font-size:1.1em;">23</span>.
                <br>
                <span style="font-family:consolas; font-size:1.1em;">BGT</span> signifie <em>Branch if Greater Than</em> (birfurcation si la première opérande est strictement supérieure à la deuxième).</td>
        </tr>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">
                <span style="font-family:consolas; font-size:1.1em;">CMP R0,#23</span>
                <br>
                <span style="font-family:consolas; font-size:1.1em;">BLT 78</span>
            </td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">La prochaine instruction à exécuter se situe à l'adresse mémoire 78 si la valeur stockée dans le registre <span style="font-family:consolas; font-size:1.1em;">R0</span> est strictement inférieure à <span style="font-family:consolas; font-size:1.1em;">23</span>.
                <br>
                <span style="font-family:consolas; font-size:1.1em;">BLT</span> signifie <em>Branch if Less Than</em> (birfurcation si la première opérande est strictement inférieure à la deuxième).</td>
        </tr>
    </tbody>
</table>

✍️ **Question 1** : En vous aidant du tableau ci-dessus, traduisez chacune des instructions suivantes.

<table class="tg first-column-not-bold" style="border-collapse:collapse;border-spacing:0;margin: auto;font-size:0.9em;">
    <tbody>
        <tr>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">
            <span style="font-family:consolas; font-size:1.1em;">CMP R2,#100</span>
            <br>
            <span style="font-family:consolas; font-size:1.1em;">BNE 36</span>
            </td>
            <td style="text-align:left;border-color:black;border-style:solid;border-width:1px;
  overflow:hidden;padding:5px 5px;word-break:normal;background:white;">
            <span style="font-family:consolas; font-size:1.1em;">CMP R1,R2</span>
            <br>
            <span style="font-family:consolas; font-size:1.1em;">BGT 36</span>
            </td>
        </tr>
    </tbody>
</table>

✍️ **Question 2** : Donnez l'instruction en assembleur correspondant à la phrase suivante : _Si la valeur située dans le registre <span style="font-family:consolas; font-size:1.1em;">R3</span> est strictement inférieure à la valeur 5, l'instruction suivante est située à l'adresse mémoire 40_.

## Utilisation d'étiquettes

En réalité, on va plutôt utiliser des _étiquettes_ (ou _label_ en anglais) avec les opérations <span style="font-family:consolas; font-size:1.1em;">BRA</span>,<span style="font-family:consolas; font-size:1.1em;">BRA</span>, <span style="font-family:consolas; font-size:1.1em;">BEQ</span>, <span style="font-family:consolas; font-size:1.1em;">BNE</span>, <span style="font-family:consolas; font-size:1.1em;">BGT</span>, <span style="font-family:consolas; font-size:1.1em;">BLT</span>, <span style="font-family:consolas; font-size:1.1em;">BRA</span> : on remplace l'adresse mémoire qui suit ces opérations par le nom de l'étiquette. On peut alors définir nous même les instructions de chaque étiquette et donc de chaque partie du programme correspondant à un saut.

>C'est l'assembleur qui se charge lui-même de convertir une étiquette en adresse mémoire.

Par exemple, voici un programme en assembleur dans lequel on utilise une étiquette appelée <span style="font-family:consolas; font-size:1.1em;">Sinon</span>. On a traduit chaque ligne :

```
        MOV R0,#5     // stocke le nombre 5 dans R0
        MOV R2,#6     // stocke le nombre 6 dans R2
        CMP R0,R2     // Compare R0 et R2
        BNE Sinon     // Si R0 != R2, saute à l'étiquette Sinon 
        ADD R0,R0,R2  // R0 <- R0 + R2
        STR R0,42     // stocke la valeur de R0 en mémoire à l'adresse 42
        HLT           // arrête l'exécution du programme
Sinon   SUB R0,R0,R2  // R0 <- R0 - R2
        STR R0,42     // stocke la valeur de R0 en mémoire à l'adresse 42
        HLT           // arrête l'exécution du programme
```

✍️ **Question 3** : Proposez un programme Python pouvant correspondre à ce programme en langage d'assemblage. On nommera `a` et `b` les variables correspondant aux registres R0 et R2. (_Indication_ : il y a une instruction conditionnelle à bien formaliser).

✍️ **Question 4** : Traduisez en langage d'assemblage le programme Python suivant

```python
a = 3
b = 2
if a <= 5:
    b = a + b
else:
    a = a + 3
```

# Exercice 4 : Décodage du code machine

Le [jeu d'instructions](http://www.peterhigginson.co.uk/RISC/instruction_set.pdf) du simulateur RISC donne le code binaire de toutes les opérations. On a regroupé dans le tableau ci-dessous certaines d'entre elles.

| Code d'opération | En langage assembleur | Description |
| --- | --- | --- |
| 0000 0 | HLT | Arrêt de l'exécution du programme |
| 0001 0 | ADD Rd,#nb | Ajoute le nombre nb à la valeur du registre Rd et stocke le résultat dans Rd |
| 0001 1 | SUB Rd,#nb | Soustrait le nombre nb à la valeur du registre Rd et stocke le résultat dans Rd |
| 0010 0 | CMP Rb,#nb | Compare le nombre nb à la valeur du registre Rb |
| 0010 1 | MOV Rd,#nb | Stocke le nombre nb dans le registre Rd |
| 0110 000 | ADD Rd,Rs,Rb | Ajoute la valeur de Rb à celle de Rs et stocke le résultat dans Rd |
| 0110 001 | SUB Rd,Rs,Rb | Soustrait la valeur de Rb à celle de Rs et stocke le résultat dans Rd |
| 100... | BRA/B&lt;cond&gt; | Instructions de saut --> voir tableau suivant
| 1110 | STR Rd,adr | Stocke la valeur du registre Rd à l'adresse mémoire adr |
| 1111 | LDR Rd,adr | Charge dans le registre Rd la valeur située à l'adresse mémoire adr |
| 0111 0110 10 | CMP Rd,Rs | Compare la valeur de Rs à celle de Rd |

Les instructions de saut ont un code de la forme <span style="font-family:consolas; font-size:1.1em;">100x xxxa aaaa aaaa</span> où xxxx correspond au type de comparaison (sur 4 bits) et aaaaaaaaa correspond à l'adresse mémoire (de l'étiquette en général) sur 9 bits. Voici un tableau récapitulatif :

| Code d'opération | En langage assembleur |
| --- | --- |
| 1000 000 | BRA |
| 1000 001 | BEQ |
| 1000 010 | BNE |
| 1001 100 | BGT |
| 1001 101 | BLT |

Tous ces codes d'opérations traduisent les opérations HTL, ADD, SUB, CMP, etc. Elles sont à compléter par les valeurs binaires des opérandes. 

Dans le cas du simulateur RISC :
* il y a 8 régistres, de R0 à R7, chacun étant codé sur 3 bits : 000 pour R0, 001 pour R1, 010 pour R2, ..., 111 pour R7.
* les adresses mémoires sont codées par leur numéro en binaire
* chaque adresse mémoire (donc chaque instruction) est codée sur 16 bits

✍️ **Question 1** : Identifiez dans chaque instruction machine, le code d'opération et la valeur des opérandes du langage assembleur.

| Instruction machine | En langage assembleur |
| --- | --- |
| 0010101000001011| MOV R2,#8 |
| 0110000101100001 | ADD R5,R4,R1  |
| 1000010000110100 | BNE 50 |



✍️ **Question 2** : Traduisez en langage machine les instructions correspondant à l'instruction : <span style="font-family:consolas; font-size:1.1em;">CMP R3,#13</span>. 

Même question avec : <span style="font-family:consolas; font-size:1.1em;">BLT 20</span>.

>**Astuce** : Pour convertir un nombre entier en binaire on peut utiliser la fonction `bin` de Python :
>
>```python
>>>> bin(27)
>'0b11011'
>```
>
> Cela signfifie que la valeur binaire de l'entier 27 est `11011` (on tient compte uniquement de ce qui suit les caractères `0b`). On peut rajouter autant de 0 que nécessaire à l'avant (`011011` ou `00011011`, etc.), cela ne change pas la valeur binaire.

✍️ **Question 3** : Retrouvez les instructions en assembleur correspondant au code machine suivant en jouant le rôle de l'unité de contrôle (UC) lors de la phase de _décodage_.

```
0010100000000101
1111001000001100
0110000001001000
1110001000001101
0000000000000000
```

>**Astuce** : Pour convertir un nombre binaire en un entier, on peut utiliser la fonction `int` de Python :
>
>```python
>>>> int('11011', 2)
>27
>```
>
> Cela signifie que le nombre binaire `11011` correspond à l'entier 27. Le deuxième paramètre passé à la fonction `int` est un `2` pour indiquer que le premier paramètre est donné en binaire (2 car deux valeurs possibles : 0 et 1).

# Exercice 5 (Bonus)

✍️ **Question** : Écrivez en assembleur les instructions correspondant à l'algorithme suivant :

```
s ← 0
Lire x
Tant que x >= 0 faire
    s ← s + x
    Lire x
fin Tant que
Afficher s
```

On supposera que les variables `s` et `x` sont stockées respectivement dans les registres R0 et R1.

Vous utiliserez à bon escient la documentation du simulateur RISC : [http://www.peterhigginson.co.uk/RISC/instruction_set.pdf](http://www.peterhigginson.co.uk/RISC/instruction_set.pdf). 

Par exemple, l'instruction <span style="font-family:consolas; font-size:1.1em;">Lire x</span> s'écrit <span style="font-family:consolas; font-size:1.1em;">INP R1,2</span>.

---

**Références :**

- Equipe pédagogique DIU EIL, Université de Nantes.
- [Jeu d'instructions](http://www.peterhigginson.co.uk/RISC/instruction_set.pdf) du simulateur RISC de Peter Higgison 
- Cours de David Roche sur le [Modèle d'architecture de von Neumann](https://pixees.fr/informatiquelycee/prem/c8c.html)

---
Germain BECKER, Lycée Mounier, ANGERS 

![Licence Creative Commons](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)
