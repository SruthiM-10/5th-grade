# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
def test_distinct(data):
  if len(data) == len(set(data)):
    print("True")
  else:
    print("false")
test_distinct([1,5,7,9])
test_distinct([2,4,5,5,7,9])
