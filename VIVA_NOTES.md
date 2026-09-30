# 🎤 CampusTrack – Viva Notes

Everything you need to explain this project confidently in your viva.

---

## ⏱️ 2-Minute Project Explanation (memorise this)

> "Sir/Madam, my mini project is **CampusTrack – a Student Academic and Expense Manager**, built with **Python, Streamlit and Pandas**.
> Students track attendance, marks and expenses separately, so my project gives **one dashboard** for all three.
> It has **8 sections**: a home dashboard with summary cards and charts, a student profile, an attendance tracker that calculates percentage and shows **Eligible or Shortage** at the 75% rule, a marks analyzer that converts marks into **grades A+ to F**, an expense tracker with validation, a Pandas data-analysis page, and two educational pages – Python concepts used and viva preparation.
> Data is stored in **CSV files**, loaded with **pd.read_csv()** and analysed with filtering, sorting and **groupby**. The code is split into **custom modules**: calculations, two data managers and an OOP module where **Student inherits from Person** and **polymorphism** is shown through `get_summary()`.
> The whole app is deployed free on **Streamlit Community Cloud**."

---

## ⏱️ 5-Minute Project Explanation (add these details)

Start with the 2-minute version, then continue:

**Flow of the project:**
> "The flow is: CSV data → manager modules load it with Pandas → calculation functions process it → Streamlit displays tables, metric cards and charts. When the user adds attendance, marks or an expense, the DataFrame is updated and saved back to the CSV file, so data is persistent even without a database."

**Architecture (why modules):**
> "I separated the project into layers. `app.py` is only the UI. `modules/calculations.py` has pure functions like `calculate_grade()` and `calculate_attendance()` – no UI code. `student_manager.py` and `expense_manager.py` handle CSV reading/writing with Pandas. `models.py` has the OOP classes. This is **modularity** – easy to test, debug and explain."

**OOP example:**
> "In `models.py`, `Person` is the parent class with `name`, `city` and `greet()`. `Student` inherits from it using `super().__init__()` and adds `roll_number`, `branch`, `semester`. Both classes have `get_summary()` – the child **overrides** it, so one loop over `[person, student]` prints two different outputs. That is **polymorphism**."

**Data structures example:**
> "I use a **list** for expense categories, a **tuple** for grade thresholds `(90, 'A+')` because grades must never change, a **set** for unique expense categories with union/intersection/difference, and **dictionaries** for the student profile and summaries. Attendance per subject is stored as a tuple `(attended, total)`."

**Testing:**
> "There are **31 unit tests** in `tests/test_functions.py` using the `unittest` module, covering attendance, all grade boundaries, validation and OOP. All pass."

---

## 🐍 Python Concept Explanations (one-liners for viva)

| Concept | What to say |
|---|---|
| Variable | A named location that stores a value, e.g. `marks_obtained = 84` |
| Identifier | The name given to a variable/function/class – letters/underscore, case-sensitive |
| Keyword | Reserved word with fixed meaning: `if, for, def, class, return, True…` |
| Operators | Symbols that operate on values – arithmetic, comparison, logical, membership, identity, assignment |
| if/elif/else | Decision-making; my `calculate_grade()` uses 5 branches |
| for loop | Repeats over a sequence – I loop over subject dictionaries |
| while loop | Repeats while a condition is True – my menu simulation and input validation |
| break | Exits the loop immediately – stop searching when a fail is found |
| continue | Skips to the next iteration – skip invalid expense amounts |
| pass | Does nothing; placeholder for future code |
| List | Ordered & mutable – `["Food", "Travel"]`, supports append/sort |
| Tuple | Ordered & immutable – `(90, "A+")`, safer for fixed values |
| Set | Unordered, no duplicates – `set()` + union/intersection/difference |
| Dictionary | Key-value pairs – `student = {"name": "Aarav"}`, keys()/values()/items()/get() |
| Function | Reusable block with parameters and return value |
| Module | A `.py` file you can import – my `modules` package has 4 |
| Class | Blueprint of data + methods |
| Object | Real instance of a class – `student_object = Student(...)` |
| Inheritance | Child reuses parent – `class Student(Person)` |
| Polymorphism | Same method, different behaviour – `get_summary()` overridden |
| Pandas | Data analysis library; DataFrame = table in memory |

