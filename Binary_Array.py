import math
n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(0,n):
    if l[i]==1 or l[i]==0:
        s+=1
if s==n:
    print('True')
else:
    print('False')
