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
    db_catalog = 'catalog.json'
    db_accounts = 'accounts.json'
    db_orders = 'orders.json'
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

    def read_json(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            return {}
        with ManagedFile(self.filename, mode='r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id_product = None
        self._identification()

    def _identification(self):
        self.file_name = ManagedFile.db_catalog
        ManagedFile.read_json(filename=self.file_name)

        if not self.file_name:
            new_id = 1
        else:
            current_ids = [int(k) for k in self.file_name.keys()]
            new_id = max(current_ids) + 1

        self.id_product = str(new_id)

        data = data[self.id_product] = {
            'name': self.name,
            'price': self.price
        }

        with ManagedFile(self.db_file, mode='w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

            print(f'Товар "{self.name}" успешно добавлен в каталог (артикул: {self.id_product})')



class Order:
    db_file = 'orders.json'
    def __init__(self):
        self.shopping_list = []
        self.amount = None
        self.id_order = None
        self.status = 'Новый'
        self._identification()



    def _identification(self):
        data = {}
        if os.path.exists(self.db_file):
            with ManagedFile(self.db_file, mode='r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {}

        if not data:
            new_id = 1
        else:
            current_ids = [int(k) for k in data.keys()]
            new_id = max(current_ids) + 1

        self.id_order = str(new_id)

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