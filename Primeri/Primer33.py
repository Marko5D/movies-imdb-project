def ukupno_vreme(lista_sati):
    ukupno = 0
    for sati in lista_sati:
        ukupno += sati

    return f'Ukupno si proveo {ukupno} sati na zadacima'