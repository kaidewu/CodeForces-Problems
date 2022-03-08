n = list(map(int,input().split()))
k = list(map(int,input().split()))
advance = 0
for i in range(n[0] - 1):
    if k[i] > n[1]:
        advance += 1
print(advance)