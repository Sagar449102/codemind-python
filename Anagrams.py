s1=input()
s2=input()
a1=s1.lower()
b1=s2.lower()
c=[0]*26
f=0
for i in a1:
    a=ord(i)-97
    c[a]+=1
for i in b1:
    a=ord(i)-97
    c[a]-=1
for i in c:
    if i!=0:
        print("False")
        f=1
        break
if f==0:
    print("True")