city = []
for i in range (5):
    user = input("Enter your city: ")
    city.append(user)
print(*city,sep="\n")