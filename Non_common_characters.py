a=input()
b=input()
a1=a.replace(" ","")
b1=b.replace(" ","")
a2=a1.lower()
b2=b1.lower()
s=""
for i in a2:
    if i not in b2:
        s+=i
for i in b2:
    if i not in a2:
        s+=i
s1=set(s)
print(len(s1))