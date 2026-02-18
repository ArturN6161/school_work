# class Planet:
#     def __init__(self, name, mass, orbit_radius):
#         self.name = name
#         self.mass = mass
#         self.orbit_radius = orbit_radius
#         self.satellites = []
#
#     def add_moon(self, satellite):
#         self.satellites.append(satellite)
#
#     def display_info(self):
#         print(f'Планета {self.name}, с массой {self.mass}. '
#               f'Имеет орбиту {self.orbit_radius} и спутники:')
#         print(self.satellites)
#
#     def __repr__(self):
#         return f'{self.name}'
#
#
# class Moon:
#     def __init__(self, name, mass, radius, planet):
#         self.name = name
#         self.mass = mass
#         self.radius = radius
#         self.planet = planet
#
#     def __repr__(self):
#         return (f'Спутник {self.name} с массой {self.mass} и радиусом '
#                 f'{self.radius}. Вращается вокруг планеты {self.planet}')
#
#
# earth = Planet(name="Земля", mass=5.972e24, orbit_radius=149.6e6)
# moon = Moon(name="Луна", mass=7.35e22, radius=1737.1, planet=earth)
# earth.add_moon(moon)
# earth.display_info()


# class Player:
#     def __init__(self, name, points):
#         self.name = name
#         self.__points = points
#
#     def __repr__(self):
#         return f'У игрока {self.name}, {self.info_points} очков'
#
#     @property
#     def info_points(self):
#         return self.__points
#
#     @info_points.setter
#     def info_points(self, points):
#         self.__points += points
#
#
# class Tournament:
#     def __init__(self):
#         self.players = []
#
#
#     def add_player(self, player):
#         self.players.append(player)
#
#     def show_leaderboard(self):
#         list_leaders = list(self.players)
#         list_leaders.sort(key=lambda x: x.info_points, reverse=True)
#         print("--- Таблица лидеров ---")
#         for i in list_leaders:
#             print(i)
#
# player1 = Player(name="Alice", points=10)
# player2 = Player(name="Bob", points=20)
# tournament = Tournament()
# tournament.add_player(player1)
# tournament.add_player(player2)
# tournament.show_leaderboard()
# print(player1.info_points)
# player1.info_points = 30
# print(player1.info_points)
# tournament.show_leaderboard()


import os
import json


class ManagedFile:
    """Контекстный менеджер для безопасной работы с БД."""
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


class DatabaseManager:
    db_catalog = 'catalog.json'
    db_accounts = 'accounts.json'
    db_orders = 'orders.json'

    @staticmethod
    def read_json(filename):
        if not os.path.exists(filename):
            return {}
        with ManagedFile(filename, mode='r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}

    @staticmethod
    def write_json(file_name, data):
        with ManagedFile(filename=file_name, mode='w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def register_item(file_name, item_data):
        data = DatabaseManager.read_json(file_name)

        if not data:
            new_id = "1"

        else:
            current_ids = [int(k) for k in data.keys()]
            new_id = str(max(current_ids) + 1)

        data[new_id] = item_data

        DatabaseManager.write_json(file_name, data)

        return new_id




class Product:
    file_name = DatabaseManager.db_catalog
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def add_to_cart(self, name):
        self.name = name
        info = {'name': self.name, 'price': self.price}
        self.id_product = DatabaseManager.register_item(self.file_name, info)

        print(f'Товар "{self.name}" успешно добавлен в каталог (артикул: {self.id_product})')



class Order:
    db_file = 'orders.json'
    def __init__(self):
        self.shopping_list = []
        self.amount = None
        self.id_order = None
        self.status = 'Новый'
        self._identification()


        data[self.id_order] = {
            'List products': self.shopping_list,
            'Amount': self.amount,
            'Status': self.status
        }

        with ManagedFile(self.db_file, mode='w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

            print(f'Заказ успешно сформирован с ID: {self.id_order}')

    def add_to_cart(self, name):
        data = {}
        if os.path.exists(self.db_file):
            with ManagedFile(self.db_file, mode='r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {}

        found_id = None
        for id, info in data.items():
            if info['name'].lower() == name.lower():
                found_id = id
                break

        if found_id:
            self.shopping_list.append(found_id)
            print(f"Товар '{name}' (ID: {found_id}) добавлен в корзину.")
        else:
            print(f"Ошибка: Товар '{name}' не найден в каталоге!")


class Shop:
    db_file = 'catalog.json'
    def __init__(self):
        self.list_products = []
        self.list_orders = []


# 1. Создаем товар (он сам запишется в базу)
apple = Product("Яблоко", 100)

# 2. Создаем заказ (БЕЗ аргументов в скобках)
my_order = Order()

# 3. Добавляем в корзину ПО НАЗВАНИЮ (строкой)
my_order.add_to_cart("Яблоко")

# Это выдаст ошибку "не найден", как и задумано
my_order.add_to_cart("Тапочки")