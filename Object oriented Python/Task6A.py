prices = [3.99, 19.50, 55.00, 48.75, 102.00, 33.40, 12.30]

prices_below_50 = []
prices_below_50 = [c for c in prices if c < 50]

print(prices_below_50)