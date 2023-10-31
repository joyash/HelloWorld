"""create an empty list
append at least five different patient name
print three name
write a function to check whether the patient is on the list
test your program is working or not"""
patient = []
patient.append(("samir","shrestha","60","flu"))
patient.append(("rajesh","sri","60","flu"))
patient.append(("bhuwan","lama","60","flu"))
patient.append(("sunil","praja","60","flu"))
patient.append(("aryan","mahat","60","flu"))

print(patient[0:])


def check_name(patient,new_name):
    for i in patient:
        if new_name in patient:
            print("name is in list")
        else:
            print("name not in the list")
    return patient

new_name = input("enter your name: ")
check_name(patient,new_name)
