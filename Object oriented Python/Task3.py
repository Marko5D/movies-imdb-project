# Initial stock level
total_stock = 1000
# List to store daily sales
sales = []
# Enter sales data for each day of the week
for day in range (7):
    # Prompt user for input and convert it to integer
    sold = int(input(f"Enter the number of items sold on day{day + 1}:"))
    sales.append(sold)
# Calculate the total sold items during the week
total_sold = sum(sales)
# Update the total stock by subtracting the total sold items
total_stock -= total_sold
# Print the remaining stock after one week
print(f"Remaining stock after one week is: {total_stock} items.")