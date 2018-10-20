import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y")
print(s)

def addloper(naam):
    file = open('hardlopers.txt', 'a')
    vandaag = datetime.datetime.today()
    file.write('{}, {}, {}\n'.format(vandaag.strftime("%a %d %b %Y"), vandaag.strftime('%X'), name))
#   schrijft in de file                voegt de tijd toe ^^ defineerd de tijd ^roept de tijd aan!
name = input('Wat is je naam: ')#functie de je naam vraagt!
addloper(name) #roept de functie addloperaan en gebruikt de input van name.
