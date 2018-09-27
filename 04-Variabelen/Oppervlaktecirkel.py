#invoer
r = float(input('Geef straal: '))

pi = 3.14159

#berekening
opp_cirkel = pi * (r**2)

#uitvoer
#De oppervlakte van een cirkel met straal 4.2222 is 56.0050396044156
resultaat = 'De oppervlakte van een cirkel met straal '
resultaat += str(r) + ' is ' + str(opp_cirkel)

print(resultaat)