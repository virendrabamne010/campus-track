"""
tests/test_functions.py  ->  Unit tests for the pure logic functions
====================================================================
Run from the project root:

    python -m unittest discover tests -v

These tests do NOT need the internet, a browser or Streamlit.
They prove the calculation and validation logic is correct.
"""

import os
import sys
import unittest

# Make sure the project ROOT is on the import path no matter
# where the tests are started from (root or inside tests/).
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from modules.calculations import (
    calculate_attendance,
    calculate_grade,
    calculate_grade_with_tuple,
    calculate_total_marks,
    calculate_average,
    calculate_percentage,
    is_pass,
    get_academic_status,
    get_subjectwise_report,
    GRADE_THRESHOLDS,
    ATTENDANCE_CRITERIA,
)
from modules.expense_manager import (
    validate_expense,
    add_expense,
    get_expense_summary,
    get_category_totals,
    get_unique_categories,
    get_category_set_report,
    get_monthly_totals,
    load_expenses_table,
)
from modules.student_manager import (
    attendance_as_dictionary,
    marks_as_dictionary,
    get_overall_attendance,
    get_marks_summary,
)
from modules.models import Person, Student


class TestAttendanceCalculations(unittest.TestCase):
    """Practical area: arithmetic + comparison operators, conditionals."""

    def test_attendance_exact_75_is_eligible_boundary(self):
        self.assertEqual(calculate_attendance(30, 40), 75.0)
        self.assertEqual(get_academic_status(75.0, 60), "Eligible - Good academic standing")

    def test_attendance_below_75_is_shortage(self):
        percentage = calculate_attendance(20, 40)
        self.assertEqual(percentage, 50.0)
        self.assertEqual(get_academic_status(percentage, 60),
                         "Attendance Shortage - Marks are fine")

    def test_attendance_zero_total_does_not_crash(self):
        self.assertEqual(calculate_attendance(0, 0), 0.0)

    def test_overall_attendance_from_dataframe(self):
        attendance_df = load_attendance_table_for_tests()
        overall = get_overall_attendance(attendance_df)
        expected = round((168 * 100) / 212, 2)
        self.assertEqual(overall, expected)


class TestGradeCalculations(unittest.TestCase):
    """Practical area: if / elif / else conditional statements."""

    def test_all_grade_boundaries(self):
        self.assertEqual(calculate_grade(95), "A+")
        self.assertEqual(calculate_grade(90), "A+")
        self.assertEqual(calculate_grade(89.99), "A")
        self.assertEqual(calculate_grade(80), "A")
        self.assertEqual(calculate_grade(75), "B")
        self.assertEqual(calculate_grade(70), "B")
        self.assertEqual(calculate_grade(65), "C")
        self.assertEqual(calculate_grade(60), "C")
        self.assertEqual(calculate_grade(55), "D")
        self.assertEqual(calculate_grade(50), "D")
        self.assertEqual(calculate_grade(49.99), "F")
        self.assertEqual(calculate_grade(10), "F")

    def test_tuple_grading_matches_if_else_grading(self):
        for percentage in (95, 85, 72, 63, 51, 40):
            self.assertEqual(
                calculate_grade(percentage),
                calculate_grade_with_tuple(percentage),
            )

    def test_grade_thresholds_tuple_is_immutable_pairs(self):
        self.assertEqual(GRADE_THRESHOLDS[0], (90, "A+"))
        self.assertEqual(len(GRADE_THRESHOLDS), 5)
        self.assertIsInstance(GRADE_THRESHOLDS, tuple)

    def test_attendance_criteria_constant(self):
        self.assertEqual(ATTENDANCE_CRITERIA, 75)


class TestMarksCalculations(unittest.TestCase):
    """Practical area: functions, for loop, lists."""

    def test_calculate_total_marks(self):
        self.assertEqual(calculate_total_marks([84, 72, 91]), 247)
        self.assertEqual(calculate_total_marks([]), 0)

    def test_calculate_average(self):
        self.assertEqual(calculate_average([80, 90]), 85.0)
        self.assertEqual(calculate_average([]), 0.0)

    def test_calculate_percentage(self):
        self.assertEqual(calculate_percentage(84, 100), 84.0)
        self.assertEqual(calculate_percentage(1, 3), 33.33)

    def test_is_pass_boundary(self):
        self.assertTrue(is_pass(50))
        self.assertFalse(is_pass(49.99))

    def test_subjectwise_report_structure(self):
        marks_dictionary = {"Python": 84, "Maths": 40}
        attendance_dictionary = {"Python": (34, 40), "Maths": (20, 40)}
        report_rows = get_subjectwise_report(marks_dictionary, attendance_dictionary)
        self.assertEqual(len(report_rows), 2)
        python_row = report_rows[0]
        self.assertEqual(python_row["grade"], "A")
        self.assertEqual(python_row["attendance_percentage"], 85.0)
        self.assertIn("Eligible", python_row["status"])
        maths_row = report_rows[1]
        self.assertEqual(maths_row["grade"], "F")


