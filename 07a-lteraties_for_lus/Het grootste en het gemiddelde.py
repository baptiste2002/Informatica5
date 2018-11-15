aantal = int(input('Hoeveel getallen wil je geven: '))
grootste = - 1000000000000
alle_getallen = 0 

for i in range(aantal):
    getal = int(input('Geef een getal: '))
    if getal > grootste:
        grootste = getal
    alle_getallen += getal
    gemiddelde = (alle_getallen / aantal)


print('Het grootste getal is ' + str(grootste) + ' en het gemiddelde is ' + str('{:.2f}'.format(gemiddelde)))