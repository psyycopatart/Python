import os #import des fonctions de navigation système
import logging as lg

lg.basicConfig(level=lg.DEBUG) #affiche les log lorsque la fonction "debug" est utilisée

def launch_analysis(data_file):
	directory = os.path.dirname(__file__)
	path_of_the_file = os.path.join(directory, "data", data_file) #recherche du fichier

	try: #gestion des erreurs
		with open(path_of_the_file, "r") as fichier:
			preview = fichier.readline() #lecture du fichier csv

		print(preview) #affichage du fichier csv
	except: #message en cas d'erreur
		lg.critical("Le fichier n'existe pas")

if __name__ == '__main__':
	launch_analysis('current_mps.csv') #lancement de la fonction à l'ouverture du script