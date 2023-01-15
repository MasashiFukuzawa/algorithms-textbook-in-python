data = [8, 4, 2, 6, 5, 7, 3, 1]
n = len(data)
print(data, '元のデータ')

def merge_sort(left: int, right: int) -> None:
    mid = (left + right) // 2
    if left < mid - 1:
        merge_sort(left, mid)
    if mid < right - 1:
        merge_sort(mid, right)
    buff = [0] * (right - left)
    i = left
    j = mid
    p = 0
    while i < mid and j < right:
        if data[i] <= data[j]:
            buff[p] = data[i]
            i += 1
        else:
            buff[p] = data[j]
            j += 1
        p += 1
    while i < mid:
        buff[p] = data[i]
        i += 1
        p += 1
    while j < right:
        buff[p] = data[j]
        j += 1
        p += 1
    for n in range(left, right):
        data[n] = buff[n - left]

merge_sort(0, n)
print(data, 'ソート後のデータ')
