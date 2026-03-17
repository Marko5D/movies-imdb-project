from abc import ABC, abstractmethod

# Apstraktna klasa
class Person(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self._email = email
        self._address = address

    # GET / SET za email
    def get_email(self):
        return self._email
    
    def set_email(self, email):
        return self._email
    
    # GET / SET za address
    def get_address(self):
        return self._address
    
    def set_address(self, address):
        self._address = address

    # Validacija emaila
    def check_email(self):
        return "@" in self._email
    
    # Apstraktna metoda
    @abstractmethod
    def display_info(self):
        pass

# Employee klasa
class Employee(Person):
    def __init__(self, name, email, salary, address):
        super().__init__(name, email, address)
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary = salary

    def increase_salary(self, percentage):
        self.__salary += self.__salary * (percentage / 100)

    def display_info(self):
        return f"Zaposleni: {self.name}, Plata: {self.__salary}"
    
# User klasa
class User(Person):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, address)
        self.phone = phone
        self.shopping_history = []

    def get_phone(self):
        return self.phone
    
    def set_phone(self, phone):
        self.phone = phone

    def add_product(self, product):
        self.shopping_history.append(product)

    def total_spent(self):
        return sum(product.get_price() for product in self.shopping_history)
    
    def display_info(self):
        return f"Korisnik: {self.name}, Telefon: {self.phone}"
    
# Product klasa
class Product:
    def __init__(self, name, price, quantity, description):
        self.name = name
        self.__price = price
        self.quantity = quantity
        self._description = description

    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self._description
    
    def set_description(self, description):
        self._description = description

    def check_quantity(self):
        return self.quantity >= 10