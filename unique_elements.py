import math
n=int(input())
l=list(map(int,input().split()))
for i in range(0,n-1):
    for j in range(i+1,n):
        if l[i]==l[j]:
            l[j]=-1
for i in range(0,n):
    if l[i]!=-1:
        print(l[i],end=" ")