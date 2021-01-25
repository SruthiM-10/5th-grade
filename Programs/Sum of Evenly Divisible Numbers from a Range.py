def evenly_divisible(a, b, c):
	count = 0
	for i in range(a,(b+1)):
		if i%c == 0:
			count = count + i
	return count
print(evenly_divisible(1,10,2))