# 1. Here's a list of all of Alex's favorite foods. For each food in the list, print out a statement that says "I really love _____" and then fill in the blank with each.
favorite_foods = ["Sushi", "Pizza", "Salmon", "Tamales dulces", "Yuca fries", "Apple pie", "Katsu curry", "Shrimp and grits", "Waffles"]
for food in favorite_foods:
  print("I really love " + food)


# 2. Now for each food in that list, let's be specific about how MUCH Alex likes them.
# For example, print out "Alex's #1 favorite food is Sushi" and then "Alex's #2 favorite food is Pizza" and so on until you've made an ordered list.
# This can be done a number of different ways, but the easiest is probably by iterating over each index in the favorite_foods list using a function called "range". Try to find it in the documentation.
for i in range(0, len(favorite_foods)):
  print("Alex's #" + str(i + 1) + " is " + favorite_foods[i])



# 3. Below is a massive list of numbers. Iterate over the list and print out only the even ones.
many_numbers = [109, 141, 44, 51, 133, 366, 339, 248, 226, 321, 97, 195, 245, 252, 238, 1, 366, 47, 189, 91, 148, 88, 194, 106, 5, 128, 165, 337, 380, 181, 143, 95]
for num in many_numbers:
  if (num % 2 == 0):
    print(num)
  



# 4. Below is a list of 99 names. Iterate over the list and find the longest name in the whole thing. Then print out "The longest name in the list is ______. It has ___ letters in it."
many_names = ["Alexa","Burke","Kasimir","Baxter","Carissa","Vielka","Derek","Jemima","Jackson","Keegan","Graham","Melissa","Jeanette","Grant","Kirsten","Naida","Brody","Ishmael","Kane","Seth","Rae","Eagan","Camille","Alana",
  "Vance","Melinda","Tarik","Risa","Jordan","Camilla","Karly","Baker","Adena","Calvin","Kendall","Nasim","Kellie","Dana","Rhoda","Linus","Tyler","Ahmed","Dante","Shay","Lael","Tana","Claudia","Chadwick","Tara",
  "Fulton","Justine","Malcolm","Rowan","Christopher","Ciaran","Ivan","Hiram","Blake","Colton","Nathaniel","Moses","Cynthia","George","Ignacia","Chanda","Wyatt","Amethyst","Vladimir","Adam","Boris","Joseph","Scarlett","Kieran","Curran",
  "Dalton","Paul","Phillip","Plato","Renee","Natalie","Barbara","Keiko","Oleg","Xerxes","Caesar","Kareem","Ahmed","Charles","Cyrus","Adria","Winifred","Pandora","Wynne","Simon","Wanda","Coby","Nolan","Marsden","Courtney"]
longName = many_names[0]
for name in many_names:
  if (len(longName) < len(name)):
    longName = name
    
print("The longest name in the list is " + longName)


# 5. Take that same list and sort it into two lists: one list of long names, which have more than 6 characters, and one list of short names which have 6 or fewer characters. Then print out both lists.
short = []
long = []
for name in many_names:
  if (len(name) > 6):
    long.append(name)
  else:
    short.append(name)
print(short)
print(long)