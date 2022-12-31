MAX = 5
stack = [0] * MAX
stack_pointer = 0

def push(value: int) -> None:
    global stack_pointer
    if stack_pointer < MAX:
        stack[stack_pointer] = value
        stack_pointer += 1
        print(f'データ {value} を追加しました')
    else:
        print(f'これ以上データを入れられません')

def pop() -> None:
    global stack_pointer
    value = None
    if stack_pointer > 0:
        stack_pointer -= 1
        value = stack[stack_pointer]
    else:
        print('取り出すデータが存在しません')
    print(f'取り出したデータ {value}')

for i in range(6):
    push(i)
for i in range(6):
    pop()
