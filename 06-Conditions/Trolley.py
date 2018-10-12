hendel_trekken = input('Trek aan de  hendel van de wissel? (ja/nee) ')

if hendel_trekken == 'ja':

    man_duwen = input('Man van brug duwen? (ja/nee) ')
    if man_duwen == 'ja':
        print('2')
    elif man_duwen == 'nee':
        print('1')

if hendel_trekken == 'nee':

    man_duwen = input('Man van brug duwen? (ja/nee) ')
    if man_duwen == 'ja':
        print('1')
    elif man_duwen == 'nee':
        print('5')
