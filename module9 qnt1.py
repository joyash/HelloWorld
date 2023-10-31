class Car:
    def __init__(self, number, mspeed, cspeed=0, distance=0):
        self.number = number
        self.mspeed = mspeed
        self.cspeed = cspeed
        self.distance = distance


car = Car("ABC-123", "142 km/h")
print(
    f"Car Information, Registration number: {car.number}, Maximum Speed: {car.mspeed}, Current Speed: {car.cspeed}, Travelled Distance: {car.distance}")
