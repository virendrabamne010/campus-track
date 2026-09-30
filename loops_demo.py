"""
loops_demo.py  ->  while loop + loop control (break, continue, pass)
====================================================================
Run it from the terminal INSIDE the project folder:

    python loops_demo.py

WHAT IT SHOWS (for viva):
* while loop: a small menu that repeats until the user chooses Exit
* break    : leave the loop immediately (Exit / invalid choice stop)
* continue : skip the rest of this round and start the next round
* pass     : a placeholder that does nothing (used where code must go later)
* validation: keep asking until the user enters a valid number
"""

# A tuple of fixed menu options (tuples never change).
MENU_OPTIONS = ("1", "2", "3", "4")


def print_menu():
    """Display the demo menu (called again and again by the while loop)."""
    print("\n===== LOOPS DEMO MENU =====")
    print("1. Counting with while loop")
    print("2. break demonstration")
    print("3. continue demonstration")
    print("4. Exit")
    print("===========================")


def counting_with_while():
    """Count 1 to 5 with a while loop (counting + controlled repetition)."""
    counter = 1
    while counter <= 5:            # condition checked every round
        print("Count is:", counter)
        counter += 1               # without this line the loop never ends!
    print("While loop finished.")


def break_demonstration():
    """
    break stops the loop at once.
    Here we search for the first subject with marks below 60 and stop.
    """
    marks_list = [84, 72, 58, 91, 45]
    for marks_obtained in marks_list:
        if marks_obtained >= 60:
            print(marks_obtained, "is a pass, keep checking")
        else:
            print(marks_obtained, "is below 60 -> BREAK! stop searching")
            break                  # jump out of the loop immediately
    print("Loop ended because of break.")


def continue_demonstration():
    """
    continue skips the rest of THIS round only.
    Here invalid (negative) expenses are skipped, valid ones are added.
    """
    expense_amounts = [120, -50, 200, 0, 85]
    valid_total = 0
    for expense_amount in expense_amounts:
        if expense_amount <= 0:
            print("Skipping invalid amount:", expense_amount)
            continue               # jump to the next round of the loop
        valid_total += expense_amount
        print("Added", expense_amount, "-> running total:", valid_total)
    print("Total of valid expenses:", valid_total)


def pass_demonstration():
    """
    pass does NOTHING - it just fills an empty block so the code runs.
    Python does not allow truly empty if/for/def blocks.
    """
    future_feature = "notifications"
    if future_feature == "notifications":
        pass                       # TODO: write this feature in future scope
    print("pass used as a placeholder - program did not crash.")

    def not_written_yet():
        pass                       # an empty function body also needs pass

    not_written_yet()
    print("Empty function with pass also works fine.")


def validate_number_input():
    """
    VALIDATION with while: keep asking until input is correct.
    (Uses a ready-made list of attempts so it cannot hang in tests.)
    """
    typed_values = ["abc", "-3", "7"]   # pretend a user typed these
    attempt_index = 0
    while attempt_index < len(typed_values):
        current_text = typed_values[attempt_index]
        attempt_index += 1
        if not current_text.isdigit():          # letters are invalid
            print("'", current_text, "' is not a number, try again")
            continue
        number_value = int(current_text)
        if number_value <= 0:                    # negative/zero invalid
            print("'", current_text, "' must be positive, try again")
            continue
        print("Valid number accepted:", number_value)
        break                                    # stop once valid input found
    return number_value


def menu_loop():
    """
    The classic WHILE-LOOP MENU:
    repeat -> show menu -> read choice -> act -> repeat,
    until the user selects Exit (break).
    """
    running = True
    while running:                 # 'running' controls the whole loop
        print_menu()
        # Simulated choices (in a real terminal you would use input()):
        simulated_choices = ["1", "2", "3", "4"]
        for choice in simulated_choices:
            if choice not in MENU_OPTIONS:      # membership test
                print("Invalid choice:", choice)
                continue
            if choice == "1":
                counting_with_while()
            elif choice == "2":
                break_demonstration()
            elif choice == "3":
                continue_demonstration()
            elif choice == "4":
                print("Exit selected -> break ends the while loop.")
                running = False
                break               # leave the for loop of choices
        running = False             # one full pass finished for the demo
    print("Menu loop closed. Goodbye!")


# ---------------- main program ----------------

if __name__ == "__main__":
    counting_with_while()
    break_demonstration()
    continue_demonstration()
    pass_demonstration()
    print()
    validate_number_input()
    print()
    menu_loop()
