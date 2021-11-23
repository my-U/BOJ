N = int(input())
dp = [0 for _ in range(N+1)]

if N <= 3 :
    print(N)
else:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[N] % 10007)


# 참고코드

# n = int(input())
# Memo = [1,1]  // 미리 선언하고 변경하지 않아도 되므로 간결해짐
# for i in range(2,n+1):
#     Memo.append((Memo[i-1]+Memo[i-2])) 값을 변경하지 않고 append로 추가
# print(Memo[n] % 10007)

