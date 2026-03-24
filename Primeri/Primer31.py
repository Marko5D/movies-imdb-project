ocene_komentara = [4, 2, 3, 5, 1, 3, 4]

for ocena in ocene_komentara:
    if ocena < 3:
        continue
    elif ocena == 5:
        break
    else:
        print(ocena)