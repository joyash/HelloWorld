class MyPet():
    counter = 0

    def __init__(self, n, c):
        self.name = n
        self.color = c
        MyPet.counter += 1

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def bark(self, n):
        for i in range(n):
            print("Vau, vau")


dog = MyPet("Snowy", "Brown")
cat = MyPet("Slowy", "Pinky")
print(f"dog name {dog.name}")
print(f"cat name: {cat.name}")
dog.bark(1)
dog.setName("Unknown")
print(f"new dog name: {dog.name}")

penguin = MyPet("Sweety", "blacknwhite")
print(f"penguin name: {penguin.name}, penguin color: {penguin.color}")
cat.setName("Caty")
print(f"My cat new name: {cat.name}, and color is: {cat.color}")
print(f"NUmber of object: {MyPet.counter}")
print(f"dog name : dog.getname()")
