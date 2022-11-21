import random

names = ["Elijah","Abiodun","Joshua","Timothy","Dayo","Daniel","Bamidele","Marvellous","James","Dotun", "Olaolu", "Afeez"]

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
