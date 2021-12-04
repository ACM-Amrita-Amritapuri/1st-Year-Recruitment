for _ in range(int(input())):
    n=int(input())
    a,b=1,1
    s=0
    while a+b<n:
        if (a+b)%2==0:
            s+=(a+b)
        a,b=b,a+b
    print(s)
