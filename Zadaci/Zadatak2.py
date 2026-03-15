# Unos broja kupaca za svaki dan
kupci_ponedeljak = int(input('Uesite broj kupaca za ponedeljak: '))
kupci_utorak = int(input('Unesite broj kupaca za utorak: '))
kupci_sreda = int(input('Unesite broj kupaca za sredu: '))
kupci_cetvrtak = int(input('Unesite broj kupaca za cetvrtak: '))
kupci_petak = int(input('Unesite broj kupaca za petak: '))
kupci_subota = int(input('Unesite broj kupaca za subotu: '))
kupci_nedelja = int(input('Unesite broj kupaca za nedelju: '))

# Ukupan broj kupaca za celu nedelju
ukupno_nedelja = (
    kupci_ponedeljak + kupci_utorak + kupci_sreda + 
    kupci_cetvrtak + kupci_petak + kupci_subota + kupci_nedelja)

print('\nUkupan broj kupaca za celu nedelju: ', ukupno_nedelja)

# Ukupan broj kupaca za radne dane
ukupno_radni_dani = (
    kupci_ponedeljak + kupci_utorak + kupci_sreda +
    kupci_cetvrtak + kupci_petak)

print('Ukupan broj kupaca za radne dane: ', ukupno_radni_dani)

# Ukupan broj kupaca za vikend
ukupno_vikend = kupci_subota + kupci_nedelja

print('Ukupan broj kupaca za vikend: ', ukupno_vikend)

# Poredjenje subote i nedelje
if kupci_nedelja > kupci_subota:
    print('Nedelja je bila bolji prodajni dan od subote.')
else:
    print('Subota je bila bolji prodajni dan od nedelje.')

# Poredjenje radnih dana i vikenda
if ukupno_radni_dani > ukupno_vikend:
    print('Radni dani su imali vise kupaca za vikend.')
else:
    print('Vikend je imao vise kupaca od radnih dana.')

# Provera vikenda preko 100 kupaca
if kupci_subota > 100 and kupci_nedelja > 100:
    print('Oba dana vikenda su imala vise od 100 kupaca.')
elif kupci_subota > 100 or kupci_nedelja > 100:
    print('Samo jedan dan vikenda je imao vise od 100 kupaca.')
else:
    print('Nijedan dan vikenda nije imao vise od 100 kupaca.')