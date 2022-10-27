N = int(input()) 
dp = [0 for _ in range(N+1)] # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(2, N+1): # 2부터 N까지
    dp[i] = dp[i-1] + 1 # i가 증가할 때마다 1씩 증가

    if i % 3 == 0 and dp[i//3] + 1 < dp[i] : # 2 또는 3으로 나뉜다는 것은 곱한 것과 마찬가지이므로 1 증가
        dp[i] = dp[i//3] + 1
    if i % 2 == 0 and dp[i//2] + 1 < dp[i] : # i는 증가할수록 1씩 커지기 때문
        dp[i] = dp[i//2] + 1
print(dp[N])