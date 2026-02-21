import unittest
from Homework.calculator import quotient, summa, different, product


class Testquotient(unittest.TestCase):
    def test_base(self):
        self.assertEqual(quotient(10, 2), 5)
        self.assertEqual(quotient(-2, -2), 1)
        self.assertEqual(quotient(1000, -500), -2)
        self.assertEqual(quotient(0, 5), 0)

    def test_borderline(self):
        self.assertEqual(quotient(0.0000000001, 2), 0.00000000005)
        self.assertEqual(quotient(0, 0.000000000001), 0)
        self.assertEqual(quotient(1_000_000_000, 0.000_000_001), 1_000_000_000_000_000_000)

    def test_big_data(self):
        self.assertEqual(quotient(1000000000000000, -1.000000), -1000000000000000)

    def test_error(self):
        self.assertRaises(TypeError, quotient, 5, '1')
        self.assertRaises(ZeroDivisionError, quotient, 5, 0)


class Testsum(unittest.TestCase):
    def test_base(self):
        self.assertEqual(summa(10, 2), 12)

    def test_borderline(self):
        self.assertEqual(summa(0.0000000001, 0.0000000001), 0.0000000002)

    def test_big_data(self):
        self.assertEqual(summa(1000000000000000, 1000000000000000), 2000000000000000)

    def test_error(self):
        self.assertRaises(TypeError, summa, 21, [1])


class Testdifferent(unittest.TestCase):
    def test_base(self):
        self.assertEqual(different(10, 2), 8)

    def test_borderline(self):
        self.assertEqual(different(0.0000000001, 0.0000000001), 0)

    def test_big_data(self):
        self.assertEqual(different(1000000000000000, 1), 99999999999999)

    def test_error(self):
        self.assertRaises(TypeError, different, 21, [1])


class Testproduct(unittest.TestCase):
    def test_base(self):
        self.assertEqual(product(10, 2), 20)

    def test_borderline(self):
        self.assertEqual(product(0.0001, -0.1), -0.00001)

    def test_big_data(self):
        self.assertEqual(product(1000000000000000, -1), -1000000000000000)

    def test_error(self):
        self.assertRaises(TypeError, product, (21,), 'f')