import random
import os
import pyautogui

class weapon:
    def __init__(self, dmg, bld, dmgType, prof, elNombre):
        self._damage = dmg
        self._bleed = bld
        self._damageType = dmgType
        self._proficiency = prof
        self._name = elNombre

    def calcDamage(self):
        modifier = 1
        if random.randint(1,15) == 15:
            modifier = modifier * 1.5
        #enemyWeakness = game.getEnemy().getWeakness()
        #enemyResistance = game.getEnemy().getResistance()
        #enemyAttributes = game.getEnemy().getAttributes()
        #if self._damageType = enemyWeakness:
        #   modifier = modifier * 1.5
        #elif self._damageType = enemyResistance:
        #   modifier = (modifier / 3) * 2
        # More if necessary

        # bleedDamage = game.getEnemy().getBleedDamage()
        damageDone = self._damage * (random.randint(8, 12) /10) * modifier# + bleedDamage

    def getName(self):
        return self._name

    def getDamage(self):
        return self._damage

    def getAttributes(self):
        return self._damageType, self._proficiency

    def setDamage(self,newDamage):
        self._damage = newDamage

    def setType(self, newType):
        self._type = newType

    def setProficiency(self, newProf):
        self._proficiency = newProf



class enemy:
    def __init__(self, difficultyLevel):
        

        self._enemyType = enemyTypes[random.randint(0,len(enemyTypes)-1)]
        self._health = (10 ** enemyTypes.index(self._enemyType)) * (random.randint(5,15)/10)
        self._damageType = "Regular"
        self._proficiency = "None"
        self._bleedDamage = 0


        if random.randint(1,10) <= difficultyLevel:
            self._damageType = game.getRandomDamageType()


        #if random.randint(1,10) <= difficultyLevel:
        #    self._proficiency = game.getRandomProficiencyType()

        if random.randint(1,10) <= difficultyLevel:
            self._bleedDamage = random.randint(1,3) * difficultyLevel

        self._damage = random.randint(1,4) * difficultyLevel

        # __init__(self, dmg, bld, dmgType, prof, elNombre)
        self._weapon = weapon(self._damage, self._bleedDamage, self._damageType, self._proficiency, self._enemyType)


    def getWeapon(self):
        return self._weapon

    def getHealth(self):
        return self._health

    def setHealth(self, newHealth):
        self._health = newHealth



class dungeonCrawler:
    def __init__(self):
        self._currentEnemy = enemy(1)
        self._damageTypes = ["Fire","Poison","Acid","Magic","Force","Sand","Plant","Blighted","Corrupted"]
        self._proficiencies = ["Small","Large","Bloodless","Relentless","Quick","Slow","Iron Stomach"]

    def getRandomDamageType(self):
        return self._damageTypes[random.randint(0,len(self._damageTypes)-1)]

    def getRandomProficiencyType(self):
        return self._proficiencies[random.randint(0,len(self._proficiencies)-1)]

    def playGame(self):
        # I'm thinking of some kind of horror/ strange elements, where the enemies get progressively weirder 
        # One idea - What if it moves your cursor (There's a library for that - It's easy)
        # --> Maybe somewhere it moves your cursor and types something
        # Maybe the setting changes. Some external voice knows it's wrong?
        # An external voice could speak in scrolling text instead of just block-placed text
        
        rawName = os.getlogin()
        #      ↓ Capitalise 1st letter      ↓ Lower case the rest of the name, then cut off first letter
        name = rawName[0].upper() + (rawName[0:].lower())[1:]

    def introduction(self):
        print("You must be the adventurer we hired.")
        print("The dungeon is up ahead. Your reward will be given when you've cleared it out.")
        print("Feel free to visit the shops if you need anything.")


    def options(self):
        print("1 - Go to Town")
        print("2 - Go to Dungeon")
        print("3 - Examine Weapons")
        print("4 - Examine Armour")
        print("5 - Examine Abilities")
        print("6 - Quit")

        while True:
            choice = input("")
            if choice in ["1","2","3","4","5","6"]:
                if choice == 6:
                    exit()

                else:
                    print("\n")
                    return choice


    def townOptions(self):
        print("1 - Return to Dungeon")
        print("2 - Visit Blacksmith")
        print("3 - Visit Brewery")

        while True:
            choice = input("")
            if choice in ["1","2","3"]:
                print("\n")
                return choice


    def entranceOptions(self):
        print("You approach the entrance to the dungeon.")
        print("1 - Enter")
        print("2 - Return to Town")
        while True:
            choice = input("")
            if choice in ["1","2"]:
                print("\n")
                return choice




enemyTypes = ("Rat", "Goblin")
enemyResistances = {"Rat" : "None", "Goblin" : "Poison"}

game = dungeonCrawler()
game.playGame()