class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_name(self):
        print(self.name)


class Customer(Person):
    def __init__(self, name, age, gender, money):
        super().__init__(name, age, gender)
        self.__money = money

    def money(self):
        return self.__money

    def get_money(self, money, other):
        self.__money += money
        other.__money -= money


class Clerk(Person):
    def __init__(self, name, age, gender, company):
        super().__init__(name, age, gender)
        self.company = company


class Child(Person):
    def __init__(self, name, age, gender, kindergarten):
        super().__init__(name, age, gender)
        self.kindergarten = kindergarten
