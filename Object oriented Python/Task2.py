# Definisemo listu proizvoda po izboru

dostupni_proizvodi = ["laptop", "tablet", "mobilni telefon", "mis", "tastatura"]

#Proizvod za proveru

proizvod_za_proveru = "mobilni telefon"

#Pravljenje petlje za proveru

if proizvod_za_proveru in dostupni_proizvodi:
    print(f"{proizvod_za_proveru} je dostupan!")
else:
    print(f"{proizvod_za_proveru} nije dostupan!")