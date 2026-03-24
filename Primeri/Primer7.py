vreme = "kisa"
temperatura = 10  # U stepenima Celzijusa
vetar = True
 
if vreme == "kiša" and temperatura < 15 and vetar:
        print("Ponesi kisobran i obuci vetrovku, hladno je!")
elif vreme == "sunce" and temperatura > 25:
        print('Obuci laganu odecu.')
else:
        print('Obuci nesto udobno')       