products_on_sale = ("Laptop", "Phone", "TV")
print(products_on_sale)

product_info = ("Laptop", 999.99, ["Black", "Silver", "Gray"])
print(product_info)

products_on_sale = ("Laptop", "Phone", "TV")
print(products_on_sale[1])  # Prints "Phone"

products_on_sale = ("Laptop", "Phone", "TV", "Headphones", "Camera")
 
# Displaying products from the first to the third element
selected_products = products_on_sale[0:3]
print(selected_products)  # Outputs ("Laptop", "Phone", "TV")

products_on_sale = ("Laptop", "Phone", "TV")
new_category = ("Headphones", "Camera")
 
# Merging two tuples
all_products = products_on_sale + new_category
print(all_products) # Outputs ("Laptop", "Phone", "TV", "Headphones", "Camera")

all_products = ("Laptop", "Phone", "TV", "Phone", "Camera")
print(all_products.count("Phone"))  # Outputs 2
print(all_products.index("TV"))

