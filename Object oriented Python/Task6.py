# Define the initial list of prices
prices = [23.99, 19.50, 55.50, 48.75, 102.00, 33.40, 12.30]
# Create an empty list to store prices below 50
prices_below_50 = []
# Iterate through the list and add prices below 50 to the new list
for price in prices:
    if price < 50:
        prices_below_50.append(price)

# Print the list of prices below 50
print(prices_below_50)