"""
Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in the
list. For testing, write a main program where you create a list, call the function, and print out the value it returned.
"""


def sumof_list(list1,total_number =None):
    if(total_number is None):
        total_number = [0]
    for count in list1:
       total_number[0] += count
    return total_number[0]



list1 = [2,5,8]
total_number = sumof_list(list1)
print(total_number)

