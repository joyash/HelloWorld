user = input("Enter your number: ")
user = int(user)
if user == 1:
    print(user, "number is not a prime number. ")
elif user > 1:
    for i in range(2, user):
        if (user % i == 0):
            print(user, "is not prime number")
            user = input("Enter your number: ")

    else:
        print(user, "is a prime number.")
        user = input("Enter your number: ")

else:
    print(user, "is not a prime number")
