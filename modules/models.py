"""
models.py  ->  Classes, Objects, Inheritance and Polymorphism
=============================================================
This module shows OOP (Object Oriented Programming) in a simple way:

    class Person          (parent class)
          |
    class Student         (child class -> inherits from Person)

CONCEPTS USED HERE (for viva):
* class      : a blueprint that groups data (attributes) and behaviour (methods)
* __init__() : the constructor, runs automatically when an object is created
* self       : refers to the current object
* inheritance: Student gets name and greet() for free from Person
* polymorphism: get_summary() is OVERRIDDEN, same call -> different result
"""


class Person:
    """Parent (base) class: common data for any person in college."""

    college_name = "Government Polytechnic College"  # class attribute (shared)

    def __init__(self, name, city):
        # Instance attributes: every object gets its own copy
        self.name = name
        self.city = city

    def greet(self):
        """Common behaviour inherited by every child class."""
        return "Hello, I am " + self.name

    def get_summary(self):
        """Base version of get_summary (polymorphism demo)."""
        return "Person: " + self.name + " from " + self.city


class Student(Person):
    """Child class: a Student IS-A Person, plus academic details."""

    def __init__(self, name, roll_number, branch, semester, city="Unknown"):
        # super() calls the parent constructor to set name and city
        super().__init__(name, city)
        self.roll_number = roll_number
        self.branch = branch
        self.semester = semester
        # Empty dictionaries the app fills later
        self.attendance = {}  # {"Python": (34, 40), ...}
        self.marks = {}       # {"Python": 84, ...}

    # ----- new method that only Student has -----
    def get_profile(self):
        """Return the student data as a dictionary (easy to show in Streamlit)."""
        return {
            "name": self.name,
            "roll_number": self.roll_number,
            "branch": self.branch,
            "semester": self.semester,
            "city": self.city,
            "college": Person.college_name,
        }

    def add_subject_marks(self, subject_name, marks_obtained):
        """Store marks for one subject inside the marks dictionary."""
        self.marks[subject_name] = marks_obtained

    def add_subject_attendance(self, subject_name, attended_lectures, total_lectures):
        """Store attendance as a TUPLE (attended, total) - it should not change."""
        self.attendance[subject_name] = (attended_lectures, total_lectures)

    def calculate_performance(self):
        """Return average marks and average attendance for this student."""
        from modules.calculations import calculate_average, calculate_attendance

        average_marks = calculate_average(list(self.marks.values()))
        percentages = []
        for subject_name, (attended, total) in self.attendance.items():
            percentages.append(calculate_attendance(attended, total))
        average_attendance = calculate_average(percentages)
        return average_marks, average_attendance

    # ----- POLYMORPHISM: same method name, different behaviour -----
    def get_summary(self):
        """Overrides Person.get_summary()."""
        return (
            "Student: " + self.name
            + " | Roll No: " + str(self.roll_number)
            + " | " + self.branch
            + " | Semester " + str(self.semester)
        )

    def display_info(self):
        """Simple text display used in demos and tests."""
        print(self.get_summary())


def demo_polymorphism():
    """
    Shows polymorphism in 4 lines:
    the SAME method call get_summary() behaves differently
    depending on which object calls it.
    """
    person_object = Person("Mr. Verma", "Bhopal")     # parent object
    student_object = Student("Aarav Sharma", "CS2301", "CSE (AI/ML)", 3, "Indore")
    # One loop, two different classes, two different outputs:
    for obj in (person_object, student_object):       # tuple of objects
        print(obj.get_summary())
    return person_object.get_summary(), student_object.get_summary()
