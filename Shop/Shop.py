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
    db_orders = 'orders.json'

    def __init__(self):
        self.file_name = None


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
    def write_json(filename, data):
        with ManagedFile(filename, mode='w') as file_object:
            json.dump(data, file_object, ensure_ascii=False, indent=4)


    @staticmethod
    def register_item(filename, item_data):
        data = DatabaseManager.read_json(filename)

        if not data:
            new_id = "1"
        else:
            current_ids = [int(k) for k in data.keys()]
            new_id = str(max(current_ids) + 1)
        # добавляем товар в словарь
        data[new_id] = item_data
        # сохраняем товар в файл
        DatabaseManager.write_json(filename, data)

        return new_id

    @staticmethod
    def found_item_id(filename, search_value):
        data = DatabaseManager.read_json(filename)
        for pid, info in data.items():
            if info.get('Наименование', '').lower() == search_value.lower():
                return pid
        return None


    @staticmethod
    def update_item(filename, item_id, new_data):
        """Находит элемент по ID и перезаписывает его данные."""
        data = DatabaseManager.read_json(filename)

        if item_id in data:
            # Обновляем данные по конкретному ключу
            data[item_id].update(new_data)
            DatabaseManager.write_json(filename, data)
            return True

        return False



class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

        # Данные для записи
        info = {'Наименование': self.name, 'Цена': self.price}

        # Передаем путь напрямую из DatabaseManager
        self.id_product = DatabaseManager.register_item(DatabaseManager.db_catalog, info)
        DatabaseManager.write_json(DatabaseManager.db_catalog, info)
        print(f'Товар "{self.name}" успешно добавлен (ID: {self.id_product})')

    # def add_to_shop(self, name):
    #     self.name = name
    #     info = {'Наименование': self.name, 'Цена': self.price}
    #     self.id_product = DatabaseManager.register_item(self.file_name, info)
    #     DatabaseManager.write_json(self.file_name, info)  # сохранение в .json
    #     print(f'Товар "{self.name}" успешно добавлен в каталог (артикул: {self.id_product})')



class Order:
    db_file = 'orders.json'
    def __init__(self, order_id=None):
        self.shopping_list = []
        self.amount = None
        self.id_order = order_id
        self.status = 'Новый'

        if self.id_order:
            self._load_order()

    def _load_order(self):
        orders = DatabaseManager.read_json(DatabaseManager.db_orders)
        order_info = orders.get(self.id_order)

        if order_info:
            self.shopping_list = order_info.get('Список покупок', [])
            self.amount = order_info.get('Сумма заказа', 0)
            self.status = order_info.get('Статус', 'Новый')
            print(f"Заказ №{self.id_order} загружен. В нем товаров: {len(self.shopping_list)}")
        else:
            print(f"Заказ №{self.id_order} не найден!")

    def add_to_cart(self, name):
        found_id = DatabaseManager.found_item_id(DatabaseManager.db_catalog, name)

        if not found_id:
            print(f"Ошибка: Товар '{name}' не найден!")
            return

        if self.id_order is None:
            self.status = 'Новый'
            initial_data = {
                'Список покупок': [],
                'Сумма заказа': 0,
                'Статус': 'В работе'
            }
            # Менеджер сам даст нам новый ID
            self.id_order = DatabaseManager.register_item(self.db_file, initial_data)
            print(f"Создан новый заказ №{self.id_order}")

        self.shopping_list.append(found_id)
        self.status = 'В работе'

        catalog = DatabaseManager.read_json(DatabaseManager.db_catalog)
        self.amount = sum(catalog[pid]['Цена'] for pid in self.shopping_list if pid in catalog)

        new_info = {
            'Список покупок': self.shopping_list,
            'Сумма заказа': self.amount,
            'Статус': self.status
        }
        DatabaseManager.update_item(self.db_file, self.id_order, new_info)

        print(f"Товар '{name}' добавлен в заказ №{self.id_order}. Сумма: {self.amount}")


class Shop:
    db_file = 'catalog.json'
    def __init__(self):
        self.list_products = []
        self.list_orders = []


if __name__ == "__main__":
    print("--- Шаг 1: Наполняем каталог ---")
    # Создаем именно те товары, которые будем искать!
    p1 = Product("Кола", 100)
    p2 = Product("Чипсы", 150)

    # Теперь проверим, что они реально добавились
    catalog_data = DatabaseManager.read_json(DatabaseManager.db_catalog)
    print(f"Сейчас в каталоге: {catalog_data}")

    print("\n--- Шаг 2: Создаем новый заказ ---")
    my_order = Order()

    # Теперь названия совпадают с теми, что мы создали выше
    my_order.add_to_cart("Кола")
    my_order.add_to_cart("Чипсы")

    saved_id = my_order.id_order

    print("\n--- Шаг 3: Возвращаемся к заказу ---")
    if saved_id:
        another_session = Order(order_id=saved_id)
        another_session.add_to_cart("Кола")