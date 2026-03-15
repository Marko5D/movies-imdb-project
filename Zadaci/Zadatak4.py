# Definisanje funkcije za brojanje samoglasnika
def broj_samoglasnika(ime):
    samoglasnici = ['a','e','i','o','u'
                    'A','E','I','O','U'
                    ]
    brojac = 0

    for slovo in ime:
        if slovo in samoglasnici:
            brojac += 1
    
    return brojac

# Postavljanje while petlje za kontinuirani unos
while True:
    ime = input('Unesite ime kupca: ')

    broj = broj_samoglasnika(ime)
# U zavisnosti od broja samoglasnika
    if broj == 0:
        print('Ime nema nijedan samoglasnik. Program se zavrsava.')
        break

    else:
        print(f"Ime '{ime}' ima {broj} samoglasnika.")