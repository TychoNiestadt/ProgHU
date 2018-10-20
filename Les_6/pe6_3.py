lengte = int(input('Voer je lengte in \'cm\':'))

def f (lengte):
    if lengte >= 120:
        print('Je bent lang genoeg voor de atrractie!')
    elif lengte <= 119:
        print('Sorry, je bent te klein!')
f(lengte)