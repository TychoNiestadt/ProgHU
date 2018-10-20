#Functie voor de kluizen die vrij zijn
def toon_aantal_kluizen_vrij():
    kluizen = open("kluizen.txt", "r+") #opent het kluizen.txt moet wel in dezelfde folder staan.
    kluizenInGebruik = len(kluizen.readlines())
    kluizenVrij = 12 - kluizenInGebruik #maximale aantal
    print("Er zijn nog " + str(kluizenVrij) + " kluizen beschikbaar.")
    return kluizenVrij

#Funtie die een nieuwe kluis aanmaakt
def nieuwe_kluis(Nieuwepincode):
    kluizen = open('kluizen.txt', 'r+')
    kluisnummer = 1
    bezet = []
    lines = kluizen.readlines()
    for line in lines:
        bezet.append(int(line.split(";")[0]))
        bezet.sort()
    for i in bezet:
        if i == kluisnummer:
            kluisnummer += 1
    kluisUitgeven = str(kluisnummer) + ";" + str(Nieuwepincode) + "\n"
    kluizen.write(kluisUitgeven)
    print("Uw kluis is kluisje nummer:" + str(kluisnummer))
    return

#Functie die de kluis opent
def kluis_openen(kluisnummer, Nieuwepincode):
    a = False
    kluizen = open("kluizen.txt", "r+")
    lines = kluizen.readlines()
    if len(lines) == 0:
        print("Deze kluis en pin combinatie is niet correct!")
    for line in lines:
        if line == str(kluisnummer + ";" + Nieuwepincode + "\n"):
            print("Uw kluis wordt nu geopend")
            a = True
    if a == False:
        print("Deze kluis en pin combinatie is niet correct!")
    return

# keuze menu
def keuze_menu():
    print('Welkom bij de NS bagagekluizen!\n')
    print('Kies uw optie\n')
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn? \n')
    print('2: Ik wil een nieuwe kluis! \n')
    print('3: Ik wil even iets uit mijn kluis halen\n')
    print('4: Verlaat keuze menu')

keuze_menu()

keuze = int(input('Voer uw keuze in:'))


if keuze > 4 or keuze <= 0:
    print('Kies voor een optie tussen de 1 en 4')

elif keuze == 1:
    toon_aantal_kluizen_vrij()

elif keuze == 2:
    if toon_aantal_kluizen_vrij() == 0:
        print('Er zijn momenteel helaas geen kluizen vrij, kom op een later tijdstip terug!')
        exit()
    else:
        Nieuwepincode = input('Voer een pincode voor uw kluis in. (Minimaal 4 tekens)')
        while len(Nieuwepincode) < 4:
            print('Uw pincode is te kort. Minimaal 4 tekens!')
            Nieuwepincode = input('Voer een pincode voor uw kluis in. (Minimaal 4 tekens)')
        nieuwe_kluis(Nieuwepincode)

elif keuze == 3:
    kluisnummer = (input('Wat is het nummer van uw kluis?'))
    pincode = (input('Voer de pincode van het kluisje in!'))
    kluis_openen(kluisnummer, pincode)
    exit()

elif keuze == 4:
    print('Menu wordt afgesloten! Tot ziens!')
    exit()
#sluit het menu af
