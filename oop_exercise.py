class Car():

    def __init__(self, number, mspeed, ):
        self.number = number
        self.mspeed = mspeed
        self.cspeed = 0
        self.distance = 0


car = Car('ABC-123', '142 km/h')
print(
    f"Registration number: {car.number}, maximum speed: {car.mspeed}, current speed: {car.cspeed}, travelled distance: {car.distance}")
