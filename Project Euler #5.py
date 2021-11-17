for _ in range(int(input())):
    n=int(input())
    i=1
    while True:
        l=[]
        for j in range(2,n+1):
            if i%j==0:l.append(True)
            else:l.append(False)
        if l.count(True)==len(l):break
        i+=1
    print(i)
