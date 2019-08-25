def findSumdigit(i):
	s = 0
	while(i):
		s = s + i%10
		i = i/10
	return s

t = input()
for test in range(t):
	n = input()
	n = n * 10
	begin = n
	end = n + 10
	num = 0
	for i in range(begin, end + 1, 1):
		p = findSumdigit(i)
		if p % 10 == 0:
			num = i
			break
	print num
