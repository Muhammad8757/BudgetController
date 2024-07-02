from datetime import *
import textwrap
from Models import Transaction_Details, User
from Services.User_Services import User_Service
from Services.Category_service import Category_Service
from Services.Transaction_service import Transaction_Service
from Menu import delimiter, login_menu, main_menu


service = User_Service()
category_service = Category_Service()
transaction_service = Transaction_Service()


def PrintSeparator():
    print("\t")



def register_user():
    name = input("Введите имя: ")
    phone_number = input("Введите телефонный номер: ")
    password = input("Введите пароль: ")
    user = User(name, phone_number, password)
    if service.CreateUser(user):
        print("Пользователь успешно зарегистрирован")
        login_user(phone_number, password)
    else:
        print("Пользователь с таким номером уже зарегистрирован или произошла ошибка при регистрации")
        return

def print_category():
    category = category_service.get_category()
    k = 1
    delimiter(1)
    while k-1 < len(category): 
        for i in category:
            print(f"{k}. {i[0]}")
            k += 1
        delimiter(1)

def category_mean(int):
    category = category_service.get_category()
    k = 1
    while k-1 < len(category): 
        for i in category:
            if k == int:
                return i[0]
            k += 1

def print_history_filter(res):
    if res:
        for transaction in res:
            amount = transaction[0]
            date = transaction[1]
            description = transaction[2]
            category = transaction[4]
            type_transaction = "Доход" if transaction[3] == 1 else "Расход"
            
            formatted_description = textwrap.fill(description, width=30)
            
            delimiter(1)
            print(f"Сумма:      {amount}")
            print(f"Дата:       {date}")
            print(f"Описание:   {formatted_description}")
            print(f"Категория:  {category_mean(category)}")
            print(f"Тип:        {type_transaction}")
    else:
        print("Ниичего не найдено")

def print_transaction(index, res):
    if res:
        for transaction in res[index]:
            amount = transaction[0]
            date = transaction[1]
            description = transaction[2]
            category = transaction[4]
            type_transaction = "Доход" if transaction[3] == 1 else "Расход"
            
            formatted_description = textwrap.fill(description, width=30)
            
            delimiter(1)
            print(f"Сумма:      {amount}")
            print(f"Дата:       {date}")
            print(f"Описание:   {formatted_description}")
            print(f"Категория:  {category_mean(category)}")
            print(f"Тип:        {type_transaction}")
    else:
        print("Ниичего не найдено")

def login_user(phone_number=None, password=None):
    PrintSeparator()
    if not phone_number:
        phone_number = input("Введите телефонный номер: ")
    while True:
        if not password:
            password = input("Введите пароль: ")
        if service.CheckUser(phone_number, password):
            print("Авторизация прошла успешно")
            PrintSeparator()
            while True:
                login_menu()
                PrintSeparator()
                cmd_login = int(input("> "))
                PrintSeparator()
                if cmd_login == 1:
                    cmd_1(phone_number, password)
                elif cmd_login == 2:
                    cmd_2(phone_number, password)
                    break
                elif cmd_login == 3:
                    cmd_3(phone_number, password)
                elif cmd_login == 4:
                    print_category()
                    PrintSeparator()
                elif cmd_login == 5:
                    cmd_5(phone_number)
                elif cmd_login == 6:
                    cmd_6(phone_number)
                elif cmd_login == 7:
                    delimiter(1)
                    print(f"Сумма пользователя: {transaction_service.check_balance(phone_number)}")
                    delimiter(1)
                    PrintSeparator()
                elif cmd_login == 8:
                    res_history = transaction_service.history_transaction(phone_number)
                    print_history_filter(res_history)
                    PrintSeparator()
                elif cmd_login == 9:
                    res_date = transaction_service.sorted_by_date(phone_number)
                    print_history_filter(res_date)
                    PrintSeparator()
                elif cmd_login == 10:
                    cmd_10(phone_number)
                elif cmd_login == 11:
                    cmd_11(phone_number)
                elif cmd_login == 12:
                    cmd_12(phone_number)
                elif cmd_login == 0:
                    break
                else:
                    print("Неверная команда. Повторите попытку")
            break
        else:
            print("Неправильный пароль. Повторите попытку.")
            retry = int(input("Хотите попробовать снова? (да - 1 / нет - 0): "))
            if retry == 1:
                phone_number = input("Введите телефонный номер: ")
                password = input("Введите пароль: ")
            else:
                print("Выход из программы")
                break



