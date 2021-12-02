N = int(input())
dp = [0] # N까지 포도주 최대값
wine = [0]

for i in range(N):
    wine.append(int(input()))

dp.append(wine[1])# 첫 번째 포도잔의 값을 넣어줌

if N > 1:
    dp.append(wine[1] + wine[2])
for i in range(3, N+1):
# 현재 포도주가 i번째 일 때 나올 수 있는 경우
# 1. 현재 포도주(i)를 마시고 이전 포도주(i-1)를 마시고 전전전 포도주(i-3)를 마실 경우
    case1 = wine[i] + wine[i-1] + dp[i-3]
# 2. 현재 포도주(i)를 마시고 전전 포도주(i-2)를 마실 경우
    case2 = wine[i] + dp[i-2]
# 3. 현재 포도주를 마시지 않고 전 포도주(i-1)와 전전 포도주(i-2)를 마실 경우
    case3 = dp[i-1]
    dp.append(max(case1, case2, case3))

print(dp[N])