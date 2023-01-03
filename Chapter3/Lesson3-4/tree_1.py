LEFT = 0
RIGHT = 1
DATA = 2
node = [
    [1, 2, 10],
    [3, 4, 20],
    [5, None, 30],
    [None, None, 40],
    [6, 7, 50],
    [None, None, 60],
    [None, None, 70],
    [None, None, 80],
]
MAX = len(node)

print('指定の番号のノードを調べます')
print('何も入力せずEnterを押すと終了します')

while True:
    s = input('number=')
    if not s:
        break

    target_idx = int(s)
    if not 0 <= target_idx < MAX:
        print(f'0から{MAX - 1}の範囲で入力してください')
        break

    left_idx = node[target_idx][LEFT]
    right_idx = node[target_idx][RIGHT]

    target = node[target_idx][DATA]
    left_child = node[left_idx][DATA] if left_idx else None
    right_child = node[right_idx][DATA] if right_idx else None

    print(f'node{target_idx}の値は{target}')
    print(f'左の子は{left_child or "存在しません"}')
    print(f'右の子は{right_child or "存在しません"}')
