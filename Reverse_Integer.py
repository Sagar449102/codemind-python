def rev(n):
    k=n
    d=0
    while(k!=0):
        r=k%10
        d=d*10+r
        k=k//10
    return d
n=int(input())
if(n>0):
    print(rev(n))
else:
    s=-rev((-1)*n)
    print(s)