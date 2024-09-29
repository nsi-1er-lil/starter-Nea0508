# t (temps du parcours), v_1 (vitesse au debut), v_2 (vitesse a la fin)

def acceleration_moyenne(t, v_1, v_2):
    return (v_2-v_1) / t

print(acceleration_moyenne(20, 30, 90))