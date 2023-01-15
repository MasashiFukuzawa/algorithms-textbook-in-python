a = [1, 3, 4, 7, 8, 9]
b = [0, 2, 5, 6]
na = len(a)
nb = len(b)
c = [0] * (na + nb)
i = 0
j = 0
p = 0

print(a, 'データa')
print(b, 'データb')

while i < na and j < nb:
    if a[i] < b[j]:
        c[p] = a[i]
        i += 1
    else:
        c[p] = b[j]
        j += 1
    p += 1

while i < na:
    c[p] = a[i]
    i += 1
    p += 1

while i < nb:
    c[p] = b[j]
    j += 1
    p += 1

print(c, 'マージ後のデータ')
