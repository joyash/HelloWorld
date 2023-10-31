"""
question 1
name = input("Enter your name: ")
print(f"Hello" ,name)
"""

""" question 2
radius = float(input("Enter the radius of circle: "))
pie = 3.14
area = 2*radius*pie*pie
print(f"The area of the circle is: {area} ")
"""
""" question 3
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
perimeter = 2*length + 2*width
area = length * width
print(f"The perimeter of the rectangle is: {perimeter}")
print(f"The area of the rectangle is: {area}")
"""
"""
a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))
d = a+b+c
e = a*b*c
f = d/3
print(f"Sum of the numbers is: {d}")
print(f"Product of the numbers is: {e}")
print(f"Average of the numbers is: {f}")

print(f"Sum of the numbers is", a+b+c)
print(f"Product of the numbers is", a*b*c)
print(f"Average of the numbers is", (a+b+c)/3)
"""

""" question 5
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
pounds1 = pounds + (20*talents)
lots1 = lots + (32*pounds1)
grams = lots1 * 13.3
kilograms = grams // 1000
remaining_grams = grams % 1000
print(f"the total weights in modern units is: {kilograms:.0f} kilogrgams and {remaining_grams:.2f} grams. ")
"""



""" module 3 question 1
zander = float(input("Tell the lenght of zander: "))
zander_less = 42 - zander
if(zander < 42):
    print("Release the fish into the lake")
    print(f"You catch {zander_less:0.2f} cm below the limit. ")
else:
    print("Put the fish inside the jar.")
"""
""" question 2
cabin_class = input("Enter your cabin class:  ")
cabin_class_upper = cabin_class.upper()
if(cabin_class_upper == "LUX"):
    print("Your cabin is upper-deck cabin with balcony.")
elif(cabin_class_upper == "A"):
    print("Your cabin is above the car deck, equipped with a window.")
elif(cabin_class_upper == "B"):
    print("Your cabin is windowless cabin above the car deck.")
elif(cabin_class_upper == "C"):
    print("Your cabin is windowless below the car deck.")
else:
    print("Invalid cabin class") """

""" question 3
gender = input("Enter your gender, (f) or (m):  ")
gender_a = gender.lower()
hem = int(input("Enter your hemoglobin value in (g/l): "))
if(gender_a == "f"):
    if(hem < 117):
        print("Your hemoglobin level is low.")
    elif(hem <= 117 and hem >= 155):
        print("Your hemoglobin level is normal.")
    elif(hem > 155):
        print("Your hemoglobin level is high")
elif(gender == "m"):
    if(hem < 117):
      print("Your hemoglobin level is low.")
    elif(hem >= 117 and hem <=155):
        print("Your hemoglobin level is normal")
    elif(hem > 155):
        print("Your hemoglobin level is high.")
else:
    print("Invalid command.") 
"""
""" Question 4
year = int(input("Enter a year:  "))
a = year % 4
b = year % 100
c = year % 400
if(a == 0 and b == 0 and c == 0):
    print(f"This year {year} is a leap year")
else:                      
   print(f"This year {year} is not a leap year.")
   """

""" while loop question 2
number = float(input("Enter the inches:"))
number_cen = number * 2.54
while(number > 0):
    print(f"The value in centimiter is, {number_cen}")
    break
else:
 print("the program ends")
 """
""" while loop question 1
num = float(input("Enter the number: "))
i = 1
while(i <= num):
    if(i % 3 == 0):
        print(i)
    i += 1
"""
"""num = int(input("Enter the number or quit by pressing enter: "))
number = []
maxi = None
while num !="":
       num = int(input("Enter the number or quit by pressing enter: "))
       number.append(num)

for element in number:
    if element > maxi:
        maxi = element
print(maxi) """

""""
max_num = 0
min_num = 0
while True:
      num = (input("Enter the number or quit by pressing enter: "))
      if(num == ""):
          break
      if num.replace(".", "", 1).isdigit() or (
              num[0] == "-" and num[1:].replace(".", "", 1).isdigit()):
       num = float(num)

       if(min_num is None or num < min_num):
          min_num = num
      if(max_num is None or num > max_num):
         max_num = num
      else:
          print("error")
if min_num is not None and max_num is not None:
  print(f"smallest: {min_num}")
  print(f"largest: {max_num}")
else:
  print("error") """

""" module 2 question 6
import random
random_num1 = random.randint(0,9),random.randint(0,9),random.randint(0,9)
print(random_num1)

import random
random_num = random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)
print(random_num)"""

"""import random
random_number = random.randint(1,10)
guess_number = int(input("Enter your guess(1-10):  "))

while True:
    if(guess_number == random_number):
        print("you win")
    elif(guess_number > random_number):
            print("Too high")
    elif(guess_number < random_number):
        print("Too low")
    else:
     guess_number = int(input("Enter your guess(1-10): "))

else:
 print("you lose")"""

"""user_name = input("Enter user name: ")
user_password = input("Enter password: ")
i = 0
while(i < 5):
    if(user_name == "python" and user_password == "rules"):
       print("Welcome")
       break
    else:
      user_name = input("Enter user name: ")
      user_password = input("Enter password:  ")
      i = i + 1

else:
    print("Access Denied.") """


"""user_name = input("Enter your name or quit by pressing enter:")
name = []
while user_name != "":
    name.append(user_name)
    user_name = input("Enter your name or quit by pressing enter:")
print(name)"""

