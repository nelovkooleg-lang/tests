import unittest
from main2 import perimeter_area

class TestPerimeterArea(unittest.TestCase):
    def test_standard_values(self):

        self.assertEqual(perimeter_area(5), (24, 35))

    def test_square(self):

        self.assertEqual(perimeter_area(4, 4), (16, 16))

    def test_float_values(self):

        self.assertEqual(perimeter_area(2.5, 4.0), (13.0, 10.0))

    def test_zero_values(self):

        self.assertEqual(perimeter_area(0, 5), (10, 0))

if __name__ == "__main__":
    unittest.main()