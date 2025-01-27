import random

def afficher_bienvenue():
    print("\nBienvenue au Jeu de la Roulette!")
    print("Votre objectif est de maximiser vos gains avant de quitter le jeu.")
    print("Bonne chance!\n")

def configurer_roue():
    # Créer la liste des numéros de la roulette
    return list(range(37))

def gerer_budget_initial():
    
    # Budget initial
    return 1000

def demander_numero_pari():
    while True:
        try:
            numero = int(input("Choisissez un numéro entre 0 et 36 sur lequel parier : "))
            if 0 <= numero <= 36:
                return numero
            else:
                print("Erreur : Veuillez choisir un numéro valide.")
        except ValueError:
            print("Erreur : Veuillez entrer un numéro entier.")

def demander_mise(budget):
    while True:
        try:
            mise = int(input(f"Combien voulez-vous miser ? (Budget actuel : {budget} MAD) : "))
            if 0 < mise <= budget:
                return mise
            else:
                print("Erreur : Le montant de la mise doit être compris entre 1 et votre budget.")
        except ValueError:
            print("Erreur : Veuillez entrer un montant entier.")

def faire_tourner_roue(roue):
    return random.choice(roue)

def afficher_resultat_pari(numero_roulette, numero_joueur, mise):
    if numero_joueur == numero_roulette:
        gain = mise * 35
        print(f"Félicitations ! Le numéro tiré est {numero_roulette}. Vous avez gagné {gain} MAD.")
        return gain
    else:
        print(f"Malheureusement, le numéro tiré est {numero_roulette}. Vous avez perdu {mise} MAD.")
        return -mise

def demander_continuer():
    while True:
        choix = input("Souhaitez-vous continuer à jouer ? (o/n) : ").lower()
        if choix in ['o', 'n']:
            return choix == 'o'
        else:
            print("Erreur : Veuillez entrer 'o' pour oui ou 'n' pour non.")

def afficher_recapitulatif(budget_initial, budget_final, tours):
    print("\n--- Récapitulatif final ---")
    print(f"Budget initial : {budget_initial} MAD")
    print(f"Budget final : {budget_final} MAD")
    print(f"Nombre de tours joués : {tours}")
    if budget_final > budget_initial:
        print("Bravo ! Vous avez réalisé des gains.")
    elif budget_final < budget_initial:
        print("Dommage, vous avez perdu une partie de votre budget.")
    else:
        print("Vous avez terminé le jeu avec le même budget qu'au départ.")
    print("Merci d'avoir joué !")

def main():
    afficher_bienvenue()
    roue = configurer_roue()
    budget = gerer_budget_initial()
    budget_initial = budget
    tours = 0

    while budget > 0:
        print(f"\n--- Tour {tours + 1} ---")
        print(f"Budget actuel : {budget} MAD")

        # Étape 3 : Accepter les paris
        numero_joueur = demander_numero_pari()
        mise = demander_mise(budget)

        # Étape 4 : Faire tourner la roue
        numero_roulette = faire_tourner_roue(roue)

        # Étape 5 : Calcul des gains/pertes
        resultat = afficher_resultat_pari(numero_roulette, numero_joueur, mise)
        budget += resultat

        tours += 1

        # Vérifier si le joueur souhaite continuer
        if budget <= 0:
            print("Vous n'avez plus d'argent pour continuer. Fin du jeu.")
            break

        if not demander_continuer():
            break

    # Étape 6 : Afficher le récapitulatif final
    afficher_recapitulatif(budget_initial, budget, tours)

if __name__ == "__main__":
    main()
