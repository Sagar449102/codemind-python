def get(n):
    k=0
    for i in range(1,n):
        if n%i==0:
            k=k+i
    return k
n=int(input())
c=get(n)
if c>n:
    print("True")
else:
    print("False")