'''
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
We are in trouble if they are both smiling or if neither of them is smiling.
Return True if we are in trouble.
'''
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif a_smile or b_smile :
    return False
  if a_smile == False and b_smile == False:
    return True

print(monkey_trouble(True,False))