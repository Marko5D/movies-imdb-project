koraci = [8450, 10234, 12000, 9800, 15000, 4000, 11000]

ukupno = 0
preko_10000 = 0

for k in koraci:
    ukupno += k
    if k > 10000:
        preko_10000 += 1

print('Ukupan broj koraka za nedelju:', ukupno)
print('Broj dana sa vise od 10.000 koraka:', preko_10000)