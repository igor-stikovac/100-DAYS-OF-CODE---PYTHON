import random

friends = ["Valerija","Igor","Jana","Mihajlo","Biljanja","Milos"]

#1 option
index_placanja = random.randint(0, len(friends)-1)
print("Racun placa " + friends[index_placanja] + "!")

#2 option

print("Racun placa " + random.choice(friends) + "!")

