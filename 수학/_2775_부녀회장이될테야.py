T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    F = [i+1 for i in range(n)]

    if k == 0:
        print(n)
    else:
        for _ in range(k):
            for i in range(1, n):
                F[i] = F[i] + F[i-1]
        print(F[n-1])