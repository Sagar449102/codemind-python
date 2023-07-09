for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    f=0
    for i in range(len(l)):
        m=0
        r=0
        for j in range(i):
            m+=l[j]
        for j in range(i+1,len(l)):
            r+=l[j]
        if m==r:
            f=1
            break
    if f==1:
        print("YES")
    else:
        print("NO")