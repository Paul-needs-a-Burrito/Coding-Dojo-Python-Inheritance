# Assignment: Zoo
# Objectives:
#     Practice utilizing inheritance
#     More practice with associations between classes
#     Practice overriding methods
#     See polymorphism in action
# Create a zoo and start raising different types of animals. Start by creating an Animal class, and then at least 3 specific animal classes that inherit from Animal.
# Each animal should have a name, an age, a health level, and happiness level. The Animal class should have a display_info method that shows the animal's name, health, and happiness. It should also have a feed method that increases health and happiness by 10.
# In at least one of the Animal child classes you've created, add at least one unique attribute. Give each animal different default levels of health and happiness. The animals should also respond to the feed method with varying levels of changes to health and happiness.
# Once you've tested out your different animals and feel more comfortable with inheritance, create a Zoo class to help manage all your animals.


class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def feed(self, amount=10):
        self.health += amount
        self.happiness += amount
        return self

    def display_info(self):
        print(f"Name: {self.name}, Health: {self.health}, Happiness: {self.happiness}")
        return self


class Lion(Animal):
    def __init__(self, name, age, color, health=100, happiness=100):
        super().__init__(name, age, health, happiness)
        self.color = color


class Tiger(Animal):
    def __init__(self, name, age, health=200, happiness=200):
        super().__init__(name, age, health, happiness)

    def feed(self, amount=20):
        super().feed(amount)
        return self


class Bear(Animal):
    def __init__(self, name, age, health=300, happiness=300):
        super().__init__(name, age, health, happiness)

    def feed(self, amount=30):
        super().feed(amount)
        return self


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name, age, color):
        self.animals.append( Lion(name, age, color) )
        return self

    def add_tiger(self, name, age):
        self.animals.append( Tiger(name, age) )
        return self

    def add_bear(self, name, age):
        self.animals.append( Bear(name, age) )
        return self

    def print_zoo_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
        return self


zoo1 = Zoo("The Looney Zoo")
zoo1.add_lion("Albert", 15, "brown").add_lion("Beatrice", 16, "yellow").add_tiger("Tiggy", 17).add_tiger("Taggy", 18).add_bear("Berry", 100).print_zoo_info()

zoo1.animals[0].feed()
zoo1.animals[3].feed()
zoo1.print_zoo_info()
