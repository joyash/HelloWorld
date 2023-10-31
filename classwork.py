class Person:
    def __init__(self, first_name, last_name, DoB, job):
        self.first_name = first_name
        self.last_name = last_name
        self.DoB = DoB
        self.job = job

    def get_name(self):
        return f"{self.first_name} {self.last_name} {self.DoB} {self.job}"


class Student(Person):
    def __init__(self, first_name, last_name, DoB, job, major):
        super().__init__(first_name, last_name, DoB, job)
        self.major = major

    def get_student_Details(self):
        print(f"{self.first_name} {self.last_name} {self.DoB} {self.job}  {self.major}")


student1 = Student("rabin", "karki", "2000-01-01", "student", "it")
print(student1.get_student_Details())
