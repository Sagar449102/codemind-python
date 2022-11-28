a=input()
a1=a.lower()
s=a1.replace(" ","")
m=[]
for i in s:
    if a.count(i)==1:
        m.append(i)
l=sorted(m)
n=""
for i in l:
    n+=i
print(n)

    