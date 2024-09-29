def pokemon_adversaire(pokemon_choisi):
    import random
    if pokemon_choisi == "Germignon":
        pokemon_adversaire = random.randint(0,1)
        if pokemon_adversaire == 0:
            return "Hericendre"
        else:
            return "Kaiminus"
    elif pokemon_choisi == "Hericendre":
        pokemon_adversaire = random.randint(0,1)
        if pokemon_adversaire == 0:
            return "Germignon"
        else:
            return "Kaiminus"
    else:
        pokemon_adversaire = random.randint(0,1)
        if pokemon_adversaire == 0:
            return "Germignon"
        else:
            return "Hericendre"

print(pokemon_adversaire("Kaiminus"))