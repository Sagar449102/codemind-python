def isprime(n):
    if n==1 or n==0:
        return False
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True

n=int(input())
s=1
if isprime(n):
    c=n
    s=0
    while c!=0:
        r=c%10
        c=c//10
        if r==1 or r==4 or r==6 or r==8:
            s=1
            print("Not Mega Prime")
            break
        
else:
    print("Not Mega Prime")
if s==0:
    print("Mega Prime")

        
