#conversion de binaire en decimale

def base10(binaires):
    return int(str(binaires) , 2)
"""
def base10(binaires):
    #cette fonction convertie un nombre du binaire en base 10.
    #il y a des cersion plus simplifiè avec int(a ,2) direct
    binaires = str(binaires)
    bits = [int(bit) for bit in binaires]
    i = 1
    decimal = 0
    for bit in bits:
        decimal += bit * (2 ** (len(bits) - i))
        i += 1
    return decimal"""

#calculatrice du nombre de bit
def nombre_bit(a):
    """cette fonction permet d'obtenir le nombre de bits minimal equivalent a un nombre decimal donne"""
    k = 1
    while 2 ** k <= a:
        k += 1
    return k


#conversion de decimale en binaires

def base2(a):
    retour = 0
    i = 0
    while a != 0:
        c = a % 2
        if c == 1:
            retour += 10 ** i
        a = a // 2
        i += 1
    return retour


# conversion du decimale en octet dans la base2
def base2_octet(a):
    """cette fonction permet de convertir un nombre reel inferieur a 255 en binaire avec 8 bits :
     elle est usuelle dans la conversion des addrsses ipv4 du decimale a point en binaire"""
    ajouts_zero = 8 - nombre_bit(a)
    octet = (ajouts_zero * "0" + str(base2(a)))
    return octet


# convesion des addrsses ipv4 du decimale a point en binaire
def ip_base2(ipv4_dec):
    liste_octets_str = ipv4_dec.split(".")
    liste_octets_int = [int(octet) for octet in liste_octets_str]
    liste_octets_bin = [base2_octet(octet) for octet in liste_octets_int]
    ipv4_bin = ".".join(liste_octets_bin)
    return ipv4_bin


#conversion d'addresse ipv4 du binaire en decimale a point
def ip_base10(ipv4_bin):
    liste_octets_str = ipv4_bin.split(".")
    liste_octets_int = [int(octet) for octet in liste_octets_str]
    liste_octets_dec = [str(base10(octet)) for octet in liste_octets_int]
    ipv4_dec = ".".join(liste_octets_dec)
    return ipv4_dec


#recherche d'addresse de sous resau a partir du nombre de bits du reseau
def masque_de_s_r(bits):
    """cette fonction convertis la classe en addresse decimale a point
    ex : /24-->bits : 24 --> 255.255.255.0"""
    if bits <= 0 or bits > 30:
        print("Erreur: sous reseau invalide")
        raise SystemExit("Fin du programme")
    else:
        nbr_oct = bits // 8
        bit_rest = bits % 8
        a = 0
        i = 1
        while i <= bit_rest and bit_rest % 8 != 0:
            a += 2 ** (8 - i)
            i += 1
        add_sr = nbr_oct * "255." + str(a) + (3 - nbr_oct) * ".0"
        return add_sr




