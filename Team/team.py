while True:
	n = int(input())
	if n in range(1, 101):
		break
final = 0
for i in range(n):
	contest = input()
	contest = contest.split(' ')
	solution = 0
	for each_contest in contest:
		if int(each_contest) == 1:
			solution += 1
	if solution > 1:
		final += 1
print(final)