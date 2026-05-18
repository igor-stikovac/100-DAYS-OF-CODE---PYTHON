import random
import string

while True:    
    br_karktera = int( input("Dobrodosli u generator sifri!\nUnesite zeljeni broj karakter u sifri!\n") )

    if br_karktera < 10:
        print("Sifra mora imati najmanje 10 karaktera!")
        print("Pokusajte ponovo!")
        continue

    slova = int(input("Unesite koliko slova zelite u sifri: "))
    if slova < 1:
        print("Sifra mora imati bar dva slova!")
        print("Pokusajte ponovo!")
        continue

    brojevi = int(input("Unesite koliko brojeva zelite u sifri: "))
    if brojevi < 1:
        print("Sifra mora imati bar jedan broj!")
        print("Pokusajte ponovo!")
        continue

    specijalni_karakteri = int(input("Unesite koliko specijalnih karaktera zelite u sifri: "))
    if specijalni_karakteri < 1:
        print("Sifra mora imati bar jedan specijalni karakter!")
        print("Pokusajte ponovo!")
        continue
    
    if slova + brojevi + specijalni_karakteri > br_karktera:
        print("Zbir slova, brojeva i specijalnih karaktera ne moze biti veci od ukupnog broja karaktera u sifri!")
        print("Pokusajte ponovo!")
        continue

    break

sifra = []

for i in range(slova):
    sifra.append(random.choice(string.ascii_letters))

for i in range(brojevi):
    sifra.append(str(random.randint(0,9)))

for i in range(specijalni_karakteri):
    sifra.append(random.choice(string.punctuation))

random.shuffle(sifra)
        
print("Vasa sifra je: " + "".join(sifra))