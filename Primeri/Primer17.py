# Pocetne vrednosti
zalihe = 50
vreme_do_isporuke = 8

# While petlja traje dok ima zaliha i dok vreme nije isteklo
while zalihe > 0 and vreme_do_isporuke > 0:
    print(f'Zalihe: {zalihe}, Preostalo vreme: {vreme_do_isporuke}h')

    # Upozorenje za kriticno nizak nivo zaliha
    if zalihe < 10:
        print('Upozorenje: Kriticno nizak nivo zaliha!')

    # Simulacija obraade narudzbine
    zalihe -= 7
    vreme_do_isporuke -= 1

# Provera razloga prekida
if zalihe <= 0:
    print('Zalihe su potrosene - narudzbine su zatvorene!')
elif vreme_do_isporuke <= 0:
    print('Istekao rok za isporuku - narudzbine su zatvorene!')