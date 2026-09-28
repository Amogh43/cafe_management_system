"""Module 2: Taking orders and storing them."""
import logging
from datetime import datetime
from cafe.config import ORDERS_FILE, TAX_RATE
from cafe.storage import load_json, save_json

log = logging.getLogger("cafe")


class OrderManager:
    def __init__(self, menu, filepath=ORDERS_FILE):
        self.menu = menu
        self.filepath = filepath
        self.orders = load_json(filepath, [])

    def create_order(self, customer_name, phone, cart):
        """cart is a dict like {"Coffee": 2, "Tea": 1}. Returns the saved order."""
        if not cart:
            raise ValueError("Cart is empty.")

        lines = {}
        subtotal = 0
        for item, qty in cart.items():
            if item not in self.menu.items:
                raise ValueError(f"'{item}' is not on the menu.")
            price = self.menu.items[item]
            lines[item] = {"quantity": qty, "price": price}
            subtotal += price * qty

        tax = round(subtotal * TAX_RATE, 2)
        order = {
            "order_id": len(self.orders) + 1,
            "customer_name": customer_name,
            "phone": phone,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "items": lines,
            "subtotal": round(subtotal, 2),
            "tax": tax,
            "total": round(subtotal + tax, 2),
        }
        self.orders.append(order)
        save_json(self.filepath, self.orders)
        log.info("Order #%s placed by %s, total Rs.%s",
                 order["order_id"], customer_name, order["total"])
        return order
