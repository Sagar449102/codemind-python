import math
n=int(input())
s1=0
s2=1
s3=s1+s2
while s3<=n:
    s1=s2
    s2=s3
    s3=s1+s2
if abs(s3-n)>abs(s2-n):
    print(s2)
elif abs(s3-n)==abs(s2-n):
    print(s2,s3)
else:
    print(s3)