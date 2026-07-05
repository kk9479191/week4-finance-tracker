def monthly_report(expenses):

    total = 0

    for expense in expenses:
        total += expense.amount

    print("\n===== MONTHLY REPORT =====")
    print("Total Expenses:", total)


def category_report(expenses):

    categories = {}

    for expense in expenses:

        if expense.category not in categories:
            categories[expense.category] = 0

        categories[expense.category] += expense.amount

    print("\n===== CATEGORY REPORT =====")

    for category, amount in categories.items():
        print(category, ":", amount)