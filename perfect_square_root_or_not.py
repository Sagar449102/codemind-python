import math
n=int(input())
r=math.sqrt(n)
s=n%r
if s==0:
    print("True")
else:
    print("False")