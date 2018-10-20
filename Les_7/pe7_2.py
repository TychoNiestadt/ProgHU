def openfile():
    lezen = open('kaartnummers.txt', 'r') #opent het bestand kaartnummers.txt
    linelist = lezen.readlines() #leest alle regeld uit het bestand!
    for string in linelist: #
        info = string.split(", ") #split de string(Het bestand) op de ,+spatie
        print('{} heeft kaartnummer: {}'.format(info[1].replace('\n', ''), info[0]))
openfile() #roept de functie aan!