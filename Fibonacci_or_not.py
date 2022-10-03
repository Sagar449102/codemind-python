n=int(input())
c=0
if n==0 or n==1:
    print("True")
else:
    s1=0
    s2=1
    s3=s1+s2
    while(s3<=n):
        s1=s2
        s2=s3
        s3=s1+s2
        if s3==n:
            c=1
            print("True")
            break
if c==0:
    print("False")
