# Unos broja kupaca za svaki dan u nedelji
ponedeljak = int(input('Unesite broj kupaca za ponedeljak: '))
utorak = int(input('Unesite broj kupaca za utorak: '))
sreda = int(input('Unesite broj kupaca za sredu: '))
cetvrtak = int(input('Unesite broj kupaca za cetvrtak: '))
petak = int(input('Unesite broj kupaca za petak: '))
subota = int(input('Unesite broj kupaca za subotu: '))
nedelja = int(input('Unesite broj kupaca za nedelju: '))

# 1. Ukupan broj kupaca za celu nedelju
ukupno = ponedeljak + utorak + sreda + cetvrtak + petak + subota + nedelja
print('\nUkupan broj kupaca u toku cele nedelje:', ukupno)

# 2. Ukupan broj kupaca za radne dane (ponedeljak-petak)
radni_dani = ponedeljak + utorak + sreda + cetvrtak + petak
print('Ukupan broj kupaca za radne dane:', radni_dani)

# 3. Ukupan broj kupaca za vikend (subota+nedelja)
vikend = subota + nedelja
print('Ukupan broj kupaca za vikend:', vikend)

# 4. Da li je u nedelju bilo vise kupaca nego u subotu?
if nedelja > subota:
    print('U nedelju je bilo vise kupaca nego u subotu.')
else:
    print('U subotu je bilo vise ili isti broj kupaca kao u nedelju.')

# 5. Da li je za pet radnih dana bilo vise kupaca nego za vikend?
if radni_dani > vikend:
    print('Za radne dane je bilo vise kupaca nego za vikend.')
else:
    print('Za vikend je bilo vise kupaca nego za radne dane.')

# 6. Provera da li je nedelja uspesna
    # Nedelja je uspesna ako:
    # - ukupno > 1000 kupaca
    #  ili
    # - vikend > 500 kupaca
if ukupno > 1000 or vikend > 500:
    print('Nedelja je bila uspesna!')
else:
    print('Nedelja nije bila uspesna.')