---

## ❓ Viva Questions & Answers (all 40)

**1. What is Python?**
A simple, high-level, interpreted programming language with clean syntax, dynamically typed, and supported by thousands of libraries.

**2. Why did you use Python?**
Simple syntax, powerful data libraries (Pandas, Streamlit), and it is the main language of AI/ML, my branch.

**3. What is a variable?**
A named location that stores a value. Example: `marks_obtained = 84`.

**4. What is an identifier?**
The name of a variable, function or class. Rules: start with letter/underscore, no spaces, case-sensitive.

**5. What are Python keywords?**
Reserved words with predefined meaning that cannot be used as identifiers: `if, else, for, while, def, class, return, import, True, False, None`, etc.

**6. What are operators?**
Symbols that perform operations: `+ - * / % // **`, comparisons `> < >= <= == !=`, logical `and or not`, membership `in / not in`, identity `is / is not`.

**7. Difference between = and ==?**
`=` assigns a value; `==` compares two values and returns True/False.

**8. What is an if statement?**
Executes a block only when a condition is True. `elif` checks more conditions, `else` covers the rest.

**9. Difference between for and while loop?**
`for` iterates over a known sequence; `while` repeats until a condition becomes False (menus, validation).

**10. What does break do?**
Terminates the loop immediately; execution continues after the loop.

**11. What does continue do?**
Skips the remaining statements of the current iteration and starts the next one.

**12. What is pass?**
A null statement – does nothing. Used as a placeholder where a statement is syntactically required.

**13. What is a list?**
An ordered, mutable collection: `categories = ["Food", "Travel"]`. Supports append, insert, remove, pop, sort, reverse.

**14. What is a tuple?**
An ordered, immutable collection: `GRADE_THRESHOLDS = ((90, "A+"), (80, "A"))`.

**15. Difference between list and tuple?**
List `[ ]` is mutable and slightly slower; tuple `( )` is immutable, faster, and protects constant data.

**16. What is a set?**
An unordered collection with unique elements: `set()`, operations add, remove, discard, union, intersection, difference.

**17. What is a dictionary?**
Key-value pairs: `student = {"name": "Aarav", "semester": 3}`. Access by key with `get()`.

**18. What is a function?**
A named reusable block of code with parameters and usually a return value.

**19. Why use functions?**
Avoid repetition, organise code, make testing and debugging easier.

**20. What is a module?**
A Python file containing functions/classes that can be imported. My project has `modules/calculations.py`, `student_manager.py`, `expense_manager.py`, `models.py`.

**21. What is a class?**
A blueprint that groups attributes (data) and methods (behaviour).

**22. What is an object?**
An instance of a class with its own data: `student_object = Student("Aarav", "CS2301", "AI/ML", 3)`.

**23. What is inheritance?**
A child class acquires the properties and methods of a parent class. `Student(Person)` reuses `name`, `city`, `greet()`.

**24. What is polymorphism?**
"Many forms" – the same method call behaves differently per object. `Person.get_summary()` vs `Student.get_summary()`.

**25. What is Pandas?**
A Python library for data manipulation and analysis; its main structure is the DataFrame.

**26. Why did you use Pandas?**
To read/write CSVs, filter rows, sort, groupby category, and compute sum/mean/max with single lines.

**27. What is a DataFrame?**
A 2-dimensional labelled table with rows and columns, like an Excel sheet in code.

**28. What is CSV?**
Comma Separated Values – a plain-text table format. My data lives in `data/*.csv`.

**29. How is attendance calculated?**
`(attended_lectures * 100) / total_lectures`. If ≥ 75 → eligible, else shortage. Function: `calculate_attendance()`.

**30. How is grade calculated?**
Percentage → if/elif chain: 90+ A+, 80–89 A, 70–79 B, 60–69 C, 50–59 D, below 50 F. Function: `calculate_grade()`.

