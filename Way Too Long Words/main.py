while True:
	num = int(input())
	if num in range(1, 101):
		break
word_list = []
for i in range(num):
	while True:
		word = input()
		if len(word) in range(1, 101):
			break
	word_list.append(word.lower())
for each_word in word_list:
	if len(each_word) <= 10:
		print(each_word)
	else:
		print(each_word[0] + str(len(each_word[1:-1])) + each_word[-1])