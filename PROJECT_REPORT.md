# 📘 PROJECT REPORT

## CampusTrack – Student Academic & Expense Manager

**Submitted by:** [Your Name], B.Tech AI/ML, Semester 3
**Subject:** Programming Methodology (Practical Mini Project)

---

## 1. Introduction

CampusTrack is a Python-based web application that helps a college student manage academic and financial information in one place. It tracks subject-wise attendance, marks with automatic grade calculation, and daily expenses with category-wise analysis. The application is built with Streamlit for the interface and Pandas for data handling, storing all records in simple CSV files so no database is required.

---

## 2. Problem Statement

Students maintain attendance, marks and expense information in different places (notebooks, memory, or not at all). As a result they cannot quickly answer: *Am I eligible as per the 75% attendance rule? What grade am I heading towards? Where is my money going?* A single tool is needed that records this data once and automatically produces eligibility status, grades and expense analytics.

---

## 3. Objectives

1. Maintain subject-wise attendance and evaluate eligibility (≥ 75%).
2. Record marks and automatically compute percentage, grade (A+–F) and pass/fail.
3. Record daily expenses with validation and category-wise totals.
4. Provide Pandas-based analysis: filtering, sorting, grouping, aggregations.
5. Visualise attendance, marks and expenses with charts.
6. Demonstrate all core Python practical concepts inside working code.
7. Deploy the application free on Streamlit Community Cloud.

---

## 4. Existing System

Currently students use paper notebooks or spreadsheets. Percentages, grades and totals must be calculated manually, which is slow and error-prone. There is no automatic eligibility check, no grade mapping, and expense tracking is usually abandoned after a few days. Existing apps are either too complex, need installation, or do not combine academics with expenses.

---

## 5. Proposed System

CampusTrack is a single web dashboard where the student enters data once:

- Attendance % and Eligible/Shortage status are computed automatically.
- Marks are converted to percentage, grade and pass/fail instantly.
- Expenses are validated (category list, amount limits) and summarised by category and month.
- All records persist in CSV files and every view is computed with Pandas.
- The system needs only Python – no database, no internet API, no installation for end users (it runs in the browser via Streamlit Community Cloud).

---

## 6. Tools & Technologies

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core programming language |
| Streamlit | Web UI framework |
| Pandas | DataFrames, filtering, groupby, aggregations |
| Matplotlib | Bar charts |
| CSV files | Persistent storage |
| GitHub + Streamlit Community Cloud | Hosting and deployment |
| unittest | Unit testing |

---

## 7. System Design

```
┌─────────────────────────────────────────────┐
│                USER (Browser)               │
└──────────────────┬──────────────────────────┘
                   │ streamlit run app.py
┌──────────────────▼──────────────────────────┐
│            PRESENTATION LAYER               │
│  app.py – 8 pages, forms, charts, metrics   │
└──────────────────┬──────────────────────────┘
┌──────────────────▼──────────────────────────┐
│               LOGIC LAYER                   │
│  modules/calculations.py                    │
│  attendance %, grades, status, operators    │
└──────────────────┬──────────────────────────┘
┌──────────────────▼──────────────────────────┐
│                OOP LAYER                    │
│  modules/models.py – Person → Student       │
└──────────────────┬──────────────────────────┘
┌──────────────────▼──────────────────────────┐
│                DATA LAYER                   │
│  modules/student_manager.py                 │
│  modules/expense_manager.py                 │
│  pd.read_csv / to_csv                       │
└──────────────────┬──────────────────────────┘
┌──────────────────▼──────────────────────────┐
│         data/*.csv (persistent storage)     │
└─────────────────────────────────────────────┘
```

**Data flow:** user input → DataFrame update → calculations → UI refresh → CSV save.

---

## 8. Module Description

| Module | Responsibility |
|---|---|
| `app.py` | All UI pages: dashboard, profile, attendance, marks, expenses, analysis, concepts, viva |
| `modules/calculations.py` | Pure functions: `calculate_attendance`, `calculate_grade`, `calculate_average`, `get_academic_status`, `get_subjectwise_report` |
| `modules/student_manager.py` | Students/attendance/marks CSV I/O, Pandas summaries, object building |
| `modules/expense_manager.py` | Expense validation, add/delete, groupby analysis, set operations |
| `modules/models.py` | OOP: `Person` (parent), `Student` (child), polymorphism demo |
| `basics_demo.py` | Teaching demo: variables, types, operators, keywords |
| `loops_demo.py` | Teaching demo: while, break, continue, pass, validation |
| `tests/test_functions.py` | 31 unit tests for all logic functions |

