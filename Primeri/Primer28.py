# Definisanje lista kupaca i clanova
kupci = ['Ana', 'Marko', 'Ivana', 'Lena']
premium_club = ['Ana']
lojalni_club = ['Ana', 'Marko', 'Ivana']

# Koriscenje for petlje za prolazak kroz sve kupce
for kupac in kupci:
    if kupac in premium_club:
        print(f'Postovani/a {kupac}, imate ekskluzivan pristup premium ponudi!')
    elif kupac in lojalni_club:
        print(f'Dragi/a {kupac}, hvala sto ste lojalni kupac! Imamo posebnu ponudu za Vas.')
    elif not kupac in lojalni_club:
        print(f'Postovani/a {kupac}, postanite nas lojalni clan i uzivajte u benefitima!')