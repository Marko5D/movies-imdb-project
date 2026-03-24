# Lista sa statusom klijenata
klijenti = ['član', 'nije član', 'član', 'nije član', 'član']
 
for status in klijenti:
    if not status == 'član':  # Proveravamo da li klijent nije član
        print("Ovaj kupac nije član lojalnog kluba.")
    else:
        print("Posebna ponuda za lojalne članove!")