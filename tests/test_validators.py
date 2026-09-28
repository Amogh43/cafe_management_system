import unittest
from cafe import validators as v


class TestValidators(unittest.TestCase):
    def test_valid_phone(self):
        self.assertEqual(v.parse_phone("9876543210"), "9876543210")

    def test_invalid_phone(self):
        for bad in ["123", "abcdefghij", "98765432101", ""]:
            with self.assertRaises(ValueError):
                v.parse_phone(bad)

    def test_price(self):
        self.assertEqual(v.parse_price("25.5"), 25.5)
        for bad in ["0", "-5", "abc"]:
            with self.assertRaises(ValueError):
                v.parse_price(bad)

    def test_quantity(self):
        self.assertEqual(v.parse_quantity("3"), 3)
        for bad in ["0", "-1", "2.5", "x"]:
            with self.assertRaises(ValueError):
                v.parse_quantity(bad)

    def test_name(self):
        self.assertEqual(v.parse_name("  Riya Sharma "), "Riya Sharma")
        for bad in ["", "R2D2"]:
            with self.assertRaises(ValueError):
                v.parse_name(bad)

    def test_menu_choice(self):
        self.assertEqual(v.parse_menu_choice("5"), 5)
        for bad in ["0", "8", "a"]:
            with self.assertRaises(ValueError):
                v.parse_menu_choice(bad)


if __name__ == "__main__":
    unittest.main()
