import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = {}

for i in range(1, N + 1):
    x = input().strip()
    P[x] = i
    P[i] = x # 숫자로도 검색을 해야하기 때문에 key와 value를 바꿔 저장

for i in range(M):
    y = input().strip()
    if y.isdigit(): # 문자열이 숫자로만 이루어져 있는지 판별하는 함수 숫자로만 이루어져 있다면 True, 문자가 1개라도 섞여있다면 False
        print(P[int(y)])
    else:
        print(P[y])

