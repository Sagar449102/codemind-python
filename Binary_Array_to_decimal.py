import math
n=int(input())
l=list(map(int,input().split()))
j=n-1
s=0
for i in range(0,n):
    if l[i]==1:
        s=s+pow(2,j)
    j=j-1
    
    
print(s)
