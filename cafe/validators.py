"""Input validation helpers. Parsers raise ValueError with a friendly message."""
import re


def parse_name(text):
    text = text.strip()
    if not text:
        raise ValueError("Name cannot be empty.")
    if not re.fullmatch(r"[A-Za-z ]+", text):
        raise ValueError("Name can contain only letters and spaces.")
    return text


def parse_phone(text):
    text = text.strip()
    if not re.fullmatch(r"\d{10}", text):
        raise ValueError("Phone number must be exactly 10 digits.")
    return text


def parse_price(text):
    try:
        price = float(text)
    except ValueError:
        raise ValueError("Price must be a number.")
    if price <= 0:
        raise ValueError("Price must be greater than 0.")
    return round(price, 2)


def parse_quantity(text):
    try:
        qty = int(text)
    except ValueError:
        raise ValueError("Quantity must be a whole number.")
    if qty <= 0:
        raise ValueError("Quantity must be greater than 0.")
    return qty


def parse_menu_choice(text, low=1, high=7):
    try:
        choice = int(text)
    except ValueError:
        raise ValueError(f"Enter a number from {low} to {high}.")
    if not low <= choice <= high:
        raise ValueError(f"Enter a number from {low} to {high}.")
    return choice


def read_input(prompt, parser):
    """Keep asking until the parser accepts the input."""
    while True:
        try:
            return parser(input(prompt))
        except ValueError as error:
            print("Invalid input:", error)
