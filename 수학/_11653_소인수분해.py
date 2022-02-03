N = int(input())
i = 2

while N > 0:    
    if N % i == 0:
        print(i)
        N //= i
    else:
        i += 1
        if N % i == 0:
            print(i)
            N //= i
    
# 참고 코드
# if N % i == 0:
#     print(i)
#     N = N // i
# elif i * i > N: N이 2로 나뉘어지지 않고 4보다 작을 경우 N은 3
#     print(N)
#     break
# else: N이 2로 나뉘어지지 않고 4보다 클 경우 i는 1증가
#     i += 1