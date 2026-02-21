import unittest
from main import sum_number


class TestSumNumber(unittest.TestCase):
    def test_base(self):
        self.assertEqual(sum_number(5, 5), 10)
        self.assertEqual(sum_number(-5, 5), 0)
        self.assertEqual(sum_number(5, 0), 5)

    def test_borderline(self):
        self.assertEqual(sum_number(0, 0.0000000), 0)
        self.assertEqual(sum_number(-0, 0), 0)
        self.assertEqual(sum_number(-0, 1.00000000), 1.0)

    def test_big_data(self):
        self.assertEqual(sum_number(37838835252, 378388352520), 416227187772)
        self.assertEqual(sum_number(10000000000, -9999999999), 1)

    def test_error(self):
        self.assertRaises(TypeError, sum_number, 5, 'a')
        self.assertRaises(TypeError, sum_number, [1], {1})
