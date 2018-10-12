a = int(input('Geef een getal van 1 tot 20 : '))
b = int(input('Geef een getal van 1 tot 20 : '))

uitkomst_1 = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format(a, b, (a+b))
uitkomst_2 = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format((a*10), (b*10),((a+b)*10))
uitkomst_3 = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format((a*10**2), (b*10**2), ((a+b)*10**2))
uitkomst_4 = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format((a*10**3), (b*10**3), ((a+b)*10**3))
uitkomst_5 = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format((a*10**4), (b*10**4), ((a+b)*10**4))

print(uitkomst_1)
print(uitkomst_2)
print(uitkomst_3)
print(uitkomst_4)
print(uitkomst_5)
