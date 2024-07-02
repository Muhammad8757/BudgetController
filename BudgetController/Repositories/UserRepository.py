import hashlib
import sqlite3
from Models import User
from Repositories.Functions import sql_request_save, sql_request_fetcone

class UserRepository:

    def create_user(self, user: User):
        try:
            hash_password = hasher(user.password)
            if sql_request_save("INSERT INTO user (name, phone_number, password) VALUES (?, ?, ?)", 
                               (user.name, user.phone_number, hash_password)) is not None:
                return True
        except sqlite3.IntegrityError as e:
            print(f"Произошла ошибка целостности данных: {e}")
            return False
        except sqlite3.Error as e:
            print(f"Произошла ошибка: {e}")
            return False

    def check_user(self, phone_user: int, password: str) -> bool:
        try:
            hash_password = hasher(password)
            if sql_request_fetcone("SELECT * FROM user WHERE phone_number = ? AND password = ?", (phone_user, hash_password)) is not None:
                return True
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return False
    
    def get_user(self, phone_user: int, password: str) -> User:
        try:
            hash_password = hasher(password)
            user = sql_request_fetcone("SELECT name, phone_number FROM user WHERE phone_number = ? AND password = ?", (phone_user, hash_password))
            if user is not None:
                return (user[0], user[1])
            else:
                return None
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def update_user(self, phone_user: int, password: str, update_password: str) -> bool:
        try:
            hash_old_password = hasher(password)
            hash_new_password = hasher(update_password)
            if UserRepository.check_user(self, phone_user, password):
                if sql_request_save("UPDATE user SET password = ? WHERE phone_number = ? AND password = ? ", 
                    (hash_new_password, phone_user, hash_old_password )) != 0:
                    return True
                else:
                    return False
                    
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def delete_user(self, phone_user: int, password: str) -> bool:
        try:
            hash_password = hasher(password)
            if UserRepository.check_user(self, phone_user, password):
                if sql_request_save("DELETE FROM user WHERE phone_number = ? AND password = ? ", (phone_user, hash_password)) != 0:
                    return True
                else:
                    return False
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

def hasher(password):
    password_bytes = password.encode()
    hash = hashlib.md5(password_bytes)
    return hash.hexdigest()