import math
n=int(input())
a=list(map(int,input().split()))
res=0
for i in range(len(a)):
    res=res+a[i]
t=res//n
f=1
for i in range(len(a)):
    if a[i]==t:
        f=0
        break
if f==0:
    print('True')
else:
    print('False')