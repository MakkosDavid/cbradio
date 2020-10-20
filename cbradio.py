from collections import namedtuple

def atszamolpercre(ora, perc):
    return ora * 60 + perc
adas = namedtuple("adas", "Ora Perc AdasDb Nev")
soforok = set()
adasok = []
with open("cb.txt") as f:
    next(f)
    for sor in f:
        a = adas(int(sor.split(';')[0]), int(sor.split(';')[1]), int(sor.split(';')[2]),
                 sor.strip().split(';')[3])
        adasok.append(a)

van4 = False
for adas in adasok:
    if adas.AdasDb == 4:
        van = True
        break
if van4:
    print("4. feladat: Volt 4 adást inditó sofőr")
else:
    print("4. feladat: Nem volt 4 adást inditó sofőr")

for adas in adasok:
    soforok.add(adas.Nev)
soforbeker = input("Kérem adjon meg egy nevet: ")
if soforbeker in soforok:
    hivasdb = 0
    for adas in adasok:
        if adas.Nev == soforbeker:
            hivasdb += adas.AdasDb
    print(f"5. feladat: {soforbeker}-nak/nek összesen {hivasdb} db hívása volt")
else:
    print("5. feladat: Nincs ilyen nevű sofőr!")

with open("cb2.txt", "w") as f:
    f.write("Kezdés;Név;AdásDb\n")
    for adat in adasok:
        f.write(f"{atszamolpercre(adas.Ora, adas.Perc)};{adat.Nev};{adat.AdasDb}\n")
