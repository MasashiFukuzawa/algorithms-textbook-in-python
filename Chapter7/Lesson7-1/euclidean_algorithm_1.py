print('a >= b となる自然数を入力してください')
a = int(input('a= '))
b = int(input('b= '))

while True:
    r = a % b
    # print(r, a, b)
    if r == 0:
        print('それらの最大公約数は', b)
        break
    a = b
    b = r
