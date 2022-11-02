n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n-2):
    if l[i]%2==0 and l[i+2]%2!=0:
        c+=1
    if l[i]%2!=0 and l[i+2]%2==0:
        c+=1
print(c)