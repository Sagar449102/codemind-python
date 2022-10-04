import math
n=int(input())
d=int(math.log10(n)+1)
c=d
k=n
s=0
while c>0:
    r=k%10
    s=s+(r**c)
    k=k//10
    c-=1

    
if s==n:
    print("True")
else:
    print("False")
