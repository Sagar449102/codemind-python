import math
n=int(input())
a=list(map(int,input().split()))
t=int(input())
c=0
for i in range(len(a)):
    if a[i]==t:
        c+=1
print(c)
        


