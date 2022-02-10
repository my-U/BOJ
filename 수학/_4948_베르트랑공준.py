k = 123456 * 2
L = [False, False] # 0과 1은 소수가 아니므로 False 입력

for i in range(2, k + 1):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            L.append(False) # 약수가 존재할 시 False 추가
            break
    else:
        L.append(True) # 소수는 True 추가

while True:
    n = int(input())
    count = 0
    if n == 0:
        break
    for i in range(n + 1, 2*n + 1): # n보다 크고 2n보다 작거나 같은 소수
        if L[i]:
            count += 1
    print(count)

# 시간초과 코드

# 이전 문제인 '소수구하기'에서와 마찬가지로 에라토스테네스의 체를 사용했지만 시간초과 뜸
# 이유는 해당 코드가 테스트케이스를 입력할 때마다 소수를 구하기 때문
# 그렇기에 n 최대값의 2배인 246912까지 소수를 미리 구한 후 입력되는 값 범위에 존재하는 소수의 개수를 구하여 시간을 단축한다

# while True:
#     n = int(input())
#     count = 0

#     if n == 0:
#         break
#     for i in range(n + 1, 2*n + 1):
#         if i == 1:
#             pass
#         else:
#             for j in range(2, int(i ** 0.5) + 1):
#                 if i % j == 0:
#                     break
#             else:
#                 count += 1
#     print(count)

