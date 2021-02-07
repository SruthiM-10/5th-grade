# Create a function that takes in a year and returns the correct century.
def century(year):
	first_two = int(str(year)[:2])
	if year % 100 == 0:
		return str(first_two) + 'th century'
	elif first_two + 1 == 21:
		return '21st century'
	else:
		return str(first_two+1) + 'th century'
print(century(1000))