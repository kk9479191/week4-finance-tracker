from finance_tracker.expense import Expense
class ExpenseManager:

    def __init__(self):
        self.expenses = []

    def add_expense(self, date, amount, category, description):

        expense = Expense(
            date,
            amount,
            category,
            description
        )

        self.expenses.append(expense)

    def get_all_expenses(self):
        return self.expenses

    def search_expense(self, keyword):

        result = []

        for expense in self.expenses:

            if keyword.lower() in expense.category.lower():
                result.append(expense)

        return result