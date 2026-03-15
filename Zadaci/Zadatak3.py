# While petlja - program radi dok unos nije validan
while True:

    # Unos broja proizvoda
    broj_proizvoda = int(input('Unesi broj proizvoda: '))

    # Provera broja proizvoda
    if broj_proizvoda < 1 or broj_proizvoda > 50:
        print('Greska: Nevalidan broj proizvoda.')
        continue

    # Unos cene
    cena = float(input('Unesi cenu narudzbine: '))

    # Provera cene
    if cena <= 0:
        print('Greska: Cena mora biti veca od 0.')
        continue
    
# Unos statusa placanja
    status = input('Unesi status placanja: ')

    if status == 'placeno':
        print(f'Broj proizvoda: {broj_proizvoda}, cena: {cena}, status placanja: {status}')
        break
    elif status == 'neplaceno' or status == 'na cekanju':
        print('Narudzbina nije placena, ne moze biti obradena.')
        continue
    else:
        print('Greska: Nepoznat status placanja.')
        continue