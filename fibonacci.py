n=int(input())
print(0,1,end=" ")
s1=0
s2=1
s3=s1+s2
c=3
while c<=n:
    print(s3,end=" ")
    s1=s2
    s2=s3
    s3=s1+s2
    c+=1


