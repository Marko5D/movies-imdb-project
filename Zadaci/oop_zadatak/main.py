from product import Product
from employee import Employee
from user import User

# lista proizvoda

products = [
    Product("Laptop", 1200, 15, "Gaming laptop"),
    Product("Telefon", 800, 5, "Smartphone"),
    Product("Monitor", 300, 12, "27 inch monitor"),
    Product("Tastatura", 50, 20, "Mechanical keyboard"),
    Product("Mis", 40, 8, "Wireless mouse")
]

# lista zaposlenih

employees = [
    Employee("Marko", "marko@gmail.com", 1000, "Beograd"),
    Employee("Ana", "ana@gmail.com", 1200, "Novi Sad")
]

# lista korisnika

users = [
    User("Petar", "petar1", "petar@gmail.com", "060111111", "Nis"),
    User("Jelena", "jelena2", "jelena@gmail.com", "060222222", "Kragujevac"),
    User("Nikola", "nikola3", "nikola@gmail.com", "060333333", "Subotica")
]

# demonstracija metoda

print(products[1].check_quantity())

print(employees[0].check_email())
employees[0].increase_salary(10)
print(employees[0].salary)

users[0].add_product(product[0])
users[0].add_product(product[3])

print(users[0].total_spent())