# Unos podataka
zalihe = int(input('Unesite broj preostalih zaliha: '))
broj_prodatih = int(input('Unesite broj prodatih jedinica: '))

# Provera uslova
if zalihe < 50 and broj_prodatih > 200:
    print('Zalihe su niske, a prodaja je visoka - preporucuje se hitna narudzbina.')
elif zalihe >= 50 and broj_prodatih >200:
    print('Prodaja je visoka, ali zalihe su dovoljne.')
elif broj_prodatih <= 200:
    print('Prodaja nije premasila 200 jedinica - preporucuju se promotivne akcije.')
else:
    print('Stanje prodaje i zaliha je stabilno.')