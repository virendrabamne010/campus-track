"""
modules package
===============
A FOLDER with __init__.py becomes a Python package.
That is why app.py can write:

    from modules.calculations import calculate_grade

Custom modules keep the project organised:
    calculations.py     -> pure maths/grade logic (no UI)
    student_manager.py  -> student, attendance, marks CSV handling
    expense_manager.py  -> expense CSV handling and analysis
    models.py           -> OOP classes (Person, Student)
"""
