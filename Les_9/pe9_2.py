while True:
    woord = input('Geef een woord van 4 letters: : ')
    if len(woord) == 4:
        print('Inlezen van correcte woord: {} is geslaagd'.format(woord))
        break
    elif len(woord) <= 3:
        print('Dit is geen string van 4 letters!')
    elif len(woord) <= 5:
        print('Dit is geen string van 4 letters!')
print('{} heeft {} letters'.format(woord, len(woord)))