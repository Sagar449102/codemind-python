import math
n=int(input())
a=list(map(int,input().split()))
res=0
res1=0
for i in range(len(a)):
    if i%2==0:
        res=res+a[i]
    else:
        res1=res1+a[i]
print(res1)

