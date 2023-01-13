# SQL avec Python

<img class="centre image-responsive" src="data/python_sql.svg" width="700" alt="illustration">

On présente dans ce tutoriel comment utiliser le langage Python, via le module `sqlite3`, pour interagir avec une base de données SQLite. Cela vous permettra d'apprendre à utiliser une base de données dans vos futurs projets.

La vidéo associée est la suivante :

<div class="video-responsive">
    <iframe class="centre" width="560" height="315" src="https://www.youtube-nocookie.com/embed/JiEoZ8Z9oUQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<p class="impression">
Source : <a href="https://youtu.be/JiEoZ8Z9oUQ">https://youtu.be/JiEoZ8Z9oUQ</a>
</p>

# Création et connexion avec la base de données

Premièrement, on doit créer une nouvelle base de données et s'y connecté pour permettre au module `sqlite3` d'intéragir avec elle.

On utilise `sqlite3.connect()` pour créer la connexion avec la base de données `eleves.db` dans le répertoire courant, cette base étant créée si elle n'existe pas.
```python
import sqlite3
conn = sqlite3.connect('eleves.db')
```

L'objet `conn` représente la connexion avec la base de données sur le disque.

Une fois la connexion établie, il est nécessaire de créer un *curseur* grâce à `conn.cursor()` (c'est un objet de la classe `Cursor`).

```python
cur = conn.cursor()
```

Maintenant que nous avons la connexion et un curseur on peut exécuter des requêtes SQL et récupérer les résultats grâce au curseur.

```python
cur.execute("""CREATE TABLE Eleve (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    prenom TEXT,
    age INTEGER,
    classe TEXT);
    """)
```

**Remarques** :
- On peut utiliser des triples guillemets pour écrire les chaînes de requêtes sur plusieurs lignes et mieux les formater visuellement. 
- SQLite ne prévoit que 5 domaines pour les attributs d'une table : `NULL`, `INTEGER`, `REAL`, `TEXT`, `BLOB`. Voir ce lien pour plus de détails : [https://www.sqlite.org/datatype3.html](https://www.sqlite.org/datatype3.html)
- On a utilisé `AUTOINCREMENT` pour ne plus avoir besoin de spécifier l'`id` comme clé primaire : celle-ci s'autoincrémente à chaque nouvel enregistrement dans la base. C'est très utile car la plupart du temps on ne sait pas quelle clé primaire utiliser pour ajouter un nouvel enregistrement.

Une fois la requête exécutée, il ne faut pas oublier de stopper la connexion avec la base de données. On utilise pour cela la méthode `close` :

```python
conn.close()
```

On peut créer une fonction qui permet de créer notre table, en la supprimant si elle existe déjà (pour mieux faire nos essais) :

```python
def creer_table():
    conn = sqlite3.connect('eleves.db')
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS Eleve;")
    cur.execute("""CREATE TABLE Eleve (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        prenom TEXT,
        age INTEGER,
        classe TEXT);
        """)
    conn.close()
```

# Insérer des enregistrements

Pour insérer des enregistrements, on utilise notre curseur pour exécuter des requêtes SQL.

## Insérer un enregistrement

Si on souhaite insérer un élève dans la table `Eleve` on appelle la méthode `cur.execute()` en lui passant en paramètre une chaîne de caractères correspondant à une requête SQL :

```python
cur.execute("INSERT INTO Eleve (id, nom, prenom, age, classe) VALUES (1, 'Dupont', 'Jean', 15, '2A')")
conn.commit()
```

><span style="font-size:1.5em;">⚠️</span> L'instruction `INSERT` crée ce qu'on appelle une *transaction*, qui doit être validée par `conn.commit()` afin que les changements soient enregistrés en base de données !

Dans le cas précédent, on les données à insérer étaient directement écrites dans la chaîne de requête. Or, bien souvent les données que l'on veut utiliser dans une requête sont stockées dans des variables et on peut utiliser ces variables pour construire la chaîne de requête. On appelle cela une **requête préparée**, qui fait appel au caractère `?` de la façon suivante :

```python
eleve_2 = ('Dupont', 'Jeanne', 17, 'TG2')
cur.execute("INSERT INTO Eleve (nom, prenom, age, classe) VALUES (?, ?, ?, ?)", eleve_2)
conn.commit()
```

On passe un `tuple` en deuxième paramètre à notre méthode `execute` : ce tuple contient les valeurs par lesquelles SQLite doit remplacer les `?`. 

> Cette manière de faire permet de se prémunir d'une faille de sécurité appelée **injection SQL** dont nous reparlerons par la suite.

Il est également possible de construire une requête à partir de données mémorisées dans un dictionnaire. Ainsi, on peut insérer un troisième élève de cette façon :

```python
eleve_3 = {'nom': 'Marchand', 'prenom': 'Marie', 'age': 15, 'classe': '2A'}
cur.execute("""INSERT INTO Eleve (nom, prenom, age, classe) VALUES (:nom, :prenom, :age, :classe)""", eleve_3)
conn.commit()
```

De cette façon, SQLite va remplacer `:nom`, `:prenom`, `:age` et `:classe` dans la chaîne de requête par les valeurs associées aux clés `'nom'`, `'prenom'`, `'age'` et `'classe'` du dictionnaire passé en deuxième argument.

L'utilisation des clés des dictionnaires a l'avantage d'être plus explicite et de ne plus se soucier de l'ordre des données (comme pour un tuple par exemple)

## Insérer plusieurs enregistrements

Si on dispose de données sur plusieurs élèves, on peut utiliser une boucle `for` en construisant la chaîne de requête SQL pour chaque élève de la façon suivante :

```python
autres_eleves = [
    ('Martin', 'Adeline', 16, '1G1'),
    ('Dupont', 'Lucas', 15, '2A'),
    ('Richard', 'Louise', 15, '1G2'),
    ('Rouger', 'Marius', 16, '1G2'),
    ('Louapre', 'Lola', 18, 'TG2'),
    ('Boudou', 'Lise', 17, 'TG1'),
    ('Dupont', 'Aurélien', 16, '1G1'),
    ('Laurent', 'Diego', 17, '1G2'),
    ('Martin', 'Anaëlle', 16, 'TG1')
]

for eleve in liste_eleves:
    cur.execute("INSERT INTO Eleve (nom, prenom, age, classe) VALUES (?, ?, ?, ?)", eleve)
conn.commit()
```

En réalité, le code précédent peut se raccourcir en utilisant la méthode `cur.executemany()` qui permet justement d'insérer plusieurs lignes en base de données directement. On préférera donc écrire le code équivalent qui suit :

```python
cur.executemany("INSERT INTO Eleve (nom, prenom, age, classe) VALUES (?, ?, ?, ?)", autres_eleves)
conn.commit()
```

Il suffit de passer en deuxième paramètre à cette méthode une liste de séquences d'éléments (ici une liste de tuples).

> On peut aussi passer une liste de dictionnaires en deuxième paramètre, en prenant soin de remplacer les `?` de la requête par des `:cle` où `cle` désigne une clé du dictionnaire (syntaxe vue plus haut).

# Récupérer des données 

## Les méthodes `fetchall`, `fetchone` et `fetchmany`

On peut exécuter des requêtes d'interrogation de la base de données. On utilise pour cela également la méthode `cur.execute()`. On peut affecter le résultat de la requête dans une variable `res`, qui est alors un itérable que l'on peut utiliser pour afficher les résultats.

Pour renvoyer tous les résultats, on applique la méthode `fetchall()` à `res` :

```python
>>> res = cur.execute("SELECT * FROM Eleve")
>>> res.fetchall()
[(1, 'Dupont', 'Jean', 15, '2A'), (2, 'Dupont', 'Jeanne', 17, 'TG2'), (3, 'Marchand', 'Marie', 15, '2A'),
(4, 'Martin', 'Adeline', 16, '1G1'), (5, 'Dupont', 'Lucas', 15, '2A'), (6, 'Richard', 'Louise', 15, '1G2'),
(7, 'Rouger', 'Marius', 16, '1G2'), (8, 'Louapre', 'Lola', 18, 'TG2'), (9, 'Boudou', 'Lise', 17, 'TG1'), 
(10, 'Dupont', 'Aurélien', 16, '1G1'), (11, 'Laurent', 'Diego', 17, '1G2')]
```

Vous remarquerez que la méthode `fetchall` renvoie une liste de tuples. À ce titre on peut aussi simplement convertir l'itérable `res` en une liste :

```python
>>> res = cur.execute("SELECT * FROM Eleve")
>>> list(res)
[(1, 'Dupont', 'Jean', 15, '2A'), (2, 'Dupont', 'Jeanne', 17, 'TG2'), (3, 'Marchand', 'Marie', 15, '2A'), 
(4, 'Martin', 'Adeline', 16, '1G1'), (5, 'Dupont', 'Lucas', 15, '2A'), (6, 'Richard', 'Louise', 15, '1G2'), 
(7, 'Rouger', 'Marius', 16, '1G2'), (8, 'Louapre', 'Lola', 18, 'TG2'), (9, 'Boudou', 'Lise', 17, 'TG1'), 
(10, 'Dupont', 'Aurélien', 16, '1G1'), (11, 'Laurent', 'Diego', 17, '1G2')]
```

Pour renvoyer un résultat, on applique la méthode `fetchone()` à `res` :

```python
>>> res = cur.execute("SELECT * FROM Eleve")
>>> res.fetchone()
(1, 'Dupont', 'Jean', 15, '2A')
```

La méthode `fetchone` renvoie en réalité la prochaine ligne du résultat de la requête. Par exemple, si on rappelle à nouveau la méthode `fetchone`, elle renvoie le deuxième élève :

```python
>>> res.fetchone()
(2, 'Dupont', 'Jeanne', 17, 'TG2')
```

Pour choisir le nombre de résultats à renvoyer, on applique la méthode `fetchmany()` à `res` en lui passant en paramètre le nombre souhaité :

```python
>>> res = cur.execute("SELECT * FROM Eleve")
>>> res.fetchmany(3)
[(1, 'Dupont', 'Jean', 15, '2A'), (2, 'Dupont', 'Jeanne', 17, 'TG2'), (3, 'Marchand', 'Marie', 15, '2A')]
>>> res.fetchmany(3)
[(4, 'Martin', 'Adeline', 16, '1G1'), (5, 'Dupont', 'Lucas', 15, '2A'), (6, 'Richard', 'Louise', 15, '1G2')]
```

> Pour les requêtes d'interrogation, il est inutile d'utiliser `conn.commit()` puisque ces requêtes n'entraînent aucun changement de la base de données.

## Requêtes avec paramètres

On peut bien sûr construire des requêtes d'interrogation avec des paramètres. Pour cela il faut écrire une **requête préparée** comme vu précédemment. Par exemple, si on veut récupérer tous les élèves ayant pour nom `Dupont`, on écrira :

```python
>>> res = cur.execute("SELECT id, nom, prenom FROM Eleve WHERE nom = ?", ('Dupont',))
>>> res.fetchall()
[(1, 'Dupont', 'Jean'), (2, 'Dupont', 'Jeanne'), 
(5, 'Dupont', 'Lucas'), (10, 'Dupont', 'Aurélien')]
```

**Remarques**
- <span style="font-size:1.5em;">⚠️</span> Vous noterez que l'on a écrit `('Dupont',)` en deuxième paramètre pour bien passer un tuple à la méthode `execute` (et non `('Dupont')` qui n'en serait pas un).
- on aurait aussi pu utiliser la syntaxe avec les dictionnaires : `cur.execute("SELECT id, nom, prenom FROM Eleve WHERE nom = :nom", {'nom': 'Dupont'})`

