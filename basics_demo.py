"""
basics_demo.py  ->  Python Basics demonstration (Practical 1, 2 and 3)
======================================================================
Run it from the terminal INSIDE the project folder:

    python basics_demo.py

WHAT IT SHOWS (for viva):
* print() output
* variables and identifiers
* type checking with type()
* input/output (works even when no keyboard is attached, e.g. in tests)
* operators: arithmetic, comparison, logical, membership, identity
* keywords used naturally: if, else, elif, for, while, def, return,
  class, import, from, in, is, and, or, not, True, False, None
"""

# 'import' brings the whole math module in
import math
# 'from' brings one specific function out of the os module
from os import getcwd


# ---------------- 1. print and variables ----------------

def demo_print_and_variables():
    """Variables store values; print() shows them on the screen."""
    student_name = "Aarav Sharma"     # str (text)
    roll_number = 2301                # int (whole number)
    attendance_percentage = 85.5      # float (decimal)
    is_regular_student = True         # bool (True/False)
    guardian_phone = None             # NoneType (no value yet)

    print("Welcome to CampusTrack!")
    print("Student :", student_name)
    print("Roll No :", roll_number)
    print("Attend. :", attendance_percentage, "%")
    print("Regular? :", is_regular_student)
    print("Phone   :", guardian_phone)

    # IDENTIFIERS are the names we choose: student_name, roll_number...
    # Rule: start with a letter or _, no spaces, case-sensitive.
    # 'roll_number' and 'Roll_Number' would be two different names!


# ---------------- 2. type checking ----------------

def demo_type_checking():
    """type() tells us the class of a value."""
    sample_values = [42, 3.14, "hello", True, None, (1, 2), [1, 2], {1, 2}, {"a": 1}]
    for value in sample_values:          # for loop over a list
        print(type(value).__name__, "->", value)


# ---------------- 3. input/output ----------------

def ask_user_name():
    """
    input() reads typed text from the keyboard.
    It ALWAYS returns a string, so we convert it with int() if needed.
    If no keyboard is available (automated testing), we return a default.
    """
    try:
        entered_name = input("Enter your name: ")
        entered_age = int(input("Enter your age: "))
        print("Hello", entered_name + ", you will be", entered_age + 1, "next year.")
        return entered_name
    except (EOFError, ValueError):
        print("No valid input received - using default name 'Guest'.")
        return "Guest"


# ---------------- 4. operators ----------------

def demo_operators_basics():
    """All operator families with one easy example each."""
    a = 17
    b = 5

    print("--- Arithmetic operators ---")
    print("a + b =", a + b)     # addition        -> 22
    print("a - b =", a - b)     # subtraction     -> 12
    print("a * b =", a * b)     # multiplication  -> 85
    print("a / b =", a / b)     # true division   -> 3.4
    print("a % b =", a % b)     # remainder       -> 2
    print("a // b =", a // b)   # floor division  -> 3
    print("a ** b =", a ** b)   # power           -> 17^5

    print("--- Assignment operators ---")
    total_marks = 100
    total_marks += 50   # same as: total_marks = total_marks + 50
    print("after += :", total_marks)
    total_marks -= 30
    print("after -= :", total_marks)
    total_marks *= 2
    print("after *= :", total_marks)

    print("--- Comparison operators ---")
    print("a > b :", a > b)
    print("a < b :", a < b)
    print("a >= 17 :", a >= 17)
    print("a <= 10 :", a <= 10)
    print("a == 17 :", a == 17)
    print("a != b :", a != b)

    print("--- Logical operators ---")
    print("(a > 10) and (b < 10) :", (a > 10) and (b < 10))
    print("(a < 10) or (b < 10)  :", (a < 10) or (b < 10))
    print("not (a > b)           :", not (a > b))

    print("--- Membership operators (in / not in) ---")
    subject_list = ["Python", "Maths", "DBMS"]
    print("'Python' in subjects   :", "Python" in subject_list)
    print("'Java' not in subjects :", "Java" not in subject_list)

    print("--- Identity operators (is / is not) ---")
    # 'is' checks whether TWO NAMES point to the SAME object in memory.
    first_list = [1, 2, 3]
    second_list = first_list       # same object!
    third_list = [1, 2, 3]         # equal content, but a NEW object
    print("first is second :", first_list is second_list)   # True
    print("first is third  :", first_list is third_list)    # False
    print("first == third  :", first_list == third_list)    # True (values equal)


# ---------------- 5. small keyword tour ----------------

def demo_keywords():
    """Shows several keywords through real code, not just words."""
    # if / elif / else
    attendance_percentage = 82
    if attendance_percentage >= 75:
        print("Keywords if/elif/else: Eligible")
    elif attendance_percentage >= 60:
        print("Keywords if/elif/else: Condonation needed")
    else:
        print("Keywords if/elif/else: Shortage")

    # while: repeat until a condition becomes False
    countdown = 3
    while countdown > 0:
        print("while loop counting:", countdown)
        countdown -= 1     # assignment -=

    # def / return
    def square(number):
        return number ** 2

    print("def/return: square(6) =", square(6))

    # in, is, and, or, not, True, False, None used in one line
    subject_list = ["Python", "Maths"]
    if "Python" in subject_list and subject_list is not None:
        print("Keywords in/is/and/not/None: all working!")
    else:
        print("This line should never print (False branch).")

    # math module usage (import at top of this file)
    print("import math: sqrt(144) =", math.sqrt(144))
    print("from os import getcwd ->", getcwd())


# ---------------- main program ----------------

if __name__ == "__main__":
    # This special condition is True only when the file is run
    # directly (python basics_demo.py), not when it is imported.
    demo_print_and_variables()
    print()
    demo_type_checking()
    print()
    ask_user_name()
    print()
    demo_operators_basics()
    print()
    demo_keywords()
