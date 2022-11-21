import random

names = ["Frank","Shola","Tolu","Timmy","David","Daniel","John","Matthew","James","Paul", "Jude", "Ralf"]

pairing = []
for i in range(int(len(names)/2)):
    brother1 = random.choice(names)
    names.remove(brother1)
    brother2 = random.choice(names)
    names.remove(brother2)
    pairing.append("Bro "+brother1 + " & " + "Bro "+brother2)

print("The Pairings Are")

for i in pairing:
    print(i)
