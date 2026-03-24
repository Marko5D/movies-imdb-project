from Primer36 import calculate_discount
from Primer37 import check_vip_status

def process_purchase(cena, procenat):
    nova_cena = calculate_discount(cena, procenat)
    vip = check_vip_status(nova_cena)

    if vip:
        return f'Cestitamo! Sa popustom od {procenat}% ostvarili ste VIP status. Cena: {nova_cena}'
    else:
        return f'Sa popustom od {procenat}% cena iznosi {nova_cena}. Posetite nas ponovo i mozda postanete VIP clan!'
    
print(process_purchase(12000, 10))
print(process_purchase(9000, 5))
print(process_purchase(15000, 20))
print(process_purchase(8000, 10))