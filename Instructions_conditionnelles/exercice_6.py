nbre_de = 4
votre_sante = 100
sante_adversaire = 120
puissance_attaque = 30

if nbre_de <= 2:
    votre_sante = votre_sante // 2
elif 3 <= nbre_de <= 8:
    sante_adversaire = sante_adversaire - puissance_attaque
else:
    sante_adversaire = 0

print(votre_sante)
print (sante_adversaire)