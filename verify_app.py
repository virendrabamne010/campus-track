"""
verify_app.py - temporary validation harness (safe to delete).
Runs app.py once per sidebar page using streamlit.testing.AppTest
and prints which pages raise exceptions.
"""
from streamlit.testing.v1 import AppTest

PAGES = [
    "Home Dashboard",
    "Student Profile",
    "Attendance Tracker",
    "Marks & Grade Analyzer",
    "Expense Tracker",
    "Data Analysis",
    "Python Concepts Used",
    "Viva Preparation",
]

failures = 0
for page_name in PAGES:
    at = AppTest.from_file("app.py", default_timeout=120)
    at.run()
    at.radio[0].set_value(page_name)
    at.run()
    if at.exception:
        failures += 1
        print("FAIL:", page_name)
        for exc in at.exception:
            print("   ", exc.message)
    else:
        print("PASS:", page_name)

print("\nRESULT:", "ALL PAGES OK" if failures == 0 else str(failures) + " PAGES FAILED")
