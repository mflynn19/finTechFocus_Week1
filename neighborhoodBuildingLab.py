# Level 1:
# Create a class called Student that has two attributes: a name, and a grade.
class Student:
    def __init__(self, name, grade, savings_account):
        self.name = name
        self.grade = grade
        self.savings_account = savings_account


# Now create instances of three different students (student1, student2, and student3).
shirley = Student("Shirley", 90, 10000)
bob = Student("Bob", 100, 400000)
tweed = Student("Tweed", 65, 700000)


# Confirm that the class works by printing out the first student's name.
print(shirley.name)

# Level 2:
# Create a class called School that has three attributes: a name, a type, and a size.
class School:
    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size


# Create instances of three individual schools.
jfk = School("JFK", "middle", "medium")
mlk = School("MLK", "high", "small")
fdr = School("FDR", "elementary", "large")


# Confirm that the class works by printing out the name and size of the third school.
print(fdr.name)
print(fdr.size)


# Level 3:
# Create a class called House that has four attributes: an address, a size, a price, and a number of bedrooms.
class House:
    def __init__(self, address, size, price, bedrooms):
        self.address = address
        self.size = size
        self.price = price
        self.bedrooms = bedrooms
    

# Create instances of at least three individual houses using.
mainSt = House("123 Main", "medium", 250000, 4)
birdSt = House("321 Bird", "large", 700000, 4)
concord = House("123 Concord", "small", 10000, 1)




# Confirm that the class works by printing out the address and size of the second house.
print(birdSt.address)
print(birdSt.size)


# Level 4: (Stretch)
# Put your three students in a list called my_students, your houses in a list for houses, and your schools in a list for schools.
my_students = [shirley, bob, tweed]
houses = [mainSt, birdSt, concord]
schools= [fdr, mlk, jfk]


# Iterate over the student list, printing out "_____ is in grade __." For each of the students.
for student in my_students:
    print(student.name + " is in grade " + str(student.grade) + ".")


# Iterate over the houses list and print out a description for each one. Do the same for your schools lists.
for house in houses:
    print(house.address + " is a " + house.size + " sized house.")


# Level 5: (Stretch)
# Modify your student class above to include a savings_account value for each student. Change your initializers so that the code still runs. 



# Write some code that compares a student and a house, and determines whether or not the student can afford to buy the house. 
for i in range(0,len(my_students)):
    for j in range(0, len(houses)):
       if my_students[i].savings_account >= houses[j].price:
           print(my_students[i].name+" can afford to buy "+houses[j].address)
           
       