# Defining the list of orders, where each order is represented as a tuple
orders = [
    (101, "John Doe", 299.99, "Pending"),
    (102, "Jane Smith", 149.50, "Shipped"),
    (103, "Mike Johnson", 89.75, "Delivered"),
    (104, "Emily Davis", 249.99, "Pending"),
    (105, "Alice Brown", 120.00, "Cancelled")
]

# Displaying all orders with status "Pending"
print("Orders with status 'Pending':")
for order in orders:
    order_id = order[0]
    customer_name = order[1]
    amount = order[2]
    status = order[3]

    if status == 'Pending':
        print(f'Order ID: {order_id}, Customer: {customer_name}, Amount: ${amount:.2f}, Status: {status}')

# Displaying the total amount of all successful orders ("Shipped" or "Delivered")
total_successful_orders = 0.0
for order in order:
    amount = order[2]
    status = order[3]

    if status in ('Shipped', "Delivered"):
        total_successful_orders += amount

print(f"Total amount of successful orders: ${total_successful_orders:.2f}")