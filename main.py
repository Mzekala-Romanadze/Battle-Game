"""
The Python program of the battle-style game ("SKY")

The program gets player name (in this case SKY is the main character),
health and attack power, and also enemies' names, health, attack power and gold reward.

The main character fights against enemies which are randomly generated in each round.
The Game lasts until the main character defeats all enemies or the main character is defeated.

"""

import random


class Character:
    def __init__(self, name, health, attack_power):
        self._name = name
        self._health = health
        self._attack_power = attack_power

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value

    def attack(self, enemy):
        damage = random.randint(1, self._attack_power)
        enemy.health -= damage
        print(f"{self._name} attacks {enemy.name} for {damage} damage!")

    def __str__(self):
        return f"{self._name} (Health: {self._health}, Attack Power: {self._attack_power})"


class Player(Character):
    def __init__(self, name, health, attack_power, gold=0):
        super().__init__(name, health, attack_power)
        self._gold = gold

    @property
    def gold(self):
        return self._gold

    def collect_gold(self, amount):
        self._gold += amount
        print(f"{self.name} has collected {amount} gold!")

    def __str__(self):
        return super().__str__() + f" (Gold: {self._gold})"


class Enemy(Character):
    def __init__(self, name, health, attack_power, gold_reward):
        super().__init__(name, health, attack_power)
        self._gold_reward = gold_reward

    def defeated(self):
        print(f"{self.name} is defeated!")
        return self._gold_reward

    def __str__(self):
        return super().__str__() + f" (Gold Reward: {self._gold_reward})"


class Game:
    def __init__(self, player):
        self._player = player
        self._enemies = []

    def add_enemy(self, enemy):
        self._enemies.append(enemy)

    def play(self):
        print(f"Welcome, {self._player.name}!")

        while self._enemies:
            enemy = random.choice(self._enemies)
            print(f"A wild {enemy.name} appears!")

            while self._player.health > 0 and enemy.health > 0:
                print(self._player)
                print(enemy)
                self._player.attack(enemy)

                if enemy.health <= 0:
                    gold_reward = enemy.defeated()
                    self._player.collect_gold(gold_reward)
                    self._enemies.remove(enemy)
                    if not self._enemies:
                        break
                    enemy = random.choice(self._enemies)
                    print(f"A wild {enemy.name} appears!")
                else:
                    enemy.attack(self._player)

            if self._player.health <= 0:
                print(f"{self._player.name} has been defeated!")
                print("\nGame over.")
                break

        if not self._enemies:
            print(f"\nCongratulations, {self._player.name}! You have defeated all enemies and won "
                  f"the game with {self._player.gold} gold.")


enemy_1 = Enemy(name="Cloud", health=15, attack_power=5, gold_reward=10)
enemy_2 = Enemy(name="Pollution", health=30, attack_power=25, gold_reward=50)
enemy_3 = Enemy(name="Thunderstorm", health=40, attack_power=15, gold_reward=30)
enemy_4 = Enemy(name="Rain", health=10, attack_power=5, gold_reward=10)
enemy_5 = Enemy(name="Storm", health=15, attack_power=10, gold_reward=20)
enemy_6 = Enemy(name="Tornado", health=10, attack_power=15, gold_reward=30)
enemy_7 = Enemy(name="Hurricane", health=20, attack_power=20, gold_reward=60)
enemy_8 = Enemy(name="Blizzard", health=10, attack_power=25, gold_reward=80)

player = Player("SKY", 100, 15)
game = Game(player)
game.add_enemy(enemy_1)
game.add_enemy(enemy_2)
game.add_enemy(enemy_3)
game.add_enemy(enemy_4)
game.add_enemy(enemy_5)
game.add_enemy(enemy_6)
game.add_enemy(enemy_7)
game.add_enemy(enemy_8)

game.play()
