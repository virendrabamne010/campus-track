"""
calculations.py  ->  Pure calculation functions (no UI code here)
=================================================================
Every function is small, has parameters and a return value.

CONCEPTS USED HERE (for viva):
* functions with parameters and return values
* arithmetic operators  : /  *  %  //  **
* comparison operators  : >=  <  ==  !=
* logical operators     : and  or  not
* conditional statements: if / elif / else
* for loop              : looping over a dictionary of subjects
* tuple                 : GRADE_THRESHOLDS is immutable
"""

# TUPLE: grade thresholds. A tuple is used because these cut-off
# values must NEVER change while the program is running.
# Each item is a pair packed as (minimum_percentage, grade_letter).
GRADE_THRESHOLDS = (
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
)

# Attendance cut-off fixed by most colleges (assignment operator =)
ATTENDANCE_CRITERIA = 75


def calculate_attendance(attended_lectures, total_lectures):
    """Return attendance percentage for one subject."""
    # Guard clause: avoid division by zero using == and return
    if total_lectures == 0:
        return 0.0
    # Arithmetic operators: * and /
    attendance_percentage = (attended_lectures * 100) / total_lectures
    # round() keeps the answer tidy, e.g. 85.0 instead of 85.00000001
    return round(attendance_percentage, 2)


def calculate_grade(percentage):
    """Return a letter grade (A+ to F) for a percentage using if / elif / else."""
    # Conditional statements decide the grade step by step
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def calculate_grade_with_tuple(percentage):
    """Same grading using a FOR LOOP + tuple (shows a second technique)."""
    # for + tuple unpacking: (minimum, grade) takes both values of each pair
    for minimum, grade in GRADE_THRESHOLDS:
        if percentage >= minimum:
            return grade
    return "F"  # below 50


def calculate_total_marks(marks_list):
    """Return the sum of all marks using a for loop (not just sum())."""
    total_marks = 0
    for marks_obtained in marks_list:  # for loop over a list
        total_marks += marks_obtained  # assignment operator +=
    return total_marks


def calculate_average(marks_list):
    """Return the average of marks, safe for an empty list."""
    if not marks_list:  # 'not' logical operator on an empty list
        return 0.0
    total_marks = calculate_total_marks(marks_list)
    # / arithmetic operator
    return round(total_marks / len(marks_list), 2)


def calculate_percentage(marks_obtained, total_marks):
    """Return percentage for one subject."""
    if total_marks == 0:
        return 0.0
    return round((marks_obtained * 100) / total_marks, 2)


def is_pass(percentage):
    """Return True if the student passed (50 or more)."""
    # Comparison >= gives True/False, so we can return it directly
    return percentage >= 50


def get_academic_status(attendance_percentage, percentage):
    """Combine attendance and marks into one simple status message."""
    # Logical operators 'and' / 'or' combine two conditions
    if attendance_percentage >= ATTENDANCE_CRITERIA and is_pass(percentage):
        return "Eligible - Good academic standing"
    elif attendance_percentage < ATTENDANCE_CRITERIA and is_pass(percentage):
        return "Attendance Shortage - Marks are fine"
    elif attendance_percentage >= ATTENDANCE_CRITERIA and not is_pass(percentage):
        return "Failed - Attendance is fine but marks are low"
    else:
        return "At Risk - Low attendance and low marks"


def get_subjectwise_report(marks_dictionary, attendance_dictionary):
    """
    Build a subject-wise report using a FOR LOOP over dictionaries.
    Returns a list of small dictionaries (one per subject).
    """
    report_rows = []  # LIST: grows with append() inside the loop
    for subject_name, marks_obtained in marks_dictionary.items():
        attended, total = attendance_dictionary.get(subject_name, (0, 0))
        attendance_percentage = calculate_attendance(attended, total)
        percentage = calculate_percentage(marks_obtained, 100)
        report_rows.append(
            {
                "subject": subject_name,
                "marks_obtained": marks_obtained,
                "percentage": percentage,
                "grade": calculate_grade(percentage),
                "attendance_percentage": attendance_percentage,
                "status": get_academic_status(attendance_percentage, percentage),
            }
        )
    return report_rows


def demo_operators():
    """
    Tiny operator demo used by the 'Python Concepts' page.
    Returns a list of (expression, result) strings.
    """
    a = 17
    b = 5
    results = [
        ("a + b  (addition)", a + b),
        ("a - b  (subtraction)", a - b),
        ("a * b  (multiplication)", a * b),
        ("a / b  (division)", a / b),
        ("a % b  (remainder)", a % b),
        ("a // b (floor division)", a // b),
        ("a ** b (power)", a ** b),
        ("a > b  (comparison)", a > b),
        ("a != b (not equal)", a != b),
        ("(a > 10) and (b < 10)  (logical and)", (a > 10) and (b < 10)),
        ("not (a > b)  (logical not)", not (a > b)),
    ]
    return results
