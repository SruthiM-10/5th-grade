'''
We have a loud talking parrot.
The "hour" parameter is the current hour time in the range 0..23.
We are in trouble if the parrot is talking and the hour is before 7 or after 20.
Return True if we are in trouble.
'''

def parrot_trouble(talking, hour):
  for i in range(0,24):
    if (i == hour and ( i<7 or i>20 )) and talking:
      return True
      break
    if (i == hour and ( i<7 or i>20 )) and not talking:
      return False
      break
    if i>hour :
      return False
      break


print(parrot_trouble(True,6))