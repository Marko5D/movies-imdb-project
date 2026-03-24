komentari = [
    "Odlično!",
    "Brza isporuka i sjajna usluga.",
    "Preskupo",
    "Kampanja je bila odlična.",
    "Problem sa narudžbinom.",
    "Sve je u redu.",
    "Lako je naručiti, hvala!"
]

for komentar in komentari:
    if " " not in komentar:
        print(f"Jednostavan komentar preskočen: '{komentar}'")
        continue
    print(f"Komentar '{komentar}' je ok.")
    if "problem" in komentar:
        print(f"Sumnjiv komentar pronađen: '{komentar}'. Prekidamo pregled.")
        break
    print(f"Analiziramo komentar: '{komentar}'")