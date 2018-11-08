#invoer
x = float(input('Geef de waarde voor x: '))

#berekeningen
from math import sqrt

if x == 2:
    mes:('{:.2f}{}'.format(x, ' is nulpunt van f'))
elif x > 2:
    mes:('f({:.2f}) = {:.2f}'.format(x, sqrt(x - 2)))
else:
    mes:('{:.2f} {}'.format(x, '∉ dom(f)'))

#uitvoer
print(mes)

