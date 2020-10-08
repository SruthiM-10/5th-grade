# Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
lst = []
e = int(input("Enter number of elements : "))
for i in range(0, e):
    ele = int(input())
    lst.append(ele)
sm = 0
for i in range(e):
    print(i)
    if sm >= e:
        lst.pop(e-sm)
        print("List value is")
        print(lst)
    else:
        print(sm)
        lst.pop(sm+2)
        sm = sm+4
        e=e-1
        print("List value is")
        print(lst)
print("List value is")
print(lst)
