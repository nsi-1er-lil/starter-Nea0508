def puissance_finale_subie(puissance_initiale, type_attaque):
     if type_attaque == "acier" or type_attaque == "electrique" or type_attaque == "vol":
         return puissance_initiale / 2
     elif type_attaque == "sol":
         return puissance_initiale * 2
     else:
         return puissance_initiale
     
print(puissance_finale_subie(120, "sol"))