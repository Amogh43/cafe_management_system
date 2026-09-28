import os
import tempfile
import unittest
from cafe.menu import Menu
from cafe.orders import OrderManager
from cafe.reports import sales_summary
from cafe.billing import format_bill


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.menu = Menu(os.path.join(self.tmp.name, "menu.json"))
        self.menu.items = {"Coffee": 30, "Sandwich": 50, "Tea": 20, "Pizza": 90}  # fixed test prices
        self.om = OrderManager(self.menu, os.path.join(self.tmp.name, "orders.json"))

    def tearDown(self):
        self.tmp.cleanup()

    def test_order_totals(self):
        order = self.om.create_order("Amit", "9876543210", {"Coffee": 2, "Tea": 1})
        self.assertEqual(order["subtotal"], 80)   # 2*30 + 20
        self.assertEqual(order["tax"], 4.0)       # 5%
        self.assertEqual(order["total"], 84.0)

    def test_empty_cart(self):
        with self.assertRaises(ValueError):
            self.om.create_order("Amit", "9876543210", {})

    def test_item_not_on_menu(self):
        with self.assertRaises(ValueError):
            self.om.create_order("Amit", "9876543210", {"Sushi": 1})

    def test_order_ids_increase(self):
        a = self.om.create_order("A", "1111111111", {"Tea": 1})
        b = self.om.create_order("B", "2222222222", {"Tea": 1})
        self.assertEqual((a["order_id"], b["order_id"]), (1, 2))

    def test_sales_summary(self):
        self.om.create_order("A", "1111111111", {"Tea": 2})
        self.om.create_order("B", "2222222222", {"Tea": 1, "Pizza": 1})
        s = sales_summary(self.om.orders)
        self.assertEqual(s["total_orders"], 2)
        self.assertEqual(s["item_counts"]["Tea"], 3)
        self.assertEqual(s["best_seller"], "Tea")

    def test_empty_summary(self):
        s = sales_summary([])
        self.assertEqual(s["revenue"], 0)
        self.assertIsNone(s["best_seller"])

    def test_bill_contains_total(self):
        order = self.om.create_order("Amit", "9876543210", {"Coffee": 1})
        self.assertIn("TOTAL", format_bill(order))


if __name__ == "__main__":
    unittest.main()
