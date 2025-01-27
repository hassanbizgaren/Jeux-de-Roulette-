import random

# Config initial
roue_de_roulette = [i for i in range(37)]  # Génération des numéros de la roue
budget = 1000  # Budget initial du joueur

print("####################################################################")
print("Bienvenue au jeu de roulette simplifié !")
print(f"Votre budget initial est : {budget} MAD")
print("Essayez de maximiser vos gains, bonne chance !")
print("####################################################################")

# Boucle principale du jeu
while budget > 0:
    # Demander au joueur de choisir un numéro
    print(f"Votre budget actuel est de {budget} MAD")
    numero_parie = input("Sur quel numéro souhaitez-vous parier (0-36) ? ")
    numero_parie = int(numero_parie) if numero_parie.isdigit() and 0 <= int(numero_parie) <= 36 else -1

    if numero_parie == -1:
        print("Numéro invalide. Veuillez entrer un nombre entre 0 et 36.")
        continue

    # Demande du joueur combien il veut miser
    mise = input("Combien souhaitez-vous miser ? ")
    mise = int(mise) if mise.isdigit() and 0 < int(mise) <= budget else -1

    if mise == -1:
        print("Mise invalide. Veuillez entrer un montant valide.")
        continue

    # Faire tourner la roue
    numero_gagnant = random.choice(roue_de_roulette)
    print("\nLa roue tourne.....")
    print(f"Et s'arrête sur le numéro {numero_gagnant} !\n")

    # Déterminer si le joueur a gagné ou perdu
    if numero_parie == numero_gagnant:
        gains = mise * 35
        budget += gains
        print(f"Félicitations ! Vous avez gagné {gains} MAD")
    else:
        budget -= mise
        print(f"Dommage ! Vous avez perdu {mise} MAD")

    # Afficher le budget actuel
    print(f"Votre budget actuel est {budget} MAD\n")

    # Demande au joueur s'il veut continuer
    if budget > 0:
        continuer = input("Souhaitez-vous continuer à jouer ? (oui/non) ").strip().lower()
        while continuer not in ["oui", "non"]:
            print("Entrée invalide, veuillez répondre par 'oui' ou 'non'.")
            continuer = input("Souhaitez-vous continuer à jouer ? (oui/non) ").strip().lower()
        if continuer == "non":
            break

# Fin du jeu
print("\nMerci d'avoir joué !")
print(f"Votre budget final est {budget} MAD")
print("À bientôt !")