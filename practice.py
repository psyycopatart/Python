# creation de set
mon_set = set()
print(type(mon_set))
mon_dico = dict()
print(type(mon_dico))
flowsers = ['rose', 'tulipe', 'lila']  # dictionnaire
print(set(flowsers))  # passage set

set1 = {'A', 'B', 'C'}
set2 = {'B', 'C', 'A'}
print(set1 == set2)  # True

first_name = "jhon"
last_name = 'doe'
full_name = (first_name, last_name)
print(full_name)

singleton = ([0, 1, 1, 2, 3, 5, 8, 13, 21],)
print(singleton)
print(type(singleton))

droite = {'macron', 'sarko'}
gauche = {'hollande', 'ségolène'}
print(droite | gauche)  # union() = | => unifie les deux sets

ghostbusters = {'Peter', 'Raymond', 'Egon'}
soldiers = {'Winston'}
secretaries = {'Janine'}
ghostbusters |= soldiers  # | et update() servent également à unifier des sets
ghostbusters.update(secretaries)
print(ghostbusters)

jedi = {'anakin', 'obi-wan'}
sith = {'doku', 'anakin'}
same_name = jedi.intersection(sith)  # affiche les elements en commun dans les sets
print(same_name)

animaux = {'chat', 'chien', 'rat'}
domestique = {'rat', 'poisson', 'chien'}
print(animaux.intersection_update(domestique))  # supprime les éléments du premier set qui ne sont pas dans le second set fourni en paramètres
beast = {'poisson', 'rat', 'ecureuil'}
beast &= domestique  # même chose pour '&='
print(beast)

basketteur = {'jordan', 'james', 'curry'}
sportif = {'jordan', 'durant', 'messi'}
print(basketteur.difference(sportif))  # affiche les éléments unique du premier set, avec comme elt de comparaison le second set
# même chose pour '-='

languages = [{'c', 'c++', 'python'}, {'python', 'javascript'}, {'python', 'java'}]
python_language = set.intersection(*languages)  # affiche les éléments commun d'une liste avec la fonction .intersection du set
# Le '*' sert à unpacker tous les éléments présent dans la liste
print(python_language)

set_1 = set('Jupiter Saturn Mars'.split())
set_2 = set('Earth Mars Venus'.split())
set_3 = set('Mars Pluto Uranus'.split())
set_4 = set_1.intersection(set_2).intersection(set_3)
print(set_4)

a = set("my code is brOKen")
b = "i'm not OK with that"
c = a.intersection(b)
print(c)

from collections import OrderedDict

marks = OrderedDict()
marks['Enzo'] = 16
marks['Jordan'] = 11
marks['James'] = 12
print(marks)
my_dict = {'Smith': 9.5, 'Brown': 8.1, 'Moore': 7.4}
my_dict = OrderedDict(my_dict)
print(my_dict)
my_dict.popitem(last=True)  # popitem supprime le dernier élément quand last=True
my_dict.popitem(last=False)  # popitem supprime le premier élément quand last=False
print(my_dict)
my_other_dict = {'Smith': 9.5, 'Brown': 8.1, 'Moore': 7.4}
my_other_dict = OrderedDict(my_other_dict)
my_other_dict.move_to_end('Smith', last=True)  # move_to_end envoi l'élément sélectionné à la fin last=True
my_other_dict.move_to_end('Moore', last=False)  # move_to_end envoi l'élément sélectionné au début last=False
print(my_other_dict)

from collections import namedtuple

person_template = namedtuple('Person', ['age', 'name', 'sexe'])
# Création de la sous-classe "Person"
print(person_template)
enzo = person_template('24', 'gros', 'male')
jhon = person_template(age="23", name="Doe", sexe='male')
print(enzo.age + "\n")
for elt in jhon:
    print(elt)
jhon = jhon._replace(age=26)
print("\nThe new age is " + str(jhon.age))
jhon = jhon._asdict()  # assemble chaque données avec sa correspondance dans la création du tuple
print(jhon)

from collections import ChainMap

laptop_labels = {'Lenovo': 600, 'Dell': 2000, 'Asus': 354}
operating_system = {'Windows': 2500, 'Linux': 400, 'MacOS': 54}
chain = ChainMap(laptop_labels, operating_system)  # concatène les deux dictionnaires
print(chain)
processor = {'Celeron': 600, 'Pentium': 2000, 'Ryzen 5': 354}
new_chain = chain.new_child(processor)  # ajoute un dictionnaire au ChainMap existant
print(new_chain)
student_template = namedtuple('Student', ['name', 'age', 'department'])
alina = student_template('Alina', '22', 'linguistics')
alex = student_template('Alex', '25', 'programming')
kate = student_template('Kate', '19', 'art')
print(alina, alex, kate, sep='\n')

dragons = list()
dragons.append('Rudror')
print(dragons)
monster = ["goule", "vampire"]
dragons.extend(monster)
# dragons.remove("goule") # or dragons.remove[0]
# append(_) insert(_,_) remove(_) extend(_) ======> LISTE
dragons.insert(1, "sorcier")
print(dragons)
print(dragons.count('sorcier'))  # indique le nombre d'élément identique dans la liste
print(dragons.index("vampire"))  # affiche l'emplacement de la clé dans la liste

games = ['backgammon', 'Scrabble', 'chess', 'battleship', 'Monopoly']
removed_game = games[2]
games.remove('chess')
print("The resultant list of games:")
print(games)
print("The removed game:")
print(removed_game)

# Listes comprehesion
numbers = [1, 2, 3]
new_lists = [elt * elt for elt in numbers]
print(new_lists)
# [x for x in some_iterable if condition] ==> if
# [x if condition else y for x in some_iterable] ==> if else
words = ['apple', 'pear', 'banana', 'Ananas']
print([elt for elt in words if elt.startswith(('a', 'A'))])

# Liste imbriquées
nested_list = [1, [2, 3], 4]
nested_numbers = nested_list[1]
print(nested_numbers)
print(nested_list[1][0])  # on affiche le premier élément de la liste imbriquée
print([elt for elt in nested_list])

# Matrice
first_matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# original list / matrice
school = [["Mary", "Jack", "Tiffany"],
          ["Brad", "Claire"],
          ["Molly", "Andy", "Carla"]]
student_list = list()
for student in school:
    for name in student:
        student_list.append(name)
print(student_list)

students = [["Jane", "B"],
            ["Kate", "B"],
            ["Alex", "C"],
            ["Elsa", "A"],
            ["Max", "B"],
            ["Chris", "A"]]
best_students = [elt[0] for elt in students if elt[1] == "A"]
print(best_students)

# global variable
# Suivre la norme LEGB pour la portée des variables
user_city = "Istanbul"


def change_city(new_user_city):
    global user_city
    user_city = new_user_city


change_city("Paris")
print(user_city)

# Dictionary method
