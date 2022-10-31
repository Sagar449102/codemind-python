import math
def isprime(n):
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True

n=int(input())
if isprime(n):
    print(0)
else:
    f=n+1
    while True:
        if isprime(f):
            break
        else:
            f=f+1
    b=n-1
    while True:
        if isprime(b):
            break
        else:
            b=b-1
    d1=f-n
    d2=n-b
    if d1<d2:
        print(d1)
    else:
        print(d2)
            
