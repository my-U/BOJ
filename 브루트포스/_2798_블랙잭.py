N, M = map(int, input().split())
a = list(map(int, input().split()))
result = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for l in range(j + 1, N):
            if a[i] + a[j] + a[l] > M:
                pass
            else:
                result = max(result, a[i] + a[j] + a[l])

print(result)