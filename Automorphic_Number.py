import math
n=int(input())
d=int(math.log10(n)+1)
s=n*n
f=s%math.pow(10,d)
if(n==f):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")