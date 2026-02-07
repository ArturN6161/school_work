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



class Solder:
    ranks = ["Рядовой", "Ефрейтор", "Сержант", "Лейтенант", "Капитан", "Майор"]
    def __init__(self, name, rank, service_number):
        self.name = name
        self.__rank = rank
        self.__service_number = service_number

    def __str__(self):
        return f'Информация о солдате {self.name}'

    @property
    def rank(self):
        print('Запрос звания...')
        return self.__rank

    @rank.setter
    def rank(self,new_rank):
        if new_rank in self.ranks:
            self.__rank = new_rank
        else:
            print('Такого звания не может быть!')

    def promote(self):
        current_idx = self.ranks.index(self.__rank)
        if  current_idx < len(self.ranks) - 1:
            self.__rank = self.ranks[current_idx + 1]
            print(f"Поздравляем! Новое звание: {self.__rank}")
        else:
            print('Повышения не может быть.')

    def demote(self):
        current_idx = self.ranks.index(self.__rank)
        if current_idx > 0:
            self.__rank = self.ranks[current_idx - 1]
            print(f"Звание понижено до: {self.__rank}")
        else:
            print('Понижения не может быть.')

    @property
    def service_number(self):
        print('Запрос номера...')
        return self.__service_number

    def confirm_number(self, number_to_check):
        if number_to_check == self.__service_number:
            print("Номер подтвержден. Доступ разрешен.")
            return True
        else:
            print("Ошибка! Неверный порядковый номер.")
            return False

    @service_number.setter
    def service_number(self, new_service_number):
        print(f'Попытка изменить текущий порядковый номер для {self.name}')
        check = int(input("Введите текущий номер для подтверждения: "))
        if check == self.__service_number:
            self.service_number = new_service_number
            print(f"Номер успешно изменен на {new_service_number}")
        else:
            print("Отказ! Номер не изменен.")


sol = Solder('Jone', 'Рядовой', 228)
print(sol)
print(sol.rank)
print(sol.service_number)
sol.promote()
print(sol.rank)


