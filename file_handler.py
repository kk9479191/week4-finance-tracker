import json
import os

FILE_PATH = "data/expenses.json"


def load_expenses():
    try:
        if not os.path.exists(FILE_PATH):
            return []

        with open(FILE_PATH, "r") as file:
            return json.load(file)

    except Exception:
        return []


def save_expenses(expenses):
    try:
        with open(FILE_PATH, "w") as file:
            json.dump(expenses, file, indent=4)

    except Exception as e:
        print("Error saving data:", e)