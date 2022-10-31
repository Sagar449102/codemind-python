def isprime(n):
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True
n=int(input())
f=1
for i in range(2,n):
    for j in range(3,n):
        if isprime(i)*isprime(j):
            if i*j==n:
                f=0
                print(i,j)
                break
    if f==0:
        break
if f==1:
    print('-1')
                