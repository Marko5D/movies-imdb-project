# Define the list of products, each product is a tuple: (product name, quantity, price per unit)
products = [
    ("Laptop", 10, 800.00),
    ("Smartphone", 25, 500.00),
    ("Headphones", 50, 30.00),
    ("Monitor", 15, 150.00),
    ("Keyboard", 40, 20.00),
    ("Mouse", 60, 15.00)
]
 
 
# Initialize total inventory value
total_inventory_value = 0.0
 
 
# Iterate over the list of products
for product in products:
    name = product[0]
    quantity = product[1]
    price = product[2]
    # Calculate the inventory value for the product
    inventory_value = quantity * price
    # Add to the total inventory value
    total_inventory_value += inventory_value
    # Optional: Print the inventory value for each product
    # print(f"{name}: Quantity = {quantity}, Price = ${price:.2f}, Inventory Value = ${inventory_value:.2f}")
 
 
# Print the total inventory value
print(f"The total value of all inventory is: ${total_inventory_value:.2f}")