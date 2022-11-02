n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
f=1
for i in l:
    if i>=a and i<=b:
        continue
    else:
        f=0
        k.append(i)
if f==1:
    print(-1)
else:
    print(max(k))
                   
