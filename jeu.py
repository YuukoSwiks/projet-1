import random

secret = random.randint(1, 100)
essais = 0
print("J'ai choisi un nombre entre 1 et 100. A toi de le trouver kelb ! ")

while True:
    reponse = int(input("Ton choix : "))
    essais = essais + 1
    if reponse < secret:
        print("c'est + tdc")
    elif reponse > secret:
        print("wallah c moins")
    else: 
        print("Bsahtek bg ta trouvé en", essais, "essais !")
        break
