# proizvod.py:

import math

# Korak 1:
def Proizvod(ime, pro, god, masa, mat):
    dozvoljeniMat = [ 'DRVO', 'PLASTIKA', 'METAL', 'STAKLO', 'PLATNO', 'DRUGI_MATERIJAL' ]

    if mat not in dozvoljeniMat:
        return False

    if masa < 0.01:
        return False

    return {
        "naziv": ime,
        "proizvodjac": pro,
        "godina": god,
        "masa": masa,
        "materijal": mat
    }

# Funkcija za proveru da li je dobra rec:
def isOk(p):
    if type(p) != dict:
        return False

    potrebni = [ 'naziv', 'proizvodjac', 'godina', 'masa', 'materijal' ]

    for potrebanKljuc in potrebni:
        if potrebanKljuc not in p.keys():
            return False

    return True

# Korak 2:
def adekvatnost(p):
    if not isOk(p):
        return False

    tablicaK = {
        "DRVO": 0.98,
        "PLASTIKA": 0.93,
        "METAL": 0.21,
        "STAKLO": 1.45,
        "PLATNO": 1.1,
        "DRUGI_MATERIJAL": 2.12
    }

    materijal = p['materijal']

    k = tablicaK[materijal]

    return ((2050 - p['godina']) * math.sqrt(p['masa'])) / (1 - k)

# Korak 3:
def formatiran(p):
    if not isOk(p):
        return False

    red1 = "{0:12s}{1:20s}{2:13s}{3:13.3f} kg\n".format("Naziv:", p['naziv'], "Masa:", p['masa'])
    red2 = "{0:12s}{1:20s}{2:13s}{3:8d}. godine\n".format("Proizvodac:", p['proizvodjac'], "Proizvedeno:", p['godina'])
    red3 = "{0:12s}{1:20s}{2:13s}{3:16.2f}\n".format("Materijal:", p['materijal'].lower(), "Adekvatnost:", adekvatnost(p))

    return red1 + red2 + red3

# Korak 4:
def load(imeDatoteke):
    with open(imeDatoteke, 'r') as ulaz:
        proizvodi = []

        while True:
            ime = ulaz.readline().strip()

            if ime == "":
                break

            pro = ulaz.readline().strip()

            godinaString = ulaz.read(4)
            godina = int(godinaString)

            masaString = ulaz.read(4).strip()
            masa = int(masaString)

            oznakaM = ulaz.readline().strip()

            tabMaterijala = {
                "D": 'DRVO',
                "P": 'PLASTIKA',
                "M": 'METAL',
                "S": 'STAKLO',
                "T": 'PLATNO',
                "O": 'DRUGI_MATERIJAL'
            }

            mat = tabMaterijala[oznakaM]

            p = Proizvod(ime, pro, godina, masa, mat)

            if p == False:
                print('Greska pri ucitavanju!')
                exit()

            proizvodi.append(p)

        return proizvodi
