import random
import csv
import sys

#names of people to be paired
names = ["Johny","Frank","Shola","Tolu","Timmy","David","Daniel","John","Matthew","James","Paul", "Jude", "Ralf"]

def help():
        print("""To generate pairs run `python app.py filename.csv group length` 
                 e.g `python app.py result.csv 12`   
                    """)
    

class NamesPairGen:
    def __init__(self, name_list = [], source = sys.argv[1], length = sys.argv[2]):
        self.name_list = name_list
        self.name_pairs = []
        self.list_length = len(name_list)
        self.symetric = False
        self.source = source
        self.length = length

    def generate_pairs(self):
        if(self.list_length % self.length != 0):
            self.symetric = True

        for x in range(len(self.name_list)//self.length):
            current_pair = []
            for i in range(self.length):
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

    def output_pairs_in_csv_file(self):
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
        print("Grouped generated in result.csv")

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

    def read_csv_to_list(self):
        csvpath = input('Enter file path')
        with open(csvpath, newline='') as csvfile:
            list_of_names = csv.reader(csvfile, quotechar='|')
        for row in list_of_names:
            #print(', '.join(row))
            self.name_list.append(row)



if(sys.argv[1] != None and sys.argv[2] != None):
    generation = NamesPairGen()
    generation.read_CSV()
    generation.generate_pairs()
    generation.output_pairs_in_csv_file()
else:
    help()
