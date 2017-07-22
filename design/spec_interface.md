# API horaires transports en commun
- arrêts autour d'une localisation
    @param (lon, lat)
    @return liste d'arrêts (triés par distance ?)
- liste des lignes de transport
    @return liste de dictionaires {numéro, nom, [tableau de terminus]}
- liste des arrêts
    @return tableau de chaînes de caractères, pour les noms des arrêts
- lignes à un arrêt
    @param nom de l'arrêt
    @return tableau de {numéro de ligne, longitude, lattitude}
- arrêts d'une ligne
    @param numéro de ligne
    @return [noms d'arrêts]
- horaires à un arrêt, pour une ligne, dans une direction
    @param arrêt (chaîne de charactères)
    @param ligne (numéro)
    @param direction (keyword argument), nom d'un terminus (il peut y en avoir plus de deux)
    @param passant à (keyword argument), nom d'un arrêt où le bus passera
    @param théorique (booléen) si défini à False, on essaye d'obtenir une information "temps réel"
    @return [horaires]
        Remarque: retourne un nombre indéterminé d'horaires, dont une partie peut être dans le passé (si c'est tous les horaires du jour par exemple)

# API météorologie
Nature de la prévision: probabilité et quantité de précipitation
- prévision la plus récente dans le passé (ou présent) proche d'une localisation
    @param longitude
    @param lattitude
    @return {heure de prévision, probabilité de précipitation, quantité de préicipation}
- prévision la plus proche dans le futur, proche d'une localisation
    @param longitude
    @param lattitude
    @return {heure de prévision, probabilité de précipitation, quantité de préicipation}

# API vélo en location
- recherche station par localisation
    @param longitude
    @param lattitude
    @return {nom de station, capacité}
- nombre de vélos disponibles à une station
    @param nom de station
    @return entier
- nombre d'emplacements disponibles à une station
    @param nom de station
    @return entier