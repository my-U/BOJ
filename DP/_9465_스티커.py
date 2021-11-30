N = int(input())

for i in range(N):
    dp = []
    t = int(input())
    for _ in range(2):
        dp.append(list(map(int, input().split())))
    for j in range(1, t):
        if j == 1: # 대각선으로만 더할 수 있음
            dp[0][j] += dp[1][j-1]
            dp[1][j] += dp[0][j-1]
        else: # 해당 위치의 스티커를 선택했을 경우 왼쪽 대각선으로 경우의 수가 존재함. 때문에 둘 중 큰 값으로 선택
            dp[0][j] += max(dp[1][j-1], dp[1][j-2])
            dp[1][j] += max(dp[0][j-1], dp[0][j-2])
    print(max(dp[0][t-1], dp[1][t-1]))