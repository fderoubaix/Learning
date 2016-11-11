#Exercices sur les conditions "if"
#Exo 4
barres_choco = None
if barres_choco < 100 or barres_choco > 500:
	print("Trop peu ou beaucoup trop")

#Exo5
somme=None
if somme > 100 and somme < 500 or somme > 1000 and somme < 5000:
	print("La somme est comprise entre 100 et 500 ou entre 1000 et 5000")

#Exo6
ninjas=5

if ninjas < 10:
	print("Je peux affronter ces ninjas !")
elif ninjas < 30:
	print("Je vais devoir me battre mais je vais les avoir")
elif ninjas < 50:
	print("Il y en a trop")
else:
	print("My gad!")