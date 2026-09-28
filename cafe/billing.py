"""Module 3a: Bill generation."""

from cafe.config import CAFE_NAME

def format_bill(order):
    line = "-" * 45
    text = [
        "=" * 45,
        f"{CAFE_NAME.upper():^45}",
        "=" * 45,
        f"Order No : {order['order_id']}",
        f"Customer : {order['customer_name']}",
        f"Contact  : {order['phone']}",
        f"Time     : {order['time']}",
        line,
    ]
    for item, info in order["items"].items():
        amount = info["price"] * info["quantity"]
        text.append(f"{item:<15} {info['quantity']} x {info['price']:<6} = Rs. {amount}")
    text += [
        line,
        f"Subtotal : Rs. {order['subtotal']}",
        f"GST (5%) : Rs. {order['tax']}",
        f"TOTAL    : Rs. {order['total']}",
        "=" * 45,
        "Thank you for visiting!",
    ]
    return "\n".join(text)
