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

"""user = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
user.append("hello")
print(user)
print(user[-3:-1])
print(user.index("Ahmed"))
loser = ["roar", "soar"]
user.extend(loser)
print(user)
"""
lst = ["kimmo", "janne", "mohammed", "luna"]
lst.append("hora")
"""for x in lst:
    print(x)"""
for xid, x in enumerate(lst):
    if(x != lst[-1]):
      print(f"{x} is having coffee with {lst[xid+1]}")