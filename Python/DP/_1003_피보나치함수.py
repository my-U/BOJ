N = int(input())

for _ in range(N):
    T = int(input())
    dp = [[1, 0], [0, 1]]
    for i in range(2, T+1):
        dp.append([dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]])

    print(dp[T][0], dp[T][1])
    print(dp)
    
# 위의 코드는 세로로 표현했을 경우 아래 코드는 가로로 표현했을 경우
# N = int(input())
# dp0 = [1, 0]
# dp1 = [0, 1]

# for i in range(2, 41):
#     dp0.append(dp0[i-2] + dp0[i-1])
#     dp1.append(dp1[i-2] + dp1[i-1])

# for _ in range(N):
#     T = int(input())

#     print(dp0[T], dp1[T])

