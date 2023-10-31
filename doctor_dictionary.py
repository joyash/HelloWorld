doctor = {

    "title": "sr specialist",
    "name": "Aamir",
    "employment_year": "1989"
}

print(doctor)
doctor["gender"] = "female"
doctor["age"] = "65"
print(doctor)


def print_doctor_details(doctor_info):
    title = doctor_info["title"]
    name = doctor_info["name"]
    year = doctor_info["employment_year"]
    gender = doctor_info["gender"]
    age = doctor_info["age"]
    formatted_info = (f"Title: {title} and name:{name} year: {year} gender: {gender} age: {age}")
    print(formatted_info)


print('doctor details based on inforamtiion')
print_doctor_details(doctor)
