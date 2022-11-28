a=input()
v="aeiouAEIOU"
c="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
k=0
if len(a)%2==0:
    b=len(a)//2 + 1 
    for i in range(0,len(a)):
        if i+1 == b:
            break
        if a[i] in v and a[len(a)-1-i] in c:
            k+=1
        if a[i] in c and a[len(a)-1-i] in v:
            k+=1
else:
    for i in range(0,len(a)):
        if a[i] in v and a[len(a)-1-i] in c:
            k+=1
        if a[i] in c and a[len(a)-1-i] in v:
            k+=1
        if i+1 == len(a)//2 :
            break
print(k)
