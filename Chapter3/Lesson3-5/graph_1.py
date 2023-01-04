data = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0],
]
node = ['(0)', '(1)', '(2)', '(3)', '(4)']

for y in range(len(data)):
    for x in range(y, len(data[y])):
        if data[y][x] == 1 and data[x][y] == 1:
            print(f'{node[y]}<->{node[x]}')
