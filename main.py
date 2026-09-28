"""Entry point of the Cafe Management System."""
from cafe.logger import setup_logger
from cafe.menu import Menu
from cafe.orders import OrderManager
from cafe import cli


def main():
    log = setup_logger()
    log.info("Application started")
    menu = Menu()
    order_manager = OrderManager(menu)
    try:
        cli.run(menu, order_manager)
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted. Goodbye!")
        log.warning("Application interrupted by user")


if __name__ == "__main__":
    main()
