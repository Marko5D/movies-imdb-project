# Definisanje funkcije za proveru VIP statusa
def vip_customer(amount):
    if amount > 10000:
        return True
    else:
        return False
# Pozivanje funkcije i prikazivanje rezultata
ans1 = vip_customer(1500)
print(f"Korisnik koji je potrošio 1500 dinara jeste VIP kupac: {ans1}")
ans2 = vip_customer(20000)
print(f"Korisnik koji je potrošio 20000 dinara jeste VIP kupac: {ans2}")