"""Module 3b: Sales analytics and reporting."""


def sales_summary(orders):
    """Return a dict with total orders, revenue, per-item counts and best seller."""
    item_counts = {}
    revenue = 0
    for order in orders:
        revenue += order["total"]
        for item, info in order["items"].items():
            item_counts[item] = item_counts.get(item, 0) + info["quantity"]

    best_seller = max(item_counts, key=item_counts.get) if item_counts else None
    return {
        "total_orders": len(orders),
        "revenue": round(revenue, 2),
        "item_counts": item_counts,
        "best_seller": best_seller,
    }


def display_report(orders):
    summary = sales_summary(orders)
    print("\n------- Sales Report -------")
    print(f"Total Orders : {summary['total_orders']}")
    print(f"Total Revenue: Rs. {summary['revenue']}")
    print(f"Best Seller  : {summary['best_seller'] or 'N/A'}")
    print("------- Items Sold -------")
    for item, qty in summary["item_counts"].items():
        print(f"{item:<15} {qty}")
