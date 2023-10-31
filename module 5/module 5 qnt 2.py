user_number = input("Enter numbers or quit by pressing enter:  ")
user1 = []
max_num = user_number
while(user_number != ""):
    user1.append(user_number)
    if(user_number > max_num):
        max_num = user_number
    user_number = input("Enter numbers or quit by pressing enter:  ")
#sort_user = sorted(user1) # this line is for personal future use it is a sort method of list
user1.sort(reverse=True)
for x in user1[:5]:
    print(x, end=" ")


