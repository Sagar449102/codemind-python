def dif(a):
    m=0
    n=0
    m=ord(min(a))
    n=ord(max(a))
    s=abs(m-n)
    return s
a=input()
s=a.split()
for i in s:
    print(dif(i),end=' ')