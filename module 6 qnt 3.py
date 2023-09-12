"""
Write a function that gets the quantity of gasoline in American gallons and returns the number
converted to litres. Write a main program that asks for a volume in gallons from the user and
converts the value to liters. The conversion must be done by using the function. Conversions
continue until the user inputs a negative value.
"""
def gas_convertor(gallons):
    if(gallons > 0):
       result = gallons * 3.78
       return result
    else:
        print("Enter the positive value: ")


gallons = int(input("Enter your quantity in gallon here: "))
result = gas_convertor(gallons)
print(f"The gas is {result} liters.")
