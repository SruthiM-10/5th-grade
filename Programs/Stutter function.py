def stutter(word):
    word = list(word)
    wo = []
    wo.append(word[0])
    wo.append(word[1])
    str1 = ""
    word = str1.join(word)
    str2 = ""
    wo = str2.join(wo)
    print(wo,"...",wo,"...",word)


stutter('incredible')
