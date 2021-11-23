N = int(input())
dp = [1, 1]

for i in range(1, N+1):
    dp.append((dp[i] + dp[i-1]*2))
print(dp[N] % 10007)

# 참고
# 경우의 수
# 1. 마지막 타일이 1X2 타일일 경우 = dp[N-1] // dp[n-1]에서 마지막에 1X2의 타일만 붙이면 되기 때문
# 2. 마지막 타일이 2X1 타일일 경우 = dp[N-2]
# 3. 마지막 타일이 2X2 타일일 경우 = dp[N-2]

# 따라서 dp[N] = dp[N-1] + dp[N-2] * 2