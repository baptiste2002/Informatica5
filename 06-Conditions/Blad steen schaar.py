speler_1 = input('Blad steen schaar? ')
speler_2 = input('Blad steen schaar? ')

if speler_1 == 'blad' and speler_2 == 'steen':
    print('speler 1 wint')
elif speler_1 == 'schaar' and speler_2 == 'blad':
    print('speler 1 wint')
elif speler_1 == 'steen' and speler_2 == 'schaar':
    print('speler 1 wint')
elif speler_1 == speler_2:
    print('onbeslist')
else:
    print('speler 2 wint')
