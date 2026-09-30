"""
app.py  ->  CampusTrack main Streamlit application
==================================================
Run from the project root:

    streamlit run app.py

This file is only the UI (presentation layer).
All calculation logic lives in  modules/calculations.py
All data handling lives in     modules/student_manager.py
                               modules/expense_manager.py
All OOP classes live in        modules/models.py

Sidebar sections:
1. Home Dashboard     5. Expense Tracker
2. Student Profile    6. Data Analysis
3. Attendance Tracker 7. Python Concepts Used
4. Marks & Grade      8. Viva Preparation
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Custom modules (this is why modules/ has an __init__.py)
from modules.calculations import (
    calculate_attendance,
    calculate_grade,
    calculate_percentage,
    is_pass,
    get_academic_status,
    get_subjectwise_report,
    demo_operators,
    ATTENDANCE_CRITERIA,
)
from modules.models import Person, Student, demo_polymorphism
from modules import student_manager, expense_manager

# ---------------- Streamlit page setup ----------------

st.set_page_config(
    page_title="CampusTrack - Student Academic & Expense Manager",
    page_icon="🎓",
    layout="wide",
)

SIDEBAR_PAGES = [
    "Home Dashboard",
    "Student Profile",
    "Attendance Tracker",
    "Marks & Grade Analyzer",
    "Expense Tracker",
    "Data Analysis",
    "Python Concepts Used",
    "Viva Preparation",
]

GRADE_SCALE_TEXT = "90+ = A+ | 80-89 = A | 70-79 = B | 60-69 = C | 50-59 = D | Below 50 = F"


# ---------------- Small reusable UI helpers ----------------

def page_header(title, subtitle):
    """One styled header used by every page (keeps the app consistent)."""
    st.title(title)
    st.caption(subtitle)


def metric_cards(list_of_metric_tuples):
    """Show 4 metric cards in one row: [(label, value, help_text), ...]."""
    columns = st.columns(len(list_of_metric_tuples))
    for column, (label, value, help_text) in zip(columns, list_of_metric_tuples):
        with column:
            st.metric(label=label, value=value, help=help_text)


def attendance_status_badge(attendance_percentage):
    """Green 'Eligible' / red 'Shortage' badge using if / else."""
    if attendance_percentage >= ATTENDANCE_CRITERIA:
        st.success("✅ Eligible (" + str(attendance_percentage) + "% >= 75%)")
    elif attendance_percentage >= 65:
        st.warning("⚠️ Borderline - attend more lectures (" + str(attendance_percentage) + "%)")
    else:
        st.error("🚨 Attendance Shortage (" + str(attendance_percentage) + "% < 75%)")


def bar_chart_matplotlib(labels, values, title_text, ylabel_text, color_choice):
    """One shared function for all bar charts (matplotlib)."""
    figure, axis = plt.subplots(figsize=(7, 3.5))
    axis.bar(labels, values, color=color_choice)
    axis.set_title(title_text)
    axis.set_ylabel(ylabel_text)
    axis.tick_params(axis="x", rotation=30)
    for index, value in enumerate(values):  # write the value on top of each bar
        axis.text(index, value, str(value), ha="center", va="bottom", fontsize=8)
    plt.tight_layout()
    return figure


# ---------------- 1. Home Dashboard ----------------

def show_home_dashboard():
    page_header(
        "🎓 CampusTrack Dashboard",
        "One place for attendance, marks and expenses - built with pure Python, Pandas and Streamlit.",
    )

    # Load all data through the custom modules
    attendance_df = student_manager.load_attendance_table()
    marks_df = student_manager.load_marks_table()
    expenses_df = expense_manager.load_expenses_table()

    overall_attendance = student_manager.get_overall_attendance(attendance_df)
    marks_summary = student_manager.get_marks_summary(marks_df)
    expense_summary = expense_manager.get_expense_summary(expenses_df)

    average_grade = calculate_grade(marks_summary["average_marks"])

    st.subheader("📋 Quick Overview")
    metric_cards([
        ("Total Subjects", marks_summary["total_subjects"], "From marks.csv"),
        ("Average Marks", marks_summary["average_marks"], "Mean of marks_obtained"),
        ("Overall Attendance", str(overall_attendance) + "%", "Attended / total lectures"),
        ("Total Expenses (₹)", expense_summary["total_expenses"], "Sum of expenses.csv"),
    ])
    metric_cards([
        ("Current Grade", average_grade, "From average marks"),
        ("Highest Marks", marks_summary["highest_marks"], "Best subject score"),
        ("Average Expense (₹)", expense_summary["average_expense"], "Per expense entry"),
        ("Expense Entries", expense_summary["number_of_expenses"], "Rows in CSV"),
    ])

    st.subheader("📊 Snapshot Charts")
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("**Attendance by Subject**")
        attendance_percentage_column = (
            (attendance_df["attended_lectures"] * 100) / attendance_df["total_lectures"]
        ).round(2)
        attendance_df["attendance_percentage"] = attendance_percentage_column
        chart = bar_chart_matplotlib(
            attendance_df["subject"].tolist(),
            attendance_df["attendance_percentage"].tolist(),
            "Attendance % per subject",
            "Percentage",
            "#2e7d32",
        )
        st.pyplot(chart)
    with right_column:
        st.markdown("**Marks by Subject**")
        chart = bar_chart_matplotlib(
            marks_df["subject"].tolist(),
            marks_df["marks_obtained"].tolist(),
            "Marks per subject",
            "Marks",
            "#1565c0",
        )
        st.pyplot(chart)

    # Short status message using conditionals + logical operators
    if overall_attendance >= ATTENDANCE_CRITERIA and marks_summary["average_marks"] >= 50:
        st.success("Status: Eligible and passing - keep it up! 🎉")
    elif overall_attendance < ATTENDANCE_CRITERIA and marks_summary["average_marks"] >= 50:
        st.warning("Status: Marks are fine but attendance is short.")
    else:
        st.error("Status: Needs attention in attendance and/or marks.")


# ---------------- 2. Student Profile ----------------

def show_student_profile():
    page_header(
        "🧑‍🎓 Student Profile",
        "This page uses the Student class (OOP): Person -> Student inheritance.",
    )

    st.subheader("Edit your profile (saved only for this session)")
    with st.form("profile_form"):
        input_name = st.text_input("Name", value="Aarav Sharma")
        input_roll = st.text_input("Roll Number", value="CS2301")
        input_branch = st.text_input("Branch", value="CSE (AI/ML)")
        input_semester = st.number_input("Semester", min_value=1, max_value=8, value=3)
        input_city = st.text_input("City", value="Indore")
        submitted = st.form_submit_button("Create Student Object")
    if submitted:
        # OOP: an OBJECT is created from the Student class right here
        student_object = Student(
            name=input_name,
            roll_number=input_roll,
            branch=input_branch,
            semester=int(input_semester),
            city=input_city,
        )
        # Fill the object with real data from the CSVs
        marks_df = student_manager.load_marks_table()
        attendance_df = student_manager.load_attendance_table()
        for row in marks_df.itertuples(index=False):
            student_object.add_subject_marks(row.subject, row.marks_obtained)
        for row in attendance_df.itertuples(index=False):
            student_object.add_subject_attendance(
                row.subject, row.attended_lectures, row.total_lectures
            )
        # Keep the object for other pages (session state = app memory)
        st.session_state["student_object"] = student_object
        st.success("Student object created and stored in session state!")

    student_object = st.session_state.get("student_object")
    if student_object is None:
        st.info("Fill the form above and click 'Create Student Object' to begin.")
        return

    st.subheader("Object methods in action")
    st.markdown("**display_info() output:**")
    student_object.display_info()  # method call on the object

    st.markdown("**get_profile() returns a dictionary:**")
    st.json(student_object.get_profile())

    average_marks, average_attendance = student_object.calculate_performance()
    metric_cards([
        ("Avg Marks (object)", average_marks, "From student_object.marks"),
        ("Avg Attendance (object)", str(average_attendance) + "%", "From student_object.attendance"),
        ("Subjects stored", len(student_object.marks), "len() of the marks dictionary"),
        ("Class", type(student_object).__name__, "Created from Student class"),
    ])
    st.code("type(student_object) -> <class 'modules.models.Student'>", language="python")


# ---------------- 3. Attendance Tracker ----------------

def show_attendance_tracker():
    page_header(
        "🗓️ Attendance Tracker",
        "Enter lectures attended vs held; percentage and eligibility are calculated automatically.",
    )

    attendance_df = student_manager.load_attendance_table()

    st.subheader("Current attendance data")
    attendance_df["attendance_percentage"] = (
        (attendance_df["attended_lectures"] * 100) / attendance_df["total_lectures"]
    ).round(2)
    st.dataframe(attendance_df, width="stretch")

    overall_attendance = student_manager.get_overall_attendance(attendance_df)
    st.markdown("### Overall attendance: " + str(overall_attendance) + "%")
    attendance_status_badge(overall_attendance)

    st.subheader("Check / update one subject")
    with st.form("attendance_form"):
        subject_name = st.text_input("Subject", value="Python Programming")
        total_lectures = st.number_input("Total lectures held", min_value=0, value=40)
        attended_lectures = st.number_input("Lectures attended", min_value=0, value=34)
        update_clicked = st.form_submit_button("Calculate & Save")
    if update_clicked:
        # Validation using comparison operators and 'not'
        if total_lectures == 0:
            st.error("Total lectures cannot be 0.")
        elif attended_lectures > total_lectures:
            st.error("Attended cannot be more than total!")
        else:
            attendance_percentage = calculate_attendance(attended_lectures, total_lectures)
            st.info(
                "Formula: (attended * 100) / total = ("
                + str(int(attended_lectures)) + " * 100) / "
                + str(int(total_lectures)) + " = "
                + str(attendance_percentage) + "%"
            )
            attendance_status_badge(attendance_percentage)
            updated_df = student_manager.update_attendance(
                subject_name, int(attended_lectures), int(total_lectures), attendance_df
            )
            student_manager.save_attendance_table(updated_df)
            st.success("Saved to data/attendance.csv - refresh to see it in the table.")
            st.rerun()

    st.subheader("Subject-wise eligibility table")
    report_rows = get_subjectwise_report(
        student_manager.marks_as_dictionary(student_manager.load_marks_table()),
        student_manager.attendance_as_dictionary(student_manager.load_attendance_table()),
    )
    st.dataframe(pd.DataFrame(report_rows), width="stretch")


# ---------------- 4. Marks & Grade Analyzer ----------------

def show_marks_analyzer():
    page_header(
        "📝 Marks & Grade Analyzer",
        "Grading scale: " + GRADE_SCALE_TEXT,
    )

    marks_df = student_manager.load_marks_table()
    marks_df["percentage"] = (
        (marks_df["marks_obtained"] * 100) / marks_df["total_marks"]
    ).round(2)
    # apply() calls our reusable calculate_grade() for every row
    marks_df["grade"] = marks_df["percentage"].apply(calculate_grade)
    marks_df["result"] = marks_df["percentage"].apply(
        lambda value: "PASS" if is_pass(value) else "FAIL"
    )
    st.dataframe(marks_df, width="stretch")

    marks_summary = student_manager.get_marks_summary(marks_df)
    st.subheader("Summary statistics")
    metric_cards([
        ("Average", marks_summary["average_marks"], "df['marks_obtained'].mean()"),
        ("Total Scored", marks_summary["total_marks_scored"], "df['marks_obtained'].sum()"),
        ("Highest", marks_summary["highest_marks"], "df['marks_obtained'].max()"),
        ("Lowest", marks_summary["lowest_marks"], "df['marks_obtained'].min()"),
    ])
    st.markdown("**Top subject:** " + student_manager.get_top_subject(marks_df))
    st.markdown("**Overall grade from average:** " + calculate_grade(marks_summary["average_marks"]))

    st.subheader("Add / update marks for a subject")
    with st.form("marks_form"):
        subject_name = st.text_input("Subject", value="Python Programming")
        marks_obtained = st.number_input("Marks obtained", min_value=0, max_value=200, value=84)
        total_marks = st.number_input("Total marks", min_value=1, max_value=200, value=100)
        save_clicked = st.form_submit_button("Calculate Grade & Save")
    if save_clicked:
        subject_percentage = calculate_percentage(marks_obtained, total_marks)
        subject_grade = calculate_grade(subject_percentage)
        st.markdown("### Percentage: " + str(subject_percentage) + "%  |  Grade: " + subject_grade)
        if is_pass(subject_percentage):
            st.success("PASS ✅")
        else:
            st.error("FAIL ❌ - below 50")
        updated_df = student_manager.update_marks(
            subject_name, int(marks_obtained), int(total_marks), marks_df
        )
        student_manager.save_marks_table(updated_df)
        st.success("Saved to data/marks.csv")

    st.subheader("Marks chart")
    chart = bar_chart_matplotlib(
        marks_df["subject"].tolist(),
        marks_df["marks_obtained"].tolist(),
        "Marks obtained per subject",
        "Marks",
        "#6a1b9a",
    )
    st.pyplot(chart)


# ---------------- 5. Expense Tracker ----------------

def show_expense_tracker():
    page_header(
        "💸 Expense Tracker",
        "Add daily expenses; lists, tuples, sets, dictionaries and functions all work together here.",
    )

    expenses_df = expense_manager.load_expenses_table()

    expense_summary = expense_manager.get_expense_summary(expenses_df)
    metric_cards([
        ("Total (₹)", expense_summary["total_expenses"], "Sum of all amounts"),
        ("Average (₹)", expense_summary["average_expense"], "Mean amount"),
        ("Highest (₹)", expense_summary["highest_expense"], "Costliest entry"),
        ("Entries", expense_summary["number_of_expenses"], "len(df)"),
    ])

    st.subheader("Add a new expense")
    with st.form("expense_form"):
        input_date = st.date_input("Date")
        input_category = st.selectbox("Category", expense_manager.EXPENSE_CATEGORIES)  # LIST
        input_description = st.text_input("Description", value="Canteen lunch")
        input_amount = st.number_input("Amount (₹)", min_value=0, value=100)
        add_clicked = st.form_submit_button("Validate & Add")
    if add_clicked:
        expenses_df, message = expense_manager.add_expense(
            str(input_date), input_category, input_description, int(input_amount), expenses_df
        )
        if message == "Expense added successfully":
            st.success(message)
            st.rerun()
        else:
            st.error("Validation failed: " + message)

    st.subheader("All expenses (newest last)")
    st.dataframe(expenses_df.sort_values(by="date", ascending=False), width="stretch")

    st.subheader("Danger zone: delete an entry")
    with st.expander("Delete one expense by row number"):
        row_index_to_delete = st.number_input(
            "Row index (0 = first)", min_value=0, max_value=len(expenses_df) - 1, value=0
        )
        if st.button("Delete this row"):
            expenses_df = expense_manager.remove_expense_by_index(int(row_index_to_delete), expenses_df)
            st.success("Row deleted and CSV updated.")
            st.rerun()

    st.subheader("Category-wise totals")
    st.dataframe(expense_manager.get_category_totals(expenses_df).reset_index(),
                 width="stretch")

    chart = bar_chart_matplotlib(
        expense_manager.get_category_totals(expenses_df).index.tolist(),
        expense_manager.get_category_totals(expenses_df).values.tolist(),
        "Expenses by category",
        "Rupees",
        "#e65100",
    )
    st.pyplot(chart)


# ---------------- 6. Data Analysis (Pandas playground) ----------------

def show_data_analysis():
    page_header(
        "🔬 Data Analysis with Pandas",
        "Real filtering, sorting, grouping and statistics on the CSV data.",
    )

    expenses_df = expense_manager.load_expenses_table()

    tab_one, tab_two, tab_three = st.tabs(["💰 Expenses", "📚 Marks", "🗓️ Attendance"])

    with tab_one:
        st.markdown("**df.head() - first 5 expense rows**")
        st.dataframe(expenses_df.head(), width="stretch")
        st.markdown("**df.tail() - last 5 expense rows**")
        st.dataframe(expenses_df.tail(), width="stretch")

        st.markdown("**Filter: expenses above a threshold**  `df[df[\"amount\"] > x]`")
        threshold_amount = st.slider("Threshold (₹)", 50, 1000, 300)
        st.dataframe(expense_manager.get_expensive_expenses(expenses_df, threshold_amount),
                     width="stretch")

        st.markdown("**Filter: one category**  `df[df[\"category\"] == value]`")
        selected_category = st.selectbox("Choose category", expense_manager.EXPENSE_CATEGORIES)
        st.dataframe(
            expense_manager.filter_expenses_by_category(expenses_df, selected_category),
            width="stretch",
        )

        st.markdown("**groupby category (sum, mean, count)**")
        grouped = expenses_df.groupby("category")["amount"].agg(["sum", "mean", "count"])
        st.dataframe(grouped, width="stretch")

        st.markdown("**Sorted by amount (highest first)**  `df.sort_values(...)`")
        st.dataframe(
            expenses_df.sort_values(by="amount", ascending=False).head(8), width="stretch"
        )

        costliest = expense_manager.get_highest_expense_row(expenses_df)
        st.markdown("**Highest single expense:**")
        st.info(
            "₹" + str(costliest["amount"]) + " - " + costliest["description"]
            + " (" + costliest["category"] + ", " + str(costliest["date"]) + ")"
        )

        st.markdown("**Set operations on categories**")
        set_report = expense_manager.get_category_set_report(expenses_df)
        st.write("Unique categories in data (set):", set_report["union"] if not expenses_df.empty else set())
        st.write("Used categories (intersection):", set_report["intersection"])
        st.write("Allowed but unused (difference):", set_report["difference"])

        st.markdown("**Monthly totals (for loop + dictionary)**")
        st.write(expense_manager.get_monthly_totals(expenses_df))

    with tab_two:
        marks_df = student_manager.load_marks_table()
        st.markdown("**Marks table with percentage and grade**")
        marks_df["percentage"] = ((marks_df["marks_obtained"] * 100) / marks_df["total_marks"]).round(2)
        marks_df["grade"] = marks_df["percentage"].apply(calculate_grade)
        st.dataframe(marks_df, width="stretch")
        st.markdown("**describe() - automatic statistics**")
        st.dataframe(marks_df["marks_obtained"].describe(), width="stretch")
        st.markdown("**Average marks:** " + str(round(marks_df["marks_obtained"].mean(), 2)))

    with tab_three:
        attendance_df = student_manager.load_attendance_table()
        attendance_df["percentage"] = (
            (attendance_df["attended_lectures"] * 100) / attendance_df["total_lectures"]
        ).round(2)
        st.markdown("**Attendance table with percentage**")
        st.dataframe(attendance_df, width="stretch")
        st.markdown("**Subjects below 75% (filter + logical thinking)**")
        low_attendance_df = attendance_df[attendance_df["percentage"] < ATTENDANCE_CRITERIA]
        if low_attendance_df.empty:
            st.success("No attendance shortage anywhere! 🎉")
        else:
            st.dataframe(low_attendance_df, width="stretch")


# ---------------- 7. Python Concepts Used ----------------

CONCEPT_SECTIONS = [
    ("Identifiers", "Names we choose for variables, functions and classes.",
     "student_name = \"Aarav Sharma\"\nattendance_percentage = 85.5",
     "Used everywhere: student_manager.py, expense_manager.py, forms in app.py."),
    ("Keywords", "Reserved words with special meaning: if, else, elif, for, while, def, return, class, import, from, in, is, and, or, not, True, False, None.",
     "if attendance_percentage >= 75:\n    return \"Eligible\"",
     "calculate_grade(), validate_expense(), every module."),
    ("Variables", "Named boxes that store values of different types (int, float, str, bool, None).",
     "total_marks = 100        # int\nattendance_percentage = 85.5   # float",
     "basics_demo.py and all modules."),
    ("Operators", "Arithmetic (+ - * / % // **), comparison (> < >= <= == !=), logical (and or not), membership (in, not in), identity (is, is not), assignment (+= -= *=).",
     "percentage = (attended * 100) / total\nif percentage >= 75 and is_pass(marks):",
     "calculations.py, expense_manager.py, basics_demo.py."),
    ("Conditional Statements", "if / elif / else let the program take decisions.",
     "if percentage >= 90:\n    grade = \"A+\"\nelif percentage >= 80:\n    grade = \"A\"\nelse:\n    grade = \"F\"",
     "calculate_grade() in calculations.py; eligibility badges in app.py."),
    ("For Loop", "Repeats over each item of a list, tuple, dictionary or DataFrame column.",
     "for subject_name, marks_obtained in marks_dictionary.items():\n    report_rows.append(...)",
     "get_subjectwise_report(), get_unique_categories(), charts in app.py."),
    ("While Loop", "Repeats as long as a condition stays True.",
     "while counter <= 5:\n    print(counter)\n    counter += 1",
     "loops_demo.py menu simulation and validation."),
    ("break", "Stops the whole loop immediately.",
     "if marks_obtained < 60:\n    break   # stop searching",
     "loops_demo.py break_demonstration()."),
    ("continue", "Skips the rest of this round, goes to the next round.",
     "if expense_amount <= 0:\n    continue   # skip invalid row",
     "loops_demo.py continue_demonstration(); concept mirrors invalid-row skipping."),
    ("pass", "Does nothing - a placeholder for future code.",
     "def not_written_yet():\n    pass",
     "loops_demo.py pass_demonstration()."),
    ("Lists", "Ordered, changeable collection: create, append, extend, insert, remove, pop, sort, reverse, len, in.",
     "EXPENSE_CATEGORIES = [\"Food\", \"Travel\", \"Education\"]\nEXPENSE_CATEGORIES.append(\"Health\")",
     "expense_manager.py categories; marks lists in calculations.py."),
    ("Tuples", "Ordered but UNCHANGEABLE - perfect for fixed values; supports indexing, slicing, len, in, packing/unpacking.",
     "GRADE_THRESHOLDS = ((90, \"A+\"), (80, \"A\"))\nminimum, grade = GRADE_THRESHOLDS[0]",
     "calculations.py GRADE_THRESHOLDS; attendance stored as (attended, total)."),
    ("Sets", "Unordered collection with NO duplicates: add, remove, discard, union, intersection, difference.",
     "unique_categories = set()\nunique_categories.add(\"Food\")",
     "expense_manager.get_unique_categories() and get_category_set_report()."),
    ("Dictionaries", "Key-value pairs: create, access, update, keys(), values(), items(), get().",
     "student = {\"name\": \"Aarav\", \"semester\": 3}\nstudent.get(\"branch\", \"N/A\")",
     "Student class, get_profile(), get_expense_summary(), get_marks_summary()."),
    ("Functions", "Reusable named blocks with parameters and return values.",
     "def calculate_average(marks_list):\n    return round(sum(marks_list) / len(marks_list), 2)",
     "calculations.py, expense_manager.py, student_manager.py - the whole project."),
    ("Modules", "Separate .py files imported with 'from modules.calculations import ...'.",
     "from modules.calculations import calculate_grade",
     "app.py imports from the modules package (see modules/__init__.py)."),
    ("Classes & Objects", "A class is a blueprint; an object is a real thing made from it.",
     "student_object = Student(\"Aarav\", \"CS2301\", \"CSE (AI/ML)\", 3)",
     "Student Profile page creates real objects; models.py defines the classes."),
    ("Inheritance", "A child class reuses the parent class code.",
     "class Student(Person):   # Student IS-A Person\n    ...",
     "models.py: Student inherits name, city and greet() from Person."),
    ("Polymorphism", "Same method name behaves differently for different objects.",
     "for obj in (person_object, student_object):\n    print(obj.get_summary())",
     "models.py get_summary() overridden in Student; demo in Python Concepts page."),
    ("Pandas", "Library for tables (DataFrames): read_csv, head, tail, filtering, sort_values, groupby, sum, mean, max.",
     "df = pd.read_csv(\"data/expenses.csv\")\ndf.groupby(\"category\")[\"amount\"].sum()",
     "student_manager.py, expense_manager.py, Data Analysis page."),
]


def show_python_concepts():
    page_header(
        "🐍 Python Concepts Used",
        "Every practical topic, where it lives in this project, and a tiny example.",
    )

    # Live polymorphism demo button
    st.subheader("▶️ Live OOP demo (polymorphism)")
    if st.button("Run get_summary() on Person and Student"):
        person_summary, student_summary = demo_polymorphism()
        st.code(person_summary)
        st.code(student_summary)
        st.caption("Same method call, two different outputs - that is polymorphism.")

    st.subheader("▶️ Live operator demo")
    st.dataframe(pd.DataFrame(demo_operators(), columns=["Expression", "Result"]),
                 width="stretch")

    st.subheader("📖 Concept-by-concept guide")
    for concept_name, concept_meaning, code_example, where_used in CONCEPT_SECTIONS:
        with st.expander("🔹 " + concept_name):
            st.markdown("**What it means:** " + concept_meaning)
            st.code(code_example, language="python")
            st.markdown("**Where it is used in CampusTrack:** " + where_used)


# ---------------- 8. Viva Preparation ----------------

VIVA_QUESTIONS = [
    ("1. What is Python?",
     "Python is a simple, high-level, interpreted programming language. Code is read almost like English, which makes it perfect for beginners."),
    ("2. Why did you use Python?",
     "Because it has simple syntax, powerful libraries like Pandas and Streamlit, and is widely used in AI/ML - my branch."),
    ("3. What is a variable?",
     "A variable is a named location that stores a value. Example: marks_obtained = 84."),
    ("4. What is an identifier?",
     "An identifier is the NAME we give to a variable, function or class. Rules: start with a letter or underscore, no spaces, case-sensitive."),
    ("5. What are Python keywords?",
     "Reserved words with fixed meaning that cannot be used as names, like if, else, for, while, def, class, return, True, False, None."),
    ("6. What are operators?",
     "Symbols that perform operations: arithmetic (+ - * / % // **), comparison (> < == !=), logical (and or not), membership (in), identity (is)."),
    ("7. Difference between = and ==?",
     "= assigns a value (x = 5). == compares two values (x == 5 returns True or False)."),
    ("8. What is an if statement?",
     "It runs a block of code only when a condition is True. elif and else handle the other cases."),
    ("9. Difference between for and while loop?",
     "for repeats over a known sequence (list, range). while repeats until a condition becomes False - good for menus and validation."),
    ("10. What does break do?",
     "It stops the whole loop immediately and jumps to the code after the loop."),
    ("11. What does continue do?",
     "It skips the remaining lines of the current round and starts the next round of the loop."),
    ("12. What is pass?",
     "pass does nothing. It is a placeholder used when Python requires a statement but we have no code yet."),
    ("13. What is a list?",
     "An ordered, changeable collection. Example: categories = [\"Food\", \"Travel\"]. We can append, remove, sort."),
    ("14. What is a tuple?",
     "An ordered but UNCHANGEABLE collection. Example: GRADE_THRESHOLDS = ((90, \"A+\"), (80, \"A\"))."),
    ("15. Difference between list and tuple?",
     "List is mutable (can change), uses [ ]. Tuple is immutable (fixed), uses ( ). Tuples are faster and safer for constant data."),
    ("16. What is a set?",
     "An unordered collection with no duplicates. I use it to find unique expense categories."),
    ("17. What is a dictionary?",
     "Key-value pairs. Example: student = {\"name\": \"Aarav\", \"semester\": 3}. We access values by key."),
    ("18. What is a function?",
     "A named block of reusable code that takes parameters and may return a value, like calculate_grade(percentage)."),
    ("19. Why use functions?",
     "They avoid repetition, make code organised, easy to test and easy to explain."),
    ("20. What is a module?",
     "A Python file with functions/classes that we can import. My project has a modules package with 4 modules."),
    ("21. What is a class?",
     "A blueprint that groups data (attributes) and behaviour (methods). Example: class Student."),
    ("22. What is an object?",
     "A real instance created from a class. student_object = Student(...) creates one object."),
    ("23. What is inheritance?",
     "A child class reuses the parent class code. My Student class inherits from Person, so it gets name and greet() for free."),
    ("24. What is polymorphism?",
     "The same method call behaves differently for different objects. Person.get_summary() and Student.get_summary() have the same name but different output."),
    ("25. What is Pandas?",
     "A Python library for data analysis. Its main structure is the DataFrame - like an Excel sheet in code."),
    ("26. Why did you use Pandas?",
     "To read CSV files, filter rows, sort, group expenses by category and calculate mean/sum/max with one line each."),
    ("27. What is a DataFrame?",
     "A 2-dimensional labelled table (rows and columns) provided by Pandas."),
    ("28. What is CSV?",
     "Comma Separated Values - a plain text table format. My data lives in data/*.csv, so no database is needed."),
    ("29. How is attendance calculated?",
     "(attended_lectures * 100) / total_lectures. If it is >= 75 the student is eligible, otherwise there is a shortage."),
    ("30. How is grade calculated?",
     "Percentage = (marks_obtained * 100) / total_marks, then if/elif: 90+ = A+, 80-89 = A, 70-79 = B, 60-69 = C, 50-59 = D, below 50 = F."),
    ("31. Explain your project flow.",
     "CSV data -> manager modules load it with Pandas -> calculation functions process it -> Streamlit shows tables, metrics and charts. User input updates the DataFrames and is saved back to CSV."),
    ("32. What are the inputs and outputs?",
     "Inputs: profile form, lectures attended/held, marks, expense details. Outputs: attendance %, grades, summaries, charts, updated CSV files."),
    ("33. Where are loops used in your project?",
     "for loops in get_subjectwise_report(), get_unique_categories() and monthly totals; while loop in loops_demo.py for menu and validation."),
    ("34. Where is OOP used?",
     "modules/models.py defines Person and Student. The Student Profile page creates a real Student object and calls its methods."),
    ("35. Where is polymorphism used?",
     "Person.get_summary() is overridden by Student.get_summary(); one loop prints both - different output per object. There is a live demo on the Python Concepts page."),
    ("36. Where are sets used?",
     "expense_manager.get_unique_categories() collects unique categories; get_category_set_report() shows union, intersection and difference."),
    ("37. Where are dictionaries used?",
     "Student.marks, Student.attendance, get_profile(), get_expense_summary(), get_marks_summary() and monthly totals."),
    ("38. Why did you create custom modules?",
     "To separate logic from UI: calculations.py = maths, managers = data, models.py = classes, app.py = interface. Easy to maintain, test and explain."),
    ("39. Why did you use Streamlit?",
     "It turns Python scripts into a web app with almost no HTML/CSS, so a beginner can build a dashboard quickly and deploy it free on Streamlit Community Cloud."),
    ("40. How can this project be improved in future?",
     "Add login, a real database (SQLite), budget alerts, monthly reports, graphs with Plotly, and mobile-friendly design."),
]


def show_viva_preparation():
    page_header(
        "🎤 Viva Preparation",
        "40 questions with simple answers you can memorise and explain naturally.",
    )

    search_text = st.text_input("Search a question (type a keyword)", value="")
    shown_count = 0
    for question_text, answer_text in VIVA_QUESTIONS:  # for loop over list of tuples
        if search_text and search_text.lower() not in (question_text + answer_text).lower():
            continue  # 'continue' skips questions that do not match the search
        with st.expander(question_text):
            st.markdown(answer_text)
        shown_count += 1
    if shown_count == 0:
        st.warning("No question matched your search.")
    st.info("Total questions: " + str(len(VIVA_QUESTIONS)) + " | Shown: " + str(shown_count))


# ---------------- Main router ----------------

def main():
    selected_page = st.sidebar.radio(
        "Navigate",
        SIDEBAR_PAGES,
    )
    st.sidebar.markdown("---")
    st.sidebar.caption(
        "CampusTrack v1.0\n\nB.Tech AI/ML - Semester 3\n\nProgramming Methodology Mini Project"
    )

    if selected_page == "Home Dashboard":
        show_home_dashboard()
    elif selected_page == "Student Profile":
        show_student_profile()
    elif selected_page == "Attendance Tracker":
        show_attendance_tracker()
    elif selected_page == "Marks & Grade Analyzer":
        show_marks_analyzer()
    elif selected_page == "Expense Tracker":
        show_expense_tracker()
    elif selected_page == "Data Analysis":
        show_data_analysis()
    elif selected_page == "Python Concepts Used":
        show_python_concepts()
    else:
        show_viva_preparation()


if __name__ == "__main__":
    main()
