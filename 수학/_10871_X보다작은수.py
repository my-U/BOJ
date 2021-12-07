import sys, random
input = sys.stdin.readline

N, X = map(int, input().split())

A = list(map(int, input().split()))

for i in range(N):
    if A[i] < X:
        print(A[i], end=" ") # 일반적으로 줄단위로 출력되기 때문에 end를 설정하면 줄바꿈을 하지 않는다

# 코드 간결화
# A = map(int, input().split()) 리스트가 없어도 가능

# for i in A:
#     if i < X:
#         print(i, end=" ")