# number 1
number = 20
if number > 20:
    print("A")
elif number > 10:
    print("B")
else:
    print("C")
print("D")

#number 2
s = "W"
while s != "Weeee":
    print(s)
    s = s + "e"

# number 3

for a in range(0, 10, 2):
    print(f"Round: {a}")

#number 4

countries1 = []
countries2 = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
countries3 = ["Estonia", "Latvia", "Lithuania"]
countries2.extend(countries3)
countries1.extend(countries2)
countries1.append("Poland")

"""print(countries1[1])
print(countries1)
"""

if "Estonia" in countries2:
    print("Yes")
else:
   print("No")
if "Estonia" in countries1:
   print("Yes it is")
else:
    print("No")
print(countries1[-1])