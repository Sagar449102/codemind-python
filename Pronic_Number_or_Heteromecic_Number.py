n=int(input())
i=1
j=2
while True:
    if (i*j)==n:
        print("YES")
        break
    if (i*j)>n:
        print("NO")
        break
    i=i+1
    j=j+1
    