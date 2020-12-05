def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif a_smile or b_smile :
    return False
  if a_smile == False and b_smile == False:
    return True

print(monkey_trouble(True,False))