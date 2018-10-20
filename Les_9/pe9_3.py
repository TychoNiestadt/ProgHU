Dict = {'Tycho': 9, 'Romy': 3, 'Karin': 9, 'Nick': 8, 'Piet': 3, 'Jesse': 9, 'Anouk': 10, 'Stefan': 8, 'Maurits': 6}

for i in Dict:
    if Dict[i] >= 9:
        print('{} heeft een {}! '.format(i, Dict[i]))
    else:
        continue