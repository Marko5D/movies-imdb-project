def ukupno_vreme(cena, popust):
    nova_cena = cena - (cena * popust/100)
    return nova_cena