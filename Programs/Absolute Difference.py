'''
Given an int n, return the absolute difference between n and 21.
Return double the absolute difference if n is over 21.
'''
n = int(input("Enter an integer: "))
def diff21(n):
  if n < 21 :
    d = 21 - n
    return abs(d)
  if n > 21 :
    d = n - 21
    return 2 * abs(d)
  if n == 21 :
    return 0


print(diff21(n))
