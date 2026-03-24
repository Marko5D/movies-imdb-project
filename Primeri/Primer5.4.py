# Unos podataka za prvog kupca
ime1 = input('Unesi ime prvog kupca: ')
kupovine1 = int(input('Unesite broj kupovina prvog kupca: '))

# Unos podataka za drugog kupca
ime2 = input('Unesite ime drugog kupca: ')
kupovine2 = int(input('Unesite broj kupovina drugog kupca: '))

# Racunanje ukupnog broja kupovina
ukupno = kupovine1 + kupovine2
print(f'Kupci {ime1} i {ime2} su zajedno ostvarili {ukupno} kupovina.')

# Bonus zadatak
ime = input('Unesi ime kupca: ')
godine = int(input('Unesi starost kupca: '))
kupovine = int(input('Unesi broj kupovina kupca: '))
print(f'Kupac {ime}, star {godine} godina, ostvario je {kupovine} kupovina.')