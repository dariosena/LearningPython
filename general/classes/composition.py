

class Student:

    def __init__(self, name, student_number):
        self.name = name
        self.student_number = student_number
        self.classes = []

    def enrol(self, course_running):
        self.classes.append(course_running)
        course_running.add_student(self)


class Departament:

    def __init__(self, name, departament_code):
        self.name = name
        self.departament_code = departament_code
        self.courses = {}

    def add_course(self, description, course_code, creds):
        self.courses[course_code] = Course(
            description, course_code, creds, self)
        return self.courses[course_code]


class Course:

    def __init__(self, description, course_code, creds, departament):
        self.description = description
        self.course_code = course_code
        self.credits = creds
        self.departament = departament
        self.departament.add_course(self)

        self.runnings = []

    def add_running(self, year):
        self.runnings.append(CourseRunning(self, year))
        return self.runnings[-1]


class CourseRunning:

    def __init__(self, course, year):
        self.course = course
        self.year = year
        self.students = []

    def add_student(self, student):
        self.students.append(student)
