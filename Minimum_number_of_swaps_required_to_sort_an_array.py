n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    m=i
    f=0
    for j in range(i+1,len(l)):
        if l[m]>l[j]:
            m=j
            f=1
    if f==1:
        l[i],l[m]=l[m],l[i]
        c+=1
print(c)