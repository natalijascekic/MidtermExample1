#koliko je parnih i neparnih brojeva u  niza
broj_elemenata_niza = int(input("Unesite broj elemenata niza:"))

niz =[]
parni = 0
neparni = 0
for i in range(broj_elemenata_niza):

   element_niza = int(input("Unesite novi element:"))
   niz.append(element_niza)


for element_niza in niz:
    if(element_niza % 2) == 0:
        parni +=11
    else:
        neparni += 1

print(niz)
print(parni)
print(neparni)