iskorisceni_kuponi = 0
preostali_dani = 10
while iskorisceni_kuponi < 100 and preostali_dani >=3:
    iskorisceni_kuponi += 10
    preostali_dani -= 1
    print('Kuponi:', iskorisceni_kuponi, 'Dan', preostali_dani)
    print('Promocija je zavrsena.')