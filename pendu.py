#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

mot_a_trouver = ["mot", "enzo", "raison"]
mot = random.choice(mot_a_trouver)
solution = ""
lettre_trouves = ""
essaie = True
for l in mot:
    solution = solution + "_ "
print(solution)

while essaie:

    proposition: str = input("annoncez une lettre : ")
    if proposition in mot:
        lettre_trouves += proposition

    affichage = ""
    x = ""
    for x in mot:
        if x in lettre_trouves:
            affichage += x + " "
        else:
            affichage += "_ "

    if x in lettre_trouves:
        print("la lettre est dans le mot")
    else:
        print("la lettre n'est pas dans le mot")

    print(affichage)

    if "_" not in affichage:
        print("Gagné !!\nLe mot a trouver était ", mot)
        break
