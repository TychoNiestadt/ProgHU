studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde(studentencijfers):
    gemiddeldeList = []
    for lst in studentencijfers:
        gemiddeldeList.append(sum(lst)/len(lst))
    return gemiddeldeList

def gemiddeldtotaal(studentencijfers):
    alleGemiddelde = 0
    for lst in studentencijfers:
        alleGemiddelde += (sum(lst)/len(lst))
    return alleGemiddelde/len(studentencijfers)

print(gemiddelde(studentencijfers))
print(gemiddeldtotaal(studentencijfers))