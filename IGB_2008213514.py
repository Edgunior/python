# Glavni:
import proizvod

lista = proizvod.load("proizvodi.dat")
len1 = len(lista)

lista2 = list(filter(lambda p : proizvod.adekvatnost(p) < 240, lista))
len2 = len(lista2)

for p in lista2:
    print(proizvod.formatiran(p))

procenat = 100 * len2 / len1

print(f'Nakon filtriranja, ostalo je {procenat:.2f}% elemenata!')
