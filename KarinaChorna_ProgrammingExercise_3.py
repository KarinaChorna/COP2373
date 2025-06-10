# Karina Chorna
# Chapter 3: Exercise 3
# The purpose of this code is to determine the user's total monthly expenses as well as the highest and lowest expense.

from functools import reduce

# prompt the user for the amount and type of expense, making sure a valid number is entered
def get_expenses():
    expenses = []
    while True:
        expense_type = input("Enter the type of expense (or type 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        try:
            amount = float(input(f"Enter the amount for {expense_type}: $"))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Please enter a valid number for the amount.")
    return expenses

def main():
    expenses = get_expenses()

    if not expenses:
        print("No expenses were provided.")
        return

    # calculate the total expenses
    total = reduce(lambda acc, item: acc + item[1], expenses, 0)

    # determine the highest expense
    highest = reduce(lambda a, b: a if a[1] > b[1] else b, expenses)

    # determine the lowest expense
    lowest = reduce(lambda a, b: a if a[1] < b[1] else b, expenses)

    # display the results
    print("\nExpense Summary:")
    print(f"Total Expense: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} at ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} at ${lowest[1]:.2f}")


if __name__ == "__main__":
    main()
