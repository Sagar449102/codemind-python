def sum(n):
    k=n
    d=0
    while(k!=0):
        r=k%10
        d=d+r
        k=k//10
    return d
def pro(n):
    k=n
    d=1
    while(k!=0):
        r=k%10
        d=d*r
        k=k//10
    return d
        
n=int(input())
s=sum(n)
p=pro(n)
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")