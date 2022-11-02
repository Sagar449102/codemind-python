n=int(input())
l=list(map(int,input().split()))
f=0
for i in l:
    if i%2!=0:
        print(i,end=" ")
for i in l:
    if i%2==0:
        print(i,end=" ")
                   
