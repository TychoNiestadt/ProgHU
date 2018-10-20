invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

lst = invoer.split("-")

for i in range(len(lst)):
    lst[i] = int(lst[i])

maxGetal = max(lst)
minGetal = min(lst)
aantalGetallen = len(lst)
somGetallen = sum(lst)
gemiddelde = sum(lst)/len(lst)


print("Gesorteerde list van ints: {}".format(lst))
print("Grootste getal: {} en Kleinste getal: {}".format(maxGetal, minGetal))
print("Aantal getallen: {} en Som van de getallen: {}".format(aantalGetallen, somGetallen))
print("Gemiddelde: {}".format(gemiddelde))


# alles in een regel print("Gesorteerde list van ints: {}\nGrootste getal: {} en Kleinste getal: {}\nAantal getallen: {} en Som van de getallen: {}\nGemiddelde: {}".format(lst, maxGetal, minGetal, aantalGetallen, somGetallen, gemiddelde))