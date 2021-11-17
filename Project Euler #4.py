r=range(100,1000)
l=[]
for i in r:
    for j in r:
        p=i*j
        if str(p)==str(p)[::-1]:
            l.append(p)
l.sort()

for _ in range(int(input())):
    n=int(input())
    
    for i in l[::-1]:
        if i<n:
            print(i)
            break
