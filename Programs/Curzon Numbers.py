def is_curzon(num):
    if num<0 :
        num = num - num - num
    num1 = 2 ** num + 1
    num2 = 2 * num + 1
    num3 = num1/num2
    if isinstance(num3,int) :
        return True
    else:
        return False

print(is_curzon(23))
print(is_curzon(-23))