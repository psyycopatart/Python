import pandas as pd
import numpy as np
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

def main():
	my_array = [70, 23]
	my_numpy_array = np.array(my_array)
	my_numpy_array_len = len(my_array)

	try:
		print(my_numpy_array / my_numpy_array_len)
	except TypeError:
		print("Les opérateurs ne sont pas supportés 'str' et 'int'.")

	famille_panda = [
	[21, 234, 3, 4], #1
	[21, 234, 134, 4], #2
	[21, 2, 34, 4], #3
	]
	famille_panda_numpy = np.array(famille_panda)
	print(famille_panda_numpy[:, 1])

	famille_panda_df = pd.DataFrame(famille_panda, index = ['papa', 'maman', 'bebe'], 
		columns = ['taille', 'poids', 'poils', 'ventre'])
	print(famille_panda_df.taille)

	for line in famille_panda_df.iterrows():
		line_panda = line[0]
		column_panda = line[1]
		print(line_panda)
		print(column_panda)
		print('------------------')

	poids_panda = famille_panda_df.poids > 200
	print(poids_panda)

	autres_pandas = pd.DataFrame([
		[23, 32, 345, 21],
		[1, 23, 78, 456]
		], 
		index = ['grand-père', 'grand-mère'],
		columns = famille_panda_df.columns)
	tous_les_pandas = famille_panda_df.append(autres_pandas)
	print(tous_les_pandas.drop_duplicates())
	print('------------------')
	lecture_depute = pd.read_csv('data/current_mps.csv', sep=";")
	print(lecture_depute)

	ages = [25, 65, 26, 26, 46, 37, 36, 36, 28, 28, 57, 37, 48, 48, 37, 28, 60,
       25, 65, 46, 26, 46, 37, 36, 37, 29, 58, 47, 47, 48, 48, 47, 48, 60]

	fig, ax = plt.subplots()
	ax.hist(ages)
	plt.show()


if __name__ == '__main__':
	main()