Imaginons que notre application possède un champ permettant à l'utilisateur de saisir un nom pour chercher un élève dans la base de données, on peut créer une fonction qui serait appelée lorsque la saisie est validée.

En effet, on peut facilement écrire une telle fonction qui renvoie la liste de tous les élèves dont le nom lui est passé en paramètre. Cela ressemble à quelque chose comme ci-dessous :

```python
def recuperer_eleves_par_nom(nom):
    conn = sqlite3.connect('eleves.db')
    cur = conn.cursor()
    res = cur.execute("SELECT id, nom, prenom FROM Eleve WHERE nom = ?", (nom, ))
    eleves = res.fetchall()  # on stocke les résultats pour pouvoir les renvoyer
    conn.close()  
    return eleves  # après avoir fermé la connexion
```

On peut bien sûr appeler cette fonction :

```python
>>> recuperer_eleves_par_nom('Martin')
[(4, 'Martin', 'Adeline', '1G1'), (12, 'Martin', 'Anaëlle', 'TG1')]
>>> recuperer_eleves_par_nom('Richard')
[(6, 'Richard', 'Louise', '1G2')]
>>> recuperer_eleves_par_nom('Obama')
[]
```

# Éviter l'injection SQL

On a vu que l'on pouvait écrire des requêtes paramétrées grâce au caractère `?` (ou en utilisant des dictionnaires), et c'est vraiment ainsi qu'il faut procéder !

