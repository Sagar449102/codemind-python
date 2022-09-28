import math
n=int(input())
k=n
d=int(math.log10(k))
c=0
s=0
while(k!=0):
    r=k//math.pow(10,d)
    if(r==6  and c==0):
        r=9
        c=1
    s=s*10+r
    k=k%math.pow(10,d)
    d=d-1
print(int(s))