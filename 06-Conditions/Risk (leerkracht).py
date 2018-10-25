a1 = int(input('Aantal gegooide ogen: '))
a2 = int(input('Aantal gegooide ogen: '))
a3 = int(input('Aantal gegooide ogen: '))
v1 = int(input('Aantal gegooide ogen: '))
v2 = int(input('Aantal gegooide ogen: '))

#sorteren
sa1 = max(a1, a2, a3)
sa3 = min(a1, a2, a3)
sa2 = a1 + a2 + a3 - sa1 - sa3
#tussen het programmeren door als controle: print(sa1, sa3)

sv1 = max(v1, v2)
sv2 = min(v1, v2)
#tussen het programmeren door als controle: print(va1, va3)

#winnaar bepalen
if sa1 > sv1 and sa2 > sv2:
    mes = 'aanvaller verliest 0 legers, verdediger verliest 2 legers'
elif sv2 >= sa1 and sv2 >= sa1:
    mes = 'aanvaller verliest 2 leger, verdediger verliest 0 legers'
else:
    mes = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'
#uitvoer
print(mes)