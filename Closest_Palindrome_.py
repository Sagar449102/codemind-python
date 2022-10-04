import math
def ispal(n):
    while True:
        k=n
        d=0
        while k!=0:
            r=k%10
            d=d*10+r
            k=k//10
        if n==d:
            return d
            break
        n+=1
def ispal1(n):
    while True:
        k=n
        d=0
        while k!=0:
            r=k%10
            d=d*10+r
            k=k//10
        if n==d:
            return d
            break
        n-=1
n=int(input())
c=ispal(n+1)
s=ispal1(n-1)
d1=c-n
d2=n-s
if d1==d2:
    print(s,c)
elif d1<d2:
    print(c)
else:
    print(s)
