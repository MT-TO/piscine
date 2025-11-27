#dononvan pas ouf 
# COM MT 
#   Projet de développement Python 
#   Gestionnaire d'utilisateurs d'une piscine 
#   donovan jltmoy

print("--- Gestionnaire d'utilisateurs d'une piscine ---")

liste = []
commande = ''

while commande != 'exit':
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        a = input("Qui nage ? ")
        b = input("quelle nage ? ")
        c = input("combien de longueur ? ")
        liste.append((a, b, c))

    if commande == 'liste':
        for elt in liste:
            print(f"Prénom {elt[0]}, nage {elt[1]}, longueur {elt[2]}")

    if commande == 'nage':
        nage_recherchee = input("Quelle nage ? ")
        trouve = False
        for elt in liste:
            if elt[1].lower() == nage_recherchee.lower():
                print(f"{elt[0]} pratique cette nage ({elt[2]} longueurs)")
                trouve = True
        if not trouve:
            print("Aucun nageur trouvé pour cette nage.")
