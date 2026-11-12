import unittest
from main3 import circle_area

class TestCircleAreaFixed(unittest.TestCase):
    def test_current_behavior(self):

        area, length = circle_area(6)
        self.assertAlmostEqual(area, 78.5)
        self.assertAlmostEqual(length, 31.4)

if __name__ == "__main__":
    unittest.main()