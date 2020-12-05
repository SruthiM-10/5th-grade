#Given a string, return a new string where the first and last chars have been exchanged.
def front_back(stri):
  es = ""
  if len(stri) == 1 :
    return stri
  if stri == "":
    return ""
  else:
    mid = stri[1:len(stri)-1]
    return (es + stri[len(stri)-1] + mid + stri[0] )


print(front_back('Code'))