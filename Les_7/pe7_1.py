def convert(x):
    for i in range(-30, 41, 10):
        f = x * 1.8 + 32
        return f

def table():
    for i in range(-30, 41, 10):
        print('{:5} {:3}'.format(str(convert(i)), str(i)))
print('{:5} {:3}'.format("F", "C"))
table()