a=input()
a1=a.replace(" ","")
s=a1.lower()
m=set(s)
l=sorted(m)
st=""
for i in l:
    st+=i
print(st)
