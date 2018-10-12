x = float(input('de waarde van x is : '))
y = float(input('de waarde van y is : '))

a = abs(abs(x)-abs(y))
b = abs(x-y)

antwoord = '{:.4f} ≤ {:.4f}'.format(float(a), float(b))

print(antwoord)


