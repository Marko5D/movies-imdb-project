# Sample customer data
 
customers = [
 
    {
 
        "first_name": "Emma",
 
        "last_name": "Smith",
 
        "purchases": [
 
            ("Laptop", 1200.0),
 
            ("Mouse", 50.0)
 
        ]
 
    },
 
    {
 
        "first_name": "Jamie",
 
        "last_name": "Lee",
 
        "purchases": [
 
            ("Smartphone", 800.0),
 
            ("Headphones", 100.0)
 
        ]
 
    },
 
    {
 
        "first_name": "Alex",
 
        "last_name": "Taylor",
 
        "purchases": [
 
            ("Tablet", 400.0),
 
            ("Keyboard", 60.0),
 
            ("Monitor", 300.0)
 
        ]
 
    }
 
]
 
  
 
# Function to calculate total spent for each customer
 
def calculate_total_spent(customers):
 
    for customer in customers:
 
        total_spent = sum(item[1] for item in customer["purchases"])
 
        print(f"Customer: {customer['first_name']} {customer['last_name']}")
 
        print(f"Total spent: {total_spent:.2f} euros\n")
 
  
 
# Function to calculate total number of items purchased by each customer
 
def total_items_purchased(customers):
 
    for customer in customers:
 
        total_items = len(customer["purchases"])
 
        print(f"Customer: {customer['first_name']} {customer['last_name']}")
 
        print(f"Total items purchased: {total_items}\n")
 
  
 
# Function to find the most expensive purchase for each customer
 
def most_expensive_purchase(customers):
 
    for customer in customers:
 
        most_expensive = max(customer["purchases"], key=lambda x: x[1])
 
        print(f"Customer: {customer['first_name']} {customer['last_name']}")
 
        print(f"Most expensive item: {most_expensive[0]} - {most_expensive[1]:.2f} euros\n")
 
  
 
# Generate a comprehensive report
 
def generate_report(customers):
 
    print("Calculating total spent by each customer:")
 
    calculate_total_spent(customers)
 
  
 
    print("Calculating total items purchased by each customer:")
 
    total_items_purchased(customers)
 
  
 
    print("Finding the most expensive purchase for each customer:")
 
    most_expensive_purchase(customers)   
 
  
 
# Running the main function
 
generate_report(customers)