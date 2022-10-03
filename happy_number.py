import math
def ishap(n):
    s=0
    while n!=0:
        r=n%10
        s=s+r**2
        n=n//10
    if s==1 or s==7:
        return 1
    if s>9:
        return ishap(s)
    if s<9:
        return 0
        
n=int(input())
c=ishap(n)
if c==1:
    print("True")
else:
    print("False")