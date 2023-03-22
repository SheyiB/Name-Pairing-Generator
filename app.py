import random

#names of people to be paired
names = ["Frank","Shola","Tolu","Timmy","David","Daniel","John","Matthew","James","Paul", "Jude", "Ralf"]

#Pairing list
pairing = []

class NamesPairGen(object):
    def __init__(self):
        pass
    
def generatePairs():
    #Looping through the pairing len/2 times because pair is in 2
    for i in range(int(len(names)/2)):
        #Generate first random name
        brother1 = random.choice(names)
        #Remove generated name from list
        names.remove(brother1)
        #Generate second name
        brother2 = random.choice(names)
        #Remove generated name from list
        names.remove(brother2)
        #Join generated pair and add it to list array
        pairing.append("Bro "+brother1 + " & " + "Bro "+brother2)

def showPairs():
    print("The Pairings Are")
    #Print pairing
    for i in pairing:
        print(i)
