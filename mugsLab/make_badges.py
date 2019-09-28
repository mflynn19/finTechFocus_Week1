from company_data import employees

#  In the adjacent file, there is a list of first names of all the people who work for a new app called Badges.
#  Their names are stored in a list called "employees".
#  For their holiday party, Jose (the CEO) wants to make personalized mugs for each one with their names on it, but the trouble is that a lot of workers have the same first names.
#  They'll save a lot of money if they can know how many of each name to make. Jose is asking you, his newest engineer, to order the mugs.

# 1. How many total mugs will you need to order? In other words, how many people work for the company?
len(employees)



# 2. How many DIFFERENT names will you need to print? In other words, how many unique, individual names are there in the company?
difNames = []
for employee in employees:
    if(difNames.count(employee)==0):
        difNames.append(employee)
len(difNames)



# 3. Almost forgot! Jose also needs you to print name tags for everyone for the holiday party.
#    For every name in the employees list, print out a string that says "Hello! My name is ______"

for employee in employees:
    print("Hello! My name is " + employee)



# 4. Let's practice counting just one name. Find out what the first name in the list is.
#    Then, iterate over the list and see how many people in the list share that same name.
shareName = 0
for employee in employees:
    if(employee == employees[0]):
        shareName +=1




# 5. Alright, let's finish the job: create the list of how many mugs per name.
listMugs = []

for name in difNames:
    listMugs.append({"Name":name,"numMugs":employees.count(name)})
print(listMugs)




# 6. Before you send it off to the printers, you should check your work. Make sure your final list has the same number of names as you found in #2, and orders the same number of mugs you found in number 1
print(str(len(listMugs)==len(difNames)))
totalMugs = 0
for name in listMugs:
    totalMugs += name["numMugs"]
print(str(totalMugs ==len(employees)))