"""class Student():
    counter = 0

    def __init__(self, name, age, degree):
        self.name = name
        self.age = age
        self.degree = degree
        Student.counter += 1
    def setName(self, newName):
        self.name = newName


student = Student("rabin", "16", "mbs")
student1 = Student("Fatima", "24", "IT")
student2 = Student("Losika", "19", "BBA")
print(f"The stundent name is {student.name} his/her age is {student.age} and studying {student.degree}")

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
