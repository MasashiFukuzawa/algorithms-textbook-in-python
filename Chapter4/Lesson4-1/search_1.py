data = [57, 48, 46, 52, 45, 59, 60, 61, 49, 71]
n = len(data)
key = 60
flg = False
for i in range(n):
    if data[i] == key:
        print(f'data[{i}]が{key}です')
        flg = True
        break
if flg == False:
    print(f'{str(key)}は存在しません')
