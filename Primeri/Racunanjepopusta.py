# Definišemo funkciju za izračunavanje popusta
def calculate_discount(price, discount_percent):
    new_price = price - (price * discount_percent) / 100
    return new_price
 
# Poziv funkcije za primer kada je cena 500, a popust 10%
print(calculate_discount(500, 10))