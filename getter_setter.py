# class BankAccount:
#     def __init__(self, owner, amount):
#         self.owner = owner
#         # Приватный атрибут (начинается с __)
#         self.__balance = amount
#
#     # ГЕТТЕР: позволяет прочитать значение __balance
#     @property
#     def balance(self):
#         print("Запрос баланса...")
#         return self.__balance
#
#     # СЕТТЕР: позволяет безопасно изменить значение __balance
#     @balance.setter
#     def balance(self, value):
#         if value < 0:
#             print("Ошибка: баланс не может быть отрицательным!")
#         else:
#             print(f"Баланс изменен на {value}")
#             self.__balance = value
#
# # --- Использование ---
# account = BankAccount("Иван", 1000)
#
# # Обращаемся как к обычному свойству (срабатывает геттер)
# print(account.balance)
#
# # Пытаемся изменить (срабатывает сеттер)
# account.balance = 5000  # Пройдет проверку
# account.balance = -100  # Выведет ошибку, значение не изменится
#
# print(account.balance)
from gettext import translation


# class Solder:
#     ranks = ["Рядовой", "Ефрейтор", "Сержант", "Лейтенант", "Капитан", "Майор"]
#     def __init__(self, name, rank, service_number):
#         self.name = name
#         self.__rank = rank
#         self.__service_number = service_number
#
#     def __str__(self):
#         return f'Информация о солдате {self.name}'
#
#     @property
#     def rank(self):
#         print('Запрос звания...')
#         return self.__rank
#
#     @rank.setter
#     def rank(self,new_rank):
#         if new_rank in self.ranks:
#             self.__rank = new_rank
#         else:
#             print('Такого звания не может быть!')
#
#     def promote(self):
#         current_idx = self.ranks.index(self.__rank)
#         if  current_idx < len(self.ranks) - 1:
#             self.__rank = self.ranks[current_idx + 1]
#             print(f"Поздравляем! Новое звание: {self.__rank}")
#         else:
#             print('Повышения не может быть.')
#
#     def demote(self):
#         current_idx = self.ranks.index(self.__rank)
#         if current_idx > 0:
#             self.__rank = self.ranks[current_idx - 1]
#             print(f"Звание понижено до: {self.__rank}")
#         else:
#             print('Понижения не может быть.')
#
#     @property
#     def service_number(self):
#         print('Запрос номера...')
#         return self.__service_number
#
#     def confirm_number(self, number_to_check):
#         if number_to_check == self.__service_number:
#             print("Номер подтвержден. Доступ разрешен.")
#             return True
#         else:
#             print("Ошибка! Неверный порядковый номер.")
#             return False
#
#     @service_number.setter
#     def service_number(self, new_service_number: int):
#         print(f'Попытка изменить текущий порядковый номер для {self.name}')
#         try:
#             check = 228 #  int(input("Введите текущий номер для подтверждения: "))
#             if check == self.__service_number:
#                 self.__service_number = new_service_number
#                 print(f"Номер успешно изменен на {new_service_number}")
#             else:
#                 print("Отказ! Номер не изменен.")
#         except ValueError:
#             print('Нужно ввести число.')
#         except KeyboardInterrupt:
#             print('\nПрограмма была прервана...')
#
# if __name__ == "__main__":
#     sol = Solder('Jone', 'Рядовой', 228)
#     print(sol)
#     print(sol.rank)
#     print(sol.service_number)
#     sol.promote()
#     print(sol.rank)
#     sol.service_number = 12


# class Candy:
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
# class Chocolate(Candy):
#     def __init__(self, name, price, weight, cocoa_percentage, chocolate_type):
#         super().__init__(self, name, price, weight)
#         self.cocoa_percentage = cocoa_percentage
#         self.chocolate_type = chocolate_type
#
#
# class Gummy(Candy):
#     def __init__(self, name, price, weight, flavor, shape):
#         super().__init__(self, name, price, weight)
#         self.flavor = flavor
#         self.shape = shape
#
#
# class HardCandy(Candy):
#     def __init__(self, name, price, weight, flavor, filled):
#         super().__init__(self, name, price, weight)
#         self.flavor = flavor
#         self.filled = filled


# class Shopping:
#     def __init__(self):
#         self.__shopping_cart = {}
#
#     def add(self):
#         name = input('Введите наименование товара: ')
#         price = int(input('Введите цену: '))
#         self.__shopping_cart[name] = price
#
#     def remove(self):
#         remove = input("Какую позицию хотите удалить из корзины? Введите наименование: ")
#         self.__shopping_cart.pop(remove)
#
#     @property
#     def cost(self):
#         cost = 0
#         for i in self.__shopping_cart.values():
#             cost += i
#         return cost
#
#
# shop = Shopping()
# shop.add()
# shop.add()
# shop.remove()
# print(shop.cost)


import os
import json


class ManagedFile:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        # Устанавливаем кодировку utf-8 для корректного чтения кириллицы
        self.file = open(self.filename, self.mode, encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


class Bank:
    db_file = 'accaunts.json'
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self._update_db()

    def _update_db(self):
        data = {}
        if os.path.exists(self.db_file):
            with ManagedFile(self.db_file, mode='r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {}

        data[self.name] = self.__balance

        with ManagedFile(self.db_file, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)



    @staticmethod
    def _log_history(name1, name2, amount):
        with ManagedFile(filename='history.txt', mode='a') as file:
            file.write(f'{name1}>{name2}:{amount}\n')

    @property
    def account_balance(self):
        return self.__balance


    def transfer(self, to_whom, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            to_whom.__balance += amount

            self._update_db()
            to_whom._update_db()

            self._log_history(self.name, to_whom.name, amount)
            print(f"Перевод от {self.name} к {to_whom.name} на сумму {amount} прошел успешно.")
        else:
            print("Маловато денег на счету!")




jone = Bank('Jone', 10000)
anna = Bank('Anna', 9000)

print(f"Баланс Jone: {jone.account_balance}")

jone.transfer(anna, 1000)

print(f"Баланс Jone: {jone.account_balance}")
print(f"Баланс Anna: {anna.account_balance}")