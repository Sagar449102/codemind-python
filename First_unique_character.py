a=input()
a1=a.lower()
m=[]
f=0
for i in a1:
    if a.count(i)==1:
        print(i)
        f=1
        break
if f==0:
    print('-1')
    
        

    