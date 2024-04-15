a = "abcde"
print(a[2:3])

a = (10, 11, 12, 13, 14)
print(a[1:4])

a = [4, 5, 6, 7, 8, 9]
print(a[0:3])

a = "Kalle Blomvist"
print(a[:5])
print(a[6:])

a = list("sara")
print(a)

print(list((1,2,3)))

a = "Hej på dej du"
print(a.split())

s = 'Nisse'
namn = list(s)
print(namn)
print('__'.join(namn))
print(''.join(namn))

#namn[3] = 10
#print(''.join(namn))

telefon = {'Anders':112233, 'Lisa':454545, 'Bertil':123456}
print(telefon['Bertil'])

for a, b in telefon.items():
    print(a, 'telnr:', b)

for namn in sorted(telefon.keys()):
    print(namn, '=', telefon[namn])



