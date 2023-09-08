def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b
def div(a,b):
    return (a+b)/2

num1 = input("enter your 1st number: ")
num2 = input("enter your 2nd number: ")
a = int(num1)
b = int(num2)
print("Select your command (add:1, sub:2, mul:3, div:4: ")
choice = input("Enter your command: ")
while(num1 != ""):
    if(choice == "1"):
        print(f"sum of {a} and {b} is {add}")
    elif(choice == "2"):
       print(f"sub of {a} and {b} is {sub}")
    elif(choice == "3"):
       print(f"sub of {a} and {b} is {mul}")
    elif(choice == "4"):
       print(f"division of {a} and {b} is {div}")

else:
 print("invalid command")




