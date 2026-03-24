# Unos podataka
broj_prodatih = int(input('Unesite broj prodatih jedinica: '))
zalihe = int(input('Unesite broj preostalih jedinica na zalihama:'))

# Provera prodaje
if broj_prodatih > 200:
    print('Prodaja je izuzetno visoka!')
    if zalihe < 50:
        print('Zalihe su niske - HITNO naruciti dodatne proizvode!')
    else:
        print('Zalihe su jos uvek dovoljne, ali pratiti stanje.')
elif broj_prodatih > 100:
    print('Prodaja je bila uspesna.')
else:
    print('Prodaja je ispod ocekivanja. Predloziti promotivne akcije.')

# Provera zaliha (opsta)
if zalihe < 50:
    print('Upozorenje: Zalihe su niske!')
else:
    print('Zalihe su na zadovoljavajucem nivou.')