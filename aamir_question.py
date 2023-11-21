class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.course_list = []

    def enroll(self, course):
        self.course_list.append(course)

    def list_course(self):
        return [course.name for course in self.course_list]


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.student_list = []

    def add_student(self, course):
        self.student_list.append(course)

    def list_student(self):
        return [student.name for student in self.student_list]


student1 = Student(1, "Lalit", )
student2 = Student(2, "Rachit")
student3 = Student(2, "Jango")

course1 = Course(101, "Mathmatic")
course2 = Course(102, "Science")
course3 = Course(103, "Language")

student1.enroll(course1)
student1.enroll(course3)
student2.enroll(course2)
student2.enroll(course3)
student3.enroll(course2)
student3.enroll(course1)

course1.add_student(student1)
course3.add_student(student1)
course2.add_student(student2)
course3.add_student(student2)
course1.add_student(student3)
course2.add_student(student3)

print(f"{student1.name} is enrolled in courses: {student1.list_course()}")
print(f"{student2.name} is enrolled in courses: {student2.list_course()}")
print(f"{student3.name} is enrolled in courses: {student3.list_course()}")

print(f"{course1.name} has the following students: {course1.list_student()}")
print(f"{course2.name} has the following students: {course2.list_student()}")
print(f"{course3.name} has the following students: {course3.list_student()}")

"""courses = [course1, course2, course3]:
for student in courses:
    print(f"{student.name} has {student.course}")
"""
