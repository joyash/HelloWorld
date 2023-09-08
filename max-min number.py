user_num = int(input("Enter number or quit by pressing enter: "))
max_num = user_num
min_num = user_num

while user_num !="":
    user_num = int(user_num)
    if(user_num < min_num):
        min_num = user_num
    elif(user_num > max_num):
       max_num = user_num
    user_num = input("Enter number or quit by pressing enter: ")
print(f"smallest number is {min_num} and the largest number is {max_num}")