Ce n'est pas évident de prime abord, mais à la place d'écrire

```python
cur.execute("SELECT id, nom, prenom FROM Eleve WHERE nom = ?", (nom, ))
```

on pourrait être tenté de construire la chaîne de requête de la façon suivante :

```python
cur.execute("SELECT id, nom, prenom FROM Eleve WHERE nom = '" + str(nom) + "'")
```

ou de manière équivalente en utilisant une `f-string` :

```python
cur.execute(f"SELECT id, nom, prenom FROM Eleve WHERE nom = '{nom}'")
```

Ces deux dernières façons de faire, en construisant notre requête SQL comme une chaîne de caractères classique, introduisent en réalité une **faille de sécurité** critique pour notre application, qui devient vulnérable à ce qu'on appelle une **injection SQL**. 

Nous expliquerons cela dans un second tutoriel, pour mettre en garde le développeur des conséquences désastreuses d'une telle faille de sécurité 👮‍♀️🥵👮 ...


# ✍️ À vous de jouer !

## 💻 Exercice 1 : Application directe

🐍 **Q1** : Écrire une fonction `recuperer_eleves_par_classe` qui prend un paramètre `classe` et qui renvoie la liste de tous les élèves de la table `Eleve` qui sont dans la classe `classe`.

*Exemple* :

