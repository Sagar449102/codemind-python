n=int(input())
l=list(map(int,input().split()))
f=sum(l)//n
c=0
for i in l:
    if i<=f:
        c+=1
print(c)
                   
