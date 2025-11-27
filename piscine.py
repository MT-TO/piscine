#dononvan pas ouf 
# COM MT 
#   Projet de développement Python 
#   Gestionnaire d'utilisateurs d'une piscine 
#   donovan jltmoy

print("--- Gestionnaire d'utilisateurs d'une piscine ---")

liste = []
commande = ''
#salut 
# com MT 2 
while commande != 'exit':
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        a = input("Qui nage ? ")
        b = input("quelle nage ? ")
        c = input("combien de longueur ? ")
        liste.append((a,b,c))
#salam
    if commande == 'liste':
        for nageur, nage, longeur in liste:
            print(f"Prénom {nageur}, nage {nage}, longueur {longeur}")

# MT 