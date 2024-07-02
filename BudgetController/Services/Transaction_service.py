from Models import *
from Repositories.TransactionRepository import TransactionRepository
from Repositories.UserRepository import *

class Transaction_Service:
    def __init__(self):
        self.transaction_repository = TransactionRepository()
    
    def add_income(self, amount, phone_number, date, description, category):
        if self.transaction_repository.add_income(amount, phone_number, date, description, category):
            return True
        else:
            return False
    
    def add_expense(self, amount, phone_number, date, description, category) -> bool:
        if self.transaction_repository.add_expense(amount, phone_number, date, description, category):
            return True
        else:
            return False
    
    def check_balance(self, phone_number):
        return self.transaction_repository.check_balance(phone_number)
    
    def history_transaction(self, phone_number):
        return self.transaction_repository.history_transaction(phone_number)

    def sorted_by_date(self, phone_number):
        return self.transaction_repository.sorting_by_date(phone_number)
    
    def sorted_by_type(self, phone_number):
        return self.transaction_repository.sorting_by_type(phone_number)
    
    def filter_by_category(self, phone_number, category):
        return self.transaction_repository.filter_by_category(phone_number, category)
    
    def filter_by_type(self, phone_number):
        return self.transaction_repository.filter_by_type(phone_number)