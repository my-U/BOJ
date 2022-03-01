# 오답 코드
# 코드는 실행이 되는데 문제 제출에서 오답이 나옴
# T = int(input())
# L = []

# for i in range(2, 10001):
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             break
#     else:
#         L.append(i)

T = int(input())
L = [0, 0] + [1] * 10000

for i in range(2, 101): # 범위가 100까지인 이유를 몰랐는데 10000의 제곱근이 100이기 때문이다
    if L[i] == 1:
        for j in range(i * 2, 10001, i): # i씩 증가하기 때문에 i의 배수들은 0의 값을 가진다
            L[j] = 0 # if문의 조건이 1이기 때문에 0으로 값이 변한 수들은 제외되어 시간이 단축된다

for i in range(T):
    n = int(input())
    h = n // 2
    for j in range(h, 1, -1):
        if L[j] == 1 and L[n - j] == 1: # 두 수가 모두 소수일 경우
            print(j, n-j)
            break
