import random

class Human():
    def __init__(self, name, happy, money, hunger):
        self.name = name
        self.happy = 10
        self.money = 5
        self.hunger = 10
        print(name, happy, money, hunger)

    def work(self, name):
        print(f"{name} поработал")
        self.money += 10
        self.happy -= 10
        self.hunger -= 2

    def rest(self, name):
        print(f"{name} отдохнул")
        self.happy += 5
        self.money -= 3
        self.hunger -= 3

    def eat(self, name):
        print(f"{name} поел")
        self.hunger += 4
        self.money -= 2

name = input("Имя: ")
person = Human(name, 10, 5, 10)

class Day():
    def human_day(self):
        person.work(person.name)
        do = random.randint(1, 2)
        if do == 1:
            person.rest(person.name)
        else:
            person.eat(person.name)

        print(f"{person.name} глод: {person.hunger}")
        print(f"{person.name} глод: {person.happy}")
        print(f"{person.name} деньги: {person.money}")

    def __init__(self):
        self.human_day()

days = Day
for i in range(1, 10):
    print("Следующий день__________________________________")
    Day()


