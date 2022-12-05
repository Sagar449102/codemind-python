a=input()
b=input()
a2=a.lower()
b2=b.lower()
a1=a2.split()
b1=b2.split()
s=[]
for i in b1:
    for j in a1:
        if i==j:
            s.append(i)
print(*s)
