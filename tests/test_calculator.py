import unittest
from src.calculator import calculate_nutrition

class TestCalculator(unittest.TestCase):
    def test_calculate_nutrition(self):
        result = calculate_nutrition(70, 175, 25, "h", "modéré")
        self.assertIn("calories", result)
        self.assertIn("protéines", result)
        self.assertIn("lipides", result)
        self.assertIn("glucides", result)
        self.assertGreater(result["calories"], 0)

if __name__ == "__main__":
    unittest.main()
