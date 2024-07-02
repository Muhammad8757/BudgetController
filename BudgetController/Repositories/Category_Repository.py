import sys
sys.path.append(r"D:\mami\Python\BudgetController")
import sqlite3
from Repositories.Functions import sql_request_fetchall


class Category_Repository:

    def get_category(self):
        try:
            categories = sql_request_fetchall("SELECT name FROM category",)
            if categories is not None:
                return categories
            else:
                print("No categories found.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
