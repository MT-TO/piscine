print("--- Gestionnaire d'utilisateurs d'une piscine ---")

liste = []
commande = ''

while commande != 'exit':
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        a = input("Qui nage ? ").strip().lower().capitalize()
        b = input("quelle nage ? ").strip().lower().capitalize()
        c = input("combien de longueur ? ")
        d = input("Quel jour ? YY_MM_DD")
        liste.append((a, b, c, d))

    if commande == 'liste':
        for nageur, nage, longeur, date in liste:
            print(f"Prénom {nageur}, nage {nage}, longueur {longeur} date {date}")

        # ton bloc chelou qui ré-ajoute encore un truc après la liste (je le laisse)
        b = input("Quelle nage ? ").strip().lower().capitalize()
        c = input("Combien de longueurs ? ")
        d = input("Quelle date ? (format JJ/MM/AAAA) ")
        liste.append((a, b, c, d))

    if commande == 'liste':
        for nageur, nage, longueur, date in liste:
            print(f"{date} - Prénom {nageur}, nage {nage}, longueurs {longueur}")

    if commande == 'nage':
        nage_recherchee = input("Quelle nage ? ").strip().lower().capitalize()
        trouve = False
        for elt in liste:
            if elt[1] == nage_recherchee:
                print(f"{elt[0]} pratique cette nage ({elt[2]} longueurs) le {elt[3]}")
                trouve = True
        if not trouve:
            print("Aucun nageur trouvé pour cette nage.")

    if commande == 'date':
        date_recherchee = input("Quelle date ? (JJ/MM/AAAA) ")
        trouve = False
        for elt in liste:
            if elt[3] == date_recherchee:
                print(f"{elt[0]} a nagé {elt[1]} ({elt[2]} longueurs)")
                trouve = True
        if not trouve:
            print("Aucune activité trouvée à cette date.")
