def ticker(filename):
    inFile = open(filename, 'r')
    lines = inFile.readlines()
    tickerDict = {}
    for line in lines:
        values = line.split(":")
        tickerDict[values[0]] = values[1].rstrip()
    return tickerDict

def tickerCompany(tickerName):
    dict = ticker("ticker.txt")
    companyName = ""
    for i in dict:
        if dict[i] == tickerName:
            companyName = i
            break
    return companyName

def companyTicker(companyName):
    dict = ticker("ticker.txt")
    tickerName = ""
    for i in dict:
        if i == companyName:
            tickerName = dict[i]
            break
    return tickerName

while True:
    print("1. Company to Ticker\n2. Ticker to Company")
    keuzen = int(input("Choose an option: "))
    if keuzen == 1:
        cName = input("Enter Company name: ")
        print("Ticker symbol: {}".format(companyTicker(cName)))
    elif keuzen == 2:
        tName = input("Enter Ticker symbol: ")
        print("Company name: {}".format(tickerCompany(tName)))
    else:
        break