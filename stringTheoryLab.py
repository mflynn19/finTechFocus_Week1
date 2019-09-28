# 1. Write a function called shout that takes in a string as an argument and returns it in all caps.
def shout(thing):
    return thing.upper()
    
print(shout("hello"))



# 2. Write a function called whisper that takes in a string as an argument and returns it in all lowercase.
def whisper(thing):
    return thing.lower()
print(whisper("HELLO"))



# 3. Write a function called how_many_letters that takes in a string as an argument and returns the number of letters in that string.
def how_many_letters(thing):
    return len(thing)
print(how_many_letters("elephant"))
    


# 4. Write a function called work_it that takes in a string as an argument and returns it backwards and with the first letter capitalized.
#    For example, work_it("I put my thing down flip it and reverse it") would return "Ti esrever dna ti pilf nwod gniht ym tup i"
def work_it(thing):
    new = thing.capitalize()
    return new[::-1]
print(work_it("i am hungry"))


# 5. Write a function called repeat_it that takes in a word and a number, and returns the word that many times.
#    For example, repeat_it("Banana", 3) would return "BananaBananaBanana"
def repeat_it(word,num):
   returnString=""
   for i in range(0,num):
       returnString += word
   return "" + returnString
   
print(repeat_it("Banana", 3))


# 6. Write a function called will_it_nametag that takes in a name and a number, and tells you whether the name can be printed on a nametag that size.
#    For example, will_it_nametag("Peter", 10) will return True, but will_it_nametag("Peter", 4) will return False, because "Peter" is 5 letters long, 
# and needs at least 5 spaces to fit on a nametag.
def will_it_nametag(name, numero):
    if (len(name) > numero):
        return False
    else:
        return True
print(will_it_nametag("Meghan", 8))


# 7. Write a function called add_liar that takes in two numbers and prints out a lie like "Sorry, I don't know how to add ___ and ___."
#    BUT even though it *prints* that it doesn't know the answer, have the function return the correct answer anyways.
def add_liar(first, second):
    print("Sorry, I don't know how to add " + first + " and " + second + ".")
    return str (first + second)



# 8. CHALLENGE: Now that you've written all these functions, try combining them. what would happen if you tried to call repeat_it(work_it("Stressed"), 3) ?
print(repeat_it(work_it("Stressed"), 3))


# 9. MEGA CHALLENGE: Write a function called doubler that takes in a string and returns it with every letter doubled.
#    For example, doubler("Lost in the Woods") would return "LLoosstt iinn tthhee WWooooddss"
def doubler(word):
    end = ""
    for elem in word:
        end += elem + elem
    return end
print(doubler("Mom"))

# 10. SUPER MEGA CHALLENGE: Head to https://codingbat.com/python/String-2 and attempt some of the challenges there!
