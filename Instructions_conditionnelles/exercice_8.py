def puissance_ball_ombre(type_pokemon_adverse):
    pi_attaque_ball_ombre = 80
    if type_pokemon_adverse in ["psy", "spectre"]:
        return pi_attaque_ball_ombre * 2
    elif type_pokemon_adverse == "tenebres":
        return pi_attaque_ball_ombre * 0.5
    elif type_pokemon_adverse == "normal":
        return pi_attaque_ball_ombre * 0
    else:
        return pi_attaque_ball_ombre

print(puissance_ball_ombre("tenebres"))


