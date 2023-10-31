class Car:
    def __init__(self, number, mspeed, cspeed=0, distance=0):
        self.number = number
        self.mspeed = mspeed
        self.cspeed = cspeed
        self.distance = distance

    def accerelate(self, new_speed):
        self.cspeed = self.cspeed + new_speed

    def deccerelate(self, new_speed):
        self.cspeed = self.cspeed - new_speed

    def drive(self, hour):
        travel = self.cspeed * hour
        self.distance = self.distance + travel


car = Car("ABC-123", mspeed=142)
car.accerelate(60)
car.drive(1.5)
print(
    f"Car Information, Registration number: {car.number}, Maximum Speed: {car.mspeed}km/h, Current Speed: {car.cspeed}km/h, "
    f"Travelled Distance: {car.distance}km")
