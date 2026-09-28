"""Module 1: Menu management (add, remove, update, display)."""
import logging
from cafe.config import MENU_FILE, DEFAULT_MENU
from cafe.storage import load_json, save_json

log = logging.getLogger("cafe")


class Menu:
    def __init__(self, filepath=MENU_FILE):
        self.filepath = filepath
        self.items = load_json(filepath, DEFAULT_MENU)

    def find(self, name):
        """Case-insensitive search. Returns the real item name or None."""
        for item in self.items:
            if item.lower() == name.strip().lower():
                return item
        return None

    def add_item(self, name, price):
        name = name.strip()
        if not name:
            raise ValueError("Item name cannot be empty.")
        if self.find(name):
            raise ValueError("This item already exists in the menu.")
        if price <= 0:
            raise ValueError("Price must be greater than 0.")
        self.items[name] = price
        save_json(self.filepath, self.items)
        log.info("Added menu item %s at Rs.%s", name, price)

    def remove_item(self, name):
        item = self.find(name)
        if item is None:
            raise ValueError("Item not found.")
        del self.items[item]
        save_json(self.filepath, self.items)
        log.info("Removed menu item %s", item)
        return item

    def update_price(self, name, new_price):
        item = self.find(name)
        if item is None:
            raise ValueError("Item not found.")
        if new_price <= 0:
            raise ValueError("Price must be greater than 0.")
        self.items[item] = new_price
        save_json(self.filepath, self.items)
        log.info("Updated price of %s to Rs.%s", item, new_price)
        return item

    def display(self):
        print("\n----- Cafe Menu -----")
        if not self.items:
            print("(menu is empty)")
        for item, price in self.items.items():
            print(f"{item:<15} Rs. {price}")
