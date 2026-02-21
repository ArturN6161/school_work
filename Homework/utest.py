import unittest
from getter_setter import Solder


class TestSolder(unittest.TestCase):

    # Метод setUp выполняется ПЕРЕД каждым тестом (как в статье)
    def setUp(self):
        # Создаем «эталонного» солдата для тестов
        self.sol = Solder('Jone', 'Рядовой', 228)

    # 1) Базовые случаи
    def test_initial_values(self):
        """Проверка правильности инициализации"""
        self.assertEqual(self.sol.name, 'Jone')
        self.assertEqual(self.sol.rank, 'Рядовой')
        self.assertEqual(self.sol.service_number, 228)

    def test_promote_base(self):
        """Проверка повышения звания"""
        self.sol.promote()
        self.assertEqual(self.sol.rank, 'Ефрейтор')

    # 2) Пограничные ситуации
    def test_promote_max_rank(self):
        """Повышение выше Капитана/Майора (граница списка)"""
        # Быстро повышаем до максимума (Майор — последний в твоем списке ranks)
        self.sol.rank = 'Майор'
        self.sol.promote()  # Должно написать, что повышения нет
        self.assertEqual(self.sol.rank, 'Майор')

    # 3) Заведомо ошибочные ситуации (через сеттеры)
    def test_invalid_rank(self):
        """Попытка установить несуществующее звание"""
        self.sol.rank = 'Генерал'  # Такого нет в ranks
        # Звание не должно измениться
        self.assertEqual(self.sol.rank, 'Рядовой')

    # 4) Проверка логики с подтверждением номера
    def test_confirm_number(self):
        """Тестируем метод confirm_number"""
        self.assertTrue(self.sol.confirm_number(228))  # Верный номер
        self.assertFalse(self.sol.confirm_number(999))  # Неверный номер


if __name__ == '__main__':
    unittest.main()