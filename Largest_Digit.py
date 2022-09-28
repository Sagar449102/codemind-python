n=int(input())
k=n
x=0
while k!=0:
    r=k%10
    if(r>x):
        x=r
    k=k//10
print(x)