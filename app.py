import random
import csv
import sys

#names of people to be paired
bch_students = []
with open(sys.argv[1], newline='') as csvfile:
    list_of_names = csv.reader(csvfile, quotechar='|')
    for row in list_of_names:
        #print(', '.join(row))
        bch_students.append(row)
names = ["Johny","Frank","Shola","Tolu","Timmy","David","Daniel","John","Matthew","James","Paul", "Jude", "Ralf"]



class NamesPairGen:
    def __init__(self, name_list = [], source = sys.argv[1]):
        self.name_list = name_list
        self.name_pairs = []
        self.list_length = len(name_list)
        self.symetric = False
        self.source = source

    def generate_pairs(self, length):
        if(self.list_length % length != 0):
            self.symetric = True

        for x in range(len(self.name_list)//length):
            current_pair = []
            for i in range(length):
                name = random.choice(self.name_list)
                current_pair.append(name)
                self.name_list.remove(name)
            self.name_pairs.append(current_pair)
        
        if(self.symetric):
            for y in range(len(self.name_list)):
                name = random.choice(self.name_list)
                self.name_pairs[y].append(name)
                self.name_list.remove(name)
            # print("List not symetric, not all Groups will have equal numbers")


    def generate_pair_in_csv_file(self):
        for x in range(len(self.name_pairs)):
           
            with open('result.csv', 'a', newline='') as csvfile:
                result = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                result.writerow(['Group', x+1])
            for y in self.name_pairs[x]:
               
                with open('result.csv', 'a', newline='') as csvfile:
                    result = csv.writer(csvfile, delimiter=' ',  quoting=csv.QUOTE_MINIMAL)
                    result.writerow(y)
            
            with open('result.csv', 'a', newline='') as csvfile:
                    result = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                    result.writerow('\n')
            

    def show_pairs(self):
         for x in range(len(self.name_pairs)):
            print("Group ", x+1)
            for y in self.name_pairs[x]:
                print(y, end= ' ')
            print(" ")
            
    def read_CSV(self):
        with open(self.source, newline='') as csvfile:
            list_of_names = csv.reader(csvfile, quotechar='|')
        for row in list_of_names:
            self.names_list.append(row)

churchBrothers = NamesPairGen(bch_students)

churchBrothers.generate_pairs(10)

churchBrothers.show_pairs()