while True:
    w = int(input())
    if w in range(1, 101):
        break
if w % 2 == 0 and w != 2:
    print('YES')
else:
    print('NO')