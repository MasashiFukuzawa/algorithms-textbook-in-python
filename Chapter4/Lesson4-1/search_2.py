data = [57, 48, 46, 52, 45, 59, 60, 61, 49, 71]
n = len(data)
key = 60
i = 0
while i < n and data[i] != key:
    i += 1
if i == n:
    print(f'{str(key)}は存在しません')
else:
    print(f'data[{i}]が{key}です')
