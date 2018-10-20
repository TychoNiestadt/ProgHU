# De variable voor de funcite
leeftijd = abs(int(input("Voer je leeftijd in: ")))
weekendritInvoer = input("Reis je in het weekend? (Ja/Nee): ")
weekendrit = "null"
afstandKM = int(input("Wat is de afstand van uw reis? (In KM): "))

# Vraagt of er in het weekend gereden wordt
if weekendritInvoer== 'Ja':
    weekendrit = True
elif weekendritInvoer=="Nee":
    weekendrit = False

# Functie (standaardtarief)
def standaardtarief(afstandKM):
    if afstandKM > 50:
        p1 = 15 + (afstandKM * 0.60)
    elif afstandKM >= 0:
        p1 = afstandKM * 0.60
    else:
        p1 = 0
    return p1

# def = Defining in dit geval de functie(ritprijs)
def ritprijs(leeftijd, weekendrit, afstandKM):
    p1 = standaardtarief(afstandKM)
    if weekendrit==False and (leeftijd<12 or leeftijd>=65):
        p2 = p1 * 0.7
    elif weekendrit==True and (leeftijd<12 or leeftijd>=65):
        p2 = p1 * 0.65
    elif weekendrit==False and (leeftijd>=12 or leeftijd<65):
        p2 = p1
    else:
        p2 = p1 * 0.6
    return p2

# Het resultaat wat uitgeprint wordt!
print("Uw kaartje kost totaal: €" + str(round((ritprijs(leeftijd, weekendrit, afstandKM)),2)))

