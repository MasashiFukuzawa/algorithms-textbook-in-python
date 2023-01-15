import random

n = 12
data = [0] * n

for i in range(n):
    data[i] = random.randint(1, 99)
print(data, '元のデータ')

# ヒープ作成
for i in range((n - 1) // 2, -1, -1):
    p = i
    c = 2 * p + 1
    while c < n:
        if c < n - 1 and data[c] < data[c + 1]:
            c += 1
        if data[p] >= data[c]:
            break
        data[c], data[p] = data[p], data[c]
        p = c
        c = 2 * p + 1
print(data, '初期ヒープ')

# 根を切り、ヒープを再構成
d = n - 1
while d > 0:
    data[0], data[d] = data[d], data[0]
    p = 0
    c = 2 * p + 1
    while c < d:
        if c < d - 1 and data[c] < data[c + 1]:
            c += 1
        if data[p] >= data[c]:
            break
        data[p], data[c] = data[c], data[p]
        p = c
        c = 2 * p + 1
    d -= 1
print(data, 'ソート後のデータ')
