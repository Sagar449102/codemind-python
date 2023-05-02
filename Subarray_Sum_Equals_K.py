n,k=map(int,input().split())
l=list(map(int,input().split()))
a=[]
c=0
for i in range(len(l)+1):
    for j in range(i):
        a=l[j:i]
        if sum(a)==k:
             c+=1
print(c)