```python
>>> recuperer_eleves_par_classe('1G1')
[(4, 'Martin', 'Adeline', 16, '1G1'), (10, 'Dupont', 'Aurélien', 16, '1G1')]
```

🐍 **Q2** : Écrire une fonction `recuperer_eleve` qui prend un entier `id_eleve` en paramètre et qui renvoie l'élève (les attributs nom, prenom, classe uniquement) ayant pour identifiant `id_eleve`.

*Exemple* :

```python
>>> recuperer_eleve(3)
('Marchand', 'Marie', '2A')
```

🐍 **Q3** : Écrire une fonction `changer_classe` qui prend en paramètre un entier `id_eleve` correspondant à l'attribut `id` d'un élève, et une chaîne de caractère `nouvelle_classe` et qui modifie la classe de l'élève en question en base de données.

*Exemple* :

```python
>>> changer_classe(3, '2C')
>>> recuperer_eleve(3)
('Marchand', 'Marie', '2C')
```

🐍 **Q4** : Écrire une fonction `recuperer_liste_alphabetique_par_classe` qui prend un paramètre `classe` et qui renvoie la liste *triée par ordre alphabétique* de tous les élèves de la table `Eleve` qui sont dans la classe `classe`. *Le tri doit être réalisé par la requête SQL (vous pourrez dans un second temps essayer de le réaliser avec Python si vous le souhaitez en triant la liste des résultats)*.

*Exemple* :

```python
>>> recuperer_liste_alphabetique_par_classe('1G2')
[('Laurent', 'Diego', 17, '1G2'), ('Richard', 'Louise', 15, '1G2'), ('Rouger', 'Marius', 16, '1G2')]
```

## 💻 Exercice 2 : Créer et utiliser une classe `Eleve`

🐍  **Q1** : Écrire une classe Python appelée `Eleve` dont les instances possèdent 4 attributs : `nom` (de type `str`), `prenom` (de type `str`), `age` (de type `int`) et `classe` (de type `str`).

🐍 **Q2** : Quelle instruction permet de créer un objet de la classe `Eleve` vous correspondant ?

🐍 **Q3** : Écrivez une fonction `ajouter_eleve(eleve)` qui prend en paramètre **un objet** `eleve` de la classe `Eleve` et qui ajoute cet élève en base de données.

🐍 **Q4** : Utilisez cette fonction pour ajouter l'élève créé à la question 2 en base de données puis vérifiez que l'ajout a bien été réalisé.

---

**Références** :

- Documentation officielle du module `sqlite` : [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
- Vidéo de Corey Schafer, *Python SQLite Tutorial: Complete Overview - Creating a Database, Table, and Running Queries* : [https://youtu.be/pd-0G0MigUA](https://youtu.be/pd-0G0MigUA)

---

Germain BECKER, Lycée Emmanuel Mounier, ANGERS

![Licence Creative Commons](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)
