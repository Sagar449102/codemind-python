a=input()
a1=a.lower()
s=a1.replace(" ","")
m=[]
c=0
for i in s:
    if a.count(i)==1:
        c+=1
print(c)

    