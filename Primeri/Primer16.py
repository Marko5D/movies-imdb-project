# Maksimalan broj kupona i vreme trajanja promocije
maks_kupona = 100
vreme_trajanja = 7
 
# Trenutni status
iskorisceni_kuponi = 0
preostalo_dana = vreme_trajanja
 
while (iskorisceni_kuponi < maks_kupona) and (preostalo_dana > 0):
    iskorisceni_kuponi += 15
    preostalo_dana -= 1
 
    # Dodatni uslov za upozorenje
    if maks_kupona - iskorisceni_kuponi < 5:
        print("Upozorenje: Ostalo je manje od 5 kupona!")
     
print(f"Istoršeno kupona: {iskorisceni_kuponi}, Preostalo dana: {preostalo_dana}")
 
print("Promocija je završena.")