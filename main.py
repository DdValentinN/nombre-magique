import random

def demander_nombre (nb_min,nb_max):


    nombre_int= 0
    while nombre_int==0:
        nombre_str = input(f"Combien ai-je de doigts ouverts ? (nombre compris entre {nb_min} et {nb_max} ?)")
        try:
            nombre_int= int(nombre_str)
        except ValueError :
            print("Erreur, tu dois rentrer un chiffre")
        else :
            if nombre_int <nb_min or nombre_int>nb_max:
                print(f"Vous devez impérativement rentrer un chiffre compris entre {nb_min} et {nb_max}. Réessayer")
                nombre_int= 0
    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN,NOMBRE_MAX)
nombre_vies = 4

nombre = 0
vies =nombre_vies
while not nombre == NOMBRE_MAGIQUE and vies> 0 :
    print(f"Il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE :
         print("Bravo, vous avez gagné")
    elif nombre < NOMBRE_MAGIQUE:
        print(" j'ai plus de doigts ouverts !")
        vies -= 1
    else:
        print("j'ai moins de doigts ouverts !")
        vies -= 1

if vies == 0 :
    print(f"Vous avez perdu ! J'avais  {NOMBRE_MAGIQUE}  doigts ouverts! ")