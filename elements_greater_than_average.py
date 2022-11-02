n=int(input())
a=list(map(int,input().split()))
f=sum(a)//n
c=0
for i in a:
    if i>=f:
        c+=1
print(c)