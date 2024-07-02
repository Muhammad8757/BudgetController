from Models import *
from Repositories.UserRepository import UserRepository
from Repositories.UserRepository import *



class User_Service:
    def __init__(self):
        self.user_repository = UserRepository()

    def CreateUser(self, user: User) -> bool:    
        return self.user_repository.create_user(user)
        
    def CheckUser(self, phone_number, password) -> bool:
        if(self.user_repository.check_user(phone_number, password)):
            return True
        else:
            return False
    
    def get_user(self, phone_user, password):
        user = self.user_repository.get_user(phone_user, password)
        return user
    
    def update_user(self, phone_number, password, update_password) -> bool:
        if self.user_repository.update_user(phone_number, password, update_password):
            return True
        else:
            return False
    
    def delete_user(self, phone_user, password) -> bool:
        if self.user_repository.delete_user(phone_user, password):
            return True
        else:
            return False