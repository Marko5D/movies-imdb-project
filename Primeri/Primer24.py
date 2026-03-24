kupci = ["Marko", "Ana", "Lena", "Tom", "Iva"]
lojalni_kupci = ["Ana", "Tom", "Iva"]

for kupac in kupci:
    if kupac not in lojalni_kupci:
        print('Postovani/a', kupac + ', imamo specijalnu ponudu za Vas da postanete lojalni clan!')