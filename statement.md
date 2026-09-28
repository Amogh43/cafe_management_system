# Problem Statement

Small cafes often manage menus, orders and daily sales on paper or in memory. This causes
billing mistakes, lost sales records and wasted time. The Cafe Management System is a
command-line application that lets a cafe manage its menu, take customer orders, generate
bills and view sales reports, with all data saved permanently.

## Scope
- In scope: menu management, order taking, billing with GST, sales reporting, data persistence, logging.
- Out of scope: online payments, multiple staff logins, graphical interface, inventory tracking.

## Target Users
- Cafe owner / manager (manages menu, views reports)
- Cashier / counter staff (takes orders and prints bills)

## High-Level Features
1. Add, remove, update and display menu items (saved in JSON).
2. Take orders with validated customer details and quantities.
3. Automatic bill with 5% GST.
4. Sales report: total orders, revenue, item-wise sales, best seller.
5. Input validation, error handling and activity logging.
