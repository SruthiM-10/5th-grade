def plant_trees(w,g):
	s = (w -1)*4
	if s%(g+1)==0:
		return s/(g+1)
	else:
		return 0
print(plant_trees(3,1))