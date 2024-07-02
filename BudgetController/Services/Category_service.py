from Models import *
from Repositories.Category_Repository import Category_Repository
from Repositories.UserRepository import *

class Category_Service:
    def __init__(self):
        self.repository = Category_Repository()
    
    def get_category(self):
        return self.repository.get_category()