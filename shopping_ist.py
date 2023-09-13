shopping_list ={
    "milk" : 2,
    "juice" : 3,
    "oat" : 9,
    "rice" : 5,
    "chicken" : 1
}

def adddic(item, quantity):
    if(item in shopping_list):
        shopping_list[item] = shopping_list + quantity
    else:
        shopping_list[item] = quantity

def displaydic():
   for item, quantity in shopping_list.items():
       print(item + ": ", quantity)


adddic("apple", 3)
adddic("rice", 5)
displaydic()

total = sum(shopping_list.values())
print("Total item on the shopping list ", total)


itemcheck = input("add item to check in the dictionary: " )

if itemcheck in shopping_list:
    print("is in didtionary.")
else:
    print("not in the list")

