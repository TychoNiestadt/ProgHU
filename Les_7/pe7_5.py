#Schrijf functie gemiddelde(), die de gebruiker vraagt om een willekeurige zin in te voeren. De functie berekent vervolgens de gemiddelde lengte van de woorden in de zin en print dit uit.

def gemiddelde(zin):
    woorden = zin.split(" ")
    aantalwoorden = len(woorden)
    aantalletters = 0
    for woord in woorden:
        aantalletters += len(woord)

    gemiddeld = aantalletters/aantalwoorden
    print('Deze opgegeven zin heeft {} woorden en elk woorden heeft gemiddeld {:.2f} letters'.format(aantalwoorden, gemiddeld))
    return

gemiddelde(input('Geef een willekeurige zin:'))
