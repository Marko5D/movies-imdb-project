# List of products
products = ["Samsung Phone", "Laptop", "iPhone", "TV", "Headphones", "Camera", "Xiaomi Phone"]
# Prompt the user to enter a keyword
keyword = input("Enter the keyword to search for in product names: ")
# Loop through the products and print those containing the keyword
for product in products:
    if keyword in product:
        print(product)

# Product list
products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
# Using len() to get the size of the list
total_products = len(products)
print(f"We have {total_products} products in our assortment.")

# Product list
products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
# Checking if "Phone" is in the product list
if "Phone" in products:
    print("Phone is available.")
else:
    print("Phone is not available.")

# Product list
products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
print("List contents before modification:")
print(products)
# Replacing the last item in the list with "Smart Watch"
products[-1] = "Smart Watch"
print("List contents after modification:")
print(products)

# Product list before modification
products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
print("List contents before modification:")
print(products)
 
# Adding a new product to the end of the list
products.append("Tablet")
print("List contents after modification:")
print(products)

# Product list
products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
print("List before modification:")
print(products)
 
# Removing the product "TV"
products.remove("TV")
print("List after modification:")
print(products)

# Product list
products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
print("List before modification:")
print(products)
 
# Removing the product at position 3
removed_item = products.pop(3)
print("List after modification:")
print(products)
print("The product at position 3 was:", removed_item)

# Product list
products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
print("List before modification:")
print(products)
 
# Deleting the product at position 3
del products[3]
print("List after modification:")
print(products)

# Two product lists
list1 = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
list2 = ["Laptop Stand", "Mouse", "Keyboard"]
 
# Combining the lists into a new list using the + operator
combined_list = list1 + list2
print("Combined List:", combined_list)

# Two product lists
list1 = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
list2 = ["Laptop Stand", "Mouse", "Keyboard"]
 
# Extending list1 by adding elements from list2 using extend()
list1.extend(list2)
print("Extended List1:", list1)

# Product list
products = ["Laptop", "Phone", "TV", "Headphones", "Camera"]
print("List before sorting:")
print(products)
 
# Sorting the list in ascending order
products.sort()
print("List after sorting:")
print(products)