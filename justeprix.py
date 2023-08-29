# Tirer au sort un prix entre 1 et 10
import random

r = random.randint(1, 10)
essais_restants = 5
while essais_restants > 0:
    try :  # GESTION D'EXCEPTION
        choix= int(input("Donnez votre prix: "))
    except ValueError :      # un type d'erreur
        print("Veuillez entrer un chiffre")
        continue

# Message "Bravo" si le prix est trouvé
    if r == choix:
        print(f"Bravo ")
        break
# Message "Pas assez" si prix trop bas
    elif choix< r:
        print(f"Pas assez il vous reste {essais_restants} essais")
# Message "Trop élévé" si prix trop haut
    elif choix> r:
        print(f"Trop élévé il vous reste {essais_restants} essais")
# Message "Perdu" au bout de cinq essais
    essais_restants -= 1
print(" Perdu trop d'essais")



# Fin au bout de cinq essais ou si le prix est trouvé