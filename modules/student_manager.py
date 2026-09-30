"""
student_manager.py  ->  Student, Attendance and Marks data handling
===================================================================
All CSV reading/writing lives in the manager modules so that
app.py stays clean (this separation is called modularity).

CONCEPTS USED HERE (for viva):
* Pandas    : read_csv, DataFrame, filtering, sorting, mean
* dictionary: keys(), values(), items(), get()
* list      : append(), len()
* modules   : this file is imported by app.py
* paths     : os.path.join keeps paths working on Windows AND cloud
"""

import os

import pandas as pd

# Relative path that works from the project root on any OS.
DATA_FOLDER = os.path.join("data")
STUDENTS_CSV = os.path.join(DATA_FOLDER, "students.csv")
ATTENDANCE_CSV = os.path.join(DATA_FOLDER, "attendance.csv")
MARKS_CSV = os.path.join(DATA_FOLDER, "marks.csv")


# ---------------- Student profile ----------------

def load_students_table():
    """Read students.csv as a Pandas DataFrame."""
    return pd.read_csv(STUDENTS_CSV)


def build_student_from_row(roll_number):
    """
    Find one student row by roll number and build a Student OBJECT.
    Shows why OOP is useful: CSV row -> real object with methods.
    """
    from modules.models import Student  # import inside function avoids circular import

    students_df = load_students_table()
    matching_rows = students_df[students_df["roll_number"] == roll_number]
    if matching_rows.empty:
        return None
    row = matching_rows.iloc[0]  # first matching row
    student_object = Student(
        name=row["name"],
        roll_number=row["roll_number"],
        branch=row["branch"],
        semester=int(row["semester"]),
        city=row["city"],
    )
    return student_object


# ---------------- Attendance ----------------

def load_attendance_table():
    """Read attendance.csv as a Pandas DataFrame."""
    return pd.read_csv(ATTENDANCE_CSV)


def attendance_as_dictionary(attendance_df):
    """
    Convert the DataFrame into a dictionary:
        {"Python Programming": (34, 40), ...}
    Tuple value = (attended, total) because the pair is fixed.
    """
    attendance_dictionary = {}
    for row in attendance_df.itertuples(index=False):
        attendance_dictionary[row.subject] = (row.attended_lectures, row.total_lectures)
    return attendance_dictionary


def save_attendance_table(attendance_df):
    """Write the attendance DataFrame back to CSV (index=False drops row numbers)."""
    attendance_df.to_csv(ATTENDANCE_CSV, index=False)


def update_attendance(subject_name, attended_lectures, total_lectures, attendance_df):
    """
    Update one subject's attendance row (or add it at the end).
    Returns the updated DataFrame.
    """
    row_mask = attendance_df["subject"] == subject_name
    if row_mask.any():  # subject already present -> update the row
        attendance_df.loc[row_mask, "total_lectures"] = total_lectures
        attendance_df.loc[row_mask, "attended_lectures"] = attended_lectures
    else:  # new subject -> append a row
        new_row = pd.DataFrame(
            [[subject_name, total_lectures, attended_lectures]],
            columns=["subject", "total_lectures", "attended_lectures"],
        )
        attendance_df = pd.concat([attendance_df, new_row], ignore_index=True)
    return attendance_df


def get_overall_attendance(attendance_df):
    """Overall attendance = total attended / total lectures across subjects."""
    total_lectures = attendance_df["total_lectures"].sum()
    attended_lectures = attendance_df["attended_lectures"].sum()
    if total_lectures == 0:
        return 0.0
    return round((attended_lectures * 100) / total_lectures, 2)


# ---------------- Marks ----------------

def load_marks_table():
    """Read marks.csv as a Pandas DataFrame."""
    return pd.read_csv(MARKS_CSV)


def marks_as_dictionary(marks_df):
    """Convert DataFrame -> {"Python Programming": 84, ...}."""
    marks_dictionary = {}
    for row in marks_df.itertuples(index=False):
        marks_dictionary[row.subject] = row.marks_obtained
    return marks_dictionary


def save_marks_table(marks_df):
    """Write the marks DataFrame back to CSV."""
    marks_df.to_csv(MARKS_CSV, index=False)


def update_marks(subject_name, marks_obtained, total_marks, marks_df):
    """Update one subject's marks row (or add it). Returns updated DataFrame."""
    row_mask = marks_df["subject"] == subject_name
    if row_mask.any():
        marks_df.loc[row_mask, "marks_obtained"] = marks_obtained
        marks_df.loc[row_mask, "total_marks"] = total_marks
    else:
        new_row = pd.DataFrame(
            [[subject_name, marks_obtained, total_marks]],
            columns=["subject", "marks_obtained", "total_marks"],
        )
        marks_df = pd.concat([marks_df, new_row], ignore_index=True)
    return marks_df


def get_marks_summary(marks_df):
    """Small dictionary of useful mark statistics (uses Pandas aggregations)."""
    summary = {
        "total_subjects": len(marks_df),
        "total_marks_scored": int(marks_df["marks_obtained"].sum()),
        "average_marks": round(marks_df["marks_obtained"].mean(), 2),
        "highest_marks": int(marks_df["marks_obtained"].max()),
        "lowest_marks": int(marks_df["marks_obtained"].min()),
    }
    return summary


def get_top_subject(marks_df):
    """Return the subject with the highest marks (sort_values + iloc)."""
    if marks_df.empty:
        return "No data"
    sorted_df = marks_df.sort_values(by="marks_obtained", ascending=False)
    return sorted_df.iloc[0]["subject"]
