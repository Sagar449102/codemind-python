n=int(input())
l=list(map(int,input().split()))
k=[]
f=0
for i in range(0,n):
    c=0
    for j in range(i,n):
        if l[i]==l[j]:
            c+=1
    if l[i]==c:
        f=1
        k.append(l[i])
if f==0:
    print('-1')
else:
    print(min(k),max(k))
