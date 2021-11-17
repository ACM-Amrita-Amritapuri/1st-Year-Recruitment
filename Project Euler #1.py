def sum(n, k):
    d = n // k
    return k * (d * (d+1)) // 2
  
def ans(n):
    return sum(n, 3) + sum(n, 5) - sum(n, 15)

for _ in range(int(input())):
    N = int(input())
    print(ans(N - 1))
