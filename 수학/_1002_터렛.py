from math import *

T = int(input())

for i in range(T):
    x, y, a, z, w, b = map(int, input().split())
    c = sqrt((x - z) ** 2 + (y - w) ** 2) # 두 좌표간의 거리

    if c == 0 and a == b: # 두 원이 동심원이고 반지름이 같을 경우
        print(-1)
    elif c == a + b or c == abs(a - b): # 두 원이 외접, 내접했을 경우. abs() : 절대값 함수
        print(1)
    elif abs(a - b) < c < (a + b): # 두 원이 서로 다른 두 점에서 접했을 경우
        print(2)
    else: # 접하지 않았을 경우
        print(0)