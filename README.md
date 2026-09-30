# 🎓 CampusTrack – Student Academic & Expense Manager

A simple, beginner-friendly **Python + Streamlit mini project** for B.Tech AI/ML (Semester 3) Programming Methodology practicals. One coherent dashboard where a student manages **subjects, attendance, marks, grades and daily expenses** – all data stored in CSV files, analysed with **Pandas**, visualised with **Matplotlib**.

> Built to cover all 15 practical requirements *inside real project functionality* – not as random demo pages.

---

## 📌 Project Overview

| Item | Detail |
|---|---|
| Title | CampusTrack – Student Academic & Expense Manager |
| Type | Web dashboard (Streamlit) |
| Language | Python 3.10+ |
| Data storage | CSV files (no database) |
| Deployment target | Streamlit Community Cloud (free) |
| Cost | 100% free – no paid or external APIs |

---

## ❗ Problem Statement

Students usually track attendance in one notebook, marks in another and pocket-money expenses in a third (or nowhere). There is no single place to answer three questions quickly:

1. *Will I be eligible (attendance ≥ 75%)?*
2. *What grade am I heading towards?*
3. *Where is my money going?*

**CampusTrack** solves this with one dashboard that calculates attendance %, grades, academic status and expense analytics automatically from CSV data.

---

## 🎯 Objectives

- Manage subjects with attendance (eligible / shortage decision).
- Enter marks and auto-calculate percentage, grade and pass/fail.
- Track daily expenses by category with validation.
- Analyse everything with Pandas (filter, sort, groupby, mean, sum, max).
- Demonstrate **all core Python concepts in real working code**.
- Deploy free on Streamlit Community Cloud.

---

## ✨ Features

- 🏠 **Home Dashboard** – metrics (subjects, average marks, attendance %, total expenses) + 2 charts + status message.
- 🧑‍🎓 **Student Profile** – form that creates a real `Student` object (OOP) and calls its methods.
- 🗓️ **Attendance Tracker** – per-subject attendance %, Eligible/Shortage badges, saves to CSV.
- 📝 **Marks & Grade Analyzer** – percentage → grade (A+ to F), pass/fail, summary stats, chart.
- 💸 **Expense Tracker** – validated entries (date, category, description, amount), category totals, delete, chart.
- 🔬 **Data Analysis** – head/tail, boolean filtering, sorting, groupby, describe(), set operations, monthly totals.
- 🐍 **Python Concepts Used** – all 20 concepts with meaning, code, and *where used in this project* + live OOP/operator demos.
- 🎤 **Viva Preparation** – 40 beginner-friendly Q&A with a search box.

---

## 🛠️ Technologies Used

- **Python 3.10+** – core language
- **Streamlit** – web UI
- **Pandas** – data loading, filtering, groupby, aggregations
- **Matplotlib** – bar charts
- **CSV files** – storage (no database needed)

---

## 🐍 Python Concepts Covered

Identifiers • Keywords • Variables • Operators (all 6 families) • Conditionals • for loop • while loop • break • continue • pass • Lists • Tuples • Sets • Dictionaries • Functions • Modules • Classes • Objects • Inheritance • Polymorphism • Pandas

*(See the in-app “Python Concepts Used” page for the concept → file → example mapping, or `IMPLEMENTATION_SUMMARY.md` for the full table.)*

---

## 📁 Project Structure

```
campus_track/
│
├── app.py                  # Streamlit UI (8 pages)
├── basics_demo.py          # Practical 1-3: print, variables, types, operators
├── loops_demo.py           # Practical 5-6: while, break, continue, pass
├── verify_app.py           # Dev-only page tester (safe to delete)
│
├── data/
│   ├── students.csv        # 5 sample students
│   ├── attendance.csv      # 6 subjects
│   ├── marks.csv           # 6 subjects
│   └── expenses.csv        # 18 realistic expenses
│
├── modules/                # Custom modules (package)
│   ├── __init__.py
│   ├── calculations.py     # Grades, attendance, status functions
│   ├── student_manager.py  # Student/attendance/marks CSV + Pandas
│   ├── expense_manager.py  # Expense validation + Pandas analysis
│   └── models.py           # Person → Student (OOP)
│
├── tests/
│   ├── __init__.py
│   └── test_functions.py   # 31 unit tests
│
├── requirements.txt
├── README.md
├── VIVA_NOTES.md           # 2-min & 5-min explanations + all Q&A
├── PROJECT_REPORT.md       # Formal college report format
├── DEPLOYMENT.md           # GitHub + Streamlit Cloud steps
├── IMPLEMENTATION_SUMMARY.md
└── .gitignore
```

---

## ⚙️ How the Code Works

```
CSV files (data/*.csv)
        │  pd.read_csv()
        ▼
Manager modules (student_manager, expense_manager)   ← data layer
        │  DataFrames / dictionaries
        ▼
Calculation functions (calculations.py)              ← logic layer
        │  percentages, grades, status, validation
        ▼
OOP layer (models.py): Student object                ← objects
        │
        ▼
app.py – Streamlit UI                                ← presentation layer
        │  tables, metric cards, charts, badges
        ▼
User edits → updated DataFrame → saved back to CSV
```

- `app.py` contains **only UI code** – every calculation comes from `modules/`.
- Example import used everywhere: `from modules.calculations import calculate_grade`
- Paths are built with `os.path.join("data", "...")` → works on Windows **and** Streamlit Cloud (Linux).

---

## 💻 How to Install Python

1. Go to <https://www.python.org/downloads/>
2. Download Python 3.10 or newer.
3. **Windows:** run the installer and ✅ tick **“Add Python to PATH”** before clicking Install.
4. Verify:

```bash
python --version
# Python 3.12.x  (anything 3.10+ is fine)
```

---

## 🧪 How to Create a Virtual Environment

```bash
# inside the project folder
python -m venv venv

# activate - Windows
venv\Scripts\activate

# activate - Mac/Linux
source venv/bin/activate
```

## 📦 How to Install Dependencies

```bash
pip install -r requirements.txt
```

(`requirements.txt` contains only: streamlit, pandas, matplotlib)

---

## ▶️ How to Run

```bash
# 1. The web application
streamlit run app.py
```

```bash
# 2. Python basics demo (practicals 1-3)
python basics_demo.py

# 3. Loops demo (practicals 5-6)
python loops_demo.py

# 4. Unit tests (31 tests)
python -m unittest discover tests -v
```

Then open the shown URL (usually <http://localhost:8501>) and explore all 8 sidebar sections.

---

## 🚀 Deployment (Streamlit Community Cloud)

Full step-by-step in **[DEPLOYMENT.md](DEPLOYMENT.md)**. Short version:

1. Push the project to a **GitHub** repository.
2. Open <https://share.streamlit.io> → sign in with GitHub.
3. **Create app** → select the repo, branch `main`, main file `app.py`.
4. Click **Deploy** → done, free permanent URL like `https://yourapp.streamlit.app`.

No secrets, no database, relative paths only → deploys as-is.

---

## 🌟 Future Scope

- Login system for multiple students
- SQLite database instead of CSV
- Monthly budget alerts (e.g., “Food above ₹2000 warning”)
- Timetable and assignment-deadline tracker
- Export reports to PDF
- Mobile app version

---

## 🏁 Conclusion

CampusTrack is one coherent mini project that manages a student’s attendance, marks and expenses while genuinely demonstrating every core Python practical concept – functions, all data structures, OOP and Pandas – in code simple enough to explain in a viva. It runs locally with three commands and deploys free on Streamlit Community Cloud.
