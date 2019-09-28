import random

class Player:
  player_list = []
  player_count = 0

  def __init__(self, name):
    self.name = name
    self.strength = random.randint(8, 12)
    self.defense = random.randint(8, 12)
    self.speed = random.randint(8, 12)
    self.max_health = random.randint(18, 24)
    self.health = self.max_health
    self.alive = True

  print("Player " + self.name + " has entered the game. \n  Strength: " + str(self.strength) + "\n  Defense: " + str(self.defense) + "\n  Speed: " + str(self.speed) + "\n  Maximum health: " + str(self.max_health) + ".\n")
  Player.player_list.append(self)
  Player.player_count += 1
  print("There are currently " + str(Player.player_count) + " player(s) in the game.\n\n")
    
  def attack(self, target):
    print("Player " + self.name + " attacks " + target.name + "!!!")
    print(self.name + "'s strength is " + str(self.strength) + " and target " + target.name + "'s defense is " + str(target.defense) + ".")
    if self.strength < target.defense:
      print("Due to the target's strong defense, the attack only does half damage...")
      damage = self.strength / 2
    elif self.strength > target.defense:
      print("Since the target is weaker than you are, the attack does double damage!")
      damage = self.strength * 2
    else:
      print("These players are evenly matched. The attack goes through normally.")
      damage = self.strength
    self.decrease_health_by(target, damage)
    
    print(target.name + " now has " + str(target.health) + "/" + str(target.max_health) + " health remaining.\n\n")

  def decrease_health_by(self, target, damage):
    if target.health < 0:
      target.alive = False
      target.health = 0
    else:
      target.health -= damage
      
class Battle:
  def __init__(self, player1, player2):
    self.player1 = player1
    self.player2 = player2
    player = Player()
    
  #def start(self):
    #while self.player1.health > 0 or self.player2.health > 0: