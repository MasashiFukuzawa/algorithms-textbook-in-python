HASH = 5
name = [None] * HASH
tel = [None] * HASH

def hash(key: str) -> str:
    h = 0
    for i in key:
        if i != ' ':
            h += ord(i)
    return h % HASH

def open_add(n: str, t: str, h: int) -> None:
    flg = False
    for i in range(HASH - 1):
        h = (h + 1) % HASH
        if name[h] is None:
            name[h] = n
            tel[h] = t
            flg = True
            print('再ハッシュ', h, 'データ格納完了')
            break
    if flg == False:
        print('データを格納できる領域がありません')

def search_rehash(key: str, h: int):
    for i in range(HASH - 1):
        h = (h + 1) % HASH
        if name[h] == key:
            return h
    return -1

while True:
    n = input('名前を入力してください ')
    if n == '':
        break
    t = input('電話番号を入力してください ')
    h = hash(n)
    if name[h] == None:
        name[h] = n
        tel[h] = t
        print('ハッシュ値', h, 'データ格納完了')
    else:
        open_add(n, t, h)

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
        h = search_rehash(n, h)
        if h == -1:
            print('その名前は登録されていません')
        else:
            print(f'{n}さんの番号は{tel[h]}')
