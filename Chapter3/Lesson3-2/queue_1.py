"""リングバッファを用いてキューのデータ構造を実装
"""

MAX = 6  # キューのデータ総数 + 1 を定義
queue = [0] * MAX
head = 0
tail = 0

def enqueue(value: int) -> None:
    global tail
    next_position = (tail + 1) % MAX  # ここで次の位置を指定しておくのがポイント
    if next_position == head:
        print('これ以上データを入れられません')
        return
    queue[tail] = value
    tail = next_position
    print(f'データ{value}を追加しました')

def dequeue() -> None:
    global head
    value = None
    if tail > head:
        value = queue[head]
        head = (head + 1) % MAX  # ここでheadを次の位置にするのがポイント
    else:
        print('取り出すデータが存在しません')
    print(f'取り出したデータ{value}')

for i in range(6):
    enqueue(i)
for i in range(6):
    dequeue()
