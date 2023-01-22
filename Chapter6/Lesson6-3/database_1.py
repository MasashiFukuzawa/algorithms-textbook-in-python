HASH = 5
name = [None] * HASH
tel = [None] * HASH

def hash(key: str) -> str:
    h = 0
    for i in key:
        if i != ' ':
            h += ord(i)
    return h % HASH

while True:
    n = input('名前を入力してください ')
    if n == '':
        break
    t = input('電話番号を入力してください ')
    if t == '':
        break
    h = hash(n)
    name[h] = n
    tel[h] = t
    print('ハッシュ値', h, 'データ格納完了')

print(name)
print(tel)

while True:
    n = input('検索する名前は? ')
    if n == '':
        break
    h = hash(n)
    if name[h] == n:
        print(f'{n}さんの番号は{tel[h]}')
    else:
        print('その名前は登録されていません')
