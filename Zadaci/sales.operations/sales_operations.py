"""
sales_operations.py

Modul za rad sa podacima o prodaji.
Sadrzi funkcije za analizu prodaje, validaciju podataka
i manipulaciju recnikom prodajnih rezultata.
"""

def total_sold(sales_data):
    """
    Vraca ukupan broj prodatih jedinica.
    """
    return sum(sales_data.values())

def most_sold_product(sales_data):
    """
    Vraca proizvod sa najvecom prodajom.
    Koristi lambda funkciju za odredjivanje maksimuma.
    """
    return max(sales_data, key=lambda product: sales_data[product])

def least_sold_product(sales_data):
    """
    Vraca proizvod sa najmanjom prodajom.
    """
    return min(sales_data, key=lambda product: sales_data[product])

def increase_quantity(sales_data, product_name, amount):
    """
    Povecava prodatu kolicinu za odredjeni proizvod.
    """
    try:
        sales_data[product_name] += amount
        return sales_data[product_name]
    except KeyError:
        print(f"Greska: proizvod '{product_name}' ne postoji u evidenciji.")
    except TypeError:
        print("Greska: neispravna operacija nad podacima.")

def check_item(sales_data, product_name):
    """
    Vraca prodaju odredjenog proizvoda.
    """
    try:
        return sales_data[product_name]
    except KeyError:
        print(f"Greska: proizvod'{product_name}' nije pronadjen.")

def get_product_sales(sales_data, product_name):
    """
    Vraca broj prodatih jedinica za dati proizvod.
    """
    try:
        return sales_data[product_name]
    except KeyError:
        print(f"Greska: proizvod'{product_name}' ne postoji.")

def validate_sales_data(sales_data):
    """
    Proverava validnost podataka:
    - negativne vrednosti
    - ekstremno velike vrednosti (>100000)
    """
    valid = True

    for product, quantity in sales_data.items():
        
        if quantity <0:
            print(f"Greska: proizvod'{product}'ima negativnu kolicinu ({quantity}).")
            valid = False

        elif quantity > 100000:
            print(f"Greska: proizvod '{product}' ima sumnjivo veliku kolicinu ({quantity}).")
            valid = False

    return valid

def critical_sales_products(sales_data):
    """
    Pronalazi proizvode sa kriticno malom prodajom (<50).
    Koristi filter i lambda funkciju.
    """
    return list(filter(lambda item: item[1] < 50, sales_data.items()))