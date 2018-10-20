def namen():
    Allenamen = {}
    while True:
        naam = input('Volgende naam: ')
        if naam == '':
            break
        else:
            if naam in Allenamen:
                Allenamen[naam] += 1
            else:
                Allenamen[naam] = 1

    return Allenamen.items()

for i in namen():
    if i[1] == 1:
        print('Er is {} student met de naam {}'.format(i[1], i[0]))
    else:
        print('Er zijn {} studenten met de naam {}'.format(i[1], i[0]))