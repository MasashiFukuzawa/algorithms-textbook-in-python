import random

n = 15
data = [0] * n
for i in range(n):
    data[i] = random.randint(1, 99)
print(data, '元のデータ')

for i in range(1, n):
    tmp = data[i]
    j = i
    while j > 0 and data[j - 1] > tmp:
        data[j] = data[j - 1]
        j -= 1
    data[j] = tmp

print(data, 'ソート後のデータ')
