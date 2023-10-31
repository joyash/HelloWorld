import random


class Car:
    def __init__(self, registration_number, current_speed=0, distance=0):
        self.registration_number = registration_number
        self.max_speed = random.randint(100, 200)
        self.current_speed = current_speed
        self.distance = distance

    def accerelate(self, speed_change):
        self.current_speed = self.current_speed + speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def decerelate(self, speed_change):
        self.cspeed = self.current_speed - speed_change

    def drive(self, hour):
        travel = self.current_speed * hour
        self.distance = self.distance + travel


# Creating cars
cars = []
for count in range(1, 11):
    max_speed = random.randint(100, 200)
    cars.append(Car(f"ABC-{count}", max_speed))

# Cars driving loop
hour = 0
end_loop = False
while True:
    # Drive for one hour
    hour += 1
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accerelate(speed_change)
        car.drive(1)

    # Check if any of the car has travelled more than 10000 km
    for car in cars:
        if car.distance >= 10000:
            end_loop = True

    # Break the loop if flag is set
    if end_loop:
        break
# Print the result
print(f"Time passed: {hour} hours")
print(f"{'Registration number':<30}{'Max speed':<30}{'Current speed':<30}{'Travelled distance'}")
for car in cars:
    print(f"{car.registration_number:<30}{car.max_speed:<30}{car.current_speed:<30}{car.distance}")
