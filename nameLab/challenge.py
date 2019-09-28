from database import people

# All the survey responses are stored in a list called "people". (Remember to use dot syntax!)



# 1. Print out the name of the first person who responded to the survey
print(people[0]["Name"])



# 2. Print out Brenton's second favorite band
print(people[7]["Favorite Bands"][1])



# 3. For each person on this list, print out a descriptor of where they live in the form "____ lives in _____."
for person in people:
    print(person["Name"] + " lives in " + person["State"])



# 4. Print out each person's nickname. Write some control flow that determines whether / how to respond if someone didn't provide a nickname.
for person in people:
    if (person["Nickname"] != ""):
        print(person["Nickname"])
    else:
        print(person["Name"])



# 5. Find the average of the respondents' ages.
total = 0
for person in people:
    total += person["Age"]
average = total/ len(people)



# 6. Print out the percentage of respondents who have brown hair.
totalBrown = 0
for person in people:
    if(person["Hair Color"] == "Brown"):
        totalBrown += 1
print(totalBrown/len(people)*100)



# 7. Create two new lists - one for programmers, and one for non programmers.
#    Sort all the people in the main list into these two more specific lists.
prog = []
nonprog = []
for person in people:
    if (person["Is Programmer"] == True):
        prog.append(person)
    else:
        nonprog.append(person)



# 8. Iterate over the list in order to figure out how many respondents listed "The Office" as one of their favorite shows.
officeFan = 0
for person in people:
    if (person["Favorite Shows"].count("The Office") > 0):
        officeFan += 1



# 9. Print out a list of all the bands that are liked by at least two people.
#    Pro-tip: some respondents capitalized band names and other respondents did not, so for example, if Panic at the Disco isn't listed, your code isn't accurately reporting your results.
allBands = []
popularBands = []
for person in people:
    allBands += person["Favorite Bands"]
allBands.sort()
prevBand = allBands[0]
for band in allBands[1:]:
    if (band.upper() == prevBand.upper() and popularBands.count(band.upper()) == 0):
        popularBands.append(band.upper())
    prevBand = band
print(popularBands)




# 10. Identify anyone on the list who has no common interests (bands or shows) with anyone else. Print their names.
allBands = []
allShows = []
blandPeople = []

for person in people:
    allBands += person["Favorite Bands"]
    allShows += person["Favorite Shows"]
    
for band in allBands:
    band = band.upper()

for show in allShows:
    show = show.upper()
    
for person in people:
    noCommonBand = True
    noCommonShow = True
    for band in person["Favorite Bands"]:
        if (allBands.count(band.upper()) > 1):
            noCommonBand = False
    for show in person["Favorite Shows"]:
        if(allShows.count(show.upper()) > 1):
            noCommonShow = False
    if (noCommonBand & noCommonShow):
        blandPeople.append(person["Name"])
        
print(blandPeople)