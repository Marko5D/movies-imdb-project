# Product list
products = ['Phone', 'Laptop', 'Phone', 'TV', 'Headphones', 'Camera', 'Phone']
print('List before modifications:')
print(products)

# Removing all occurences of "Phone"
while 'Phone' in products:
    products.remove('Phone')

print('List after modification:')
print(products)