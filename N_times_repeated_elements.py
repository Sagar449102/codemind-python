n=int(input())
l=list(map(int,input().split()))
k=int(input())
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
l=[]
for i,v in d.items():
    if k==v:
        l.append(i)
if l==[]:
    print(-1)
else:
    print(*l)