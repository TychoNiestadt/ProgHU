'''Schrijf een programma dat het bestand kaartnummers.txt opnieuw opent en het aantal regels en het grootste kaartnummer in het bestand bepaalt. Print deze gegevens vervolgens uit:

Uitvoer:

Deze file telt 6 regels
Het grootste kaartnummer is: 645345 en dat staat op regel 4'''
def teller():
    lezen = open('kaartnummers.txt', 'r')
    linelist = lezen.readlines()
    kaartnummers = []
    for kaartnum in linelist:
        split = kaartnum.split(', ')
        kaartnummers.append(int(split[0]))
        print('Deze file telt {} regels\nHet grootste kaartnummer is: {} en dat staat op regel {}'.format(len(linelist), max(kaartnummers), kaartnummers.index(max(kaartnummers))+1))
teller()