F = 99999
way = [
    [F, 3, 2, 5, F, F, F],
    [3, F, F, F, 7, F, F],
    [2, F, F, 2, F, 4, F],
    [5, F, 2, F, F, 1, F],
    [F, 7, F, F, F, 4, 5],
    [F, F, 4, 1, 4, F, 3],
    [F, F, F, F, 5, 3, F],
]
dist = [F] * 7
flg = [0] * 7
route = [-1] * 7
start = 0
p = start
dist[p] = 0
print('始点', p)

for i in range(7):
    print(f'{i + 1}回目のループ ------------')
    d = F
    for j in range(7):
        if flg[j] == 0 and dist[j] < d:
            p = j
            d = dist[j]
    print(f'{p=}')
    flg[p] = 1
    for k in range(7):
        if dist[p] + way[p][k] < dist[k]:
            dist[k] = dist[p] + way[p][k]
            route[k] = p
            print(f'{k=}')
    print(f'{flg=}')
    print(f'{dist=}')

print('各ノードまでの距離')
print(f'routeの値 {route}')
e = int(input('道順を示す終点ノードの番号は？ '))
while route[e] >= 0:
    print(e, end='<-')
    e = route[e]
print(start)
