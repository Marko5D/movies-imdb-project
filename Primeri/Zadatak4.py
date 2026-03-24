ocene = [5, 4, 3, 5, 2, 4, 5]

# 1. Izracunavanje prosecne ocene pomocu petlje
zbir = 0
ukupno = 0
for ocena in ocene:
    zbir += ocena
    ukupno += 1

prosek = zbir / ukupno

# 2. Brojanje petica
broj_petica = 0
for ocena in ocene:
    if ocena == 5:
        broj_petica += 1

print(f'Prosek = {prosek}')
print(f'Ocene 5 = {broj_petica}')