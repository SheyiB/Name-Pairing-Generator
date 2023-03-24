def area_of_rectangle(length, breadth):
    return length * breadth

def area_of_square():
    length = int(input("What is the length"))
    area = length**2
    print("The area of the square", area)

print("The Area is", area_of_rectangle(10,20))