r,c=map(int,input().split())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]
s=0
for i in range(r):
    val=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=val[j]
        s+=d[i][j]
res=0
for i in range(r):
    if i%2==0:
         for j in range(c):
             res+=d[i][j]
print(res,s-res)
             
        