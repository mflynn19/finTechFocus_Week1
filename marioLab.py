def downstairs(flights):
    hash = "#"
    for i in range(0,flights):
      print(hash)
      hash += "#"
downstairs(4)
   
def upstairs(flights):
    for stairs in range(1, flights + 1):
        print(" " * (flights - stairs) + '#' * stairs)
upstairs(4)
        
def pyramid(flights):
    for stairs in range(0, flights + 1):
        print(" " * (flights - stairs) + '#' * stairs + " " + '#' * stairs + " " * (flights - stairs))
pyramid(4)
        