# fonction permettant de faire le et loique
def etlogique(a):
    """Ctete fonction nous permet de faire le et logique par addition des bits si la somme de deux bits
    donne deux (les deux sont des bits de 1 ) alors le resultat donne 1 sinon 0 . le resultat est renvoyer
    sous forme de liste de bits """
    l = []
    for i in range(7, -1, -1):
        if a // (10 ** i) == 2:
            l.append(1)
        elif a // (10 ** i) == 1 or a // (10 ** i) == 0:
            l.append(0)
        a = a - ((a // (10 ** i)) * (10 ** i))
    return l


#fonction permettant de calculer l'addresse reseau a partir d'une addresse ip et d'un masque de sous reseau
#le masque de sous reseau utilise ici est le nombres de bites de la partie reseau (/23 /24 /8 .....)mis sana le slash

def add_reseau(ad, bits):
    #onconvertion du masque du sous reseau en decimale à point avec la fonction masque_de_s_r
    sr_dec = masque_de_s_r(bits)
    #Convertion du masque de sous reseau et l'addresse ip en binare de quatre octets
    ad_dec = ip_base2(ad)
    sr = ip_base2(sr_dec)
    #Convertion du masque de sous reseau et l'addresse ip du binare de quatre octets en une liste de quatre elements
    #chaque octet correspond a une chaine (un element de la liste)
    l1 = ad_dec.split(".")
    l2 = sr.split(".")
    #pour pouvoir faire le etlogique on convertis les elementsde notre liste du string en entier
    l1 = [int(i) for i in l1]
    l2 = [int(j) for j in l2]
    #on somme les elements des deux listes monberes à mambres et on le place dans un tableau l3
    l3 = [l1[r] + l2[r] for r in range(len(l1))]
    #etant donne que nous voulons appliquer le et logique a base de la somme dans le l3 ,
    #on fait appellea la fonction etlogique qui se base sur le chiffre (2 = 1+1 =1 et 1 donc 1) et
    # les autres cas 0 une fois fais on envoie les valeurs obtenue dans la liste lf
    lf = []
    for i in range(len(l1)):
        lf.append(etlogique(l3[i]))
    #on reconveris la liste en chaine de ces ocets separer par des points et ensuite avec la fonction
    #ip_base10 on le reconveri en decimale à point
    l4 = []
    for m in range(4):
        a = ""
        for n in range(8):
            a += str(lf[m][n])
        l4.append(a)
    for q in range(len(l4)):
        l4[q] = str(base10(int(l4[q])))
    sort = ".".join(l4)
    return sort


def monetlogique(a):
    l = []
    for i in range(7, -1, -1):
        if a // (10 ** i) == 1:
            l.append(1)
        elif a // (10 ** i) == 0:
            l.append(0)
        a = a - ((a // (10 ** i)) * (10 ** i))
    return l


#focntion permettant de calculer l'addresee reseau et de brodcoast selon que les bits hots prennent respectivement tous 0 ou 1
def add_reseaux(ad, bits, replace_bit):
    ad_dec = ip_base2(ad)
    l1 = ad_dec.split(".")
    l1 = [int(i) for i in l1]
    lf = []
    for i in range(len(l1)):
        lf.append(monetlogique(l1[i]))
    l5 = []
    for m in range(4):
        for n in range(8):
            l5.append(lf[m][n])
    for p in range(bits, 32):
        l5[p] = replace_bit
    l6 = []
    l7 = []
    for t in range(32):
        l6.append(l5[t])
        if t in [7, 15, 23, 31]:
            l7.append(l6)
            l6 = []
    l4 = []
    for m in range(4):
        a = ""
        for n in range(8):
            a += str(l7[m][n])
        l4.append(a)
    for q in range(len(l4)):
        l4[q] = str(base10(int(l4[q])))
    sort = ".".join(l4)
    return sort


#deuxieme facon de chercher l'addresse reseau
def add_reseau2(ad, bits):
    sort = add_reseaux(ad, bits, 0)
    return sort


#Addresse de diffusion
def add_diff(ad, bits):
    sort = add_reseaux(ad, bits, 1)
    return sort


#fonction permettant de determiner le premirer et le dernier addresse utilisable dans un reseau
def extreme_add(ad, bits, replace_bit, end_replace):
    ad_dec = ip_base2(ad)
    l1 = ad_dec.split(".")
    l1 = [int(i) for i in l1]
    lf = []
    for i in range(len(l1)):
        lf.append(monetlogique(l1[i]))
    l5 = []
    for m in range(4):
        for n in range(8):
            l5.append(lf[m][n])
    for p in range(bits, 32):
        l5[p] = replace_bit
        if p == 31:
            l5[p] = end_replace
    l6 = []
    l7 = []
    for t in range(32):
        l6.append(l5[t])
        if t in [7, 15, 23, 31]:
            l7.append(l6)
            l6 = []
    l4 = []
    for m in range(4):
        a = ""
        for n in range(8):
            a += str(l7[m][n])
        l4.append(a)
    for q in range(len(l4)):
        l4[q] = str(base10(int(l4[q])))
    sort = ""
    for o in l4:
        sort += o + "."
    sort = sort.strip(".")
    return sort


#Premier addresse utilisable dans un reseau
def first_add(ad, bits):
    sort = extreme_add(ad, bits, 0, 1)
    return sort


#Dernier addresse utilisable dans un reseau
def last_add(ad, bits):
    sort = extreme_add(ad, bits, 1, 0)
    return sort
