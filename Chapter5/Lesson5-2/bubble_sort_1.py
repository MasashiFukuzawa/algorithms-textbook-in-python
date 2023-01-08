data = [9, 3, 7, 1, 4, 2, 5, 8, 6, 0]
n = len(data)
print(data, '元のデータ')

for i in range(0, n - 1):
    for j in range(n - 1 , 0, -1):
        if data[j-1] > data[j]:
            data[j], data[j-1] = data[j-1], data[j]

print(data, 'ソート後のデータ')
