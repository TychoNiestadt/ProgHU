excuse = 'I am sick'
excuse1 = "I am sick"
''' Standaard string'''
print(excuse)
print(excuse1)

excuse = 'I\'m sick'
print(excuse)
''' De \ toont aan dat de \' bij de tekst hoort '''

excuse1 = 'I\'m ... \n ... "sick"'
print(excuse1)
''' De \n zorgt ervoor dat de tekst op de nieuwe regel begint'''

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(list)

'''
de letters van de list sorteren
list[0:2]
['a', 'b']
list[2:4]
['c', 'd']
list[0:3]
['a', 'b', 'c']
'''

''' String methods

s.capitalize() = Geeft een resultaat terug met het eerste character in hoofdletters
s.count() = Geeft een aantal met het opgegeven getal terug
s.find() = Geeft het eerste gevonden item weer
s.lower = Geeft een resultaat in kleine letters terug
s.replace(old, new) = Geeft een resultaat waar alle oude voorvallen worden vervangen met nieuwe.

s.split(sep) returns a list of substrings of s, delimited by sep????

s.strip returns copy of s without leading and trailing whitespace

s.upper returns uppercase copy of s
'''

prod = 'morels'
cost = 139
wght = 1/2
total = cost * wght
print(prod, cost, wght, total)
'''Dit print meerdere variables uit '''
'''OUTPUT FORMAT TYPE
TYPE    EXPLANATION
b       binary
c       character
d       decimal
X       hexadecimal
e       scientific
f       fixed-point   

OPEN FILE MODE
MODE    DESCRIPTION
r       Reading
w       Writing
a       Append
r+      Reading and Writing
t       Text(default)
b       Binary
'''


