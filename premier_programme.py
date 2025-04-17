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




# def demander_nom():
#     nom_reponse = ""
#     nom_reponse = input("Quel est votre nom ? ")

#     return nom_reponse
# prenom = "Ahmed"
# nom = demander_nom()
# print("Votre nom est : " +nom)
# print(f"Votre nom est : {nom}")
# print("Votre nom est : %s %s" % (nom,prenom))
# print("""
# Dima Dima Raja
#         o li mabghana ta3ma 3ayno
# """)


# print("Dima Dima Raja")
import random

bonus = 0
NBR_QUESTION = 4
for i in range(0,NBR_QUESTION):
    print(f"Question n°{i+1} sur {NBR_QUESTION}")
    nbr1 = random.randint(1,10)
    nbr2 = random.randint(1,10)
    operateur = random.choice(["+","-","*","/"])
    reponse = input(f"Calculez: {nbr1} {operateur} {nbr2} = ")
    if operateur == "+":
        result = nbr1 + nbr2
    elif operateur == "*":
        result = nbr1 * nbr2
    elif operateur == "/":
        result = int(nbr1 / nbr2)
    else :
        result = nbr1 - nbr2

    if int(reponse) == result :
        print("Réponse correcte")
        bonus += 1
    else :
        print("Réponse incorrecte")
    print()


print(f"Votre note est : {bonus} / {NBR_QUESTION}")
if  bonus == NBR_QUESTION:
    print("Géniaaaaal, t'es le meilleur")
elif  bonus == 0 :
    print("Révisez vos maths!")
elif bonus >= 2 :
    print("Pas mal !")
else :
    print("Peut mieux faire")
    

