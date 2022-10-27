# 소수를 구하는 코드는 맞지만 채점결과에서 시간초과가 뜸
# 약수는 대칭으로 짝을 이루기 때문에
# 해당 수의 제곱근까지만 나누어보면 된다 = j ** 0.5


# M, N = map(int, input().split())

# for i in range(M, N+1):
#     Error = 0
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 Error += 1
#         if Error == 0:
#             print(i)

M, N = map(int, input().split())

for i in range(M, N+1):
    if i == 1: # 1을 패스로 거르면
        pass
    else:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break # Error를 사용하지 않아도 됨
        else:
            print(i)