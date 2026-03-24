def ukupno_vreme(iznos):
    if iznos > 2500:
        return True
    else:
        return False

print(ukupno_vreme(3000))
print(ukupno_vreme(2500))
print(ukupno_vreme(1800))