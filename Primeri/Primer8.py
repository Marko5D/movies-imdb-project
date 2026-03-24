iznos_kupovine = float(input('Unesite iznos kupovine: '))

if iznos_kupovine < 100:
    print('Nema popusta.')
else:
    if 100 <= iznos_kupovine <= 500:
        print('Kupac dobija 5% popusta.')
    elif 500 < iznos_kupovine <=1000:
        print('Kupac dobija 10% popusta.')
    else:
        print('Kupac dobija 15% popusta.')