"""name = []
user_name = input("Enter name or quit by pressing enter: ")
while user_name !="":
    name.append(user_name)
    user_name = input("Enter name or quit by pressing enter")

for i in name:
  print(f"hello jiii {i} kese ho")"""

"""for n in range(3,31,3):
    print(n,end=" ")"""

"""city = []
for n in range(5):
    user_city = input("Enter name of city: ")
    city.append(user_city)
print(*city, sep="\n")"""

"""user_input = ""
while(user_input != "stop"):
    user_input("Enter a command (use 'stop' to stop): ")
    print(input) """

"""a = 0
while(a<5):
    b=0
    while(b<6):
        b +=1
        print(f"{a} multiply with {b} is {a*b}")
    a += 1"""
import mysql.connector
import random

mydb = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game_team12',
    user='root',
    password='xenun333',
    autocommit=True
)


# function to retrive and select a random event

def select_random_event():
    mycursor = mydb.cursor()
    # retrive event data from database
    mycursor.execute(
        "SELECT id, info, type, IFNULL(co2_change, 0.0) AS co2_change, IFNULL(distance_change, 0.0) AS distange_change FROM event")
    events_data = mycursor.fetchall()
    # Filter out events with insufficient data
    valid_events = [event for event in events_data if len(event) == 6]
    # calculate total probability
    total_probability = sum(event[3] for event in valid_events)
    # if total probability is 0, add a default event with non-zero probability
    if total_probability == 0:
        default_event = (0, "Default Event", "default", 0.1, 0.01, 0.05)
        valid_events.append(default_event)
        total_probability += 0.1  # adjusting total probability
    # generate a random number
    random_value = random.uniform(0, 1)
    cumulative_probability = 0

    # iterate through events
    for event in valid_events:
        event_id, info, event_type, probability, co2_change, distance_change = event

        # Check for missing values and assign defaults
        if event_type is None:
            event_type = "default_type"  # Assign a default event type
        if probability is None:
            probability = 0.1  # Assign a default probability
        if co2_change is None:
            co2_change = 0.01  # Assign a default CO2 change
        if distance_change is None:
            distance_change = 0.05  # Assign a default distance change

        normalized_probability = probability / total_probability
        cumulative_probability += normalized_probability

        if random_value <= cumulative_probability:
            selected_event = event
            break
    else:
        selected_event = None
    mycursor.close()

    return selected_event


selected_event = select_random_event()

if selected_event:
    event_id, info, event_type, probability, co2_change, distance_change = selected_event
    print("Random Event:")
    print(f"ID: {event_id}")
    print(f"Info: {info}")
    print(f"Type: {event_type}")
    print(f"Probability: {probability}")
    print(f"CO2 Change: {co2_change}")
    print(f"Distance Change: {distance_change}")
else:
    print("No event selected")

"""lst = ["kinno", "jnne", "sita", "extra"]
newlst = [x for x in lst if(x != "kinno")]
print(f"new list is {newlst}")

nmb = ["45", "33", "65"]
print(nmb)
nmb = [int(x) for x in nmb]
print()

total = 0
for count in range(5):
    total = total + count
print(total)"""

"""def add_taks(task:):
    mylist.append(task)

def remove_task(task):
    if task in to
    mylist.remove(task)

def display_task
"""

"""mytuples = (1,2,3)
print(mytuples)
print(mytuples[1:])
mytuples1=(1,)
print(mytuples1)
point = (2,3)
x,y = point
print(y)
grades =(2,3,4,5,6,7)
total = 0
for grade in grades:
    total += grade
print(f"the total is {total}")
avg = total/len(grades)
print(f"here is the average{avg}")
"""

"""students = []
students.append(("Rabin", (30,36,89.100)))
students.append(("sujog", (34,66,99.100)))
students.append(("sabir", (80,96,29.100)))

nametoFind = "Rabin"
found = False
for student in students:
    if student[0] == "Rabin":
        print(f"name is {student[0]}")
        print(f"grade is {student[1]}")
        avg = sum(student[1]) / len(student[1])
        print(f"the average is {avg:.2f}")
        found = True
        break
    if not found:
       print("student doesnot exist:")
"""
"""user = input("Enter your number: ")
user = int(user)
if user == 1:
    print(user,"number is not a prime number. ")
elif user > 1:
   for i in range(2,user):
     if(user % i == 0):
      print(user, "is not prime number")
      break
   else:
     print(user,"is a prime number.")

else:
  print(user,"is not a prime number")

"""

"""
def distance_cal(km):
    liter = km * (5/100)
    return liter
def liter_euro(liter):
    price = liter * 1.95
    return price


user = float(input("How far you want to go: "))
print(f"the gas you need {distance_cal(user)} liter to travel {user} km")
print(f"It cost {liter_euro(user)} euro to travel{user}")
ask_again = input("Do you want to continue: ")
while ask_again == "yes":
    user = float(input("How far you want to go: "))
    print(f"the gas you need {distance_cal(user)} liter to travel {user} km")
    print(f"It cost {liter_euro(user:.2f)} euro to travel{user}")
else:
   print("Thank you for the game, you played well.") """

n = 0
for outer in range(3, 0, -1):
    m = 0
    for inner in [2, 0, 2, 3]:
        if inner == outer:
            print(inner)
            m += 1
    n += 1

"""(red, blue) = (5,6)
colors = (red, blue)
print(colors)
print(blue)
j =


"""
