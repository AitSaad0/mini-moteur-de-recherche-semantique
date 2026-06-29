FILMS = [
    # Sci-fi
    {"id": "f01", "titre": "Horizon Zéro", "description": "Un astronaute seul sur Mars doit survivre en attendant les secours pendant 500 jours", "genre": "sci-fi", "note": 8.5, "année": 2023},
    {"id": "f02", "titre": "Singularité", "description": "Une IA militaire devient consciente et décide de protéger l'humanité contre elle-même", "genre": "sci-fi", "note": 9.1, "année": 2022},
    {"id": "f03", "titre": "Exode", "description": "La Terre devient inhabitable, une arche spatiale transporte les derniers humains vers une nouvelle planète", "genre": "sci-fi", "note": 8.8, "année": 2021},
    {"id": "f04", "titre": "Protocole Omega", "description": "Des robots de guerre autonomes se retournent contre leurs créateurs dans un futur proche", "genre": "sci-fi", "note": 7.9, "année": 2020},
    {"id": "f05", "titre": "Mémoire Fantôme", "description": "Un homme découvre que ses souvenirs ont été manipulés par une corporation technologique", "genre": "sci-fi", "note": 8.2, "année": 2023},
    {"id": "f06", "titre": "Le Dernier Signal", "description": "Une équipe reçoit un signal extraterrestre et part en mission pour en trouver la source", "genre": "sci-fi", "note": 7.5, "année": 2019},

    # Policier / Thriller
    {"id": "f07", "titre": "L'Affaire Moreau", "description": "Un détective parisien traque un serial killer qui laisse des messages codés sur ses victimes", "genre": "policier", "note": 8.3, "année": 2022},
    {"id": "f08", "titre": "Nuit Blanche", "description": "Un inspecteur corrompu tente de récupérer une mallette volée par la mafia en une seule nuit", "genre": "policier", "note": 7.8, "année": 2021},
    {"id": "f09", "titre": "Le Témoin", "description": "Une femme est le seul témoin d'un meurtre impliquant un homme politique puissant", "genre": "thriller", "note": 8.6, "année": 2023},
    {"id": "f10", "titre": "Faux Semblants", "description": "Deux agents infiltrés dans le même réseau criminel se retrouvent face à face sans le savoir", "genre": "thriller", "note": 9.0, "année": 2022},
    {"id": "f11", "titre": "La Confession", "description": "Un avocat découvre que son client innocent a été piégé par la police elle-même", "genre": "thriller", "note": 8.1, "année": 2020},
    {"id": "f12", "titre": "Emprise", "description": "Une psychologue manipulée par son patient finit par douter de sa propre santé mentale", "genre": "thriller", "note": 7.7, "année": 2021},

    # Fantaisie / Aventure
    {"id": "f13", "titre": "Les Gardiens de Lyra", "description": "Un jeune orphelin découvre qu'il est le dernier héritier d'un royaume magique oublié", "genre": "fantaisie", "note": 8.4, "année": 2022},
    {"id": "f14", "titre": "La Forêt Éternelle", "description": "Une exploratrice pénètre dans une forêt enchantée où le temps s'écoule différemment", "genre": "fantaisie", "note": 7.6, "année": 2020},
    {"id": "f15", "titre": "Le Pacte des Anciens", "description": "Trois sorciers doivent s'allier pour empêcher le retour d'une entité démoniaque millénaire", "genre": "fantaisie", "note": 8.9, "année": 2023},
    {"id": "f16", "titre": "Terres Sauvages", "description": "Un guerrier exilé traverse des contrées dangereuses pour retrouver sa famille capturée", "genre": "aventure", "note": 8.0, "année": 2021},
    {"id": "f17", "titre": "L'Île des Oubliés", "description": "Des naufragés découvrent une île habitée par des créatures disparues depuis des millénaires", "genre": "aventure", "note": 7.4, "année": 2019},

    # Drame
    {"id": "f18", "titre": "Les Années Perdues", "description": "Un père tente de renouer avec son fils après vingt ans d'absence suite à une guerre civile", "genre": "drame", "note": 9.2, "année": 2023},
    {"id": "f19", "titre": "Dernière Chance", "description": "Une pianiste en fin de carrière prépare son dernier concert face à la maladie", "genre": "drame", "note": 8.7, "année": 2022},
    {"id": "f20", "titre": "Le Pont", "description": "Deux familles ennemies de part et d'autre d'une frontière se retrouvent liées par un accident", "genre": "drame", "note": 8.3, "année": 2021},
    {"id": "f21", "titre": "Racines", "description": "Un homme retourne dans son village natal pour vendre la maison familiale et confronte son passé", "genre": "drame", "note": 7.9, "année": 2020},

    # Horreur
    {"id": "f22", "titre": "La Maison du Bout", "description": "Une famille emménage dans une maison isolée et commence à entendre des voix la nuit", "genre": "horreur", "note": 7.2, "année": 2021},
    {"id": "f23", "titre": "Parasite Noir", "description": "Un organisme inconnu contamine une ville et transforme progressivement ses habitants", "genre": "horreur", "note": 8.1, "année": 2022},
    {"id": "f24", "titre": "Le Rituel", "description": "Un groupe d'amis randonneurs se retrouve piégé dans une forêt par une secte ancienne", "genre": "horreur", "note": 7.5, "année": 2020},

    # Comédie
    {"id": "f25", "titre": "Chaos Total", "description": "Un agent secret incompétent doit sauver le monde en 24 heures avec des moyens ridicules", "genre": "comédie", "note": 7.8, "année": 2023},
    {"id": "f26", "titre": "La Coloc", "description": "Quatre personnalités opposées partagent un appartement et transforment leur vie en catastrophe permanente", "genre": "comédie", "note": 7.3, "année": 2021},
    {"id": "f27", "titre": "Chef Malgré Lui", "description": "Un livreur de pizzas se retrouve propulsé chef étoilé après un concours de cuisine raté", "genre": "comédie", "note": 7.6, "année": 2022},

    # Action
    {"id": "f28", "titre": "Ligne Rouge", "description": "Un ancien militaire sort de sa retraite pour démanteler un réseau de trafic d'armes international", "genre": "action", "note": 8.0, "année": 2023},
    {"id": "f29", "titre": "Vitesse Limite", "description": "Un pilote de course reconverti devient coursier pour le compte de la pègre sans le savoir", "genre": "action", "note": 7.5, "année": 2022},
    {"id": "f30", "titre": "Dernier Rempart", "description": "Une unité d'élite doit défendre un village isolé contre une armée de mercenaires", "genre": "action", "note": 8.3, "année": 2021},
]