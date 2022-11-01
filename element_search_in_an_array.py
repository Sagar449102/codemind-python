import math
n=int(input())
a=list(map(int,input().split()))
t=int(input())
f=0
for i in range(len(a)):
    if a[i]==t:
        f=1
        break
if f==1:
    print('True')
else:
    print('False')