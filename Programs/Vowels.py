def count_vowels(txt):
	v = 'aeiou'
	count = 0
	for i in txt:
		for n in v :
			if i == n:
				count = count + 1
		print(count)

count_vowels('Celebration')