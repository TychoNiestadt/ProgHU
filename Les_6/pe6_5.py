def kwadraten_som(x):
    a = 0
    g = 0
    for g in x:
        if g > 0:
            g = g**2
            a += g
    return a
cijfers = [4, 5, 3, -81]
print(kwadraten_som(cijfers))