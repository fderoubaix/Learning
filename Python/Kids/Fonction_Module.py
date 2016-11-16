#coding=utf-8
#Exercices sur la création et l'appel de fonctions
#
#===
#Exo1 : création de la fonction "poids_lune"
#===
def poids_lune(poids, increment):

 	for x in range(1, 16):
		poids=poids+increment
		print("annee %s = le poids est de : %s" % (x, poids))  
#utilisation de la fonction "poids_lune"
poids_lune(30, 0.45)

#===
#Exo2 : meme excercice avec 3 arguments
#===
def poids_lune2(poids, increment, annee):
	annee=int(annee) + 1
 	for x in range(1, annee):
		poids=poids+increment
		print("annee %s = le poids est de : %s" % (x, poids))  
poids_lune2(30, 0.45, 5)

#===
#Exo3 : meme excercice sans arguments mais avec des entrées utilisateur
#===
def poids_lune3():
	import sys
	print('entre ton poids actuel sur la terre :')
	poids=int(sys.stdin.readline())
	print('entre le poids que tu prends en plus chaque année :')
	increment=float(sys.stdin.readline())
	print('entre le nombre d\'année :')
	annee=int(sys.stdin.readline()) +1
 	for x in range(1, annee):
		poids=poids+increment
		print("annee %s = le poids est de : %s" % (x, poids))  
poids_lune3()
