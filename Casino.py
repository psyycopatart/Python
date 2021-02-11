import math
import random

question = input("Mettez le montant que vous voulez mettre pour jouer à la roulette : ")
banque = int(question)
couleur = str()
pairImpair = bool()
parite = str()

if pairImpair:
    parite = "paire"
    couleur = "noir"
else:
    parite = "impaire"
    couleur = "rouge"

while banque > 0:

    miseNombre = int(input("Veuillez entrer un nombre sur lequel miser : "))
    miseSomme = int(input("Veuillez entrer une mise pour ce tour : "))
    nombreRoulette = random.randrange(50)

    # Case pair ou impair
    if miseNombre % 2 == 0 or nombreRoulette % 2 == 0:
        pairImpair = True
    else:
        pairImpair = False

    if nombreRoulette == miseNombre:
        print("Bravo vous avez gagné, le boin nombre était : ", nombreRoulette, " sa couleur était ", couleur,
              " et c'était un nombre ", parite)
        miseSomme3 = miseSomme * 3
        banque = miseSomme3 + banque
        print("Vous avez gagné ", miseSomme3, ", il vous reste ", banque, " en banque")

    elif nombreRoulette == pairImpair and miseNombre == pairImpair or nombreRoulette != pairImpair and miseNombre != pairImpair:
        miseSomme2 = int(math.ceil(miseSomme * 0.5))
        print("Le nombre choisit était ", nombreRoulette,
              " néanmoins votre nombre est de la bonne couleur, vous gagnez ", miseSomme2)
        banque = banque + miseSomme2
        print("il vous reste ", banque, " en banque")

    else:
        print("Dommage la roulette a sorti le numéro : ", nombreRoulette, " sa couleur était ", couleur,
              " et c'était un nombre ", parite)
        banque = banque - miseSomme
        print("Il vous reste ", banque, " en banque")

    if banque <= 0 or banque == 0:
        print("Vous n'avez plus d'argent en baque")
        break

    exit_game = input("Voulez-vous continuer (Oui/Non) ? ")
    if exit_game == "Non":
        print("Merci d'avoir jouer et à bientôt")
        break