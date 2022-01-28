# Projet : Créer une application Web qui interroge une API et qui affiche les données récupérées

<img class="image-responsive centre" src="data/api.svg" alt="illustration API" width="200">

L'objectif de ce projet est d'interroger une API avec JavaScript puis d'afficher les données récupérées dans une page Web.

<img class="image-responsive centre" src="data/logoJS.svg" alt="logo JS" width="200">

# Création des fichiers du projet

Aucune installation n'est nécessaire pour ce projet.

**Q1** : Utilisez uniquement les lignes de commandes pour créer un répertoire vide `projet_api_web`, et créer les 3 fichiers suivants (vides pour le moment) dans ce répertoire :

- `index.html` : pour le code HTML de la page Web ;
- `script.js` : le fichier JavaScript qui interrogera l'API et ajoutera les données à la page Web.
- `apikey.js` : le fichier JavaScript qui contiendra la clé d'API utilisée (qui doit normalement restée cachée. En production, ce fichier ne serait bien sûr pas visible)

**Q2** : Vérifiez que le répertoire et les fichiers ont bien été créés, toujours en utilisant les lignes de commande.

# Exemple d'illustration

On propose ici d'utiliser la balise HTML `<template>` qui permet de créer un modèle de contenu. Ensuite, on interrogera l'API (via la méthode `fetch` de JavaScript) puis on ajoutera les données récupérés à notre page Web selon le modèle défini dans la balise `<template>`.

**Q3** : Regardez attentivement la vidéo suivante qui présente exactement ce que l'on souhaite faire (n'hésitez pas à reproduire ce qui est fait pour tester !) :

<div class="video-responsive">
    <iframe class="centre" width="560" height="315" src="https://www.youtube-nocookie.com/embed/oh6Wtys98ig" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

**Aide** : Voici quelques ressources supplémentaires :
- documentation sur la balise `<template>` : [https://developer.mozilla.org/fr/docs/Web/HTML/Element/template](https://developer.mozilla.org/fr/docs/Web/HTML/Element/template)
- documentation sur l'utilisation de la méthode `fetch` : [https://developer.mozilla.org/fr/docs/Web/API/Fetch_API/Using_Fetch](https://developer.mozilla.org/fr/docs/Web/API/Fetch_API/Using_Fetch)
- vidéos sur la méthode `fetch` :
    - Chaîne "Le Designer du Web" : *La méthode Fetch JS pour aller chercher des données* : [https://youtu.be/sGvEqHkDyFc](https://youtu.be/sGvEqHkDyFc)
    - Chaîne "Nouvelle Techno" : *Utilisation de fetch* [https://youtu.be/gNPRe_lxosE](https://youtu.be/gNPRe_lxosE)

# À vous de jouer !

Vous devez écrire deux petites applications Web :

- La première doit interroger l'API de [data/angers.fr](https://data.angers.fr/explore/dataset/parking-angers/information/) et afficher le nombre de places disponibles pour chaque parking angevin. Vous utiliserez la balise `<template>` pour afficher selon le même modèle les données pour chaque parking.
- La seconde doit permettre à un utilisateur de saisir une ville dans un champ de saisie et un bouton pour interroger l'API *Current weather data* du site OpenWeather : [https://openweathermap.org/current](https://openweathermap.org/current) pour obtenir et afficher des données sur la météo en temps réel de cette ville (l'accès à cette API est gratuit mais un compte doit être créé pour obtenir une clé d'API)

**Remarques** : 

- **Attention** : dans la seconde application, la clé d'API devra être mémorisée dans une chaîne de caractères dans le fichier `apikey.js` et devra être importée dans le fichier `script.js` qui l'utilise. Pour cela, cherchez du côté des instructions `import` et `export` dans la documentation de JavaScript.
- On n'attend pas de CSS pour ce projet, mais libre à vous de styliser votre page si vous le souhaitez.
- Vous pouvez consulter le cours de Première pour revoir comment créer un champ de saisie et récupérer son contenu : 
    - le cours [https://info-mounier.fr/premiere_nsi/web/data/T4_C1_Interaction_page_web.pdf](https://info-mounier.fr/premiere_nsi/web/data/T4_C1_Interaction_page_web.pdf)
    - la vidéo [https://youtu.be/LE4SHWN2FWk](https://youtu.be/LE4SHWN2FWk)

---

**Références** : 

- La vidéo de la chaîne YouTube *Nouvelle Techno* sur la balise `<template>`: [https://youtu.be/oh6Wtys98ig](https://youtu.be/oh6Wtys98ig) pour l'idée du projet

---

Germain BECKER, Lycée Mounier, ANGERS

Ressource éducative libre distribuée sous [Licence Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International](http://creativecommons.org/licenses/by-sa/4.0/) 

![Licence Creative Commons](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)