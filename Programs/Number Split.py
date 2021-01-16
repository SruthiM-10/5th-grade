def numbersplit(n):
    list1 = []
    if n%2 == 0:
        list1 = [n/2,n/2]
        print(list1)
    else:
        list1 = [n/2 - 0.5 , n/2 + 0.5]
        print(list1)


numbersplit(4)