**31. Explain your project flow.**
CSV → Pandas load → calculation functions → Streamlit UI (tables/metrics/charts). User input updates DataFrames and is saved back to CSV.

**32. What are the inputs and outputs?**
Inputs: profile details, lectures attended/held, marks, expense entries. Outputs: attendance %, grades, summaries, charts, updated CSV files.

**33. Where are loops used?**
`for`: `get_subjectwise_report()`, `get_unique_categories()`, monthly totals, building charts. `while`: `loops_demo.py` menu and validation.

**34. Where is OOP used?**
`modules/models.py` – `Person` and `Student` classes; the Student Profile page creates a real object and calls `display_info()`, `get_profile()`, `calculate_performance()`.

**35. Where is polymorphism used?**
`get_summary()` is defined in `Person` and overridden in `Student`; one loop prints both outputs. Live demo on the Python Concepts page.

**36. Where are sets used?**
`get_unique_categories()` and `get_category_set_report()` (union, intersection, difference) in `expense_manager.py`.

**37. Where are dictionaries used?**
`Student.marks`, `Student.attendance`, `get_profile()`, `get_expense_summary()`, `get_marks_summary()`, monthly totals.

**38. Why did you create custom modules?**
Separation of concerns: UI separate from logic and data, easier testing, cleaner imports like `from modules.calculations import calculate_grade`.

**39. Why did you use Streamlit?**
It converts Python scripts into interactive web apps without HTML/CSS, and deploys free on Streamlit Community Cloud.

**40. How can this project be improved in future?**
Login, SQLite database, budget alerts, PDF reports, timetable/deadline tracker, Plotly interactive charts.

---

## 💬 What to Say When Mam Asks "Where is this concept used?"

| Concept | Exact answer |
|---|---|
| Operators | "`calculate_attendance()` uses `*`, `/` and `>=`; `validate_expense()` uses `not in`, `or`, `<=`" |
| Conditionals | "`calculate_grade()` is a full if/elif/else chain" |
| for loop | "`get_subjectwise_report()` loops over `marks_dictionary.items()`" |
| while loop | "`loops_demo.py` has a menu that repeats with while" |
| break/continue | "break stops a search in `loops_demo.py`; my viva search page uses `continue` to skip non-matching questions" |
| Lists | "`EXPENSE_CATEGORIES` in expense_manager.py" |
| Tuples | "`GRADE_THRESHOLDS` and attendance stored as `(attended, total)`" |
| Sets | "`get_unique_categories()` returns a set; `get_category_set_report()` shows union/intersection/difference" |
| Dictionaries | "`get_expense_summary()` returns a dictionary of totals" |
| Functions | "9 reusable functions in calculations.py alone, each with parameters and return" |
| Modules | "`app.py` starts with `from modules.calculations import ...`" |
| Class/Object | "Student Profile page: `student_object = Student(...)`" |
| Inheritance | "`class Student(Person)` with `super().__init__()`" |
| Polymorphism | "`get_summary()` overridden; `demo_polymorphism()` prints both" |
| Pandas | "`pd.read_csv()`, `groupby`, `sort_values`, `mean`, `sum`, `idxmax` in the manager modules" |

---

## 🧾 Important Code Snippets (know these by heart)

```python
# Attendance (arithmetic + comparison)
def calculate_attendance(attended_lectures, total_lectures):
    if total_lectures == 0:
        return 0.0
    return round((attended_lectures * 100) / total_lectures, 2)
```

```python
# Grade (if / elif / else)
def calculate_grade(percentage):
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
```

```python
# Set (unique categories)
def get_unique_categories(expenses_df):
    unique_category_set = set()
    for expense_category in expenses_df["category"]:
        unique_category_set.add(expense_category)
    return unique_category_set
```

```python
# Inheritance + Polymorphism
class Person:
    def get_summary(self):
        return "Person: " + self.name

class Student(Person):
    def get_summary(self):
        return "Student: " + self.name + " | " + str(self.roll_number)
```

```python
# Pandas groupby
category_totals = expenses_df.groupby("category")["amount"].sum().sort_values(ascending=False)
```
