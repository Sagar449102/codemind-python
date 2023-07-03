n,m=map(int,input().split())
m1=[]
for i in range(n):
    l=list(map(int,input().split()))
    m1.append(l)
s=0
for i in range(n):
    for j in range(m):
        if i==0 or j==0 or i==n-1 or j==m-1:
            continue
        else:
            s+=m1[i][j]
print(s)