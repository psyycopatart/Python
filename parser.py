import argparse
import math

parser = argparse.ArgumentParser(description="calculer volume d'un cylinder")
parser.add_argument("radius", type=int, help="rayon du cylindre", choices=[2, 4, 5])
parser.add_argument("hauteur", type=int, help="hauteur du cylinder")
args = parser.parse_args()


def volume_cylindre(rayon, hauteur):
	vol = (math.pi) * (rayon**2) * (hauteur)
	print(vol)
	# return end function


if __name__ == '__main__':
	volume_cylindre(args.radius, args.hauteur)