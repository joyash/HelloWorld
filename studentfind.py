student = {
    "name" : "timo",
    "age" : 20,
    "grade" : "A",
    "courses" : ["math","physics","prigramming"]
}

print("name: ", student["name"])
print("age: ", student["age"])
print("grade: ", student["grade"])
print("courses: ", student["courses"])

student["age"] = 25
student["courses"].append("language")
print(student)
student["city"] = "helsinki"


#iterating through the dictonary.
for key,value in student.items():
    print(key + " :", value)


del student["grade"]
#checking  if a key exist in dictonary

if "age" in student:
    print("age exist and here is the value:", student["age"] )
else:
    print("age not found on the dictonary")

