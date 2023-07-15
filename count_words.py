n=input()
s=n.split()
a="aeiouAEIOU"
c=0
for i in s:
    if i[0] in a and i[-1] not in a:
        c+=1
print(c)