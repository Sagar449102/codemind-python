def get(n):
    k=n
    s=0
    for i in range(1,n):
        if k%i==0:
            s=s+i
    return s
n=int(input())
m=int(input())
if(n==get(m) and m==get(n)):
    print("Amicable")
else:
    print("Not Amicable")
    