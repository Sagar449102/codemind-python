def get(n):
    k=n
    d=0
    while(k!=0):
        r=k%10
        d=d+r
        k=k//10
    return d
n=int(input())
res=get(n*n)
if(n==res):
    print("Neon Number")
else:
    print("Not Neon Number")
