def ispal(i):
    n=i[::-1]
    return n
a=input()
a1=a.lower()
a2=a1.split()
c=0
for i in a2:
    if ispal(i)==i:
        c+=1
print(c)