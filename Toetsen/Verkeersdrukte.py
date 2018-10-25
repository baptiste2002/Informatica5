#invoer
Dv = float(input('Geef de verkeersdichtheid van de vrachtwagens: '))
Vv = float(input('Geef de snelheid van de vrachtwagens: '))
Da = float(input('Geef de verkeersdichtheid van de personenautos: '))
Va = float(input('Geef de snelheid van de personenautos: '))

#berekeningen
Pv = min(((Vv * Dv) / 40), 1)
Pa = min(((Va * Da) / 40), 1)

if min(Pv, Pa) > 0.7:
    mes = 'zwart'
elif max(Pv, Pa) > 0.7 and abs(Pv - Pa) < 0.2:
    mes = 'rood'
elif abs(Pv - Pa) > 0.7:
    mes = 'geel'
else:
    mes = 'groen'

#uitvoer
print(mes)