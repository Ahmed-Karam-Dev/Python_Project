# Karamora 04/10/2025
"""
 Premier code python
pour commenter un bloc de données : Ctrl + /
généralement, il n'a pas de constantes dans python mais par convention on déclare les constantes avec un nom majiscule
"""

# nom = input("Quel est votre nom ? ")
# age = input("Quel est votre age ? ")

# try:
#     age_prochain = int(age) + 1
# except:
#     print('Erreur, veuillez entrer un age valide')  
# else:
#     print("Tu es " + nom + " et l'année prochaine t'aura " + str(age_prochain))  


# --------------------------------------------------------------------------------------------------------------------------------------
# n = 0

# while n < 10 :
#     print("Le nombre est : " + str(n))
#     n = n + 1

# print("fin de la boucle")    


# --------------------------------------------------------------------------------------------------------------------------------------
# mot_choisi = ""

# while mot_choisi != "TOTO" :
#     mot_choisi = input("Veuillez entrer le nom recherché :")

# print("Bravoooo!!!!!!")    




def demander_nom():
    nom_reponse = ""
    nom_reponse = input("Quel est votre nom ? ")

    return nom_reponse
prenom = "Ahmed"
nom = demander_nom()
print("Votre nom est : " +nom)
print(f"Votre nom est : {nom}")
print("Votre nom est : %s %s" % (nom,prenom))
print("""
Dima Dima Raja
        o li mabghana ta3ma 3ayno
""")


print("Dima Dima Raja")