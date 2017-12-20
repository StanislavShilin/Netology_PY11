class Animal:
    name = None
    weight = 0
    max_speed_of_movement = 5
    number_of_feet = 0

    def wash(self):
        print("{} чистый(-ая)!".format(self.name))

    def feed(self, quantity_of_eat):
        self.weight += quantity_of_eat
        print("{} поел(-a) и весит {}".format(self.name, self.weight))

    def kick(self, power):
        self.max_speed_of_movement *= power
        print("Максимальная скорость животного по имени {} при перемещении составила {}"
              .format(self.name, self.max_speed_of_movement))


class Mammals(Animal):
    number_of_feet = 4
    form_of_animal = "Млекопитающие"

    def kick(self, power):
        self.max_speed_of_movement *= power
        print("Максимальная скорость животного {} по имени {} при перемещении составила {}"
              .format(self.form_of_animal, self.name, self.max_speed_of_movement))


class Bird(Animal):
    number_of_feet = 2
    max_speed_of_fly = 20
    form_of_animal = "Птица"

    def kick(self, power):
        self.max_speed_of_movement *= power
        self.max_speed_of_fly *= power
        print("Максимальная скорость животного {} по имени {} при беге составила {}, а в стадии полета {}"
              .format(self.form_of_animal, self.name, self.max_speed_of_movement, self.max_speed_of_fly))


class Cow(Mammals):
    form_of_animal = "Корова"


class Goat(Mammals):
    form_of_animal = "Коза"
    max_speed_of_movement = 15


class Sheep(Mammals):
    form_of_animal = "Овца"
    max_speed_of_movement = 11


class Pig(Mammals):
    form_of_animal = "Свинья"
    max_speed_of_movement = 11


class Duck(Bird):
    form_of_animal = "Утка"
    max_speed_of_movement = 21
    max_speed_of_fly = 30


class Chicken(Bird):
    form_of_animal = "Курица"
    max_speed_of_movement = 19
    max_speed_of_fly = 25


class Goose(Bird):
    form_of_animal = "Гусь"
    max_speed_of_movement = 16
    max_speed_of_fly = 22


cow_1 = Cow()
cow_1.name = "Вика"
cow_1.weight = 110
cow_1.kick(2)
print(cow_1.number_of_feet)
cow_1.wash()
cow_1.feed(5)
cow_1.feed(10)

goat_1 = Sheep()
goat_1.name = "Анна"
goat_1.weight = 60
goat_1.kick(1)
print(goat_1.number_of_feet)
goat_1.wash()
goat_1.feed(2)
goat_1.feed(4)

goose_1 = Goose()
goose_1.name = "Виктор"
goose_1.weight = 25
goose_1.kick(5)
print(goose_1.number_of_feet)
goose_1.wash()
goose_1.feed(1)
goose_1.feed(2)