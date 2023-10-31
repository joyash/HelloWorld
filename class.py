class Animal:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(self.name)

    def speak(self):
        pass


class Mammal(Animal):
    def speak(self):
        pass

    def protest(self):
        pass


class Dog(Mammal):
    def speak(self):
        print(f"{self.name}")


class Cat(Animal):
    def speak(self):
        return (f"{self.name} says: meow meow")


dog = Dog("Snowy")
print(f"my dog name is: {dog.name}")
dog.speak()
myMammal = Mammal("some Mammal")
myMammal.print_info()
myCat = Cat("Lio")
print(myCat.speak())

"""myAnimal = []
myAnimal.append(Animal("Dog"))
myAnimal.append(Animal("Cat"))
myAnimal.append(Animal("Fish"))

for Animal in myAnimal:
    Animal.print_info()
"""
