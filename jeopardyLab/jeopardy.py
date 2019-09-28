import requests
import random
from similar_text import similar_text
from prettytable import PrettyTable


#JSON objects are pm dictionaries
response = requests.get('http://jservice.io/api/clues?category=139').json()

print(response)
#Levels 1-3
rounds = 100
score = 0
while (rounds < 101):
    trivia = random.randint(0, len(response))
    print(response[trivia]["question"])
    answer = input(" ").upper()
    if (response[trivia]["answer"].upper() == answer):
        print("Congratulations! That's the correct answer!")
        score += response[trivia]["value"]
        print(score)
    elif (similar_text(response[trivia]["answer"].upper(),trivia)):
        print("You were so close to the correct answer! Type carefully next time!")
    else:
        print("Sorry. That's incorrect. The correct response would be " + response[trivia]["answer"])
        score += response[trivia]["value"]
        print(score)
    rounds -= 1

#Level 4
board = PrettyTable()
column_names = ["5 Letter Word", "Area", "Population", "Annual Rainfall"]

    



