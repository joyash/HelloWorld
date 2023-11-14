class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.enrollments = []


class Course:
    def __init__(self, course_code, course_name, instructor):
        self.course_name = course_code
        self.course_code = course_name
        self.instructor = instructor
        self.enrollments = []


class Enrollment:
    def __init__(self, student, course, progress=0.0):
        self.student = student
        self.course = course
        self.progress = progress


def enroll(student, course):
    enrollment = Enrollment(student, course)
    student.enrollments.append(enrollment)
    course.enrollments.append(enrollment)


def update_progress(student, course, progress):
    for enrollment in student.enrollments:
        if enrollment.course == course:
            enrollment.progress = progress


def print_student_enrollments(student):
    print(f"Student ID: {student.student_id}")
    print(f"Student NAME: {student.student_name}")
    print("Enrollments:")
    for enrollment in student.enrollments:
        print(f"Course: {enrollment.course.course_name}")
        print(f"Course CODE: {enrollment.course.course_code}")
        print(f"Progress: {enrollment.progress}")
        print("Instructors:", " ".join(enrollment.course.instructor))
        print("")


# create student
student1 = Student("1", "Timo")
student2 = Student("2", "Phuong")

# create course
course1 = Course("CS101", "Introduction to Python", ["Chau"])
course2 = Course("CS202", "Physics", ["Timo"])
course3 = Course("CS103", "Smart IoT", ["Kimmo"])

# enroll students in course
enroll(student1, course1)
enroll(student1, course2)
enroll(student2, course1)
enroll(student2, course3)

# update progress
update_progress(student1, course1, 70.5)
update_progress(student1, course2, 85.0)
update_progress(student2, course1, 60.0)
update_progress(student2, course2, 75.5)

print_student_enrollments(student1)
print_student_enrollments(student2)
