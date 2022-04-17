while True:
    x = int(input())
    if x in range(1, 1_000_000):
        break
one_move = [1, 2, 3, 4, 5]
for i in one_move:
    if x % i == 0:
        print(int(x/i))
        break