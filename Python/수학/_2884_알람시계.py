import sys
input = sys.stdin.readline

H, M = map(int, input().split())

if M - 45 >= 0:
    print(H, M-45)
else:
    if H > 0:
        print(H-1, M+15)
    else:
        print(23, M+15)

# 참고 코드
# a,b=map(int,input().split())
# c=60*a+b  입력받은 a와 b를 분으로 변환
# print(((c-45)//60)%24,(c-45)%60)
# 만약 a=0, b=30일 경우
# -15 / 60 = -0.xxxxxx 이기 때문에 몫은 -1
# -1/24 = (-1)*24 + 23 이기 때문에 나머지는 23
