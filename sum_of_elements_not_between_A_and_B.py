n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
f=0
for i in l:
    if i>=a and i<=b:
        continue
    else:
        f+=i
print(f)
                   