class TestExpenseValidation(unittest.TestCase):
    """Practical area: operators, membership, tuples, conditionals."""

    def test_valid_expense_passes(self):
        is_valid, message = validate_expense(120, "Food")
        self.assertTrue(is_valid)
        self.assertEqual(message, "Valid")

    def test_invalid_category_rejected(self):
        is_valid, message = validate_expense(120, "Weapons")
        self.assertFalse(is_valid)

    def test_zero_amount_rejected(self):
        is_valid, _ = validate_expense(0, "Food")
        self.assertFalse(is_valid)

    def test_negative_amount_rejected(self):
        is_valid, _ = validate_expense(-50, "Food")
        self.assertFalse(is_valid)

    def test_huge_amount_rejected(self):
        is_valid, _ = validate_expense(999999, "Food")
        self.assertFalse(is_valid)

    def test_minimum_boundary_amount_is_valid(self):
        is_valid, _ = validate_expense(1, "Travel")
        self.assertTrue(is_valid)

    def test_text_amount_rejected(self):
        is_valid, _ = validate_expense("many", "Food")  # not a number
        self.assertFalse(is_valid)


class TestExpenseAnalysis(unittest.TestCase):
    """Practical area: Pandas, dictionaries, sets, loops."""

    def test_add_expense_adds_row_and_is_reversible(self):
        expenses_df = load_expenses_table()
        original_row_count = len(expenses_df)
        updated_df, message = add_expense("2026-09-30", "Food", "test snack", 5, expenses_df)
        self.assertEqual(message, "Expense added successfully")
        self.assertEqual(len(updated_df), original_row_count + 1)
        # cleanup: remove the added row and restore the CSV
        from modules.expense_manager import remove_expense_by_index, save_expenses_table
        cleaned_df = remove_expense_by_index(len(updated_df) - 1, updated_df)
        save_expenses_table(cleaned_df)
        self.assertEqual(len(cleaned_df), original_row_count)

    def test_invalid_expense_is_not_added(self):
        expenses_df = load_expenses_table()
        original_row_count = len(expenses_df)
        updated_df, message = add_expense("2026-09-30", "Junk", "bad", 5, expenses_df)
        self.assertNotEqual(message, "Expense added successfully")
        self.assertEqual(len(updated_df), original_row_count)

    def test_expense_summary_dictionary(self):
        expenses_df = load_expenses_table()
        summary = get_expense_summary(expenses_df)
        self.assertIn("total_expenses", summary)
        self.assertIn("average_expense", summary)
        self.assertEqual(summary["number_of_expenses"], len(expenses_df))
        self.assertIsInstance(summary, dict)

    def test_category_totals_sorted_descending(self):
        totals = get_category_totals(load_expenses_table())
        values = totals.values.tolist()
        self.assertEqual(values, sorted(values, reverse=True))

    def test_unique_categories_is_a_set(self):
        unique_categories = get_unique_categories(load_expenses_table())
        self.assertIsInstance(unique_categories, set)
        self.assertTrue(unique_categories.issubset(set(["Food", "Travel", "Education",
                                                        "Entertainment", "Other"])))

    def test_set_report_has_union_intersection_difference(self):
        report = get_category_set_report(load_expenses_table())
        self.assertIn("union", report)
        self.assertIn("intersection", report)
        self.assertIn("difference", report)
        self.assertTrue(report["intersection"].issubset(report["union"]))
        self.assertTrue(report["difference"].isdisjoint(report["intersection"]))

    def test_monthly_totals_uses_month_keys(self):
        monthly_totals = get_monthly_totals(load_expenses_table())
        for month_key in monthly_totals:
            self.assertEqual(len(month_key), 7)  # "2026-09"


class TestStudentModel(unittest.TestCase):
    """Practical area: OOP classes, objects, inheritance, polymorphism."""

    def test_student_is_child_of_person(self):
        self.assertTrue(issubclass(Student, Person))

    def test_inherited_greet_method(self):
        student_object = Student("Test Student", "CS9999", "AI/ML", 3, "Bhopal")
        self.assertEqual(student_object.greet(), "Hello, I am Test Student")

    def test_polymorphism_different_summaries(self):
        person_object = Person("Teacher", "Indore")
        student_object = Student("Aarav", "CS2301", "AI/ML", 3, "Indore")
        self.assertNotEqual(person_object.get_summary(), student_object.get_summary())
        self.assertIn("Roll No", student_object.get_summary())
        self.assertIn("Person", person_object.get_summary())

    def test_student_performance_calculation(self):
        student_object = Student("Aarav", "CS2301", "AI/ML", 3, "Indore")
        student_object.add_subject_marks("Python", 80)
        student_object.add_subject_marks("Maths", 90)
        student_object.add_subject_attendance("Python", 32, 40)
        student_object.add_subject_attendance("Maths", 36, 40)
        average_marks, average_attendance = student_object.calculate_performance()
        self.assertEqual(average_marks, 85.0)
        self.assertEqual(average_attendance, 85.0)


# ---------------- helpers ----------------

def load_attendance_table_for_tests():
    """Import here so the helper sits with other data utilities."""
    from modules.student_manager import load_attendance_table
    return load_attendance_table()


if __name__ == "__main__":
    unittest.main()
