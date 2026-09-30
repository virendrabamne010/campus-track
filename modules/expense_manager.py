"""
expense_manager.py  ->  Add, validate and analyse daily expenses
================================================================
CONCEPTS USED HERE (for viva):
* LIST       : EXPENSE_CATEGORIES, adding rows with append()
* TUPLE      : MIN_MAX_LIMITS (values that must never change)
* SET        : get_unique_categories(), set operations
* DICTIONARY : get_expense_summary() result
* FUNCTIONS  : every task is a small reusable function
* OPERATORS  : >, <=, and, or, not in
* LOOP       : for loop over rows in get_expense_summary
* Pandas     : read_csv, groupby, sort_values, sum, mean, max
"""

import os

import pandas as pd

DATA_FOLDER = os.path.join("data")
EXPENSES_CSV = os.path.join(DATA_FOLDER, "expenses.csv")

# LIST: expense categories used in the entry form.
EXPENSE_CATEGORIES = ["Food", "Travel", "Education", "Entertainment", "Other"]

# TUPLE: amount limits. Tuples cannot be changed, which is perfect
# for validation rules that must stay fixed.
MIN_MAX_LIMITS = (1, 100000)  # (minimum_amount, maximum_amount)

VALID_STATUS_MESSAGES = ("Valid", "Invalid")  # another small tuple


def load_expenses_table():
    """Read expenses.csv as a Pandas DataFrame."""
    return pd.read_csv(EXPENSES_CSV)


def save_expenses_table(expenses_df):
    """Write the expenses DataFrame back to CSV."""
    expenses_df.to_csv(EXPENSES_CSV, index=False)


def validate_expense(expense_amount, expense_category):
    """
    Check one expense. Returns (is_valid, message).
    Demonstrates comparison + logical operators and tuples.
    """
    minimum_amount, maximum_amount = MIN_MAX_LIMITS  # tuple unpacking

    # isinstance check first, so a text amount can never crash the maths below
    if not isinstance(expense_amount, (int, float)):
        return False, "Amount must be a number"

    # 'not in' membership operator checks the category list
    if expense_category not in EXPENSE_CATEGORIES:
        return False, "Category is not in the allowed list"

    # 'and' combines two comparison conditions
    if expense_amount < minimum_amount or expense_amount > maximum_amount:
        return False, "Amount must be between 1 and 100000"

    return True, VALID_STATUS_MESSAGES[0]  # "Valid"


def add_expense(expense_date, expense_category, expense_description, expense_amount, expenses_df):
    """Add one validated expense row to the DataFrame and CSV."""
    is_valid, validation_message = validate_expense(expense_amount, expense_category)
    if not is_valid:
        return expenses_df, validation_message

    new_row = pd.DataFrame(
        [[expense_date, expense_category, expense_description, expense_amount]],
        columns=["date", "category", "description", "amount"],
    )
    expenses_df = pd.concat([expenses_df, new_row], ignore_index=True)
    save_expenses_table(expenses_df)
    return expenses_df, "Expense added successfully"


def get_expense_summary(expenses_df):
    """Return totals as a dictionary using Pandas aggregations."""
    expense_summary = {
        "total_expenses": round(expenses_df["amount"].sum(), 2),
        "average_expense": round(expenses_df["amount"].mean(), 2),
        "highest_expense": round(expenses_df["amount"].max(), 2),
        "lowest_expense": round(expenses_df["amount"].min(), 2),
        "number_of_expenses": len(expenses_df),
    }
    return expense_summary


def get_category_totals(expenses_df):
    """GROUP BY category -> Series of totals, sorted high to low."""
    return expenses_df.groupby("category")["amount"].sum().sort_values(ascending=False)


def get_highest_expense_row(expenses_df):
    """Return the single costliest expense as a Series (row)."""
    return expenses_df.loc[expenses_df["amount"].idxmax()]


def get_unique_categories(expenses_df):
    """
    SET: unique category names from the data.
    Duplicates, if any, disappear automatically in a set.
    """
    unique_category_set = set()
    for expense_category in expenses_df["category"]:  # for loop over the column
        unique_category_set.add(expense_category)     # set add()
    return unique_category_set


def get_category_set_report(expenses_df):
    """
    Demonstrate set operations with real data:
      union        -> all categories seen anywhere (data + allowed list)
      intersection -> categories present in BOTH data and allowed list
      difference   -> allowed categories never used yet
    """
    data_category_set = get_unique_categories(expenses_df)
    allowed_category_set = set(EXPENSE_CATEGORIES)  # list converted to set
    report = {
        "union": data_category_set | allowed_category_set,
        "intersection": data_category_set & allowed_category_set,
        "difference": allowed_category_set - data_category_set,
    }
    return report


def filter_expenses_by_category(expenses_df, selected_category):
    """Boolean filtering: df[df["category"] == value]."""
    return expenses_df[expenses_df["category"] == selected_category]


def get_expensive_expenses(expenses_df, threshold_amount):
    """Expenses above a threshold -> df[df["amount"] > value]."""
    return expenses_df[expenses_df["amount"] > threshold_amount]


def get_monthly_totals(expenses_df):
    """
    Group expenses by month using a for loop + dictionary
    (beginner-friendly alternative to datetime grouping).
    Key format: "2026-09".
    """
    monthly_totals = {}
    for row in expenses_df.itertuples(index=False):
        month_key = str(row.date)[:7]  # first 7 chars of "2026-09-02"
        if month_key in monthly_totals:  # 'in' membership on dictionary keys
            monthly_totals[month_key] += row.amount
        else:
            monthly_totals[month_key] = row.amount
    return monthly_totals


def remove_expense_by_index(row_index, expenses_df):
    """Delete one row by position; returns updated DataFrame."""
    expenses_df = expenses_df.drop(index=row_index).reset_index(drop=True)
    save_expenses_table(expenses_df)
    return expenses_df
