import unittest
from main import square_params

class TestSquareParams(unittest.TestCase):
    def test_standard_side(self):
        # Проверка для стороны 6 (периметр 24, площадь 36)
        self.assertEqual(square_params(6), (24, 36))

    def test_unit_side(self):
        # Проверка для стороны 1 (периметр 4, площадь 1)
        self.assertEqual(square_params(1), (4, 1))

    def test_float_side(self):
        # Проверка для дробной стороны 2.5
        self.assertEqual(square_params(2.5), (10.0, 6.25))

    def test_zero_side(self):
        # Проверка для нулевой стороны
        self.assertEqual(square_params(0), (0, 0))

if __name__ == "__main__":
    unittest.main()