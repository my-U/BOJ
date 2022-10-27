N = int(input())
dp = [[0 for _ in range(10)] ]

for i in range(1, N+1):
    new_dp = [0 for _ in range(10)]
    new_dp[0] = 1
    dp.append(new_dp)
    for j in range(1, 10):
        if i == 1:
            dp[1][j] = 1
        else:
            for k in range(0, j+1):
                dp[i][j] += dp[i-1][k]
print(sum(dp[N]) % 10007)