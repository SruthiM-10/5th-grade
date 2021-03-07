'''Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself.
This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...
'''
def add_indexes(lst):
	lst1 = [lst[i]+i for i in range(0,len(lst))]
	return lst1

print(add_indexes([0,1,2,3,4,5]))