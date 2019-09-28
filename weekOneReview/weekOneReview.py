#1 Print your name to the console!
print("Meghan Flynn")

#2 Ask for a user's birthday year and return how old they will turn this year.
def birthday():
    birthday = input("What year were you born?\n")
    answer = 2019 - int(birthday)
    return answer

#3 Write a short program that asks the name of the user.  If they write in all caps, thank them for their enthusiasm.  Otherwise, ask them to speak louder next time.
#NOT CRITICAL PATH: Make the program repeatedly ask the user for their name, until they finally comply and write it in all caps.
shout = False
while (shout == False):
    name = input("What is your name?\n")
    if (name == name.upper()):
        print("Thanks for the enthusiasm!")
        shout = True
    elif (name == name.lower()):
        print("Speak louder next time please.")



#4 Write a function that tells whether a number is divisible by 3.
def threes(number):
    if (number % 3 == 0):
        return True
    else:
        return False


#5 Write a function that takes in three numbers and tells the user which one is the largest.
def maximum(first, second, third):
    return "The largest number is " + str(max(first, second, third))
print(maximum(1,2,3))


#6 Write a function that takes in the per-person cost of breakfast and the per-person cost of lunch, and then calculates the cost of all food for the three-week FinTech program.
def totalCost(breakfast, lunch):
    days = 15
    people = 19
    return (breakfast + lunch) * 15 * 19



#7 Here is a list (which you will un-comment):
classesInHighSchool = ["Algebra", "French", "Physics", "Global History", "Gym", "English", "Biology", "Band"]
# Add another course at the end of the list.  Print your new list.
# Let's say you didn't take French in high school.  Replace French with a class you did take.  Print your new list.
# Alphabetize the list.  Print your new list.
# NOT CRITICAL PATH: Create a new list that contains only the 7-letter elements from your list.  Print this new list.
classesInHighSchool.append("Chorus")
print(classesInHighSchool)
classesInHighSchool[1] = "Spanish"
classesInHighSchool.sort()
newSchedule = []
for course in classesInHighSchool:
    newSchedule.append(course)
print(newSchedule)


#8a Write a line of code that will enable this Python file to pull from the baseballTeamsEast dictionary in baseball.py
from baseball import baseballTeamsEast

#8b Print the city where the Braves play.
print(baseballTeamsEast["Braves"])

#8c Correct the city of the Blue Jays.  They actually play in Toronto.
baseballTeamsEast["Trenton"] = "Toronto"

#8d Remove the entry for the Jets.  They play football, not baseball.
baseballTeamsEast.pop("Jets")
print(baseballTeamsEast)

#8e Add a key-value pair for the Yankees (or the Mets, if you have bad taste).
baseballTeamsEast["Yankees"] = "New York"


#9 Uncomment the line below.  Then write code that will print the first element of the second element of the third element.
myAlphabet = [[["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]], [["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r"]], [["s", "t", "u"], ["v", "w", "x"], ["y", "z", "end"]]]
print(myAlphabet[2][1][0])