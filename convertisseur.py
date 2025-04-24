# Programme de conversion du pouces vers cm ou l'inverse


v_continue = True
while (v_continue) :
    v_choix = input("Voulez vous convertir du pouces vers cm ou l'inverse ? Tapez 1 pour le premier choix et 2 pour le 2ème : ")
    if v_choix == "1" :
        v_valuer = input("Veuillez entrer la valeur en pouces à convertir : ")
        v_resultat = float(v_valuer) * 2.54
        print(f"La valeur convertie {v_resultat} cm")
    elif v_choix == "2":
        v_valuer = input("Veuillez entrer la valeur en cm à convertir : ")
        v_resultat = float(v_valuer) * 0.394
        print(f"La valeur convertie {v_resultat} pouces")
    else :
        print("Le choix que vous avez taper n'existe pas")

    v_sortir = input("Voulez vous réessayer ? O(OUI) / N(NON) : ")
    if v_sortir == "N" or v_sortir == "NON":
        v_continue = False

    