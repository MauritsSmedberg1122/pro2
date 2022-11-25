from unicodedata import name


class Person:
    def __init__ (self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Elev(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
