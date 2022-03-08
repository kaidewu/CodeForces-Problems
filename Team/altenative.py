cases = int(input())
flag = 0
while cases>0:
    stand = list(map(int,input().split()))
    if(stand.count(1)>1):
        flag+=1
    cases-=1
print(flag)