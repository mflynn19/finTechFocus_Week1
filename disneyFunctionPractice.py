#Task 1) How much money does it cost to enter Disney Land?
#How many people, which park, how much per ticket, staying over/day ticket, age (number of kids and adults), souvenirs, food, & travel expenses
# adult ticket is $100 - kid's ticket is $80

# def familyPrice(adults, kids, days):
#   legal = 100 * adults
#   minors = 80 * kids
#   total = (legal + minors) * days
#   return total

# print(familyPrice(2,3,2))

#Task 2 - Calling with Variables
def greet(player):
  #Special logic to greet JJJS
  name = input("Welcome! What is you name?\n")
  if (player.lower() == "john jacob jingleheimer schmidt"):
    return "Hi Guy!"
  else:
    return "Ew."
  
  print(greet(name))

#Test your function by calling it with an inputted name
  # name1 = input("Enter player 1's name")
  # print(greet(name1)) # Notice that we're passing a variable as the argument for our greet function.

  # name2 = input("Enter player 2's name")
  # print(greet(name2))





#Task 3 - Default Variables
# def greetPlayer(name = "User"):
#   print("Welcome to the game, " + name + ".")
#   print("Your current level is 1.")

# greetPlayer("David") # Code if the user provides their name
# greetPlayer()  # Code if the user chooses not to provide their name



# def createUser(name, email, password = "abcd1234"):
#   # Some code to create the user

# createUser("John Smith", "Jsmith123@gmail.com")
# createUser("Marta Guzman", "MartaG789@gmail.com", "Puppies1")
# createUser("Artie Krausmann")




#Task 3) Scope >=[
age = 15
def have_a_birthday():
    global age
    age = 20
    age += 1
    print("Happy birthday! You're now " + str(age))
    return age

have_a_birthday()

print(age)