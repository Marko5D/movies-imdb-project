# 1. Kreiranje recnika sales
sales = {
    'Laptop': 15,
    'Mouse': 150,
    'Keyboard': 85,
    'Monitor': 30,
    'USB cable': 200
}

# 3.1 Ukupna kolicina prodatih proizvoda
ukupno_prodatih = sum(sales.values())

# 3.2 Proizvod koji se najvise prodavao
najvise_prodat = max(sales, key=sales.get)

# 3.3 Proizvod koji se najmanje prodavao
najmanje_prodat = min(sales, key=sales.get)

# 3.4 Provera da li postoji "Web camera"
if "Web camera" not in sales:
    sales['Web camera'] = 0

# 3.5 Povecati prodaju Monitora za 5
sales['Monitor'] += 5

# 4. Ispis rezultata
print('Azurirani recnik:', sales)
print('Ukupno prodatih proizvoda:', ukupno_prodatih)
print('Najvise se prodavao:', najvise_prodat)
print('Najmanje se prodavao:', najmanje_prodat)

# 5. Funkcija za kriticne proizvode (<50 jedinica)
def kriticni_proizvodi(sales_dict):
    return [proizvod for proizvod, kolicina in sales_dict.items() if kolicina < 50]

kriticni = kriticni_proizvodi(sales)
print("Kriticni proizvodi:", kriticni)

# 6. Provera validnosti (negativne vrednosti)
negativni = [p for p, k in sales.items() if k <0]

if negativni:
    print('Postoje proizvodi sa negativnom kolicinom:', negativni)
else:
    print('Svi podaci su validni')