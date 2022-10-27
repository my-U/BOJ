N = int(input())
stairs = [0]
dp = [0]

for i in range(1, N+1):
    stairs.append(int(input()))

    if i == 1:
        dp.append(stairs[i])
    elif i == 2:
        dp.append(stairs[i] + stairs[i-1])
    else:
        case1 = stairs[i] + stairs[i-1] + dp[i-3]
        case2 = stairs[i] + dp[i-2]
        dp.append(max(case1, case2))
print(dp[N])