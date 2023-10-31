"""class Dog:
    def __init__(self, name, birth_year, sound = "woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
    def bark(self, times):
        """


class Portfolio:
    def __init__(self, name):
        self.name = name
        self.stock = []

    def buystock(self, stock, amount):
        self.stock.append([stock, amount])

    def sellStock(self, stock, amount):
        self.stock.remove(stock)

    def printPortfolio(self):
        print(f"Your portfolio {self.name} contains following stock")
        for x in self.stock:
            print("You have ")


class Stock:
    def __init__(self, name, amount, value):
        self.name = name
        self.value = value

    def print(self):
        print(f"You have {self.amount} {self.name} with value {self.value}")


p = Portfolio("Kimmo's stocks")
s1 = Stock("Nokia", 500)
s2 = Stock("motorola", 600)
p.buystock(s1, 100)
p.sellstock(s1, )

p2 = Portfolio("Jenny's stock")
s2 = Stock("bmv", )

p.buystock(s1)
p.buystock(s2)
p.printPortfolio()
