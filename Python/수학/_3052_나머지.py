dp = [int(input()) for i in range(10)] 

for i in range(10): # dp = [int(input())%42 for i in range(10)] 간결하게 가능
    dp[i] = dp[i] % 42

print(len(set(dp)))

# 참고 코드
# s = set()

# for _ in range(10):
#     s.add(int(input()%42))  set으로 바로 추가 가능

# print(len(s))