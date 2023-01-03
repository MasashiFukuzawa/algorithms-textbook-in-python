from typing import List

MAX = 5
data = [None] * MAX
pointer = [None] * MAX
head = 0

def filtered_data() -> List[int]:
    return list(filter(lambda x: x is not None, data))

def add_list(value: int) -> None:
    if len(filtered_data()) == MAX:
        print('データ領域に空きがありません')
        return

    idx = data.index(None) if filtered_data() else 0
    data[idx] = value
    pointer[idx] = idx + 1 if idx + 1 < MAX else None
    print(f'データ {value} を追加しました')

def delete_list(value: int) -> None:
    try:
        idx = data.index(value)
    except ValueError:
        print('そのデータは存在しません')
        return

    data[idx] = None
    pointer[idx] = None
    print(f'データ {value} を削除しました')

    global head
    for i in range(MAX):
        if data[i] is not None:
            head = i
            break
        head = 0

def print_list() -> None:
    if not filtered_data():
        return
    str_values = list(map(lambda x: str(x), filtered_data()))
    print('->'.join(str_values), end='->EOF')

for i in range(10, 70, 10):
    add_list(i)
delete_list(10)
print_list()
