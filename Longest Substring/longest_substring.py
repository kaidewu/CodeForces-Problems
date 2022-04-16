while True:
    string = input()
    if len(string) in range(1, 10000):
        break
str_list = []
for i in range(len(string)):
    if i == (len(string) - 1):
        break
    if string[i] != string[i+1]:
        if string[i] not in str_list and string[i+1] not in str_list:
            str_list.append(string[i])
            str_list.append(string[i+1])
        elif string[i] not in str_list:
            str_list.append(string[i])
        elif string[i+1] not in str_list:
            str_list.append(string[i+1])
result = ''.join(str_list)
print(result)