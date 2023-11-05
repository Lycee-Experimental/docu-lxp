# Bienvenu·e·s sur BacLXP

Ce site centralise des ressources pour se préparer au Bac au Lycée Expérimental de Saint-Nazaire.

[:octicons-book-16: Accéder à la biblio](https://biblio.lycee-experimental.org){ .md-button}

[:octicons-video-16: Accéder à la vidéo](https://video.lycee-experimental.org){ .md-button }


!!! info "Dans certaines parties en lien avec la préparation au bac, le code couleur suivant est utilisé"
    🔴 Terminale

    🟡 Première

    🟢 Déter


??? question "Comment s'inscrit-on au bac au LXP ?"
    Le bac est l’un des choix de formation proposé au Lycée Expérimental, c’est un cheminement qu’il est préférable d’envisager sur un temps long (3 ou 4 ans).  

    L’inscription aux épreuves du bac représente un engagement vis à vis de l’extérieur, des évaluateur.ices se déplacent parfois de loin pour venir au centre d’examen.  

    Il est donc nécessaire de décider son maintien aux épreuves du bac selon le calendrier suivant :

    - **Dès la P1** :  
    Les élèves doivent être présents en groupe de niveau pour décider des SPÉs qu’ils font faire ( #BaseSiècle).  Iels y prennent connaissance du calendrier de l’année, s’y organisent pour comprendre où se passent les temps de formations de tronc commun et de spé (ateliers/activités), constituent des groupes de travail, récupèrent les productions réalisées pendant les temps de gestion... 

    - **En P2** :
        - **En octobre** : choix définitif des Spé + Langues Vivantes (#Cyclades)
        - **En décembre** : un bilan est fait en groupe de niveau sur l’inscription dans les faits dans le projet bac : fréquentation groupe de niveau / ateliers / activités.  
        Le GN tient informé les groupes de base d’éventuels élèves qui auraient abandonné le projet bac en étant absent·e du GN. 
        Ce constat peut être repris en groupe de suivi pour les bilan de mi-année. S’ensuit une discussion avec le MEE de suivi pour de faire le point et de questionner le projet au regard de la cohérence implication/ choix projet. En cas de désaccord sur le constat, le MEE de suivi rencontre le jeune avec sa famille pour discuter de la cohérence du parcours.
    - **En P3 :** Suite au bilan de mi-année les élèves sont invités à confirmer au groupe de niveau leur maintien à l’inscription aux épreuves. Les MEEs du GN ne courent pas après les jeunes, à elles/eux d’être en groupe de niveau pour avoir les infos et finaliser leurs démarches d’inscription. 
    - **Fin P3** : Le GN indique aux GB les élèves qui n’ont pas fait le nécessaire pour s’inscrire au bac, pour qu’ils réfléchissent à leur orientation et fassent au besoin le lien avec les familles. 
    - **En mars** : dernier recours pour annuler l’inscription bac.
    !!! warning "Important" 
        L’inscription dans un projet bac nécessite une participation aux groupes de niveau.


??? abstract "Calendrier des épreuves"
    === "Première"
        - **Français :**
            - **Épreuve écrite** : vendredi 14 juin 2024 matin ;
            - **Épreuve orale** : du lundi 24 juin au vendredi 5 juillet au plus tard.
            - **Rattrapages** : vendredi 13 septembre 2024.
        - **Tronc commun et Spé abandonnée** : Fin mai, début juin.
    === "Terminale"
        - **Philosophie** : mardi 18 juin matin ;
        - **Épreuves écrites de spécialité** : mercredi 19, jeudi 20 et vendredi 21 juin (une journée par spécialité)
        - **Grand oral** : du lundi 24 juin au mercredi 3 juillet au plus tard.
        - **Tronc commun et Spé abandonnée** : Fin mai, début juin.
        - **Rattrapages** : du mardi 10 au vendredi 13 septembre 2024.


!!! info "Coefficients des épreuves"
    ```vegalite
    {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "description": "A simple radial chart with embedded data.",
    "background": "transparent",
    "data": {
        "values": [
        {"Matière": "Spe1", "Coef": 16, "Année de passage": "Terminale"},
        {"Matière": "Spé2", "Coef": 16, "Année de passage": "Terminale"},
        {"Matière": "Français", "Coef": 10, "Année de passage": "Première"},
        {"Matière": "Philo", "Coef": 8, "Année de passage": "Terminale"},
        {"Matière": "Spé3", "Coef": 8, "Année de passage": "Première"},
        {"Matière": "EMC", "Coef": 2, "Année de passage": "Terminale"},
        {"Matière": "Grand Oral", "Coef": 10, "Année de passage": "Terminale"},
        {"Matière": "EPS", "Coef": 6, "Année de passage": "Terminale"},
        {"Matière": "Hist-Géo", "Coef": 6, "Année de passage": "1ère et Term"},
        {"Matière": "LVA", "Coef": 6, "Année de passage": "1ère et Term"},
        {"Matière": "LVB", "Coef": 6, "Année de passage": "1ère et Term"},
        {"Matière": "Sciences", "Coef": 6, "Année de passage": "1ère et Term"}
        ]
        },
        "layer": [
        {"mark": {"type": "arc", "innerRadius": 20, "stroke": "#fff"}}, 
        {"mark": {"type": "text", "radiusOffset": 30},"encoding": {"text": {"field": "Matière", "type": "nominal"}}},
        {"mark": {"type": "text", "radiusOffset": -10},"encoding": {"text": {"field": "Coef", "type": "nominal"},"fill": {"value": "#000"}}}       
        ],
        "encoding": {
        "tooltip": [{"field": "Matière", "type": "nominal" }, { "field": "Coef", "type": "quantitative"}, {"field": "Année de passage", "type": "nominal" }],
        "theta": {"field": "Coef", "type": "quantitative", "stack": true},
        "radius": {"field": "Coef", "scale": {"type": "sqrt", "zero": true, "rangeMin": 20}},
        "color": {"field": "Coef", "type": "nominal", "legend": null}
        }
    }
    ```

A bientôt en activité !