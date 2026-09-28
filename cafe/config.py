"""Central configuration: file paths and constants."""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(BASE_DIR, "logs")

MENU_FILE = os.path.join(DATA_DIR, "menu.json")
ORDERS_FILE = os.path.join(DATA_DIR, "orders.json")
LOG_FILE = os.path.join(LOG_DIR, "cafe.log")

TAX_RATE = 0.05  # 5% GST
CAFE_NAME = "Amogh Brew House"   

DEFAULT_MENU = {"Coffee": 20, "Sandwich": 30, "Tea": 15, "Pizza": 80, "French Fries": 40}