---

## 9. Python Concepts Used

| # | Concept | Where in project |
|---|---|---|
| 1 | Identifiers/Variables | All modules (`student_name`, `marks_obtained`…) |
| 2 | Keywords | Every module (`if, def, return, class…`) |
| 3 | Operators (all 6 families) | calculations.py, expense_manager.py, basics_demo.py |
| 4 | Conditionals | `calculate_grade()`, eligibility badges |
| 5 | for loop | `get_subjectwise_report()`, category loops, charts |
| 6 | while loop | `loops_demo.py` menu + validation |
| 7 | break/continue/pass | `loops_demo.py`; `continue` in viva search filter |
| 8 | Lists | `EXPENSE_CATEGORIES`, marks lists |
| 9 | Tuples | `GRADE_THRESHOLDS`, `(attended, total)` pairs |
| 10 | Sets | `get_unique_categories()`, union/intersection/difference |
| 11 | Dictionaries | Student data, summaries, monthly totals |
| 12 | Functions | 20+ reusable functions with parameters/returns |
| 13 | Modules | `modules` package with `__init__.py` |
| 14 | Class/Object | `Student` objects on the Profile page |
| 15 | Inheritance | `class Student(Person)` with `super().__init__()` |
| 16 | Polymorphism | `get_summary()` overridden; live demo page |
| 17 | Pandas | read_csv, head/tail, filtering, sort_values, groupby, mean/sum/max, describe |

---

## 10. Implementation

**Key implementation details:**

1. **Attendance** – `(attended * 100) / total`, rounded to 2 decimals; division-by-zero guarded.
2. **Grades** – if/elif chain plus an alternative tuple-loop implementation (`calculate_grade_with_tuple`) proving the same result.
3. **Validation** – `validate_expense()` checks the type first (`isinstance`), then category membership (`not in`), then amount range (`< minimum or > maximum`).
4. **Persistence** – `pd.to_csv(index=False)` after every update; paths built with `os.path.join` so they work on Windows and Linux (cloud).
5. **OOP** – `Student` extends `Person`; `super().__init__()` reuses the parent constructor; `get_summary()` demonstrates overriding.
6. **Charts** – one shared `bar_chart_matplotlib()` helper renders attendance, marks and expense charts.
7. **Testing** – `tests/test_functions.py` (unittest) covers all grade boundaries, attendance formulas, validation failures and OOP behaviour.

---

## 11. Results

- All 8 dashboard sections work without errors (verified with Streamlit AppTest).
- 31/31 unit tests pass.
- Attendance eligibility correctly flags subjects below 75%.
- Grades match the specified scale exactly at every boundary (90, 80, 70, 60, 50).
- Expense validation rejects zero/negative/oversized amounts and unknown categories.
- App runs with `streamlit run app.py` and shows HTTP 200 on the local server.

---

## 12. Advantages

- One place for attendance, marks and expenses.
- Automatic, error-free calculations.
- No database or installation needed – CSV + browser.
- Free cloud deployment with a permanent shareable link.
- Educational pages make it a self-explaining project for viva.
- Clean modular code, easy to extend.

---

## 13. Limitations

- CSV storage suits one user; not built for concurrent multi-user edits.
- No login/authentication (by design, to keep it simple).
- Expense data can be edited by anyone with file access.
- Charts are basic matplotlib bars, not interactive drill-downs.
- Profile edits are session-only and not saved to `students.csv`.

---

## 14. Future Scope

- Login system for multiple students with separate data.
- SQLite/MySQL database for robust persistence.
- Monthly budget limits with alert notifications.
- Timetable and assignment-deadline tracking.
- PDF report export for parents/mentors.
- Interactive Plotly charts and mobile app version.

---

## 15. Conclusion

CampusTrack successfully combines academic tracking (attendance, marks, grades) and personal finance (expenses) into one coherent, beginner-friendly dashboard. It satisfies every Programming Methodology practical requirement – operators, conditionals, loops, data structures, functions, modules, OOP and Pandas – inside genuine application code rather than artificial demos. The project runs locally with three commands, passes 31 unit tests, and deploys free on Streamlit Community Cloud, making it both a useful tool and a strong academic submission.
