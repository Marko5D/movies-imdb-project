preferencije_kupaca = ['sport', 'moda', 'tehnologija', 'kućni uređaji', 'moda']

for preferencije in preferencije_kupaca:
    if preferencije == "sport":
        print('Specijalna ponuda za sportsku opremu!')
    elif preferencije == 'moda':
        print('Najnovije kolekcije po sniženim cenama!')
    elif preferencije == 'kućni uređaji':
        print('Popusti na kućne aparate koji će olakšati vaš život!')
    else:
        print('Pogledajte naše aktuelne ponude!')