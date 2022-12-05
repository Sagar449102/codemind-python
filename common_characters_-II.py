a=input()
b=input()
a1=a.replace(" ","")
b1=b.replace(" ","")
s1=a1.lower()
s2=b1.lower()
s=""
if len(s1)<len(s2):
    for i in s2:
        if i in s1:
            s+=i
else:
    for i in s1:
        if i in s2:
            s+=i
st=set(s)
print(len(st))
