import os #import des fonctions de navigation système

def launch_analysis(data_file):
	directory = os.path.dirname(__file__)
	path_of_the_file = os.path.join(directory, "data", data_file) #recherche du fichier

	with open(path_of_the_file, "r") as fichier:
		preview = fichier.readline() #lecture du fichier csv

	print(preview) #affichage du fichier csv

if __name__ == '__main__':
	launch_analysis('SysceronBrut.xml') #lancement de la fonction à l'ouverture du script