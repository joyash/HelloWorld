"""Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise
the same as the original list except that all uneven numbers have been removed. For testing, write a main program
where you create a list, call the function, and then print out both the original as well as the cut-down list.
"""

new_number = []
def uneven_remove(whole_number):
    for index in whole_number:
        if(index % 2 == 0):
          new_number.append(index)
    return


whole_number = [2,4,3,5,8,9,12,13,15]
uneven_remove(whole_number)
print(new_number)
