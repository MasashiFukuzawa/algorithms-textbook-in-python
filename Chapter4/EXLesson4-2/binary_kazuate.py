import random

n = 0
r = random.randint(1, 100)
print('1から100の数を当てるゲームです')

left = 0
right = 99

while True:
    mid = (left + right) // 2
    print(mid)
    n += 1
    if r == mid:
        print(f'{str(n)}回で正解です')
        break

    if r > mid:
        print('それより大きい数です')
        left = mid + 1
    else:
        print('それより小さい数です')
        right = mid - 1
