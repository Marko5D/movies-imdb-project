status = input('Unesite status (redovan/lojalnost): ').strip().lower()
iznos = float(input('Unesite iznos kupovine: '))

if status == 'redovan':
    if iznos < 100:
        popust = 0
    elif iznos <= 500:
        popust = 5
    else:
        popust = 10

elif status == 'lojalnost':
    if iznos < 100:
        popust = 5
    elif iznos < 500:
        popust = 10
    else:
        popust = 15

else:
    popust = None
    print("Nepoznat status kupca. Koristi 'redovan' ili 'lojalnost'")

if popust is not None:
    cena_posle = iznos * (1 - popust / 100)
    print(f'Popust: {popust}%')
    print(f'Cena posle popusta: {cena_posle:.2f}')