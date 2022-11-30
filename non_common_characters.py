a=input()
b=input()
a1=a.replace(" ","")
b1=b.replace(" ","")
s1=a1.lower()
s2=b1.lower()
s=""
for i in s2:
    if i not in s1:
        s+=i
for i in s1:
    if i not in s2:
        s+=i
st=set(s)
r=sorted(st)
d=""
for i in r:
    d+=i
print(d)
