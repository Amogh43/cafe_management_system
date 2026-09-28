"""Command-line interface: connects the user to the modules."""
import logging
from cafe import validators as v
from cafe.billing import format_bill
from cafe.reports import display_report
from cafe.config import CAFE_NAME

log = logging.getLogger("cafe")

MENU_TEXT = f"""
===== Welcome to {CAFE_NAME} =====
1. Add a new item to the menu
2. Display the menu
3. Remove an item
4. Update the price of an item
5. Take an order
6. Sales report
7. Exit"""


def handle_add(menu):
    name = input("Enter the name of the new item: ")
    price = v.read_input("Enter the price: ", v.parse_price)
    try:
        menu.add_item(name, price)
        print(f"{name.strip()} added to the menu.")
        menu.display()
    except ValueError as error:
        print("Error:", error)


def handle_remove(menu):
    name = input("Enter the item to remove: ")
    try:
        removed = menu.remove_item(name)
        print(f"{removed} removed.")
        menu.display()
    except ValueError as error:
        print("Error:", error)


def handle_update(menu):
    name = input("Enter the item to update: ")
    if menu.find(name) is None:
        print("Error: Item not found.")
        return
    price = v.read_input("Enter the new price: ", v.parse_price)
    try:
        item = menu.update_price(name, price)
        print(f"Price of {item} updated.")
        menu.display()
    except ValueError as error:
        print("Error:", error)


def handle_order(menu, order_manager):
    name = v.read_input("Enter your name: ", v.parse_name)
    phone = v.read_input("Enter your 10-digit phone number: ", v.parse_phone)

    cart = {}
    menu.display()
    while True:
        text = input("Enter an item to order (or 'done' to finish): ")
        if text.strip().lower() == "done":
            break
        item = menu.find(text)
        if item is None:
            print("This item is not on the menu.")
            continue
        qty = v.read_input("Enter the quantity: ", v.parse_quantity)
        cart[item] = cart.get(item, 0) + qty

    if not cart:
        print("No items were ordered.")
        return
    try:
        order = order_manager.create_order(name, phone, cart)
        print(format_bill(order))
    except ValueError as error:
        print("Error:", error)


def run(menu, order_manager):
    while True:
        print(MENU_TEXT)
        choice = v.read_input("Enter your choice (1-7): ", v.parse_menu_choice)
        if choice == 1:
            handle_add(menu)
        elif choice == 2:
            menu.display()
        elif choice == 3:
            handle_remove(menu)
        elif choice == 4:
            handle_update(menu)
        elif choice == 5:
            handle_order(menu, order_manager)
        elif choice == 6:
            display_report(order_manager.orders)
        elif choice == 7:
            print(f"Thanks for visiting {CAFE_NAME}. Goodbye!")
            log.info("Application closed")
            break
