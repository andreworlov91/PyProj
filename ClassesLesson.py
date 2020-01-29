class Hero:
    """"Class to Create Hero for our game"""

    def __init__(self, name, level, race):
        """"Initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """"Print all parameters of this Hero"""
        description = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health is: " + str(
            self.health)).title()
        print(description)

    def level_up(self):
        """"Upgrade level of Hero"""
        self.level += 1

    def move(self):
        """"Start moving hero"""
        print("Hero " + self.name + " start moving...")


class SuperHero(Hero):
    """"Class to Create Super Hero"""

    def __init__(self, name, level, race, magiclevel):
        """"Initiate our Super Hero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.__magic = 100

    def make_magic(self):
        """"Use magic"""
        self.__magic -= 10

    def show_hero(self):
        """"Print all parameters of this Super Hero"""
        description = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health is: " + str(
            self.health) + " Magic is " + str(self.__magic)).title()
        print(description)

    def set_magic(self, magic):
        self.__magic = magic