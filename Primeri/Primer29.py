kupci = ['Sara', 'Tom', 'Lena', 'Marko', 'Ana']
lojalni_club = ['Tom', 'Lena', 'Ana']
premium_club = ['Ana']

for kupac in kupci:
    if kupac in premium_club:
        print(f'Postovani/a {kupac}, imate ekskluzivan pristup nasoj premium ponudi!')
    elif kupac in lojalni_club and kupac not in premium_club:
        print(f'Dragi/a {kupac}, hvala na lojalnosti! Ocekuje Vas posebna ponuda.')
    else:
        print(f'Postovani/a {kupac}, pridruzite se nasem klubu i uzivajte u pogodnostima!')