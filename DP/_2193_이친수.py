N = int(input())
dp = [0, 1, 1]

if 1 <= N <= 99:
    for i in range(3, N+1):
        dp.append(dp[i-2] + dp[i-1])
    print(dp[N])
else:
    0