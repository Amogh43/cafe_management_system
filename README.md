# Cafe Management System

## Overview
A Python command-line application that helps a small cafe manage its menu, take orders,
generate bills and analyse sales. Data is stored in JSON files so it is not lost when the
program closes.

## Features
- **Menu Management** – add, remove, update price, display (case-insensitive search)
- **Order Processing** – customer details, multiple items, quantity validation
- **Billing & Reports** – bill with GST, total revenue, item-wise sales, best seller
- Persistent storage (JSON), logging (`logs/cafe.log`), input validation, unit tests

## Technologies Used
- Python 3.8+ (standard library only: `json`, `logging`, `re`, `datetime`, `unittest`)
- Git & GitHub for version control

## Project Structure
```
cafe_management_system/
├── main.py              # entry point
├── cafe/
│   ├── config.py        # paths and constants
│   ├── logger.py        # logging setup
│   ├── validators.py    # input validation
│   ├── storage.py       # JSON read/write
│   ├── menu.py          # Module 1: menu management
│   ├── orders.py        # Module 2: order processing
│   ├── billing.py       # Module 3: bill generation
│   ├── reports.py       # Module 3: sales analytics
│   └── cli.py           # user interface / workflow
├── tests/               # unit tests
├── data/                # menu.json, orders.json (auto-created)
├── logs/                # cafe.log (auto-created)
├── docs/design.md       # diagrams and requirements
├── statement.md
└── README.md
```

## How to Install and Run
1. Install Python 3.8 or higher.
2. Clone the repo: `git clone <your-repo-url>` and `cd cafe_management_system`
3. Run: `python main.py`

No extra libraries need to be installed.

## How to Run Tests
```
python -m unittest discover -s tests -t .
```

## Sample Usage
```
Enter your choice (1-7): 5
Enter your name: Riya Sharma
Enter your 10-digit phone number: 9876543210
Enter an item to order (or 'done' to finish): coffee
Enter the quantity: 2
```

## Screenshots

### Main Menu
![Main Menu](docs/images/main_menu.png)

### Display Menu
![Display Menu](docs/images/display_menu.png)

### Sales Report
![Sales Report](docs/images/sales_report.png)

### Take Order
![Order](docs/images/take_order.png)

### Unit Tests
![Tests](docs/images/tests.png)

### Bill
![Bill](docs/images/bill.png)


## Design Diagrams

### System Architecture
![Architecture](docs/images/system_architecture.png)

### Workflow
![Workflow](docs/images/workflow_diagram.png)

### Class Diagram
![Class Diagram](docs/images/class_diagram.png)

### Sequence
![Sequence](docs/images/sequence_diagram.png)

### Storage Design
![Storage Design](docs/images/storage_design.png)

### Use Case
![USECASE](docs/images/use_case.png)