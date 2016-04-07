import os
print("Bienvenue sur BC Dox")

#Menu
print("Que voulez vous faire?")
print("1 pour creer une nouvelle cible")
print("2 pour lire une cible")
menu = input()
if menu == "1":
	
	#Prenom
	print("Entrer le prenom de la cible")
	prenomDeLaPersonne = input()
	print("La cible a pour prenom :", prenomDeLaPersonne)

	#Nom
	print("Entrer le nom de la cible")
	nomDeLaPersonne = input()
	print("La cible a pour nom :", nomDeLaPersonne)
	
	#Ville de résidence
	print("Entrer la ville de résidence de la cible")
	ville = input()
	print("Votre cible est dans cette ville :", ville)
	
	#Création du fichier
	print("création du fichier")
	nomPrenom = nomDeLaPersonne + prenomDeLaPersonne
	fichierCible = open(nomPrenom , 'a')
	fichierCible.close()

	#Enregistrement des infos
	print("enregistrement des infos")
	fichierCible = open(nomPrenom , 'w')
	fichierCible.write(prenomDeLaPersonne)
	fichierCible.write("\n")
	fichierCible.write(nomDeLaPersonne)
	fichierCible.write("\n")
	fichierCible.write(ville)
	fichierCible.close()
	
	
	

elif menu == "2":
	print("Entrer les nom puis le prenom de la cible tous colée")
	choixDeLaPersonne = input()

	#Lecture ligne par ligne
	fichierCible = open(choixDeLaPersonne, 'r')
	fichierCible1 = fichierCible.readline(62)
	fichierCible2 = fichierCible.readline(62)
	fichierCible3 = fichierCible.readline(62)
	fichierCible.close()
	
	#Info de la personne
	print("La cible a pour prenom :", fichierCible1)
	print("La cible a pour nom :", fichierCible2)
	print("La cible habite a:", fichierCible3)
	
	
	
else:
	print("Numéro invalide")
