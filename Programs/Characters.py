'''
Given a non-empty string and an int n, return a new string where the char at index n has been removed.
The value of n will be a valid index of a char in the original string
(i.e. n will be in the range 0..len(str)-1 inclusive).
'''
def missing_char(str, n):
  front = str[0:n]   # up to but not including n
  back = str[n+1:len(str)]  # n+1 through end of string
  return front + back

print(missing_char('Ranjani',1))