kupci = ['Marko', 'Ana', 'Lena', 'Tom', 'Iva']
lojalni_kupci = ['Ana', 'Tom', 'Iva']

for k in kupci:
    if k not in lojalni_kupci:
        print(f'Postovani {k}, imamo specijalnu ponudu za vas da postanete lojalni clan!')