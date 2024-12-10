import random, os

class Target():
    def __init__(self):
        self.health = random.randint(5, 10)
        self.power = random.randint(3, 7)
        self.shield = random.randint(3, 7)
        self.alive = True

    def hit(self, player):
        attack = self.power - player.shield
        player.health -= attack
        if player.health <= 0:
            player.alive = False

class Player():
    def __init__(self):
        self.health = 50
        self.power = 7
        self.shield = 3
        self.alive = True

    def hit(self, target):
        attack = self.power - target.shield
        target.health -= attack
        if target.health <= 0:
            target.alive = False
            targets.remove(target)

targets = list()
for _ in range(5):
    targets.append(Target())
player = Player()

while True:
    os.system("cls")
    print("Player Status: ------ Health: {} ------ Attack: {} ------ Shield: {}".format(player.health, player.power, player.shield))
    if not player.alive:
        print("Game Over!")
        quit()
    if not targets:
        print("Congratulations, You Won!")
        quit()
    for target in targets:
        print("{}. Target ------ Health: {} ------ Attack: {} ------ Shield: {}".format(targets.index(target), target.health, target.power, target.shield))

    choice = int(input("Select Target: "))
    selected_target = targets[choice]
    player.hit(selected_target)
    if targets:
        attacker = targets[random.randint(0, len(targets) - 1)]
        attacker.hit(player)
