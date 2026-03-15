# 1. Unos i validacija imena i prezimena
while True:
    puno_ime = input('Unesite ime i prezime: ').strip()
    if ' ' in puno_ime:
        ime, prezime = puno_ime.split(' ', 1)
        break
    else:
        print('Ime nije dobro uneto. Pokusajte ponovo.')

# 2. Unos broja kupovina (mora biti pozitivan broj)
while True:
    broj_kupovina = int(input('Unesite broj kupovina u poslednjih godinu dana: '))
    if broj_kupovina > 0:
        break
    else:
        print('Broj kupovina mora biti pozitivan.')

# 3. Unos iznosa kupovina i racunanje ukupnog iznosa
ukupan_iznos = 0
kupovine_preko_10000 = 0

for i in range(broj_kupovina):
    iznos = float(input(f'Unesite iznos za kupovinu {i + 1}:'))
    ukupan_iznos += iznos
    if iznos > 10000:
        kupovine_preko_10000 += 1

# 4. Odredjivanje statusa korisnika
def odredi_status(ukupan_iznos, broj_kupovina):
    if ukupan_iznos > 10000 and broj_kupovina > 10:
        return 'VIP'
    else:
        return 'STANDARD'
    
status = odredi_status(ukupan_iznos, broj_kupovina)

# 5. Odredjivanje popusta
if status == 'VIP':
    popust = 0.10
else:
    popust = 0.05

# 6. Unos cene proizvoda i racunanje cene sa popustom
cena_prozivoda = float(input('Unesite cenu proizvoda: '))
cena_sa_popustom = cena_prozivoda * (1 - popust)

# 7. Prikaz rezultata
print('\n---REZULTATI---')
print(f'Korisnik: {ime} {prezime}')
print(f'Ukupan potrosen iznos: {ukupan_iznos:.2f} din')
print(f'Broj kupovina preko 10.000 din: {kupovine_preko_10000}')
print(f'Status korisnika: {status}')
print(f'Cena sa popustom: {cena_sa_popustom:.2f} din')