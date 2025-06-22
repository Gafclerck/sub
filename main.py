from ip_fonctions import *

ad = "259.168.2.3"
bits = 24
print(f"Addresse Réseau : {add_reseau(ad, bits)}")
print(f"Addresse Réseau : {add_reseau2(ad, bits)}")
print(f"Addresse de Diffusion : {add_diff(ad, bits)}")
print(f"Premiere Addresse : {first_add(ad, bits)}")
print(f"Dernière Addresse : {last_add(ad, bits)}")

