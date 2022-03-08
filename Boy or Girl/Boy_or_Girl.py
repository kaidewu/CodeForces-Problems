username = input()
dis_char = 0
if username == '' and len(username) > 100:
    pass
for char in username:
    for i in range(len(username) - 1):
        if char != username[i]:
            dis_char += 1
if dis_char % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')