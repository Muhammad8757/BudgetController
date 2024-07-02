LOGIN_MENU_TUPLE = (
    "1. Получение данных о пользователе",
    "2. Для обновления пароля",
    "3. Удаление пользователя",
    "4. Все категории",
    "5. Новый расход",
    "6. Новый доход",
    "7. Вывод счета",
    "8. Вывод истории",
    "9. Сортировка по дате",
    "10. Сортировка по типу",
    "11. Фильтр по категории",
    "12. Фильта по типу",
    "0. Для выхода из аккаунта"
)

MAIN_MENU_TUPLE = (
    "Добро пожаловать!",
    "1. Регистрации пользователя",
    "2. Вход в аккаунт",
    "0. Выход из программы"
)

def delimiter(count):
    for i in range(count):
        print("="*40)

def login_menu():
    delimiter(1)
    for i in LOGIN_MENU_TUPLE:
        print(i)
    delimiter(1)

def main_menu():
    delimiter(1)
    for i in MAIN_MENU_TUPLE:
        print(i)
    delimiter(1)