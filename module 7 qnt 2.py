"""Write a program that asks the user to enter names until he/she enters an empty string. After each name is read the
program either prints out New name or Existing name depending on whether the name was entered for the first time.
Finally, the program lists out the input names one by one, one below another in any order. Use the set data structure
to store the names.
"""

name_set = set()
name_set.add("rabin")
new_name = input("Enter your name here or quit by pressing enter: ")
while new_name != "":
     if new_name not in name_set:
         name_set.add(new_name)
         print("It is a new name.")
         new_name = input("Enter your name here or quit by pressing enter: ")
     else:
         print("Name already in set")
         new_name = input("Enter your name here or quit by pressing enter: ")




else:
    print("You select to quit")
    print(name_set)
