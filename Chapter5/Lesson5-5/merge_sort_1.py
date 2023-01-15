import random

n = 15
data = [0] * n
for i in range(n):
    data[i] = random.randint(1, 99)

def merge(left: int, mid: int, right: int) -> None:
    buff = [0] * (right - left)
    i = left
    j = mid
    p = 0
    while i < mid and j < right:
        if data[i] <= data[j]:
            buff[p] = data[i]
            i += 1
        else:
            buff[p] = data[j]
            j += 1
        p += 1
    while i < mid:
        buff[p] = data[i]
        i += 1
        p += 1
    while j < right:
        buff[p] = data[j]
        j += 1
        p += 1
    for n in range(left, right):
        data[n] = buff[n - left]

print(data, '元のデータ')
s = 2
while s <= n:
    loop = n // s
    fragment = n % s
    for i in range(loop):
        merge(i * s, i * s + (s // 2), i * s + s)
    if fragment > 0:
        merge((loop - 1) * s, loop * s, n)
    s *= 2
print(data, 'ソート後のデータ')
