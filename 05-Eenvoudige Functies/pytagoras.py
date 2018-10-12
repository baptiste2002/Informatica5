a = float(input('Geef lengte lange zijde : '))
b = float(input('Geef lengte korte zijde : '))
c = 'schuine_zijde'

from math import sqrt

schuine_zijde = sqrt((a ** 2) + (b ** 2))

print('{} {:.2f} {} {:.2f} {} {:.2f}'.format('In een rechthoekige driehoek met rechthoekszijden a = ', float(a), ' en b = ', float(b), ' is de schuine zijde ', schuine_zijde))