'''
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
'''
weekday1 = bool(input("Enter True if today is a weekday. Otherwise, enter False."))
vacation1 = bool(input("Enter True if you are on vacation. Otherwise, enter False."))
def sleep_in(weekday, vacation):
  if weekday is True and vacation is True:
    return True
  elif vacation is False and weekday is False:
    return True
  elif vacation is True or weekday is False:
    return True
  else:
    return False


print(sleep_in(weekday1,vacation1))