a=input()
s=a.split()
v="aeiouAEIOU"
c="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
k=0
for i in s:
    m=i[0]
    e=i[len(i)-1]
    if m in v and e in c:
        k+=1
print(k)
