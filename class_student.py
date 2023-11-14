"""class Student():
    counter = 0

    def __init__(self, name, age, degree):
        self.name = name
        self.age = age
        self.degree = degree
        Student.counter += 1
    def setName(self, newName):
        self.name = newName

    def print_information(self):
        print(f"The stundent name is {self.name} his/her age is {self.age} and studying {self.degree}")

student = Student("rabin", "16", "mbs")
student1 = Student("Fatima", "24", "IT")
student2 = Student("Losika", "19", "BBA")
student.print_information()
student1.print_information()
student2.print_information()"""

"""print(f"The stundent name is {student.name} his/her age is {student.age} and studying {student.degree}")
print(f"The stundent name is {student2.name} his/her age is {student2.age} and studying {student2.degree}")
student1.setName("Elisha")
print(f"The stundent name is {student1.name} his/her age is {student1.age} and studying {student1.degree}")
print(f"Number of student in class is {student.counter}")
"""

"""class Rectangle():
    pass

    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def Perimeter(self):
        return (self.width + self.height) * 2

rec1 = Rectangle()
rec1.set_dimensions(3,4)
rec2 = Rectangle()
rec2.set_dimensions(6, 9)
print(f"Area of the rectangle is {rec1.area( )}")
print(f"Perimeter of the rectangle is {rec1.Perimeter()}")
print(f"Area of the rectangle is {rec2.area( )}")
print(f"Perimeter of the rectangle is {rec2.Perimeter()}")
"""

"""class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity
    def get_fare(self):
        return self.capacity * 100
class Bus(Vehicle):
    def __init__(self, capacity):
        super().__init__(capacity)

    def get_fare(self):
        vehicle_fare = super().get_fare()
        maintenance_fare = 0.1 * vehicle_fare
        total_fare = vehicle_fare + maintenance_fare
        return total_fare


vehicle = Vehicle(50)
print(f"Vehicle Fare: {vehicle.get_fare()}")

bus = Bus(50)
print(f"Bus Fare: {bus.get_fare()}")

"""
"""import requests
keyword = input("Enter keyword: ")
request = "https://api.google.com/search/shows?q=" + keyword
response = requests.get(request).json()
print(response)"""

"""class Customer:
    customer_number = 0
    def __init__(self, first_name, last_name, loyalty_points ):
        self.first_name = first_name
        self.last_name = last_name
        self.loyalty_points = loyalty_points
        Customer.customer_number += 1

    def loyalty(self, i):
        self.loyalty_points += i
         print(f"{self.first_name} {self.last_name} has {self.loyalty_points} loyalty points. ")


customer = Customer("arav", "karki", 0)
customer1 = Customer("bishes", "pandit", 1)
customer2 = Customer("pooja", "neupane", 2)

new_variable = customer.loyalty(3)
new_variable = customer.loyalty(4)
new_variable = customer.loyalty(4)

new_variable1 = customer1.loyalty(4)
new_variable2 = customer1.loyalty(4)

new_variable3 = customer2.loyalty(3)
add_points = customer2.loyalty(10)


print(f"{customer.first_name} {customer.last_name} has {customer.loyalty_points} loyalty points. ")
print(f"{customer1.first_name} {customer1.last_name} has {customer1.loyalty_points} loyalty points. ")
print(f"{customer2.first_name} {customer2.last_name} has {customer2.loyalty_points} loyalty points. ")
print(f"number of customer are {Customer.customer_number}")

"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def calculate_sum():
    args = request.args
    number1 = 12  # float(args.get("number1"))
    number2 = 13  # //float(args.get("number2"))
    total_sum = number1 + number2
    return str(total_sum)


if __name__ == '__main__':
    app.run(debug=True)
