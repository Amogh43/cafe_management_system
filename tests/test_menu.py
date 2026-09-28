import os
import tempfile
import unittest
from cafe.menu import Menu


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.menu = Menu(os.path.join(self.tmp.name, "menu.json"))

    def tearDown(self):
        self.tmp.cleanup()

    def test_default_items_loaded(self):
        self.assertIn("Coffee", self.menu.items)

    def test_add_item(self):
        self.menu.add_item("Burger", 60)
        self.assertEqual(self.menu.items["Burger"], 60)

    def test_add_duplicate_case_insensitive(self):
        with self.assertRaises(ValueError):
            self.menu.add_item("coffee", 40)

    def test_add_invalid_price(self):
        with self.assertRaises(ValueError):
            self.menu.add_item("Cake", 0)

    def test_remove_item(self):
        self.menu.remove_item("tea")
        self.assertNotIn("Tea", self.menu.items)

    def test_remove_missing(self):
        with self.assertRaises(ValueError):
            self.menu.remove_item("Sushi")

    def test_update_price(self):
        self.menu.update_price("PIZZA", 120)
        self.assertEqual(self.menu.items["Pizza"], 120)

    def test_persistence(self):
        self.menu.add_item("Muffin", 35)
        reloaded = Menu(self.menu.filepath)
        self.assertEqual(reloaded.items["Muffin"], 35)


if __name__ == "__main__":
    unittest.main()
