# Unos podataka
broj_kupaca = int(input('Unesite broj kupaca: '))
popust_iskoriscen = input('Da li je popust iskoriscen (True/False)')

# Pretvaranje unosa u boolean
popust_iskoriscen = popust_iskoriscen == 'True'

# Provera uspesnosti prodaje
if broj_kupaca > 100 and popust_iskoriscen:
    print('Prodaja je uspesna!')
else:
    print('Prodaja nije uspesna!')