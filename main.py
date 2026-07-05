from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.file_handler import save_expenses, load_expenses
from finance_tracker.reports import monthly_report, category_report


def main():

    manager = ExpenseManager()

    data = load_expenses()

    for item in data:
        manager.add_expense(
            item["date"],
            item["amount"],
            item["category"],
            item["description"]
        )

    while True:

        print("\n========================")
        print("PERSONAL FINANCE TRACKER")
        print("========================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Monthly Report")
        print("5. Category Report")
        print("0. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":

            date = input("Date: ")
            amount = float(input("Amount: "))
            category = input("Category: ")
            description = input("Description: ")

            manager.add_expense(
                date,
                amount,
                category,
                description
            )

            expenses_data = []

            for expense in manager.get_all_expenses():
                expenses_data.append(expense.to_dict())

            save_expenses(expenses_data)

            print("Expense Added Successfully")

        elif choice == "2":

            expenses = manager.get_all_expenses()

            print("\n===== ALL EXPENSES =====")

            for expense in expenses:
                print(
                    expense.date,
                    expense.amount,
                    expense.category,
                    expense.description
                )

        elif choice == "3":

            keyword = input("Enter Category: ")

            result = manager.search_expense(keyword)

            for expense in result:
                print(
                    expense.date,
                    expense.amount,
                    expense.category,
                    expense.description
                )

        elif choice == "4":

            monthly_report(
                manager.get_all_expenses()
            )

        elif choice == "5":

            category_report(
                manager.get_all_expenses()
            )

        elif choice == "0":

            print("Thank You")
            break

        else:
            print("Invalid Choice")