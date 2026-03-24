# Unapred određeni maksimalan broj iskorišćenih kupona
maksimalan_broj_kupona = 100
 
# Trenutni broj iskorišćenih kupona
brojac_kupona = 0
 
while brojac_kupona < maksimalan_broj_kupona:
    brojac_kupona += 1  # Povećavamo brojač za svaki iskorišćeni kupon
    print(f"Kupon {brojac_kupona} je iskorišćen.")
     
print(f"Ukupan broj iskorišćenih kupona: {brojac_kupona}")