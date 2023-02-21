class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I'm {self.name}!")


class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('woof!')


class Cat(Mammal):
    def meow(self):
        print('meow')


totem = Dog()
totem.walk()
totem.bark()
