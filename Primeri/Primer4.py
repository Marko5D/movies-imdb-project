ime = input("Unesite ime:")
prezime = input('Unesite prezime:')
devojacko_prezime = input('Unesite devojacko prezime:')
grad = input('Unesite grad:')


fantasy_name = ime[0:3] + prezime[0:2] + devojacko_prezime[0:2] + grad[0:2]
print(fantasy_name)