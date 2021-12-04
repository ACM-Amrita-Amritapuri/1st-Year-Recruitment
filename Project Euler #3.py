def LP(n):
    p,i=1,2
    while i <= n / i:
        if n % i == 0:
            p = i
            n /= i
        else:i += 1
    if p < n: p = int(n)
    return p
for _ in range(int(input())):print(LP(int(input())))
