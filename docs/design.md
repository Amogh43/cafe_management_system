# Design Document – Cafe Management System

## 1. Objectives
- Digitise menu, ordering, billing and sales tracking for a small cafe.
- Apply modular programming, file handling, exception handling, and testing.

## 2. Functional Requirements
| ID | Module | Requirement |
|----|--------|-------------|
| FR1 | Menu Management | Add, remove, update price and display items |
| FR2 | Order Processing | Take customer details and multiple items with quantities |
| FR3 | Billing & Reports | Generate bill with GST; show sales report |
| FR4 | Storage | Save menu and orders to JSON files |

**Input/Output:** Input = keyboard (menu choice, names, prices, quantities). Output = console menu, bill, report; `data/*.json`; `logs/cafe.log`.

## 3. Non-Functional Requirements
1. **Usability** – simple numbered menu, clear error messages.
2. **Reliability / Error handling** – invalid input never crashes the program; corrupted JSON falls back to defaults.
3. **Maintainability** – separate modules, each with one responsibility.
4. **Logging** – all key actions are recorded in `logs/cafe.log`.
5. **Performance** – all operations respond instantly for typical cafe data sizes.

## 4. System Architecture
Refer to readme.md or docs/images

## 5. Workflow Diagram
Refer to readme.md or docs/images


## 6. Use Case Diagram
Refer to readme.md or docs/images

## 7. Class Diagram
Refer to readme.md or docs/images

## 8. Sequence Diagram (Taking an Order)
Refer to readme.md or docs/images

## 9. Storage Design (ER Diagram)
Refer to readme.md or docs/images


## 10. Testing
21 unit tests (`tests/`) cover validators, menu operations, order totals, reports, billing and persistence.
