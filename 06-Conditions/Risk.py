x = int(input('Aantal gegooide ogen: '))
y = int(input('Aantal gegooide ogen: '))
z = int(input('Aantal gegooide ogen: '))
a = int(input('Aantal gegooide ogen: '))
b = int(input('Aantal gegooide ogen: '))

getal_2 = float(x + y + z) - max(x, y, z) - min(x, y, z)

if max(x, y, z) > max(a, b):
    if getal_2 > min(a, b):
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    elif getal_2 <= min(a, b):
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
elif max(x, y, z) <= max(a, b):
    if getal_2 <= min(a, b):
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
    elif getal_2 > min(a, b):
        print('aanvaller verliest 1 leger, verdediger verliest 1 leger')