def get_transaction_details():
    while True:
        try:
            amount = float(input("Введите сумму: "))
            if amount < 0:
                print("Введите сумму больше 0")
                continue
        except ValueError:
            print("Введите числовое значение для суммы")
            continue

        description = input("Введите описание (или оставьте пустым): ")
        print_category()
        category = input("Введите категорию (или оставьте пустым): ")

        if category:
            try:
                category_id = int(category)
                if category_id < 1 or category_id > len(category_service.get_category()):
                    print("Введите правильную категорию")
                    continue
            except ValueError:
                print("Введите числовое значение для категории")
                continue
        else:
            category_id = None

        date = datetime.now().replace(second=0, microsecond=0)
        transaction_details = Transaction_Details(amount, date, description, category_id)
        return transaction_details


def cmd_1(phone_number, password):
    user = service.get_user(phone_number, password)
    if user is not None:
        PrintSeparator()
        delimiter(1)
        print(f"Имя пользователя:  {user[0]}")
        print(f"Номер телефона:    {user[1]}")
        
        delimiter(1)
        PrintSeparator()
    else:
        print("Пользователь не найден")

def cmd_2(phone_number, password):
    new_password = input("Введите новый пароль: ")
    confirm_password = input("Введите старый для подверждения: ")
    if confirm_password == password:
        if service.update_user(phone_number, password, new_password):
            print("Пароль успешно обновлен")
            login_user(phone_number, new_password)
    else:
        print("Произошла ошибка. Повторите попытку")

def cmd_3(phone_number, password):
    confirm_password = input("Введите пароль для подверждения: ")
    confirm_delete = input("Вы уверены, что хотите удалить пользователя? (да -1/нет -0): ")
    if confirm_delete.lower() == '1':
        if confirm_password == password:
            if service.delete_user(phone_number, password):
                print("Пользователь успешно удален")
                return 
        else:
            print("Произошла ошибка при удалении пользователя")
    else:
        print("Удаление отменено")

def cmd_5(phone_number):
    details = get_transaction_details()
    if details:
        amount, date, description, category = details.amount, details.date, details.description, details.category_id
        if transaction_service.add_expense(amount, phone_number, date, description, category):
            PrintSeparator()
            print("Доход успешно добавлен")
            PrintSeparator()
        else:
            print("Произошла ошибка")

def cmd_6(phone_number):
    details = get_transaction_details()
    if details:
        amount, date, description, category = details.amount, details.date, details.description, details.category_id
        if transaction_service.add_income(amount, phone_number, date, description, category):
            PrintSeparator()
            print("Расход успешно добавлен")
            PrintSeparator()
        else:
            print("Произошла ошибка")




def cmd_10(phone_number):
    res_type = transaction_service.sorted_by_type(phone_number)
    if res_type:
        type_sort_int = int(input(f"1. Сортировка по Доходу\n0. Сортировка по Расход\n> "))
        if type_sort_int == 1:
            print_transaction(0, res_type) # income 0
            print_transaction(1, res_type) # expense 1
        else:
            print_transaction(1, res_type)
            print_transaction(0, res_type)
    else:
        print("Ничего не найдено")

def cmd_11(phone_number):
    print_category()
    category = int(input("Введите категорию: "))
    res_category = transaction_service.filter_by_category(phone_number, category)
    if res_category is False:
        PrintSeparator()
        print("Ничего не найдено")
        PrintSeparator()
    else:
        print_transaction(0, res_category)
        print_transaction(1, res_category)
        PrintSeparator()

def cmd_12(phone_number):
    type_int = int(input("Введите тип (например: 1 - (Доход) или 0 - (Расход)): "))
    PrintSeparator()
    if type_int > 1 or type_int < 0:
        PrintSeparator()
        print("Введите правильный тип")
        PrintSeparator()
    else:
        res_type = transaction_service.filter_by_type(phone_number)
        if res_type is False:
            PrintSeparator()
            print("Ничего не найдено")
            PrintSeparator()
        else:
            if type_int == 1:
                print_transaction(1, res_type)
            else:
                print_transaction(0, res_type)
            PrintSeparator()


def main() -> None:
    while True:
        main_menu()
        cmd = int(input("> "))
        if cmd == 1:
            register_user()
        elif cmd == 2:
            login_user()
        elif cmd == 0:
            print("Выход из программы")
            break
        else:
            print("Неверная команда. Повторите попытку")


main()

# if __name__ == "__main__":
#     main()