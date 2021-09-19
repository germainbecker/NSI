<h1 style="font-size: 30px; text-align: center">Modèle relationnel - EXERCICES</h1>

---

# Exercice 1

Deux relations modélisent la flotte de voitures d'un réseau de location de voitures.

- Relation _Agence_ :

| id_agence | ville     | département |
|-----------|-----------|-------------|
| 1         | Paris     | 75          |
| 2         | Lyon      | 69          |
| 3         | Marseille | 13          |
| 4         | Aubagne   | 13          |

- Relation _Voiture_ :

| id_voiture | marque  | modèle | kilométrage | couleur | id_agence |
|------------|---------|--------|-------------|---------|-----------|
| 1          | Renault | Clio   | 12000       | Rouge   | 2         |
| 2          | Peugeot | 205    | 22000       | Noir    | 3         |
| 3          | Toyota  | Yaris  | 33000       | Noir    | 3         |

**Questions**

1. Combien la relation _Voiture_ comporte-t-elle d'attributs ?
2. Que vaut son cardinal (= le nombre d'enregistrements) ?
3. Quel est le domaine de l'attribut `id_agence`  dans la relation _Voiture_ ?
4. Quel est le schéma relationnel de la relation _Agence_ ?
5. Quelle est la clé primaire de la relation _Agence_ ?
6. Quelle est la clé primaire de la relation _Voiture_ ?
7. Quelle est la clé étrangère de la relation _Voiture_ ?
8. Quel est le schéma relationnel de la relation _Voiture_ ?


# Exercice 2

Considérons la base de données Tour de France 2020, contenant les relations suivantes : 

* Relation Equipe :

| code_equipe | nom_equipe |
|------|-----------------------------|
| ALM  |  AG2R La Mondiale           |
| AST  |  Astana Pro Team            |
| TBM  |  Bahrain - McLaren          |
| BOH  |  BORA - hansgrohe           |
| CCC  |  CCC Team                   |
| COF  |  Cofidis, Solutions Crédits |
| DQT  |  Deceuninck - Quick Step    |
| EF1  |  EF Pro Cycling             |
| GFC  |  Groupama - FDJ             |
| LTS  |  Lotto Soudal               |
| ...  | ...                         |

* Relation _Coureur_

| dossard | nom_coureur  | prenom_coureur | code_equipe |
|---------------|-------------|---------------|------------|
| 141           | LÓPEZ       | Miguel Ángel  | AST        |
| 142           | FRAILE      | Omar          | AST        |
| 143           | HOULE       | Hugo          | AST        |
| 11            | ROGLIČ      | Primož        | TJV        |
| 12            | BENNETT     | George        | TJV        |
| 41            | ALAPHILIPPE | Julian        | DQT        |
| 44            | CAVAGNA     | Rémi          | DQT        |
| 45            | DECLERCQ    | Tim           | DQT        |
| 121           | MARTIN      | Guillaume     | COF        |
| 122           | CONSONNI    | Simone        | COF        |
| 123           | EDET        | Nicolas       | COF        |
| …             | …           | …             | …          |


* Relation _Etape_ :

| num_etape   | ville_depart | ville_arrivee     | km  |
|-------------|--------------|-------------------|-----|
| 1           | Nice         | Nice              | 156 |
| 2           | Nice         | Nice              | 185 |
| 3           | Nice         | Sisteron          | 198 |
| 4           | Sisteron     | Orcières-Merlette | 160 |
| 5           | Gap          | Privas            | 198 |
| ...         | ...          | ...               | ... |

* Relation _Temps_ :

| dossard | num_etape | temps |
|:-------------:|:-----------:|:------------:|
| 41            | 2           | 04:55:27     |
| 121           | 4           | 04:07:47     |
| 11            | 5           | 04:21:22     |
| 122           | 5           | 04:21:22     |
| ...           | ...         | ...          |

**Questions**

1. Donner le schéma de la base de données.
2. Quel temps a réalisé Guillaume MARTIN sur l'étape Sisteron / Orcières-Merlette ?
3. À l'arrivée à Privas, qui est arrivé le premier entre Primož ROGLIČ et Simone CONSONNI ?
4. Comment modifier le schéma de la base pour connaître le vainqueur de chaque étape ?

# Exercice 3

On considère une base de données permettant de gérer des réservations dans une compagnie d'hôtels. Voic le schéma de cette base :

<pre style="padding-bottom:10px;">
    <code><em>Client</em>(<span style="padding-bottom:3px; border-bottom: 1px solid black;"><em>nom</em></span> TEXT, <span style="padding-bottom:3px; border-bottom: 1px solid black;"><em>prenom</em></span> TEXT)</code>
</pre>
<pre style="padding-bottom:10px;">
    <code><em>Reservation</em>(<span style="padding-bottom:1px; border-bottom: 1px solid black;"><em>id_reservation</em></span> INT, <em>num_chambre</em> INT, <em>nom_hotel</em> TEXT)</code>
</pre>
<pre style="padding-bottom:10px;">
    <code><em>Hotel</em>(<span style="padding-bottom:3px; border-bottom: 1px solid black;"><em>id_hotel</em></span> TEXT, <em>nom_hotel</em> TEXT, <em>adresse</em> TEXT)</code>
</pre>
<pre style="padding-bottom:10px;">
    <code><em>Chambre</em>(<span style="padding-bottom:3px; border-bottom: 1px solid black;"><em>num_chambre</em></span> INT, <em>nom_hotel</em> TEXT, <em>prix</em> INT)</code>
</pre>

Repérez, expliquez et corrigez toutes les anomalies dans le schéma relationnel de cette base.

# Exercice 4

Une sandwicherie effectuant des livraisons à domicile dispose d'une base de données dont certains extraits de tables sont reproduits ici.

La table _Sandwich_ comporte les informations relatives aux sandwichs proposés à la vente :

| nom_sandwich   | prix   |
|----------------|--------|
| Cheesburger    | 3,90   |
| Double cheese  |  4,90  |
| Italien        |  4,90  |
| Foie gras      |  15,00 |

La table _Client_ comporte les informations relatives aux clients :

| nom      | prenom | adresse                            | numero_client |
|----------|--------|------------------------------------|---------------|
| Bernard  | Alain  | 9, rue Bienvenue, 13008 MARSEILLE | 42            |
| Bernard  | Yves   | 2, rue Vive la joie, 13400 AUBAGNE | 51            |

La table _Commande_ comporte les informations relatives aux commande passées :

| numero_client | nom_sandwich | quantite | numero_commande | date       |
|---------------|--------------|----------|-----------------|------------|
| 42            | Italien      | 2        | 12452           | 2020-12-11 |
| 42            | Foie gras    | 1        | 12452           | 2020-12-11 |
| 51            | Cheesburger  | 4        | 13301           | 2020-12-23 |



**Questions**

1. Une commande peut-elle comporter plusieurs sandwichs de types différents ?
2. Quel est le schéma des relations _Sandwich_ et _Client_ ? Vous identifierez les clés primaires et étrangères de ces deux tables.
3. La relation _Commande_ possède-t-elle un attribut pouvant être clé primaire ? En l'absence d'un attribut clé primaire, un couple ou un triplet d'attributs peut-il jouer ce rôle ? Expliquer.
4. Cette base de données semble-t-elle bien modélisée ? Si ce n'est pas le cas, proposer des modifications.

# Exercice 5

Donner la modélisation relationnelle d'un bulletin scolaire. Cette dernière doit permettre de mentionner :

- des élèves, possédant un numéro d'étudiant alphanumérique unique
- un ensemble de matières fixées, mais qui ne sont pas données
- au plus une note sur 20, par élève et par matière


***Correction***

<pre style="padding-bottom:10px;">
    <code><em>Eleve</em>(<span style="padding-bottom:3px; border-bottom: 1px solid black;"><em>num_eleve</em></span> INT, <em>nom</em> TEXT, <em>prenom</em> TEXT)</code>
</pre>

<pre style="padding-bottom:10px;">
    <code><em>Matiere</em>(<span style="padding-bottom:3px; border-bottom: 1px solid black;"><em>id_matiere</em></span> INT, <em>intitule</em> TEXT)</code>
</pre> 

<pre style="padding-bottom:10px;">
    <code><em>Note</em>(<span style="padding-bottom:3px; border-bottom: 1px solid black;"><em>#id_matiere</em></span> INT, <span style="padding-bottom:3px; border-bottom: 1px solid black;"><em>#num_eleve</em></span> INT, <em>note</em> FLOAT)</code>
</pre> 

# Exercice 6

On considère dans cet exercice une base de données stockant des informations sur les élèves d'un lycée. En voici un extrait :

| nom      | prenom  | date_naissance | classe | option1     | option2  | option3      |
|----------|---------|----------------|--------|-------------|----------|--------------|
| Armand   | Léa     | 12/02/05       | 1G1    | Maths       | NSI      | LLCE Anglais |
| Joulain  | Marie   | 13/01/06       | 2de3   | DNL Anglais | NULL     | NULL         |
| Marchand | Anthony | 12/12/05       | 1G1    | HGGSP       | SES      | Maths        |
| Marchand | Sophie  | 06/04/04       | TG2    | Maths       | Physique | NULL         |

**Questions**

1. Quel est le schéma relationnel de cette base ?
2. Quel défaut de conception majeur présente cette base de données ?
3. Certains attributs n'existent pas pour certains enregistrements. Scindez cette table en deux tables pour éviter ce problème. Vous donnerez les enregistrements des deux tables.


--- 
**Références**

- Exercices 1 et 2 : d'après la [page github](https://github.com/glassus/terminale_nsi/blob/main/docs/T4_Bases_de_donnees/4.1_Modele_relationnel/02_exercices.md) de Gilles Lassus.
- Exercices 4 et 6 : d'après *Prépabac NSI, Terminale*, G.CONNAN, V.PETROV, G.ROZSAVOLGYI, L.SIGNAC, éditions HATIER.
- Exercice 5 : d'après *Numérique et Sciences Informatiques, 24 leçons, Terminale*, T. BALABONSKI, S. CONCHON, J.-C. FILLIATRE, K. NGUYEN, éditions ELLIPSES.

---
Germain BECKER, Lycée Mounier, ANGERS
