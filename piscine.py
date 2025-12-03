print("--- Gestionnaire d'utilisateurs d'une piscine ---")

liste_nageurs = ["Pierre", "Léa", "Michel"]

liste = [
    (1, "Brasse", 15, "25-11-24"),
    (0, "Brasse", 9,  "25-11-24"),
    (2, "Crawl",   8,  "25-11-26"),
    (1, "Crawl",  10, "25-11-25"),
    (0, "Dos",     9,  "25-11-26"),
    (1, "Brasse",  9,  "25-11-26"),
    (2, "Brasse",  7,  "25-11-27")
]
commande = ''

while commande != 'exit':
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        """
        nom = input("Qui nage ? ").strip().lower().capitalize()

        if nom in liste_nageurs:
            a = liste_nageurs.index(nom)
        else:
            print("Ce nageur n'existe pas dans la liste.")
            continue
        """
        for id, nageur in enumerate(liste_nageurs):
            print(f"{id}->{nageur}")
        a = int(input("Qui nage?"))

        b = input("Quelle nage ? ").strip().lower().capitalize()
        c = input("Combien de longueurs ? ")
        d = input("Quel jour ? YY_MM_DD")

        liste.append((a, b, c, d))

    if commande == 'liste':
        for nageur, nage, longueur, date in liste:
            print(f"Prénom {liste_nageurs[nageur]}, nage {nage}, longueur {longueur}, date {date}")

        nom = input("Quel nageur ajouter ? ").strip().lower().capitalize()
        if nom in liste_nageurs:
            a = liste_nageurs.index(nom)
        else:
            print("Ce nageur n'existe pas.")
            continue

        b = input("Quelle nage ? ").strip().lower().capitalize()
        c = input("Combien de longueurs ? ")
        d = input("Quelle date ? (JJ/MM/AAAA) ")
        liste.append((a, b, c, d))

    if commande == 'listeB':
        for nageur, nage, longueur, date in liste:
            print(f"{date} - Prénom {liste_nageurs[nageur]}, nage {nage}, longueurs {longueur}")

    if commande == 'nage':
        nage_recherchee = inp_
