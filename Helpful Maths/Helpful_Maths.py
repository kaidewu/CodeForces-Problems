while True:
    s = input()
    if len(s) in range(1, 101) and ' ' not in s:
        break
num = s.split('+')
num.sort()
print('+'.join(num))
