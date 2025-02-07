import random

def jeu_de_devinette():
    # Générer un nombre aléatoire entre 1 et 100
    nombre_a_deviner = random.randint(1, 100)
    tentatives = 0
    devine = False

    print("Bienvenue dans le jeu de devinette !")
    print("J'ai choisi un nombre entre 1 et 100. Pouvez-vous le deviner ?")

    while not devine:
        # Demander au joueur de deviner
        try:
            guess = int(input("Entrez votre proposition : "))
            tentatives += 1

            if guess < nombre_a_deviner:
                print("Trop bas !")
            elif guess > nombre_a_deviner:
                print("Trop haut !")
            else:
                print(f"Félicitations ! Vous avez trouvé le nombre en {tentatives} tentatives.")
                devine = True
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    print("Merci d'avoir joué !")

# Lancer le jeu
jeu_de_devinette()