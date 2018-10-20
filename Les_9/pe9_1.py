totaal = []
while True:
    getal = int(input('Geef een getal:'))
    if getal == 0:
        break
    totaal.append(getal)
print('Er zijn {} getallen ingevoerd, de som is: {}'.format(len(totaal), sum(totaal)))