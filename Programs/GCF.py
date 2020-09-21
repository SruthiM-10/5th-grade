x=int(input("ENter a number"))
y=int(input("ENter a number"))

gcd=1

if x%y==0:
    gcd=y
for i in range(int(y/2),0,-1):
    if x%i==0 and y%i==0:
        gcd=i
        break
print(gcd)
