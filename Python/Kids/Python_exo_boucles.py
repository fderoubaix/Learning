#Exo sur les boucles "for" et "while"

#Exo1
age=0
while age <= 30:
	print(age)
	age=age+2

#Exo2
y=1
Ingredients=['escargots','sangsues','tranche de gorille','sourcils de chenilles','orteils de mille-pattes']
for x in Ingredients:
	print(y, x)
	y=y+1

#Exo3
poids=80*0.165
for x in range(1, 16):
	poids=poids+0.165
	print("annee %s = le poids est de : %s" % (x, poids)) #Attention aux accents qui peuvent provoquer une erreur ! 