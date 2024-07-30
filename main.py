class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Звук животного")

    def eat(self):
        print("Ест")


class Bird(Animal):

    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        print("Чирикает")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print("Гавкает")


class Reptile(Animal):
    def __init__(self, name, age, scales):
        super().__init__(name, age)
        self.scales = scales

    def make_sound(self):
        """Издает звук рептилии"""
        print("Шипит")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

# Пример использования
my_zoo = Zoo()

bird1 = Bird("Воробей", 2, 20)
mammal1 = Mammal("Собака", 5, "коричневый")
reptile1 = Reptile("Змея", 3, "зелёные")

my_zoo.add_animal(bird1)
my_zoo.add_animal(mammal1)
my_zoo.add_animal(reptile1)

zoo_keeper1 = ZooKeeper("Иван")
veterinarian1 = Veterinarian("Мария")

my_zoo.add_employee(zoo_keeper1)
my_zoo.add_employee(veterinarian1)

print("Звуки животных:")
animal_sound(my_zoo.animals)

print("\nКормление и лечение животных:")
zoo_keeper1.feed_animal(mammal1)
veterinarian1.heal_animal(bird1)
